'''两个窗口共用的小工具：资源路径、图标加载、QSS 读取

手写文件，随便改；GUI.py / image_viewer.py 是 pyuic 生成的，不要往那边写逻辑。
'''

import sys
from pathlib import Path
from PySide6.QtCore import QByteArray, QRectF, Qt
from PySide6.QtGui import QColor, QIcon, QPainter, QPainterPath, QPen, QPixmap
from PySide6.QtSvg import QSvgRenderer

ICON_SIZE = 20          # 图标统一大小
ICON_COLOR = "#333333"  # 图标默认颜色

if getattr(sys, 'frozen', False):
    SOURCE = Path(sys._MEIPASS)
else:
    SOURCE = Path(__file__).parent.parent

GUI_DIR = SOURCE / "GUI"          # 界面资源都在这个目录下
BUTTON_DIR = GUI_DIR / "button"   # svg 图标
AVATAR_DIR = GUI_DIR / "avatar"   # 头像图片


def load_icon(name, color=ICON_COLOR, size=ICON_SIZE):
    '''加载 button/ 目录下的 svg 图标

    QtSvg 不认 css 的 currentColor（会画不出来或者全黑），
    所以这里先把源码里的 currentColor 换成具体的颜色再渲染。
    想改颜色就传第二个参数，比如 load_icon("send", "#ffffff")。
    '''

    text = (BUTTON_DIR / f"{name}.svg").read_text(encoding="utf-8")
    renderer = QSvgRenderer(QByteArray(text.replace("currentColor", color).encode("utf-8")))

    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()

    return QIcon(pixmap)


def load_qss():
    '''读取 QSS.css 的文本（主窗口和图片查看器共用同一份样式）'''

    return (GUI_DIR / "QSS.css").read_text(encoding="utf-8")


def avatar_pixmap(path, size=200, radius=12, border=None, border_width=3):
    '''生成头像缩略图：圆角，可选边框（给「当前正在用的那张」加上）

    边框直接画进图片里，不走 QSS 动态属性——那样改完属性还要等重绘，容易留残影。
    '''

    source_pixmap = QPixmap(str(path)).scaled(size, size, Qt.KeepAspectRatioByExpanding,
                                              Qt.SmoothTransformation)
    out = QPixmap(size, size)
    out.fill(Qt.transparent)

    painter = QPainter(out)
    painter.setRenderHint(QPainter.Antialiasing)

    clip = QPainterPath()
    clip.addRoundedRect(QRectF(0, 0, size, size), radius, radius)
    painter.setClipPath(clip)
    painter.drawPixmap(0, 0, source_pixmap)

    if border is not None:
        inset = border_width / 2
        painter.setClipping(False)
        painter.setPen(QPen(QColor(border), border_width))
        painter.setBrush(Qt.NoBrush)
        painter.drawRoundedRect(QRectF(inset, inset, size - border_width, size - border_width),
                                radius, radius)

    painter.end()
    return out


def round_pixmap(pixmap, radius=12, size=None):
    '''把图片裁成圆角（顺便缩放），用来做缩略图'''

    if size is not None:
        pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

    rounded = QPixmap(pixmap.size())
    rounded.fill(Qt.transparent)
    painter = QPainter(rounded)
    painter.setRenderHint(QPainter.Antialiasing)
    path = QPainterPath()
    path.addRoundedRect(rounded.rect(), radius, radius)
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()

    return rounded
