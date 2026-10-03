import sys
from pathlib import Path
from PySide6.QtCore import QPoint, QRect, QSize, Qt, QTimer, QEvent, QPropertyAnimation
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor, QIcon
from GUI import Ui_MainWindow

if getattr(sys, 'frozen', False):
    source = Path(sys._MEIPASS)
else:
    source = Path(__file__).parent.parent

class MainWindow(QMainWindow):
    '''主窗口类'''

# ====================初始化====================

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.avatar_event_time = 500    # 头像点击事件公共时间
        self.avatar_angle = 0  # 初始化头像旋转角度
        self.ui.avatarMenu.hide()  # 初始化时隐藏头像菜单
        self.avatar_anim_state = False  # 头像动画状态，防止重复点击
        # 设置主窗口布局
        layout = QVBoxLayout(self.ui.mainContainer)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 设置鼠标滚轮滚动的行数
        QApplication.setWheelScrollLines(6)

        # 添加控件
        layout.addWidget(self.ui.titleBar)
        layout.addWidget(self.ui.chatScroll, 1)  # 设置chatScroll为可扩展的
        layout.addWidget(self.ui.statusBar)

        # 窗口
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框窗口
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        qss_path = source / "GUI" /"QSS.css"
        # 读取QSS文件并应用样式
        with open(qss_path, "r", encoding="utf-8") as f:
            qss = f.read()
        self.setStyleSheet(qss)

        # 关闭窗口
        self.ui.closeBtn.clicked.connect(self.close)
        # 最小化窗口
        self.ui.minBtn.clicked.connect(self.showMinimized)
        # 最大化/还原窗口
        self.ui.maxBtn.clicked.connect(self.max_toggle)

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

        # 初始化
        self.resizeEvent(None)

        for i in range(30):
            label = QLabel(f"测试消息 {i+1}")
            label.setStyleSheet("padding: 8px; color: black")
            self.ui.chatLayout.addWidget(label)

        # 事件过滤器
        self.ui.chatScroll.installEventFilter(self)

        # 头像点击事件
        self.ui.avatarBtn.setIcon(QIcon(str(source / "GUI" / "avatar" /"原版-80x80.png")))
        self.ui.avatarBtn.setIconSize(QSize(60, 60))
        self.ui.avatarBtn.clicked.connect(self.rotate_avatar)
        self.ui.avatarBtn.clicked.connect(self.toggle_avatat_menu)

# ====================自定义方法====================

    def resizeEvent(self, event):
        '''重写resizeEvent，动态调整各组件位置'''

        super().resizeEvent(event)
        QTimer.singleShot(0, self._update_input_row)  # 延迟更新输入区位置
        QTimer.singleShot(0, self._update_avatar_menu)  # 延迟更新头像菜单位置

    # ==========头像相关事件==========    
    def rotate_avatar(self):
        '''头像旋转动画'''

        # 创建动画
        if getattr(self, 'avatar_anim', None):
            self.avatar_anim.stop()  # 停止当前动画

        anim = QPropertyAnimation(self.ui.avatarBtn, b"angle")
        anim.setDuration(self.avatar_event_time)   # 动画持续时间
        if self.avatar_angle == 0:
            anim.setStartValue(0)   # 起始角度
            anim.setEndValue(360)   # 结束角度
            self.avatar_angle = 360
        else:
            anim.setStartValue(360)
            anim.setEndValue(0)
            self.avatar_angle = 0
        anim.start()            # 启动动画
        self.avatar_anim = anim  # 保持对动画的引用，防止被垃圾回收

    def toggle_avatat_menu(self):
        '''头像菜单展开/收起切换'''

        if getattr(self, 'avatar_menu_anim', None):
            self.avatar_menu_anim.stop()  # 停止当前动画

        if self.avatar_anim_state:
            self.hide_avatar_menu()
            self.avatar_anim_state = False
        else:
            self.show_avatar_menu()
            self.avatar_anim_state = True

    def _update_avatar_menu(self):
        '''更新头像菜单位置和大小'''

        # 位置
        avatar_pos = self.ui.avatarBtn.mapTo(self.ui.mainContainer, QPoint(0, 0))
        x = avatar_pos.x()
        y = avatar_pos.y()
        w = 90
        h = self.ui.avatarMenu.sizeHint().height()
        self.ui.avatarMenu.setGeometry(x-15, y+70, w, h)

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

    def hide_avatar_menu(self):
        '''头像菜单收起动画'''

        start = self.ui.avatarMenu.geometry()  # 起始大小
        end = QRect(start.x(), start.y(), start.width(), 0)  # 目标大小

        anim = QPropertyAnimation(self.ui.avatarMenu, b"geometry")  # 创建动画
        anim.setDuration(500)  # 动画持续时间
        anim.setStartValue(start)  # 设置起始值
        anim.setEndValue(end)  # 设置结束值
        anim.finished.connect(self.ui.avatarMenu.hide)  # 动画结束后隐藏菜单
        anim.start()  # 启动动画
        self.avatar_menu_anim = anim  # 防止被回收

    # ==========标题栏相关事件==========
    def max_toggle(self):
        '''最大化/还原窗口'''

        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    # ==========对话区相关事件==========
    def eventFilter(self, obj, event):
        '''事件过滤器，处理滚动条样式'''

        # 处理滚动条事件
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
    def _update_input_row(self):
        '''更新输入区位置和大小'''
        
        # 输入区高度
        h = 50

        # 位置
        w = self.width()
        x = 0
        y = self.ui.mainContainer.height() - h - 60
        self.ui.inputRow.setGeometry(x, y, w, h)    # 设置输入区位置和大小
        self.ui.fadeMask.setGeometry(x, y, w-8, 82)  # 设置渐变遮罩位置和大小

        # 加载完毕后，滚动到底部
        scrollbar = self.ui.chatScroll.verticalScrollBar()
        QTimer.singleShot(0, lambda: scrollbar.setValue(scrollbar.maximum()))  # 滚动到底部






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())