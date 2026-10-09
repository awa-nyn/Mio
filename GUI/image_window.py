'''图片查看器：和主窗口同风格的无边框小窗口

界面在 image_viewer.py（pyuic 生成的），这里只放逻辑。
功能：滚轮缩放、右键菜单（复制到剪贴板 / 保存 / 另存为）、标题栏拖动、模态（挡住主窗口）。
'''

import sys
from pathlib import Path
from PySide6.QtCore import QRect, QSize, Qt, QTimer, QEvent
from PySide6.QtGui import QGuiApplication, QPixmap
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QFileDialog,
                               QMenu, QMessageBox, QWidget)
from image_viewer import Ui_Dialog

from ui_common import load_icon, load_qss

RESIZE_MARGIN = 6       # 鼠标离窗口边多少像素算「抓到了边框」
ZOOM_MIN = 0.1          # 最小缩放（相对适配大小）
ZOOM_MAX = 8.0          # 最大缩放
ZOOM_STEP = 1.15        # 每格滚轮的缩放比例
MIN_W, MIN_H = 480, 360  # 窗口最小尺寸


class ImageViewer(QDialog):
    '''图片查看器

    image_path：要看的原图
    save_dir：右键「保存」的目标目录（TODO: 以后从设置里读，现在允许是 None）
    '''

# ====================初始化====================

    def __init__(self, image_path, owner=None, save_dir=None):
        super().__init__(None)      # 故意不给 Qt 父对象：独立窗口，主窗口被禁用时不会跟着变灰
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.owner = owner          # 主窗口：打开时禁掉它，关掉时放回来
        self.image_path = Path(image_path)
        self.save_dir = save_dir
        self.original = QPixmap(str(self.image_path))
        self.zoom = 1.0                 # 缩放倍数（1.0 = 适配窗口）
        self._drag_offset = None        # 拖动窗口用的鼠标偏移
        self._resizing = None           # 正在拉的边
        self._resize_start_geo = None
        self._resize_start_pos = None

        # 窗口
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)   # 无边框 + 独立窗口
        self.setAttribute(Qt.WA_TranslucentBackground)            # 背景透明，圆角才露得出来
        self.setStyleSheet(load_qss())                            # 和主窗口同一份样式

        # 打开期间主窗口不能操作：直接把主窗口禁掉。
        # 注意查看器不能是主窗口的子窗口——父窗口一禁用，子窗口会跟着变灰。
        if self.owner is not None:
            self.owner.setEnabled(False)

        # .ui 里把最小尺寸写成了 1300x1300，屏幕矮一点就会超出屏幕，
        # 所以这里放宽，窗口大小按图片和屏幕可用区域来定
        self.ui.image.setMinimumSize(0, 0)
        self.setMinimumSize(MIN_W, MIN_H)
        available = self.screen().availableGeometry()
        self.resize(min(max(self.original.width() + 60, 640), available.width() - 120),
                    min(max(self.original.height() + 100, 480), available.height() - 120))

        if self.owner is not None:      # 对着主窗口居中，别跳到屏幕角上
            self.move(self.owner.geometry().center() - self.frameGeometry().center())

        # 标题栏按钮
        self.ui.minBtn.setIcon(load_icon("min"))
        self.ui.maxBtn.setIcon(load_icon("max"))
        self.ui.closeBtn.setIcon(load_icon("close"))
        for btn in (self.ui.minBtn, self.ui.maxBtn, self.ui.closeBtn):
            btn.setIconSize(QSize(16, 16))
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.minBtn.clicked.connect(self._minimize)
        self.ui.maxBtn.clicked.connect(self._max_toggle)

        # 图片居中显示
        self.ui.image.setAlignment(Qt.AlignCenter)
        # 右键菜单自己接管（不然 QLabel 会弹它自带的那套）
        self.ui.image.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.image.customContextMenuRequested.connect(self._show_context_menu)

        # 标题栏负责拖动（和主窗口一个思路：按钮的点击不会经过这里）
        self.ui.titleBar.installEventFilter(self)
        self.setMouseTracking(True)
        for widget in self.findChildren(QWidget):
            widget.setMouseTracking(True)

        self._render()
        QTimer.singleShot(0, self._render)   # 布局排完之后再画一次

# ====================自定义方法====================

    def resizeEvent(self, event):
        super().resizeEvent(event)
        QTimer.singleShot(0, self._render)   # 窗口变了要重新按适配大小画

    def _minimize(self):
        '''最小化（现在可以正常最小化了：窗口不是模态，合成器不会再拦）'''

        self.showMinimized()

    def closeEvent(self, event):
        '''关掉的时候把主窗口还回来，不然主窗口会一直点不动'''

        if self.owner is not None:
            self.owner.setEnabled(True)
        super().closeEvent(event)

    def _max_toggle(self):
        '''最大化/还原'''

        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def _render(self):
        '''按当前缩放倍数把图重新画到 Label 上'''

        if self.original.isNull():
            self.ui.image.setText("图片加载失败了喵")
            return

        area = self.ui.image.size()
        if area.width() <= 0 or area.height() <= 0:
            return

        # 适配倍数：让整张图能塞进 Label（算出来比 1 大就压回 1，放大交给滚轮）
        fit = min(area.width() / self.original.width(),
                  area.height() / self.original.height(), 1.0)
        scale = fit * self.zoom

        pixmap = self.original.scaled(max(1, int(self.original.width() * scale)),
                                      max(1, int(self.original.height() * scale)),
                                      Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.image.setPixmap(pixmap)

    def _set_zoom(self, zoom):
        '''夹住缩放范围再重画'''

        self.zoom = max(ZOOM_MIN, min(ZOOM_MAX, zoom))
        self._render()

    # ==========滚轮缩放==========
    def wheelEvent(self, event):
        '''在图片区域滚轮放大缩小（Label 不处理滚轮，会冒泡到这里）'''

        delta = event.angleDelta().y()
        if delta > 0:
            self._set_zoom(self.zoom * ZOOM_STEP)
        elif delta < 0:
            self._set_zoom(self.zoom / ZOOM_STEP)
        event.accept()

    # ==========右键菜单==========
    def _show_context_menu(self, pos):
        '''右键菜单：复制到剪贴板 / 保存 / 另存为'''

        menu = QMenu(self)
        act_copy = menu.addAction("复制到剪贴板")
        act_save = menu.addAction("保存")
        act_save_as = menu.addAction("另存为…")

        chosen = menu.exec(self.ui.image.mapToGlobal(pos))
        if chosen is act_copy:
            self._copy_to_clipboard()
        elif chosen is act_save:
            self._save()
        elif chosen is act_save_as:
            self._save_as()

    def _copy_to_clipboard(self):
        '''把原图塞进剪贴板'''

        if not self.original.isNull():
            QGuiApplication.clipboard().setPixmap(self.original)

    def _save(self):
        '''保存到设置的目录（还没有设置界面，所以先占位：没设置就走另存为）'''

        if self.save_dir is None:
            QMessageBox.information(self, "还没设置保存目录",
                                    "保存目录以后在设置里选，这里先走「另存为」喵。")
            self._save_as()
            return

        dest = Path(self.save_dir) / self.image_path.name
        self.original.save(str(dest))

    def _save_as(self):
        '''另存为'''

        dest, _ = QFileDialog.getSaveFileName(self, "另存为", str(self.image_path),
                                             "PNG 图片 (*.png);;所有文件 (*)")
        if dest:
            self.original.save(dest)

    # ==========标题栏拖动 / 拉边框==========
    def _edge_flags(self, pos):
        '''判断窗口内的坐标贴着哪几条边'''

        m = RESIZE_MARGIN
        return (pos.x() <= m,
                pos.y() <= m,
                pos.x() >= self.width() - m,
                pos.y() >= self.height() - m)

    def _cursor_for_edges(self, edges):
        '''按贴着哪条边/哪个角给出鼠标形状'''

        left, top, right, bottom = edges
        if (top and left) or (bottom and right):
            return Qt.CursorShape.SizeFDiagCursor
        if (top and right) or (bottom and left):
            return Qt.CursorShape.SizeBDiagCursor
        if left or right:
            return Qt.CursorShape.SizeHorCursor
        if top or bottom:
            return Qt.CursorShape.SizeVerCursor
        return None

    def _resize_by_drag(self, global_pos):
        '''按住边框拖动改窗口大小（夹住，不弹回去）'''

        left, top, right, bottom = self._resizing
        geo = QRect(self._resize_start_geo)
        dx = global_pos.x() - self._resize_start_pos.x()
        dy = global_pos.y() - self._resize_start_pos.y()

        if left:
            geo.setLeft(min(geo.left() + dx, geo.right() - MIN_W + 1))
        if right:
            geo.setRight(max(geo.right() + dx, geo.left() + MIN_W - 1))
        if top:
            geo.setTop(min(geo.top() + dy, geo.bottom() - MIN_H + 1))
        if bottom:
            geo.setBottom(max(geo.bottom() + dy, geo.top() + MIN_H - 1))

        self.setGeometry(geo)

    def eventFilter(self, obj, event):
        '''标题栏拖动 + 边框缩放'''

        if obj is self.ui.titleBar:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
                handle = self.windowHandle()          # 交给系统拖（Wayland 下只能这样）
                if handle is None or not handle.startSystemMove():
                    self._drag_offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                return True
            if (event.type() == QEvent.MouseMove and self._drag_offset is not None
                    and (event.buttons() & Qt.MouseButton.LeftButton)):
                self.move(event.globalPosition().toPoint() - self._drag_offset)
                return True
            if event.type() == QEvent.MouseButtonRelease:
                self._drag_offset = None

        if event.type() in (QEvent.MouseMove, QEvent.MouseButtonPress, QEvent.MouseButtonRelease):
            global_pos = event.globalPosition().toPoint()
            local_pos = self.mapFromGlobal(global_pos)

            if event.type() == QEvent.MouseMove:
                if self._resizing:
                    self._resize_by_drag(global_pos)
                    return True
                if not (event.buttons() & Qt.MouseButton.LeftButton):
                    cursor = self._cursor_for_edges(self._edge_flags(local_pos))
                    if cursor:
                        self.setCursor(cursor)
                    else:
                        self.unsetCursor()

            elif event.type() == QEvent.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
                if not isinstance(obj, QAbstractButton) and any(self._edge_flags(local_pos)):
                    self._resizing = self._edge_flags(local_pos)
                    self._resize_start_geo = self.geometry()
                    self._resize_start_pos = global_pos
                    return True

            elif event.type() == QEvent.MouseButtonRelease:
                self._resizing = None

        return super().eventFilter(obj, event)


if __name__ == "__main__":      # 单独跑这个文件可以直接看图，方便调试
    app = QApplication(sys.argv)
    viewer = ImageViewer(sys.argv[1] if len(sys.argv) > 1 else "avatar/原版.png")
    viewer.show()
    sys.exit(app.exec())
