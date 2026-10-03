from PySide6.QtCore import Property
from PySide6.QtGui import QPainter, QPainterPath
from PySide6.QtWidgets import QToolButton


class AvatarButton(QToolButton):
    '''自定义头像按钮'''

    # ==========初始化==========
    def __init__(self, parent=None):
        super().__init__(parent)
        self._angle = 0

    # ==========属性==========
    def get_angle(self):
        return self._angle

    def set_angle(self, value):
        self._angle = value
        self.update()

    angle = Property(int, get_angle, set_angle)

    # ==========绘制==========
    def paintEvent(self, event):
        # 绘制旋转后的图标
        painter = QPainter(self)
        # 设置抗锯齿
        painter.setRenderHint(QPainter.Antialiasing)
        # 设置旋转中心为按钮的中心
        painter.translate(self.width() / 2, self.height() / 2)
        # 设置旋转角度
        painter.rotate(self._angle)
        # 将坐标系平移回左上角
        painter.translate(-self.width() / 2, -self.height() / 2)
        # 绘制图标
        pixmap = self.icon().pixmap(self.iconSize())
        if pixmap.isNull():
            return
        # 裁剪图标为圆形
        path = QPainterPath()
        path.addEllipse(0, 0, self.width(), self.height())  # 使用按钮的宽高来定义圆形区域
        painter.setClipPath(path)   # 设置裁剪路径为圆形
        # 绘制图标
        painter.drawPixmap(0, 0, pixmap)
