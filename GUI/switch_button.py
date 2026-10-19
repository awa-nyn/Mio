'''自己画的滑动开关（不依赖第三方库）

Designer 里怎么用：
    放一个 QCheckBox → 右键 → 「提升为……」
    基类名称：QCheckBox
    提升的类名称：SwitchButton
    头文件：switch_button        （本文件名，不带 .py）

行为跟 QCheckBox 完全一致：isChecked() / setChecked() / toggled / clicked / setEnabled
全都能用，所以代码里不用区分它是开关还是勾选框。

颜色和尺寸可以在 QSS 里改（不写就用下面的默认值）：
    #someSwitch {
        qproperty-on_color: #1e88e5;      /* 打开时的底色 */
        qproperty-off_color: #cfcfcf;     /* 关闭时的底色 */
        qproperty-knob_color: #ffffff;    /* 圆球 */
        qproperty-track_width: 46;        /* 底槽宽度 */
        qproperty-track_height: 24;       /* 底槽高度 */
    }
'''

from PySide6.QtCore import (Property, QEasingCurve, QPropertyAnimation, QRectF,
                            QSize, Qt)
from PySide6.QtGui import QColor, QFontMetrics, QPainter
from PySide6.QtWidgets import QCheckBox

ANIM_MS = 160       # 滑动动画时长


class SwitchButton(QCheckBox):
    '''滑动开关：底槽 + 圆球，圆球从左滑到右'''

    def __init__(self, parent=None):
        super().__init__(parent)

        self._on_color = QColor("#1e88e5")
        self._off_color = QColor("#cfcfcf")
        self._knob_color = QColor("#ffffff")
        self._disabled_color = QColor("#ededed")
        self._track_width = 46
        self._track_height = 24
        self._position = 1.0 if self.isChecked() else 0.0

        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(self._track_height)

        self._anim = QPropertyAnimation(self, b"position", self)
        self._anim.setDuration(ANIM_MS)
        self._anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.toggled.connect(self._slide)

    # ==========滑动动画==========
    def get_position(self):
        return self._position

    def set_position(self, value):
        self._position = value
        self.update()

    position = Property(float, get_position, set_position)

    def _slide(self, checked):
        '''状态变了就让圆球滑过去'''

        self._anim.stop()
        self._anim.setStartValue(self._position)
        self._anim.setEndValue(1.0 if checked else 0.0)
        self._anim.start()

    # ==========QSS 里可调的属性==========
    def get_on_color(self):
        return self._on_color

    def set_on_color(self, color):
        self._on_color = QColor(color)
        self.update()

    def get_off_color(self):
        return self._off_color

    def set_off_color(self, color):
        self._off_color = QColor(color)
        self.update()

    def get_knob_color(self):
        return self._knob_color

    def set_knob_color(self, color):
        self._knob_color = QColor(color)
        self.update()

    def get_track_width(self):
        return self._track_width

    def set_track_width(self, value):
        self._track_width = max(24, int(value))
        self.updateGeometry()
        self.update()

    def get_track_height(self):
        return self._track_height

    def set_track_height(self, value):
        self._track_height = max(12, int(value))
        self.setMinimumHeight(self._track_height)
        self.updateGeometry()
        self.update()

    on_color = Property(QColor, get_on_color, set_on_color)
    off_color = Property(QColor, get_off_color, set_off_color)
    knob_color = Property(QColor, get_knob_color, set_knob_color)
    track_width = Property(int, get_track_width, set_track_width)
    track_height = Property(int, get_track_height, set_track_height)

    # ==========尺寸与绘制==========
    def sizeHint(self):
        '''控件大小 = 底槽 + 右边可能有的文字'''

        width = self._track_width
        height = max(self._track_height, super().sizeHint().height())
        if self.text():
            width += 8 + QFontMetrics(self.font()).horizontalAdvance(self.text())
        return QSize(width, height)

    def minimumSizeHint(self):
        return QSize(self._track_width, self._track_height)

    def hitButton(self, pos):
        '''整个控件都算可点区域

        QCheckBox 默认只认「指示器 + 文字」那一小块，控件拉长之后右边就成了死区。
        '''

        return self.rect().contains(pos)

    def _mirrored(self):
        '''文字和底槽谁在左谁在右，看 layoutDirection

        在 Designer 里把「布局方向」设成从右到左（RightToLeft），
        就变成「文字靠左、开关靠右」——一行设置项通常就是这样。
        默认（从左到右）是「开关靠左、文字紧跟其后」。
        '''

        return self.layoutDirection() == Qt.LayoutDirection.RightToLeft

    def _track_rect(self):
        '''底槽的位置：竖直居中，横向按 layoutDirection 靠左或靠右'''

        height = min(self._track_height, self.height())
        top = (self.height() - height) / 2
        left = self.width() - self._track_width if self._mirrored() else 0
        return QRectF(left, top, self._track_width, height)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        track = self._track_rect()

        # 底色：从「关闭色」到「打开色」按圆球位置插值；禁用时是灰的
        if self.isEnabled():
            color = QColor(
                round(self._off_color.red() + (self._on_color.red() - self._off_color.red()) * self._position),
                round(self._off_color.green() + (self._on_color.green() - self._off_color.green()) * self._position),
                round(self._off_color.blue() + (self._on_color.blue() - self._off_color.blue()) * self._position),
            )
        else:
            color = self._disabled_color

        radius = track.height() / 2
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(color)
        painter.drawRoundedRect(track, radius, radius)

        # 圆球：竖直方向永远以槽心为中线，这样按下去也不会往下偏
        margin = max(2.0, track.height() * 0.11)
        knob_height = track.height() - margin * 2
        knob_width = knob_height
        if self.isDown():
            # 按住的时候只往横向胖一点，像被按扁了
            knob_width += min(track.width() * 0.2, knob_height * 0.4)

        room = max(track.width() - knob_width - margin * 2, 0)
        x = track.left() + margin + room * self._position
        y = track.center().y() - knob_height / 2

        painter.setBrush(self._knob_color)
        painter.drawRoundedRect(QRectF(x, y, knob_width, knob_height),
                                knob_height / 2, knob_height / 2)

        # 文字：默认画在底槽右边；布局方向是从右到左时，画在最左边
        if self.text():
            metrics = QFontMetrics(self.font())
            text_y = (self.height() + metrics.ascent() - metrics.descent()) / 2
            text_x = 0 if self._mirrored() else track.right() + 8
            painter.setPen(self.palette().color(self.foregroundRole()))
            painter.drawText(int(text_x), int(text_y), self.text())

        painter.end()

    # ==========调试用：单独跑这个文件就能看效果==========
    if __name__ == '__main__':
        import sys

        from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

        app = QApplication(sys.argv)
        window = QWidget()
        window.setStyleSheet("background: white;")
        layout = QVBoxLayout(window)

        for checked in (False, True):
            switch = SwitchButton()
            switch.setChecked(checked)
            switch.setText("已开启" if checked else "已关闭")
            layout.addWidget(switch)

        disabled = SwitchButton()
        disabled.setText("禁用状态")
        disabled.setEnabled(False)
        layout.addWidget(disabled)

        window.resize(240, 180)
        window.show()
        sys.exit(app.exec())
