import signal
import sys
from pathlib import Path
from PySide6.QtCore import QPoint, QRect, QSize, Qt, QTimer, QEvent, QPropertyAnimation
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QLabel, QMainWindow,
                               QPushButton, QVBoxLayout, QWidget, QGraphicsDropShadowEffect)
from PySide6.QtGui import QColor, QIcon, QPixmap
from GUI import Ui_MainWindow

from image_window import ImageViewer
from memory_panel import MemoryPanel
from settings_page import SettingsPage
from ui_common import (AVATAR_DIR, ICON_COLOR, ICON_SIZE, avatar_pixmap, load_icon,
                       load_qss, round_pixmap)

MENU_MIN_W = 90         # 菜单最小宽度
RESIZE_MARGIN = 6           # 鼠标离窗口边多少像素算「抓到了边框」
RESIZE_MARGIN_RIGHT = 1     # 右边只留 1px：再宽就把聊天区的滚动条抢走了（滚动条才 8px 宽）
INPUT_BOTTOM_GAP = 32       # 输入区底部留白（正好让 82 高的渐变遮罩底边对齐页面底部）
SNAP_MARGIN = 2         # 拖到离屏幕边多少像素算「贴边了」
SNAP_MIN_DRAG = 20      # 拖动不足这么多像素，就不允许吸附（防止一上手就误触发）
ENABLE_WINDOW_MOVE = True   # 窗口拖动开关（排查问题时可以先改成 False）

# 头像挑选区：(缩略图 Label, 200x200 缩略图, 原图, 放大按钮)
AVATARS = (
    ("Mio",      "原版-200x200.png",      "原版.png",      "zoomBtn1"),
    ("MioCat",   "猫耳-200x200.png",      "猫耳.png",      "zoomBtn2"),
    ("QMio",     "Q版-200x200.png",       "Q版.png",       "zoomBtn3"),
    ("QMioCat",  "Q版 猫耳-200x200.png",  "Q版 猫耳.png",  "zoomBtn4"),
)


class MainWindow(QMainWindow):
    '''主窗口类'''

# ====================初始化====================

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.avatar_event_time = 500    # 头像点击事件公共时间
        self.avatar_menu_open = False   # 头像菜单当前是否展开（头像旋转状态跟着它走）
        self.more_menu_open = False     # 更多菜单当前是否展开
        self.save_dir = None            # TODO: 保存目录以后从设置里读，先占位
        self._drag_offset = None        # 拖动窗口时的鼠标偏移（None 表示没在拖）
        self._drag_start_pos = None     # 按下时鼠标的全局坐标
        self._resizing = None           # 正在缩放的那几条边（None 表示没在缩放）
        self._resize_start_geo = None   # 缩放开始时的窗口位置
        self._resize_start_pos = None   # 缩放开始时的鼠标位置
        self._holding_btn = None        # 正被按住的那个按钮（用来维持深灰）
        self.ui.avatarMenu.hide()       # 初始化时隐藏头像菜单
        self.ui.moreMenu.hide()         # 初始化时隐藏更多菜单

        # 设置主窗口布局
        layout = QVBoxLayout(self.ui.mainContainer)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 设置鼠标滚轮滚动的行数
        QApplication.setWheelScrollLines(6)

        # 添加控件
        layout.addWidget(self.ui.titleBar)
        layout.addWidget(self.ui.stack, 1)      # 聊天页和其它页都装在这个堆叠容器里
        layout.addWidget(self.ui.statusBar)

        # 聊天页：聊天区铺满整页，输入区和渐变遮罩浮在它上面
        # （输入区和遮罩在 .ui 里是绝对定位的，位置由 _update_input_row 算）
        page_layout = QVBoxLayout(self.ui.page1)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.setSpacing(0)
        page_layout.addWidget(self.ui.chatScroll)

        # 窗口
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框窗口
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setStyleSheet(load_qss())  # QSS 和图片查看器共用同一份

        # 拖动窗口交给标题栏自己：装在 titleBar 上，按钮的点击压根不会走到这里
        self.ui.titleBar.installEventFilter(self)

        # 让窗口里所有控件都把鼠标移动事件报上来，不然贴着边框时收不到 hover，光标形状变不了
        self.setMouseTracking(True)
        for widget in self.findChildren(QWidget):
            widget.setMouseTracking(True)

        # 关闭窗口
        self.ui.closeBtn.clicked.connect(self.close)
        # 最小化窗口
        self.ui.minBtn.clicked.connect(self.showMinimized)
        # 最大化/还原窗口
        self.ui.maxBtn.clicked.connect(self.max_toggle)
        # 更多菜单
        self.ui.moreBtn.clicked.connect(self.toggle_more_menu)
        # 头像菜单
        self.ui.avatarBtn.clicked.connect(self.toggle_avatar_menu)
        # 头像挑选区
        self._setup_avatar_picker()
        # 底部那个灰色的临时提示：两秒后自己消失，不挡操作
        self._toast = QLabel(self.ui.mainContainer)
        self._toast.setObjectName("toast")
        self._toast.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._toast.hide()
        self._toast_timer = QTimer(self)
        self._toast_timer.setSingleShot(True)
        self._toast_timer.timeout.connect(self._toast.hide)

        # 第二页（修改设定）
        self.settings = SettingsPage(self)
        self.ui.editPersonaBtn.clicked.connect(self.open_settings)
        self.ui.PromptClose.setIcon(load_icon("close"))
        self.ui.PromptClose.setIconSize(QSize(16, 16))
        self.ui.PromptClose.setText("")

        # 记忆面板：从左边滑出来盖在对话区上
        self.memory_panel = MemoryPanel(self)
        self.ui.memoryBtn.clicked.connect(self.open_memory)

        # 输入框里有内容才显示发送按钮
        self.ui.sendBtn.setVisible(False)   # 一开始是空的，先藏起来
        self.ui.inputEdit.textChanged.connect(self._toggle_send_btn)

        # 设置输入区阴影
        input_row_shadow = QGraphicsDropShadowEffect(self)
        input_row_shadow.setBlurRadius(60)
        input_row_shadow.setColor(QColor(0, 0, 0, 80))
        input_row_shadow.setOffset(0, 4)
        self.ui.inputRow.setGraphicsEffect(input_row_shadow)
        # 设置头像菜单阴影
        avatar_menu_shadow = QGraphicsDropShadowEffect(self)
        avatar_menu_shadow.setBlurRadius(60)
        avatar_menu_shadow.setColor(QColor(0, 0, 0, 80))
        avatar_menu_shadow.setOffset(0, 8)
        self.ui.avatarMenu.setGraphicsEffect(avatar_menu_shadow)
        # 设置更多菜单阴影
        more_menu_shadow = QGraphicsDropShadowEffect(self)
        more_menu_shadow.setBlurRadius(60)
        more_menu_shadow.setColor(QColor(0, 0, 0, 80))
        more_menu_shadow.setOffset(0, 8)
        self.ui.moreMenu.setGraphicsEffect(more_menu_shadow)

        # 图标（值是 button/ 下的文件名，不带 .svg；要改颜色就写成 (文件名, 颜色)）
        icon_map = {
            # 标题栏
            self.ui.callBtn:     "phone",
            self.ui.voiceBtn:    "voice",
            self.ui.settingsBtn: "setting",
            self.ui.moreBtn:     "more",
            self.ui.minBtn:      "min",
            self.ui.maxBtn:      "max",
            self.ui.closeBtn:    "close",
            # 输入区
            self.ui.attachBtn:   "attachment",
            self.ui.imageBtn:    "image",
            self.ui.speechBtn:   "microphone",
            self.ui.sendBtn:     ("send", "#ffffff"),   # 蓝底上要白图标
            # 头像菜单
            self.ui.chooseAvatarBtn: "avatar",
            self.ui.editPersonaBtn:  "edit",
            self.ui.memoryBtn:       "memory",
            # 更多菜单
            self.ui.help:     "help",
            self.ui.update:   "update",
            self.ui.ComfyUI:  "run_ComfyUI",
            self.ui.feedback: "feedback",
            self.ui.about:    "about",
            self.ui.reset:    "restart",
        }
        for btn, value in icon_map.items():
            name, color = value if isinstance(value, tuple) else (value, ICON_COLOR)
            btn.setIcon(load_icon(name, color))
            btn.setIconSize(QSize(ICON_SIZE, ICON_SIZE))

        # 初始化
        self.resizeEvent(None)

        for i in range(30):
            label = QLabel(f"测试消息 {i+1}")
            label.setStyleSheet("padding: 8px; color: black")
            self.ui.chatLayout.addWidget(label)

        # 事件过滤器：聊天区滚动条样式
        self.ui.chatScroll.installEventFilter(self)
        # 事件过滤器：点击别处收菜单 / 拉边框 / 按住按钮的样式
        # 装在 QApplication 上，这样窗口里任何控件的事件都会先经过这里
        QApplication.instance().installEventFilter(self)

        # 头像
        self.ui.avatarBtn.setIcon(QIcon(str(AVATAR_DIR / "原版-80x80.png")))
        self.ui.avatarBtn.setIconSize(QSize(60, 60))

# ====================自定义方法====================

    def resizeEvent(self, event):
        '''重写resizeEvent，动态调整各组件位置'''

        super().resizeEvent(event)
        QTimer.singleShot(0, self._update_input_row)  # 延迟更新输入区位置
        QTimer.singleShot(0, self._update_avatar_menu)  # 延迟更新头像菜单位置
        QTimer.singleShot(0, self._update_more_menu)  # 延迟更新更多菜单位置
        if getattr(self, 'memory_panel', None) is not None:
            QTimer.singleShot(0, self.memory_panel.refresh)  # 记忆面板跟着窗口尺寸走

    def closeEvent(self, event):
        '''主窗口关掉的时候，把子窗口一起带走（不然进程会赖在后台）'''

        if getattr(self, 'viewer', None) is not None:
            self.viewer.close()     # 查看器是独立窗口，findChildren 找不到它，得单独关
        for child in self.findChildren(QDialog):
            child.close()
        super().closeEvent(event)

    def _menu_top(self):
        '''两个下拉菜单共用的纵向起点：和标题栏底边齐平（现在都是 80）'''

        return self.ui.titleBar.height()

    def _hit(self, widget, global_pos):
        '''判断一个全局坐标是否落在某个控件身上'''

        return widget.rect().contains(widget.mapFromGlobal(global_pos))

    def _repolish(self, widget):
        '''改过动态属性之后，要让样式重新算一遍才会生效'''

        widget.style().unpolish(widget)
        widget.style().polish(widget)

    def _set_btn_active(self, btn, active):
        '''给按钮打上/去掉[菜单展开中]的标记，样式交给 QSS 里的 [menuOpen="true"]'''

        btn.setProperty("menuOpen", "true" if active else "false")
        self._repolish(btn)

    def _hold_btn(self, btn):
        '''按住按钮时挂上 [holding="true"] 标记

        QAbstractButton 自己的逻辑是：按住之后把鼠标移到按钮外面，就会取消按下状态。
        所以这里额外挂一个属性，样式靠它维持深灰，直到松开为止。
        头像按钮不参与（它有自己的旋转动画）。
        '''

        if btn is self.ui.avatarBtn or btn.objectName() == "avatarPick":
            return      # 头像按钮和缩略图上的透明按钮都不参与按住样式

        if self._holding_btn is not None and self._holding_btn is not btn:
            self._release_btn()     # 换了个按钮按，先把旧的收掉

        self._holding_btn = btn
        btn.setProperty("holding", "true")
        self._repolish(btn)

    def _release_btn(self):
        '''松开时把 [holding] 标记收掉'''

        btn = self._holding_btn
        self._holding_btn = None
        if btn is None:
            return

        btn.setProperty("holding", "false")
        self._repolish(btn)

    # ==========头像挑选区==========
    def _setup_avatar_picker(self):
        '''把四个缩略图和放大按钮填好，一开始整个挑选区是藏着的'''

        self.ui.avatarPicker.setVisible(False)      # 默认收起
        self.ui.chooseAvatarBtn.clicked.connect(self.toggle_avatar_picker)
        self._avatar_items = []     # [(缩略图 Label, 原图文件名, 缩略图文件名), ...]

        for label_name, thumb_file, full_file, zoom_name in AVATARS:
            # 缩略图（圆角，边框在选中的时候再画上去）
            label = getattr(self.ui, label_name)
            label.setScaledContents(False)
            self._avatar_items.append((label, full_file, thumb_file))

            # 缩略图上盖一层透明按钮：点它就选这张
            # （QLabel 本身不处理鼠标，走事件过滤器在有些环境下不稳，直接用按钮最省心）
            pick = QPushButton(label.parentWidget())
            pick.setObjectName("avatarPick")
            pick.setGeometry(0, 0, label.width(), label.height())
            pick.setCursor(Qt.CursorShape.PointingHandCursor)
            pick.clicked.connect(lambda _=False, f=full_file: self._set_avatar(f))
            pick.show()

            # 右上角的放大按钮
            zoom = getattr(self.ui, zoom_name)
            zoom.setIcon(load_icon("max"))
            zoom.setIconSize(QSize(16, 16))
            zoom.clicked.connect(lambda _=False, f=full_file: self.open_image_viewer(f))
            zoom.raise_()       # 放大按钮得压在透明按钮上面，不然点不到

        self._set_avatar(AVATARS[0][2])     # 默认是「原版」，边框会画在它上面

    def toggle_avatar_picker(self):
        '''「更换形象」和缩略图网格之间切换，菜单跟着伸缩'''

        show = not self.ui.avatarPicker.isVisible()
        self.ui.avatarPicker.setVisible(show)
        self.ui.editPersonaBtn.setVisible(not show)     # 挑图的时候先让一让
        self.ui.memoryBtn.setVisible(not show)
        self.ui.chooseAvatarBtn.setText("收起" if show else "更换形象")

        self._update_avatar_menu()      # 挑选区不做展开动画，直接换大小，干脆一点

    def _set_avatar(self, full_file):
        '''换头像：换掉左上角的图标，并把边框画到选中的那张缩略图上'''

        stem = Path(full_file).stem
        self.ui.avatarBtn.setIcon(QIcon(str(AVATAR_DIR / f"{stem}-80x80.png")))
        self.ui.avatarBtn.setIconSize(QSize(60, 60))
        self.avatar_file = full_file        # 记住当前用的是哪张

        for label, name, thumb_file in self._avatar_items:
            border = "#1e88e5" if name == full_file else None
            label.setPixmap(avatar_pixmap(AVATAR_DIR / thumb_file, 200, 12, border))

    def _reset_avatar_picker(self):
        '''把挑选区收回去，让下次展开还是最初的样子'''

        if not self.ui.avatarPicker.isVisible():
            return

        self.ui.avatarPicker.setVisible(False)
        self.ui.editPersonaBtn.setVisible(True)
        self.ui.memoryBtn.setVisible(True)
        self.ui.chooseAvatarBtn.setText("更换形象")
        self._update_avatar_menu()

    def open_image_viewer(self, file_name):
        '''打开图片查看器（模态，但不阻塞）

        用 show() 而不是 exec()：exec() 会在主事件循环里再套一层，
        关主窗口时子窗口还活着、终端 Ctrl+C 也进不来，很容易把进程卡死。
        '''

        # 主窗口能不能操作由查看器自己管（它会直接禁掉主窗口），
        # 这里不用 Qt 的模态：Wayland 下模态窗口是没法最小化的
        self.viewer = ImageViewer(AVATAR_DIR / file_name, owner=self, save_dir=self.save_dir)
        self.viewer.show()

    # ==========翻页 / 临时提示==========
    def go_page(self, index):
        '''切页：0 = 聊天，1 = 修改设定'''

        self.ui.stack.setCurrentIndex(index)

    def open_settings(self):
        '''从头像菜单进「修改设定」'''

        self.hide_avatar_menu()
        self.settings.load()        # 每次进页面都重新读一遍数据库
        self.go_page(1)

    def open_memory(self):
        '''从头像菜单打开记忆面板'''

        self.hide_avatar_menu()
        self.memory_panel.open()

    def show_toast(self, text, ms=2000):
        '''屏幕中下方弹出的灰色小提示：不挡操作，过一会儿自己消失'''

        self._toast.setText(text)
        self._toast.adjustSize()
        self._toast.move((self.ui.mainContainer.width() - self._toast.width()) // 2,
                         self.ui.mainContainer.height() - self._toast.height() - 150)
        self._toast.show()
        self._toast.raise_()
        self._toast_timer.start(ms)

    def _resize_menu(self, menu, update_func):
        '''菜单内容变了之后，把菜单大小用动画补上'''

        old = menu.geometry()
        update_func()               # 先按新内容算出目标大小并设进去
        target = menu.geometry()
        if old.height() == target.height():
            return                  # 没变就不用动画了

        menu.setGeometry(old)       # 拉回旧的大小，再动画过渡到新的
        anim = QPropertyAnimation(menu, b"geometry")
        anim.setDuration(self.avatar_event_time)
        anim.setStartValue(old)
        anim.setEndValue(target)
        anim.start()
        self.avatar_menu_anim = anim    # 防止被回收

    # ==========窗口拖动 / 拉边框==========
    def _edge_flags(self, pos):
        '''判断窗口内的坐标贴着哪几条边，返回 (左, 上, 右, 下)'''

        m = RESIZE_MARGIN
        return (pos.x() <= m,
                pos.y() <= m,
                pos.x() >= self.width() - RESIZE_MARGIN_RIGHT,
                pos.y() >= self.height() - m)

    def _cursor_for_edges(self, edges):
        '''按贴着哪条边/哪个角，给出对应的鼠标形状'''

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
        '''按住边框拖动时，按边改窗口大小

        注意这里是「夹住」而不是「超了就不动」，
        不然一旦拉过下限，窗口会弹回按下时的尺寸，手感很奇怪。
        '''

        left, top, right, bottom = self._resizing
        geo = QRect(self._resize_start_geo)
        dx = global_pos.x() - self._resize_start_pos.x()
        dy = global_pos.y() - self._resize_start_pos.y()
        min_w = self.ui.mainContainer.minimumWidth()
        min_h = self.ui.mainContainer.minimumHeight()

        if left:
            geo.setLeft(min(geo.left() + dx, geo.right() - min_w + 1))
        if right:
            geo.setRight(max(geo.right() + dx, geo.left() + min_w - 1))
        if top:
            geo.setTop(min(geo.top() + dy, geo.bottom() - min_h + 1))
        if bottom:
            geo.setBottom(max(geo.bottom() + dy, geo.top() + min_h - 1))

        self.setGeometry(geo)

    def _snap_by_drag(self, global_pos):
        '''拖到屏幕边缘就吸附：顶部=最大化，左右=半屏（只在自己挪窗口的兜底路径里用）'''

        # 拖得太短就先不吸附，免得窗口本来就在屏幕边上时一上手就被吸走
        if (global_pos - self._drag_start_pos).manhattanLength() < SNAP_MIN_DRAG:
            return False

        area = self.screen().availableGeometry()

        if global_pos.y() <= area.top() + SNAP_MARGIN:          # 顶边
            self.showMaximized()
            return True
        if global_pos.x() <= area.left() + SNAP_MARGIN:         # 左边
            self.showNormal()
            self.setGeometry(area.left(), area.top(), area.width() // 2, area.height())
            return True
        if global_pos.x() >= area.right() - SNAP_MARGIN:        # 右边
            self.showNormal()
            self.setGeometry(area.left() + area.width() - area.width() // 2,
                             area.top(), area.width() // 2, area.height())
            return True

        return False

    def _move_by_system(self, global_pos):
        '''把拖动整个交给系统

        Wayland 下客户端无权自己挪窗口，move() 是无效的，必须请合成器来拖；
        成功的话系统会接管指针，我们只要坐着等松开就行。
        系统不给的话（返回 False），退回自己算坐标挪。
        '''

        handle = self.windowHandle()
        if handle is not None and handle.startSystemMove():
            return True

        # 兜底：自己按鼠标位移挪窗口
        self._drag_start_pos = global_pos
        self._drag_offset = global_pos - self.frameGeometry().topLeft()
        return False

    # ==========标题栏相关事件==========
    def max_toggle(self):
        '''最大化/还原窗口'''

        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    # ==========头像相关事件==========
    def _animate_avatar(self, target_angle):
        '''把头像转到指定角度'''

        # 创建动画
        if getattr(self, 'avatar_anim', None):
            self.avatar_anim.stop()  # 停止当前动画

        anim = QPropertyAnimation(self.ui.avatarBtn, b"angle")
        anim.setDuration(self.avatar_event_time)          # 动画持续时间
        anim.setStartValue(self.ui.avatarBtn.angle)       # 从"当前真实角度"出发，中途打断也不会跳
        anim.setEndValue(target_angle)                    # 结束角度
        anim.start()                                      # 启动动画
        self.avatar_anim = anim                           # 保持引用，防止被垃圾回收

    def toggle_avatar_menu(self):
        '''头像菜单展开/收起切换'''

        if self.avatar_menu_open:
            self.hide_avatar_menu()
        else:
            self.show_avatar_menu()

    def _update_avatar_menu(self):
        '''更新头像菜单位置和大小'''

        # 位置
        avatar_pos = self.ui.avatarBtn.mapTo(self.ui.mainContainer, QPoint(0, 0))
        x = avatar_pos.x()
        y = self._menu_top()
        # 宽高都跟着内容自适应，最少留 MENU_MIN_W
        w = max(self.ui.avatarMenu.sizeHint().width(), MENU_MIN_W)
        h = self.ui.avatarMenu.sizeHint().height()
        self.ui.avatarMenu.setGeometry(max(x-15, 0), y, w, h)

    def show_avatar_menu(self):
        '''头像菜单展开动画'''

        self._update_avatar_menu()  # 定位

        target = self.ui.avatarMenu.geometry()  # 目标大小
        start = QRect(target.x(), target.y(), target.width(), 0)  # 起始大小
        self.ui.avatarMenu.setGeometry(start)  # 设置初始大小
        self.ui.avatarMenu.show()  # 显示菜单
        self.ui.avatarMenu.raise_()  # 确保菜单在最上层

        anim = QPropertyAnimation(self.ui.avatarMenu, b"geometry")
        anim.setDuration(self.avatar_event_time)  # 动画持续时间
        anim.setStartValue(start)  # 设置起始值
        anim.setEndValue(target)  # 设置结束值
        anim.start()  # 启动动画
        self.avatar_menu_anim = anim  # 防止被回收

        self.avatar_menu_open = True  # 记下状态
        self._animate_avatar(360)     # 头像转过去

    def hide_avatar_menu(self):
        '''头像菜单收起动画（收起的同时头像转回来）'''

        if not self.avatar_menu_open:
            return  # 已经收起就不重复播动画

        self._reset_avatar_picker()    # 收起菜单时把挑选区复位，下次展开还是最初的样子
        self.avatar_menu_open = False  # 先改状态，避免重复触发

        start = self.ui.avatarMenu.geometry()  # 起始大小
        end = QRect(start.x(), start.y(), start.width(), 0)  # 目标大小

        anim = QPropertyAnimation(self.ui.avatarMenu, b"geometry")  # 创建动画
        anim.setDuration(self.avatar_event_time)  # 动画持续时间
        anim.setStartValue(start)  # 设置起始值
        anim.setEndValue(end)  # 设置结束值
        anim.finished.connect(self.ui.avatarMenu.hide)  # 动画结束后隐藏菜单
        anim.start()  # 启动动画
        self.avatar_menu_anim = anim  # 防止被回收

        self._animate_avatar(0)  # 头像转回来

    # ==========更多按钮相关事件==========
    def toggle_more_menu(self):
        '''更多菜单展开/收起切换'''

        if self.more_menu_open:
            self.hide_more_menu()
        else:
            self.show_more_menu()

    def _update_more_menu(self):
        '''更新更多菜单位置和大小（横向以更多按钮为中心对称，纵向和头像菜单一致）'''

        btn_pos = self.ui.moreBtn.mapTo(self.ui.mainContainer, QPoint(0, 0))
        # 宽高都跟着内容自适应，最少留 MENU_MIN_W
        w = max(self.ui.moreMenu.sizeHint().width(), MENU_MIN_W)
        h = self.ui.moreMenu.sizeHint().height()
        # 居中：让菜单中心对准按钮中心
        x = btn_pos.x() + (self.ui.moreBtn.width() - w) // 2
        y = self._menu_top()  # 和头像菜单同一个高度
        self.ui.moreMenu.setGeometry(max(x, 0), y, w, h)

    def show_more_menu(self):
        '''更多菜单展开动画'''

        self._update_more_menu()  # 定位

        target = self.ui.moreMenu.geometry()  # 目标大小
        start = QRect(target.x(), target.y(), target.width(), 0)  # 起始大小
        self.ui.moreMenu.setGeometry(start)  # 设置初始大小
        self.ui.moreMenu.show()  # 显示菜单
        self.ui.moreMenu.raise_()  # 确保菜单在最上层

        anim = QPropertyAnimation(self.ui.moreMenu, b"geometry")
        anim.setDuration(self.avatar_event_time)  # 动画持续时间
        anim.setStartValue(start)  # 设置起始值
        anim.setEndValue(target)  # 设置结束值
        anim.start()  # 启动动画
        self.more_menu_anim = anim  # 防止被回收

        self.more_menu_open = True  # 记下状态
        self._set_btn_active(self.ui.moreBtn, True)  # 按钮保持深灰

    def hide_more_menu(self):
        '''更多菜单收起动画'''

        if not self.more_menu_open:
            return  # 已经收起就不重复播动画

        self.more_menu_open = False  # 先改状态，避免重复触发

        start = self.ui.moreMenu.geometry()  # 起始大小
        end = QRect(start.x(), start.y(), start.width(), 0)  # 目标大小

        anim = QPropertyAnimation(self.ui.moreMenu, b"geometry")  # 创建动画
        anim.setDuration(self.avatar_event_time)  # 动画持续时间
        anim.setStartValue(start)  # 设置起始值
        anim.setEndValue(end)  # 设置结束值
        anim.finished.connect(self.ui.moreMenu.hide)  # 动画结束后隐藏菜单
        anim.start()  # 启动动画
        self.more_menu_anim = anim  # 防止被回收

        self._set_btn_active(self.ui.moreBtn, False)  # 深灰褪回普通状态

    # ==========对话区相关事件==========
    def eventFilter(self, obj, event):
        '''事件过滤器：拖动窗口（titleBar）+ 点击别处收菜单 / 拉边框 / 按住按钮（全局）'''

        # 只看本窗口自己的事件：图片查看器是独立窗口，它的事件不归这里管。
        # 否则它上面靠近主窗口边缘的按钮，会被当成「在拉主窗口的边框」而吃掉按下事件。
        if obj is not self and (not isinstance(obj, QWidget) or obj.window() is not self):
            return super().eventFilter(obj, event)

        # ----拖动窗口：只处理标题栏自己收到的那些事件----
        # 按钮的点击是发给按钮的，压根不会走到这里，所以不会互相打架
        if ENABLE_WINDOW_MOVE and obj is self.ui.titleBar:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
                self._move_by_system(event.globalPosition().toPoint())
                return True
            if (event.type() == QEvent.MouseMove and self._drag_offset is not None
                    and (event.buttons() & Qt.MouseButton.LeftButton)):
                global_pos = event.globalPosition().toPoint()
                self.move(global_pos - self._drag_offset)   # 兜底路径：自己挪
                if self._snap_by_drag(global_pos):          # 贴到屏幕边就吸附
                    self._drag_offset = None
                return True
            if event.type() == QEvent.MouseButtonRelease:
                self._drag_offset = None
                self._drag_start_pos = None

        # ----菜单相关：点击窗口里除菜单和它对应按钮以外的位置，就收起----
        if event.type() == QEvent.MouseButtonPress:
            global_pos = event.globalPosition().toPoint()
            if self.avatar_menu_open and not (
                    self._hit(self.ui.avatarMenu, global_pos) or
                    self._hit(self.ui.avatarBtn, global_pos)):
                self.hide_avatar_menu()
            if self.more_menu_open and not (
                    self._hit(self.ui.moreMenu, global_pos) or
                    self._hit(self.ui.moreBtn, global_pos)):
                self.hide_more_menu()

            # 记忆面板：点面板以外的地方收起；点面板里面则收起它自己的菜单
            if self.memory_panel.is_open:
                if not self._hit(self.ui.memoryWidget, global_pos):
                    self.memory_panel.close()
                elif (self.memory_panel.menu_open
                      and not self._hit(self.ui.memoryMoreMenu, global_pos)
                      and not self._hit(self.ui.memoryMoreBtn, global_pos)):
                    self.memory_panel.hide_menu()

        # ----按住的样式 / 拉边框 / 鼠标形状----
        if event.type() in (QEvent.MouseMove, QEvent.MouseButtonPress,
                            QEvent.MouseButtonRelease, QEvent.MouseButtonDblClick):
            global_pos = event.globalPosition().toPoint()
            local_pos = self.mapFromGlobal(global_pos)

            if event.type() == QEvent.MouseMove:
                if self._resizing:                          # 正在拉边框
                    self._resize_by_drag(global_pos)
                    return True
                if not (event.buttons() & Qt.MouseButton.LeftButton):
                    cursor = self._cursor_for_edges(self._edge_flags(local_pos))  # 空手移动，改光标形状
                    if cursor:
                        self.setCursor(cursor)
                    else:
                        self.unsetCursor()

            elif event.type() in (QEvent.MouseButtonPress, QEvent.MouseButtonDblClick) \
                    and event.button() == Qt.MouseButton.LeftButton:
                if isinstance(obj, QAbstractButton):
                    self._hold_btn(obj)                     # 按住的样子留住，拖出按钮外也不掉
                elif any(self._edge_flags(local_pos)):      # 按在窗口边框上，开始拉
                    self._resizing = self._edge_flags(local_pos)
                    self._resize_start_geo = self.geometry()
                    self._resize_start_pos = global_pos
                    return True

            elif event.type() == QEvent.MouseButtonRelease:
                self._resizing = None   # 松开就结束缩放
                self._release_btn()     # 也把按钮的深灰收掉

        # ----滚动条样式----
        if obj == self.ui.chatScroll:
            bar = self.ui.chatScroll.verticalScrollBar()
            if event.type() == QEvent.Enter:
                bar.setStyleSheet('''
                    QScrollBar::handle:vertical {
                        background: #d0d0d0;
                        border-radius: 2px;
                        min-height: 30px;
                        margin: 2px;
                    }

                    QScrollBar::handle:vertical:hover {
                        background: #b0b0b0;
                        border-radius: 4px;
                        margin: 0px;
                    }

                ''')
            elif event.type() == QEvent.Leave:
                bar.setStyleSheet('''
                    QScrollBar::handle:vertical {
                        background: transparent;
                    }
                ''')
        return super().eventFilter(obj, event)

    # ==========输入区相关事件==========
    def _toggle_send_btn(self):
        '''输入框有内容就显示发送按钮，空着就藏起来（纯空格不算）'''

        has_text = bool(self.ui.inputEdit.toPlainText().strip())
        self.ui.sendBtn.setVisible(has_text)

    def _update_input_row(self):
        '''更新输入区位置和大小

        输入区和渐变遮罩现在挂在 page1 上（绝对定位），
        所以尺寸要按 page1 算，不能再用整个窗口的宽高。
        '''

        page = self.ui.page1
        h = 50                              # 输入区高度
        w = page.width()
        y = page.height() - h - INPUT_BOTTOM_GAP    # 贴着页面底部往上留一点

        self.ui.inputRow.setGeometry(0, y, w, h)     # 设置输入区位置和大小
        self.ui.fadeMask.setGeometry(0, y, w-8, 82)  # 设置渐变遮罩位置和大小
        self.ui.inputRow.raise_()                    # 输入区得压在渐变遮罩上面

        # 加载完毕后，滚动到底部
        scrollbar = self.ui.chatScroll.verticalScrollBar()
        QTimer.singleShot(0, lambda: scrollbar.setValue(scrollbar.maximum()))  # 滚动到底部






if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 让终端的 Ctrl+C 能生效：Qt 的事件循环在 C++ 里跑、不执行 Python 字节码，
    # 信号处理函数一直没机会执行，所以用一个空定时器时不时把控制权还给 Python
    def _on_sigint(*_):
        '''收到 Ctrl+C 就直接让 Qt 退出（光靠抛异常会被 Qt 接住，程序不走）'''

        app.quit()

    signal.signal(signal.SIGINT, _on_sigint)
    keep_alive = QTimer()
    keep_alive.timeout.connect(lambda: None)   # 定时把控制权还给 Python，信号才有机会被处理
    keep_alive.start(200)

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
