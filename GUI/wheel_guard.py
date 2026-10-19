'''滚轮守卫：鼠标划过下拉框、数字框时别偷偷改值

默认行为：这类控件一律不吃滚轮（想改值就点它、拖它、或者拿键盘改）。
被吃掉的滚轮会转交给外面的滚动区，所以页面照常滚。

可切换：把 ALLOW_AFTER_CLICK 改成 True，就变成「点过它之后，滚轮才生效」。

为什么不看 hasFocus：窗口一显示，第一个能拿焦点的控件会自动拿到焦点，
设置页的第一项又常常正好是下拉框，只看 hasFocus 等于没有门槛。

用法（装一次，管全局）：
    self.wheel_guard = WheelGuard(self)
    QApplication.instance().installEventFilter(self.wheel_guard)
'''

from PySide6.QtCore import QEvent, QObject, QPointF, Qt
from PySide6.QtGui import QWheelEvent
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox,
                               QApplication, QComboBox, QSlider, QWidget)


class WheelGuard(QObject):
    '''给「滚轮一划就改值」的控件加一道门槛'''

    # 要管的控件类型。不想管滑块就把 QSlider 去掉。
    TYPES = (QComboBox, QAbstractSpinBox, QSlider)

    ALLOW_AFTER_CLICK = True    # True = 点过之后滚轮才生效；False = 一律不吃滚轮

    # 焦点策略：滚轮不给焦点，点一下才给。
    # Qt 默认的 WheelFocus 会让鼠标滚过就「看着像选中」，改掉之后就不会了。
    FOCUS_POLICY = Qt.FocusPolicy.StrongFocus

    def __init__(self, parent=None):
        super().__init__(parent)
        self._clicked = None    # 最近一次鼠标点到的受管控件

    # ==========工具==========
    def apply(self, root):
        '''把某个控件底下的受管控件都设一遍焦点策略

        启动时扫一次，之后新加的控件由事件过滤器兜底补上。
        '''

        for widget in root.findChildren(QWidget):
            if isinstance(widget, self.TYPES):
                widget.setFocusPolicy(self.FOCUS_POLICY)


    def _guarded(self, widget):
        '''从这个控件往上找最近的受管控件（点在数字框的子控件上也算点到它）

        注意：应用级的过滤器也会收到 QWindow 之类的事件，它们没有 parentWidget()，
        所以每一步都要先确认是 QWidget 再往上爬。
        '''

        while widget is not None and not isinstance(widget, self.TYPES):
            if not isinstance(widget, QWidget):
                return None
            widget = widget.parentWidget()
        return widget

    def _scroll_area(self, widget):
        '''往上找最近的滚动区'''

        parent = widget.parentWidget() if isinstance(widget, QWidget) else None
        while parent is not None:
            if isinstance(parent, QAbstractScrollArea):
                return parent
            parent = parent.parentWidget() if isinstance(parent, QWidget) else None
        return None

    def _forward(self, widget, event):
        '''把滚轮转交给滚动区的视口，让页面继续滚'''

        area = self._scroll_area(widget)
        if area is None:
            return
        viewport = area.viewport()
        local = QPointF(viewport.mapFromGlobal(event.globalPosition().toPoint()))
        moved = QWheelEvent(local, event.globalPosition(),
                            event.pixelDelta(), event.angleDelta(),
                            event.buttons(), event.modifiers(),
                            event.phase(), event.inverted())
        QApplication.sendEvent(viewport, moved)

    # ==========事件过滤==========
    def eventFilter(self, obj, event):
        if isinstance(obj, self.TYPES) and obj.focusPolicy() != self.FOCUS_POLICY:
            obj.setFocusPolicy(self.FOCUS_POLICY)       # 后加进来的控件也补上

        if event.type() == QEvent.Type.MouseButtonPress:
            self._clicked = self._guarded(obj)
            return False

        if event.type() == QEvent.Type.Wheel and isinstance(obj, self.TYPES):
            if self.ALLOW_AFTER_CLICK and self._clicked is obj:
                return False                    # 点过它了，滚轮放行
            self._forward(obj, event)
            return True                         # 原事件不给控件，值不会变

        return False
