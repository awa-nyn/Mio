'''记忆面板：从左边滑出来、盖在对话区上的那块

界面在 GUI.py（pyuic 生成的）里，这里只放逻辑。
数据来自 core/mem.py：get_memory() 拿全部，del_memory([id...]) 删指定的。
'''

import sys
from pathlib import Path

from PySide6.QtCore import (QEvent, QObject, QPoint, QRect, QRectF, QSize, Qt,
                            QPropertyAnimation)
from PySide6.QtGui import QColor, QIcon, QPainter, QPainterPath, QPen, QPixmap
from PySide6.QtWidgets import (QGraphicsDropShadowEffect, QHBoxLayout, QLabel,
                               QToolButton, QVBoxLayout, QWidget)

from ui_common import BUTTON_DIR, load_icon
from info_dialog import InfoDialog

# 让 GUI 里的代码能 import 到 Agent/core
AGENT_DIR = Path(__file__).parent.parent
if str(AGENT_DIR) not in sys.path:
    sys.path.append(str(AGENT_DIR))

try:
    from core.mem import del_memory, get_memory      # noqa: E402
except Exception as exc:                             # 配置没填全（比如没 API Key）时别把整个界面拖垮
    print(f"记忆功能暂时用不了：{exc}")

    def get_memory():
        '''读不到就当作没有记忆'''

        return None

    def del_memory(memory_ids):
        '''删不了也返回失败，界面照常跑'''

        return False

MARGIN_LEFT = 0         # 贴在窗口最左边（所以左边不做圆角）
RIGHT_KEEP = 50         # 右边缘最多拉到「窗口宽 - 50」
HANDLE = 6              # 右边缘多宽的一条算「抓到了」用来拖宽
TITLE_TOP_PAD = 8       # 面板顶部到「记忆」那一条之间留的空
TITLE_HEIGHT = 40       # 「记忆」那一条的高度（要装得下放大的按钮）
MIN_WIDTH = 200         # 面板最窄能到多少
DEFAULT_WIDTH = 300     # 每次开面板的默认宽度
ANIM_MS = 260           # 滑出/收起动画时长


def _check_icon(checked, size=18):
    '''画一个方框图标：没勾是淡灰空框，勾上是蓝底白勾

    用画的而不是找图片：这样颜色和大小都在代码里，改起来不用动资源文件。
    '''

    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.transparent)

    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    box = QRectF(0.5, 0.5, size - 1, size - 1)

    if checked:
        painter.setPen(QPen(QColor("#1e88e5"), 1))
        painter.setBrush(QColor("#1e88e5"))
        painter.drawRoundedRect(box, 4, 4)
        # 白勾
        pen = QPen(QColor("#ffffff"), 2)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        painter.setPen(pen)
        path = QPainterPath()
        path.moveTo(size * 0.26, size * 0.52)
        path.lineTo(size * 0.44, size * 0.70)
        path.lineTo(size * 0.75, size * 0.32)
        painter.drawPath(path)
    else:
        painter.setPen(QPen(QColor("#c8c8c8"), 1))
        painter.setBrush(QColor("#f0f0f0"))
        painter.drawRoundedRect(box, 4, 4)

    painter.end()
    return QIcon(pixmap)


def _trash_icon(color):
    '''垃圾桶图标：button 目录里叫什么都行，找不到就退回红叉'''

    for name in ("trash", "delete", "remove", "垃圾桶"):
        if (BUTTON_DIR / f"{name}.svg").exists():
            return load_icon(name, color)
    return load_icon("close", color)


class MemoryPanel(QObject):
    '''记忆面板

    window：主窗口（用来拿 ui、算尺寸、弹确认框）
    '''

# ====================初始化====================

    def __init__(self, window):
        super().__init__(window)    # 要继承 QObject 才能当事件过滤器用
        self.window = window
        self.ui = window.ui
        self.is_open = False
        self.manage_mode = False
        self.menu_open = False
        self.ui.memoryWidget.setMinimumWidth(MIN_WIDTH)     # .ui 里写的是 250，这里收到 200
        self.width = DEFAULT_WIDTH                          # 默认宽度
        self.cards = {}             # 记忆 id -> {"widget", "check", "delete"}
        self._dragging = False      # 正在拖右边缘
        self._drag_start = None
        self._drag_start_width = 0
        self._no_memory_label = None

        self.ui.memoryWidget.hide()
        self.ui.memoryMoreMenu.hide()

        # 内层边距：上边留一点空，右边留 6px 给「拖宽」那条把手（滚动条别贴着边）
        self.ui.verticalLayout_8.setContentsMargins(0, TITLE_TOP_PAD, HANDLE, 0)

        # 菜单那层布局的边距收紧：默认那圈边距太大，看着像右边空了一大块
        menu_layout = self.ui.memoryMoreMenu.layout()
        menu_layout.setContentsMargins(4, 4, 4, 4)
        menu_layout.setSpacing(2)

        # 标题那一条抬高点，放大后的按钮才不挤
        self.ui.memoryTitle.setMinimumHeight(TITLE_HEIGHT)
        self.ui.memoryTitle.setMaximumHeight(TITLE_HEIGHT)

        # 向右偏的阴影，看起来像是浮在对话区上面
        shadow = QGraphicsDropShadowEffect(self.ui.memoryWidget)
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 75))
        shadow.setOffset(8, 0)
        self.ui.memoryWidget.setGraphicsEffect(shadow)

        # 图标
        self.ui.memoryMoreBtn.setIcon(load_icon("more"))
        self.ui.memoryMoreBtn.setIconSize(QSize(20, 20))
        self.ui.memoryMoreBtn.setText("")
        self.ui.delMemoryBtn.setIcon(_trash_icon("#e05a5a"))
        self.ui.delMemoryBtn.setIconSize(QSize(20, 20))
        self.ui.delMemoryBtn.setText("")
        self.ui.delMemoryBtn.hide()

        # 管理模式里顶替「更多」的那个「取消」按钮（.ui 里没有，这里用代码建）
        # QToolButton 设成「只显示文字」，用起来就跟 push button 一样
        self.cancel_manage_btn = QToolButton(self.ui.memoryTitle)
        self.cancel_manage_btn.setObjectName("memoryManageCancel")
        self.cancel_manage_btn.setText("取消")
        self.cancel_manage_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.cancel_manage_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.cancel_manage_btn.clicked.connect(lambda: self._set_manage(False))
        self.cancel_manage_btn.hide()
        self.ui.horizontalLayout_12.addWidget(self.cancel_manage_btn)

        # 菜单里两项的文字（清空那个在 QSS 里配成红字）
        self.ui.manageBtn.setText("管理")
        self.ui.clearBtn.setText("清空")

        # 信号
        self.ui.memoryMoreBtn.clicked.connect(self.toggle_menu)
        self.ui.manageBtn.clicked.connect(self.toggle_manage)
        self.ui.clearBtn.clicked.connect(self.clear_all)
        self.ui.delMemoryBtn.clicked.connect(self.delete_checked)

        # 右边缘拖宽
        self.ui.memoryWidget.installEventFilter(self)

# ====================位置 / 开合====================

    def _region(self):
        '''面板该占的位置：贴窗口左边，纵向从标题栏下沿到状态栏上沿'''

        container = self.ui.mainContainer
        y = self.ui.titleBar.height()
        height = max(container.height() - y - self.ui.statusBar.height(), 100)

        min_w = self.ui.memoryWidget.minimumWidth()
        width = max(min_w, min(self.width, container.width() - RIGHT_KEEP))

        return QRect(MARGIN_LEFT, y, width, height)

    def _stop_anim(self):
        '''停掉正在跑的滑出/收起动画

        不停的话，动画每个 tick 都会把面板拉回它的目标宽度，
        用户在滑出过程中去拖右边那条边就会被「按回去」。
        '''

        anim = getattr(self, '_anim', None)
        if anim is not None and anim.state() == QPropertyAnimation.State.Running:
            anim.stop()

    def refresh(self):
        '''窗口大小变了之后重算位置（开着才动）'''

        if self.is_open:
            self._stop_anim()
            self.ui.memoryWidget.setGeometry(self._region())
            self._place_menu()

    def open(self):
        '''滑出来'''

        self.reload()
        self._set_manage(False)     # 每次打开都从「非管理模式」开始
        target = self._region()
        # 从屏幕左边外面滑进来：宽度不变，改的是 x
        start = QRect(target.x() - target.width(), target.y(), target.width(), target.height())
        self.ui.memoryWidget.setGeometry(start)
        self.ui.memoryWidget.show()
        self.ui.memoryWidget.raise_()

        anim = QPropertyAnimation(self.ui.memoryWidget, b"geometry")
        anim.setDuration(ANIM_MS)
        anim.setStartValue(start)
        anim.setEndValue(target)
        anim.start()
        self._anim = anim
        self.is_open = True

    def close(self):
        '''收回去'''

        if not self.is_open:
            return

        self.is_open = False
        self.hide_menu()
        self._set_manage(False)     # 收起时也退出管理模式，免得「取消」那个状态留着

        start = self.ui.memoryWidget.geometry()
        end = QRect(start.x() - start.width(), start.y(), start.width(), start.height())

        anim = QPropertyAnimation(self.ui.memoryWidget, b"geometry")
        anim.setDuration(ANIM_MS)
        anim.setStartValue(start)
        anim.setEndValue(end)
        anim.finished.connect(self.ui.memoryWidget.hide)
        anim.start()
        self._anim = anim

# ====================右边缘拖宽====================

    def eventFilter(self, obj, event):
        '''在面板右边缘那条细带上按住拖动，就能把它拉宽'''

        if obj is not self.ui.memoryWidget:
            return False

        if event.type() == QEvent.MouseMove and not (event.buttons() & Qt.MouseButton.LeftButton):
            near_edge = event.position().x() >= self.ui.memoryWidget.width() - HANDLE
            self.ui.memoryWidget.setCursor(
                Qt.CursorShape.SizeHorCursor if near_edge else Qt.CursorShape.ArrowCursor)

        elif event.type() == QEvent.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
            if event.position().x() >= self.ui.memoryWidget.width() - HANDLE:
                self._stop_anim()       # 拖的时候别让动画跟我们抢宽度
                self._dragging = True
                self._drag_start = event.globalPosition().toPoint()
                self._drag_start_width = self.ui.memoryWidget.width()
                return True

        elif event.type() == QEvent.MouseMove and self._dragging:
            moved = event.globalPosition().toPoint().x() - self._drag_start.x()
            self.width = self._drag_start_width + moved
            self.ui.memoryWidget.setGeometry(self._region())
            self._place_menu()
            return True

        elif event.type() == QEvent.MouseButtonRelease:
            self._dragging = False

        return False

# ====================读取与画卡片====================

    def reload(self):
        '''重新读一遍记忆，把卡片画出来'''

        self._clear_cards()
        memories = get_memory() or []
        has_memory = bool(memories)

        # 没记忆的时候，菜单里那两项是灰的
        self.ui.manageBtn.setEnabled(has_memory)
        self.ui.clearBtn.setEnabled(has_memory)

        self._no_memory().setVisible(not has_memory)
        if not has_memory:
            self._set_manage(False)
            return

        for memory in memories:
            self._add_card(memory)

        self.ui.memoryAreaWidget.layout().addStretch(1)
        self._refresh_del_btn()

    def _clear_cards(self):
        '''把上一次画的卡片和弹簧都清掉'''

        layout = self.ui.memoryAreaWidget.layout()
        for info in self.cards.values():
            layout.removeWidget(info["widget"])
            info["widget"].deleteLater()
        self.cards.clear()

        for i in reversed(range(layout.count())):
            if layout.itemAt(i).spacerItem() is not None:
                layout.takeAt(i)

    def _no_memory(self):
        '''「还没有记忆」那条提示：.ui 里有就用它的，没有就现建一个'''

        if self._no_memory_label is None:
            label = getattr(self.ui, "noMemoryLabel", None)
            if label is None:
                label = QLabel("还没有记录任何记忆喵", self.ui.memoryAreaWidget)
                label.setObjectName("noMemoryLabel")
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.ui.memoryAreaWidget.layout().addWidget(label)
                self.ui.noMemoryLabel = label
            self._no_memory_label = label

        return self._no_memory_label

    def _add_card(self, memory):
        '''一张记忆卡片：正文 + 左下角日期 + 右边删除（管理模式变成勾选框）'''

        card = QWidget(self.ui.memoryAreaWidget)
        card.setObjectName("memoryCard")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(12, 10, 12, 10)
        card_layout.setSpacing(6)

        text = QLabel(str(memory.get("content", "")), card)
        text.setObjectName("memoryText")
        text.setWordWrap(True)
        text.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        card_layout.addWidget(text)

        bottom = QWidget(card)
        bottom_layout = QHBoxLayout(bottom)
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(6)

        date = QLabel(str(memory.get("timestamp") or ""), bottom)
        date.setObjectName("memoryDate")
        bottom_layout.addWidget(date)
        bottom_layout.addStretch(1)

        # 勾选框用可切换的按钮：图标自己在代码里画，所以能做成蓝底白勾
        check = QToolButton(bottom)
        check.setObjectName("memoryCheck")
        check.setCheckable(True)
        check.setIcon(_check_icon(False))
        check.setIconSize(QSize(18, 18))
        check.setCursor(Qt.CursorShape.PointingHandCursor)
        check.hide()
        check.toggled.connect(lambda _=False, c=check: self._on_check_toggled(c))
        bottom_layout.addWidget(check)

        delete = QToolButton(bottom)
        delete.setObjectName("memoryDel")
        delete.setIcon(load_icon("close", "#d9534f"))
        delete.setIconSize(QSize(18, 18))
        delete.setToolTip("删除这条记忆")
        delete.clicked.connect(lambda _=False, m=memory: self.delete_one(m))
        bottom_layout.addWidget(delete)

        card_layout.addWidget(bottom)
        self.ui.memoryAreaWidget.layout().addWidget(card)

        self.cards[memory.get("id")] = {"widget": card, "check": check, "delete": delete}

# ====================菜单====================

    def _place_menu(self):
        '''菜单贴着更多按钮的右下角'''

        btn = self.ui.memoryMoreBtn
        pos = btn.mapTo(self.ui.mainContainer, QPoint(0, 0))
        width = max(self.ui.memoryMoreMenu.sizeHint().width(), 78)   # 宽度只按内容算
        height = self.ui.memoryMoreMenu.sizeHint().height()
        x = pos.x() + btn.width() - width
        y = pos.y() + btn.height() + 4
        self.ui.memoryMoreMenu.setGeometry(max(x, 0), y, width, height)

    def toggle_menu(self):
        if self.menu_open:
            self.hide_menu()
        else:
            self.show_menu()

    def show_menu(self):
        self._place_menu()
        self.ui.memoryMoreMenu.show()
        self.ui.memoryMoreMenu.raise_()
        self.menu_open = True

    def hide_menu(self):
        if not self.menu_open:
            return
        self.ui.memoryMoreMenu.hide()
        self.menu_open = False

# ====================管理模式 / 删除====================

    def toggle_manage(self):
        '''菜单里的「管理」：把每张卡片右边的红叉换成勾选框'''

        self._set_manage(not self.manage_mode)
        self.hide_menu()

    def _set_manage(self, on):
        '''开关管理模式

        开着的时候：右上角的「更多」换成「取消」，垃圾桶出现，卡片右边换成勾选框
        '''

        self.manage_mode = on
        self.cancel_manage_btn.setVisible(on)
        self.ui.memoryMoreBtn.setVisible(not on)
        self.ui.delMemoryBtn.setVisible(on)
        self.ui.manageBtn.setText("管理")       # 菜单里那项永远叫「管理」

        for info in self.cards.values():
            info["check"].setChecked(False)
            info["check"].setVisible(on)
            info["delete"].setVisible(not on)

        self._refresh_del_btn()

    def _on_check_toggled(self, button):
        '''勾选状态变了：换图标颜色，并刷新右上角垃圾桶'''

        button.setIcon(_check_icon(button.isChecked()))
        self._refresh_del_btn()

    def _refresh_del_btn(self):
        '''勾选了任意一条，垃圾桶才变红可用'''

        checked = any(info["check"].isChecked() for info in self.cards.values())
        self.ui.delMemoryBtn.setEnabled(checked)
        self.ui.delMemoryBtn.setIcon(_trash_icon("#e05a5a" if checked else "#c8c8c8"))

    def delete_one(self, memory):
        '''单条删除'''

        index = InfoDialog.ask(self.window, "确认删除？", "此操作无法恢复。", ["取消", "确认"], danger=1)
        if index == 1:
            del_memory([memory.get("id")])
            self.reload()

    def delete_checked(self):
        '''删掉所有勾选的'''

        ids = [mid for mid, info in self.cards.items() if info["check"].isChecked()]
        if not ids:
            return

        index = InfoDialog.ask(self.window, "确认删除？",
                               f"将删除 {len(ids)} 条记忆，此操作无法恢复。",
                               ["取消", "确认"], danger=1)
        if index == 1:
            del_memory(ids)
            self._set_manage(False)
            self.reload()

    def clear_all(self):
        '''清空全部记忆'''

        ids = list(self.cards)
        if not ids:
            return

        index = InfoDialog.ask(self.window, "确认清空所有记忆？",
                               "此操作无法恢复。", ["取消", "确认"], danger=1)
        if index == 1:
            del_memory(ids)
            self._set_manage(False)
            self.reload()
