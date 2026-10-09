# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

from widgets import AvatarButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(985, 802)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy)
        self.mainContainer.setMinimumSize(QSize(896, 672))
        self.titleBar = QWidget(self.mainContainer)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setGeometry(QRect(0, 0, 896, 80))
        sizePolicy.setHeightForWidth(self.titleBar.sizePolicy().hasHeightForWidth())
        self.titleBar.setSizePolicy(sizePolicy)
        self.titleBar.setMinimumSize(QSize(896, 80))
        self.titleBar.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 5, -1, 5)
        self.avatarBtn = AvatarButton(self.titleBar)
        self.avatarBtn.setObjectName(u"avatarBtn")
        self.avatarBtn.setMinimumSize(QSize(60, 60))
        self.avatarBtn.setMaximumSize(QSize(60, 60))
        icon = QIcon()
        icon.addFile(u"../../../../../../../../../../../../../../../../../../../../\u4e0b\u8f7d/Mio.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.avatarBtn.setIcon(icon)
        self.avatarBtn.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.avatarBtn)

        self.nameBox = QWidget(self.titleBar)
        self.nameBox.setObjectName(u"nameBox")
        self.verticalLayout_5 = QVBoxLayout(self.nameBox)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 10, -1, 0)
        self.nameLabel = QLabel(self.nameBox)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setMinimumSize(QSize(0, 0))
        self.nameLabel.setMaximumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.nameLabel)

        self.statusBox = QWidget(self.nameBox)
        self.statusBox.setObjectName(u"statusBox")
        self.horizontalLayout_2 = QHBoxLayout(self.statusBox)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.statusDot = QLabel(self.statusBox)
        self.statusDot.setObjectName(u"statusDot")
        self.statusDot.setMinimumSize(QSize(0, 16))
        self.statusDot.setMaximumSize(QSize(10, 16777215))
        self.statusDot.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.statusDot.setMargin(0)

        self.horizontalLayout_2.addWidget(self.statusDot)

        self.statusLabel = QLabel(self.statusBox)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setMinimumSize(QSize(0, 0))
        self.statusLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.statusLabel)


        self.verticalLayout_5.addWidget(self.statusBox)


        self.horizontalLayout.addWidget(self.nameBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.voiceBtn = QToolButton(self.titleBar)
        self.voiceBtn.setObjectName(u"voiceBtn")

        self.horizontalLayout.addWidget(self.voiceBtn)

        self.callBtn = QToolButton(self.titleBar)
        self.callBtn.setObjectName(u"callBtn")

        self.horizontalLayout.addWidget(self.callBtn)

        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.dividerD = QWidget(self.titleBar)
        self.dividerD.setObjectName(u"dividerD")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dividerD.sizePolicy().hasHeightForWidth())
        self.dividerD.setSizePolicy(sizePolicy1)
        self.dividerD.setMinimumSize(QSize(1, 50))
        self.dividerD.setMaximumSize(QSize(1, 50))
        self.dividerD.setSizeIncrement(QSize(0, 0))
        self.dividerD.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.dividerD)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.settingsBtn = QToolButton(self.titleBar)
        self.settingsBtn.setObjectName(u"settingsBtn")

        self.horizontalLayout.addWidget(self.settingsBtn)

        self.moreBtn = QToolButton(self.titleBar)
        self.moreBtn.setObjectName(u"moreBtn")

        self.horizontalLayout.addWidget(self.moreBtn)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.divider = QWidget(self.titleBar)
        self.divider.setObjectName(u"divider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.divider.sizePolicy().hasHeightForWidth())
        self.divider.setSizePolicy(sizePolicy2)
        self.divider.setMinimumSize(QSize(1, 50))
        self.divider.setMaximumSize(QSize(1, 50))

        self.horizontalLayout.addWidget(self.divider)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.minBtn = QToolButton(self.titleBar)
        self.minBtn.setObjectName(u"minBtn")

        self.horizontalLayout.addWidget(self.minBtn)

        self.maxBtn = QToolButton(self.titleBar)
        self.maxBtn.setObjectName(u"maxBtn")

        self.horizontalLayout.addWidget(self.maxBtn)

        self.closeBtn = QToolButton(self.titleBar)
        self.closeBtn.setObjectName(u"closeBtn")

        self.horizontalLayout.addWidget(self.closeBtn)

        self.nameBox.raise_()
        self.settingsBtn.raise_()
        self.moreBtn.raise_()
        self.minBtn.raise_()
        self.maxBtn.raise_()
        self.closeBtn.raise_()
        self.avatarBtn.raise_()
        self.callBtn.raise_()
        self.dividerD.raise_()
        self.divider.raise_()
        self.voiceBtn.raise_()
        self.statusBar = QWidget(self.mainContainer)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setGeometry(QRect(0, 661, 896, 28))
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setMinimumSize(QSize(0, 28))
        self.statusBar.setMaximumSize(QSize(16777215, 28))
        self.horizontalLayout_4 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.statusDotA = QLabel(self.statusBar)
        self.statusDotA.setObjectName(u"statusDotA")
        self.statusDotA.setMaximumSize(QSize(10, 16777215))

        self.horizontalLayout_4.addWidget(self.statusDotA)

        self.statusLabel_2 = QLabel(self.statusBar)
        self.statusLabel_2.setObjectName(u"statusLabel_2")
        self.statusLabel_2.setMinimumSize(QSize(0, 0))
        self.statusLabel_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.statusLabel_2)

        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.dividerB = QWidget(self.statusBar)
        self.dividerB.setObjectName(u"dividerB")
        self.dividerB.setMinimumSize(QSize(1, 20))
        self.dividerB.setMaximumSize(QSize(1, 20))

        self.horizontalLayout_4.addWidget(self.dividerB)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.modelLabel = QLabel(self.statusBar)
        self.modelLabel.setObjectName(u"modelLabel")

        self.horizontalLayout_4.addWidget(self.modelLabel)

        self.horizontalSpacer_7 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.dividerC = QWidget(self.statusBar)
        self.dividerC.setObjectName(u"dividerC")
        self.dividerC.setMinimumSize(QSize(1, 21))
        self.dividerC.setMaximumSize(QSize(1, 20))

        self.horizontalLayout_4.addWidget(self.dividerC)

        self.horizontalSpacer_8 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.envLabel = QLabel(self.statusBar)
        self.envLabel.setObjectName(u"envLabel")

        self.horizontalLayout_4.addWidget(self.envLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.quoteLabel = QLabel(self.statusBar)
        self.quoteLabel.setObjectName(u"quoteLabel")

        self.horizontalLayout_4.addWidget(self.quoteLabel)

        self.avatarMenu = QWidget(self.mainContainer)
        self.avatarMenu.setObjectName(u"avatarMenu")
        self.avatarMenu.setGeometry(QRect(650, 510, 131, 201))
        sizePolicy.setHeightForWidth(self.avatarMenu.sizePolicy().hasHeightForWidth())
        self.avatarMenu.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.avatarMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chooseAvatarBtn = QPushButton(self.avatarMenu)
        self.chooseAvatarBtn.setObjectName(u"chooseAvatarBtn")

        self.verticalLayout.addWidget(self.chooseAvatarBtn)

        self.avatarPicker = QWidget(self.avatarMenu)
        self.avatarPicker.setObjectName(u"avatarPicker")
        sizePolicy.setHeightForWidth(self.avatarPicker.sizePolicy().hasHeightForWidth())
        self.avatarPicker.setSizePolicy(sizePolicy)
        self.avatarPicker.setMinimumSize(QSize(30, 30))
        self.gridLayout = QGridLayout(self.avatarPicker)
        self.gridLayout.setObjectName(u"gridLayout")
        self.avatar1 = QWidget(self.avatarPicker)
        self.avatar1.setObjectName(u"avatar1")
        self.avatar1.setMinimumSize(QSize(200, 200))
        self.avatar1.setMaximumSize(QSize(200, 200))
        self.Mio = QLabel(self.avatar1)
        self.Mio.setObjectName(u"Mio")
        self.Mio.setGeometry(QRect(0, 0, 200, 200))
        self.Mio.setMinimumSize(QSize(200, 200))
        self.zoomBtn1 = QToolButton(self.avatar1)
        self.zoomBtn1.setObjectName(u"zoomBtn1")
        self.zoomBtn1.setGeometry(QRect(10, 10, 30, 31))

        self.gridLayout.addWidget(self.avatar1, 1, 0, 1, 1)

        self.avatar3 = QWidget(self.avatarPicker)
        self.avatar3.setObjectName(u"avatar3")
        self.avatar3.setMinimumSize(QSize(200, 200))
        self.avatar3.setMaximumSize(QSize(200, 200))
        self.QMio = QLabel(self.avatar3)
        self.QMio.setObjectName(u"QMio")
        self.QMio.setGeometry(QRect(0, 0, 200, 200))
        self.QMio.setMinimumSize(QSize(200, 200))
        self.QMio.setMaximumSize(QSize(200, 200))
        self.zoomBtn3 = QToolButton(self.avatar3)
        self.zoomBtn3.setObjectName(u"zoomBtn3")
        self.zoomBtn3.setGeometry(QRect(10, 10, 30, 31))

        self.gridLayout.addWidget(self.avatar3, 2, 0, 1, 1)

        self.avatar2 = QWidget(self.avatarPicker)
        self.avatar2.setObjectName(u"avatar2")
        self.avatar2.setMinimumSize(QSize(200, 200))
        self.avatar2.setMaximumSize(QSize(200, 200))
        self.MioCat = QLabel(self.avatar2)
        self.MioCat.setObjectName(u"MioCat")
        self.MioCat.setGeometry(QRect(0, 0, 200, 200))
        self.MioCat.setMinimumSize(QSize(200, 200))
        self.MioCat.setMaximumSize(QSize(200, 200))
        self.zoomBtn2 = QToolButton(self.avatar2)
        self.zoomBtn2.setObjectName(u"zoomBtn2")
        self.zoomBtn2.setGeometry(QRect(10, 10, 30, 31))

        self.gridLayout.addWidget(self.avatar2, 1, 1, 1, 1)

        self.avatar4 = QWidget(self.avatarPicker)
        self.avatar4.setObjectName(u"avatar4")
        self.avatar4.setMinimumSize(QSize(200, 200))
        self.avatar4.setMaximumSize(QSize(200, 200))
        self.QMioCat = QLabel(self.avatar4)
        self.QMioCat.setObjectName(u"QMioCat")
        self.QMioCat.setGeometry(QRect(0, 0, 200, 200))
        self.QMioCat.setMinimumSize(QSize(200, 200))
        self.QMioCat.setMaximumSize(QSize(200, 200))
        self.zoomBtn4 = QToolButton(self.avatar4)
        self.zoomBtn4.setObjectName(u"zoomBtn4")
        self.zoomBtn4.setGeometry(QRect(10, 10, 30, 31))

        self.gridLayout.addWidget(self.avatar4, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.avatarPicker)

        self.editPersonaBtn = QPushButton(self.avatarMenu)
        self.editPersonaBtn.setObjectName(u"editPersonaBtn")

        self.verticalLayout.addWidget(self.editPersonaBtn)

        self.memoryBtn = QPushButton(self.avatarMenu)
        self.memoryBtn.setObjectName(u"memoryBtn")

        self.verticalLayout.addWidget(self.memoryBtn)

        self.moreMenu = QWidget(self.mainContainer)
        self.moreMenu.setObjectName(u"moreMenu")
        self.moreMenu.setGeometry(QRect(600, 570, 121, 181))
        self.verticalLayout_6 = QVBoxLayout(self.moreMenu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.help = QPushButton(self.moreMenu)
        self.help.setObjectName(u"help")

        self.verticalLayout_6.addWidget(self.help)

        self.update = QPushButton(self.moreMenu)
        self.update.setObjectName(u"update")

        self.verticalLayout_6.addWidget(self.update)

        self.ComfyUI = QPushButton(self.moreMenu)
        self.ComfyUI.setObjectName(u"ComfyUI")

        self.verticalLayout_6.addWidget(self.ComfyUI)

        self.feedback = QPushButton(self.moreMenu)
        self.feedback.setObjectName(u"feedback")

        self.verticalLayout_6.addWidget(self.feedback)

        self.about = QPushButton(self.moreMenu)
        self.about.setObjectName(u"about")

        self.verticalLayout_6.addWidget(self.about)

        self.line = QFrame(self.moreMenu)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.reset = QPushButton(self.moreMenu)
        self.reset.setObjectName(u"reset")

        self.verticalLayout_6.addWidget(self.reset)

        self.stack = QStackedWidget(self.mainContainer)
        self.stack.setObjectName(u"stack")
        self.stack.setGeometry(QRect(860, 640, 81, 131))
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.stack.setMinimumSize(QSize(0, 0))
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setMinimumSize(QSize(50, 50))
        self.chatScroll = QScrollArea(self.page1)
        self.chatScroll.setObjectName(u"chatScroll")
        self.chatScroll.setGeometry(QRect(9, 153, 52, 146))
        self.chatScroll.setMaximumSize(QSize(16777215, 16777215))
        self.chatScroll.setWidgetResizable(True)
        self.chatWidget = QWidget()
        self.chatWidget.setObjectName(u"chatWidget")
        self.chatWidget.setGeometry(QRect(0, 0, 50, 144))
        sizePolicy.setHeightForWidth(self.chatWidget.sizePolicy().hasHeightForWidth())
        self.chatWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.chatWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.chatLayout = QVBoxLayout()
        self.chatLayout.setSpacing(8)
        self.chatLayout.setObjectName(u"chatLayout")
        self.chatLayout.setContentsMargins(16, 16, 16, 110)

        self.verticalLayout_2.addLayout(self.chatLayout)

        self.chatScroll.setWidget(self.chatWidget)
        self.inputRow = QWidget(self.page1)
        self.inputRow.setObjectName(u"inputRow")
        self.inputRow.setGeometry(QRect(9, 9, 654, 50))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.inputRow.sizePolicy().hasHeightForWidth())
        self.inputRow.setSizePolicy(sizePolicy3)
        self.inputRow.setMinimumSize(QSize(0, 50))
        self.inputRow.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.inputRow)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(50, 0, 50, 0)
        self.inputArea = QWidget(self.inputRow)
        self.inputArea.setObjectName(u"inputArea")
        sizePolicy3.setHeightForWidth(self.inputArea.sizePolicy().hasHeightForWidth())
        self.inputArea.setSizePolicy(sizePolicy3)
        self.inputArea.setMinimumSize(QSize(0, 50))
        self.inputArea.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.inputArea)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(25, 0, 25, 0)
        self.attachBtn = QToolButton(self.inputArea)
        self.attachBtn.setObjectName(u"attachBtn")

        self.horizontalLayout_3.addWidget(self.attachBtn)

        self.imageBtn = QToolButton(self.inputArea)
        self.imageBtn.setObjectName(u"imageBtn")

        self.horizontalLayout_3.addWidget(self.imageBtn)

        self.dividerA = QWidget(self.inputArea)
        self.dividerA.setObjectName(u"dividerA")
        self.dividerA.setMinimumSize(QSize(1, 38))
        self.dividerA.setMaximumSize(QSize(1, 38))

        self.horizontalLayout_3.addWidget(self.dividerA)

        self.inputEdit = QTextEdit(self.inputArea)
        self.inputEdit.setObjectName(u"inputEdit")
        self.inputEdit.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_3.addWidget(self.inputEdit)

        self.speechBtn = QToolButton(self.inputArea)
        self.speechBtn.setObjectName(u"speechBtn")

        self.horizontalLayout_3.addWidget(self.speechBtn)

        self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.dividerE = QWidget(self.inputArea)
        self.dividerE.setObjectName(u"dividerE")
        self.dividerE.setMinimumSize(QSize(1, 35))
        self.dividerE.setMaximumSize(QSize(1, 35))

        self.horizontalLayout_3.addWidget(self.dividerE)

        self.horizontalSpacer_12 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_12)

        self.sendBtn = QPushButton(self.inputArea)
        self.sendBtn.setObjectName(u"sendBtn")
        self.sendBtn.setMinimumSize(QSize(80, 36))
        self.sendBtn.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout_3.addWidget(self.sendBtn)


        self.horizontalLayout_5.addWidget(self.inputArea)

        self.fadeMask = QWidget(self.page1)
        self.fadeMask.setObjectName(u"fadeMask")
        self.fadeMask.setGeometry(QRect(9, 65, 654, 82))
        sizePolicy3.setHeightForWidth(self.fadeMask.sizePolicy().hasHeightForWidth())
        self.fadeMask.setSizePolicy(sizePolicy3)
        self.fadeMask.setMinimumSize(QSize(0, 82))
        self.fadeMask.setMaximumSize(QSize(16777215, 82))
        self.stack.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_4 = QVBoxLayout(self.page2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.topBar = QWidget(self.page2)
        self.topBar.setObjectName(u"topBar")
        sizePolicy3.setHeightForWidth(self.topBar.sizePolicy().hasHeightForWidth())
        self.topBar.setSizePolicy(sizePolicy3)
        self.topBar.setMinimumSize(QSize(0, 30))
        self.topBar.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_6 = QHBoxLayout(self.topBar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 15, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)

        self.PromptClose = QToolButton(self.topBar)
        self.PromptClose.setObjectName(u"PromptClose")

        self.horizontalLayout_6.addWidget(self.PromptClose)


        self.verticalLayout_4.addWidget(self.topBar)

        self.promptEditArea = QScrollArea(self.page2)
        self.promptEditArea.setObjectName(u"promptEditArea")
        self.promptEditArea.setWidgetResizable(True)
        self.promptEditWidget = QWidget()
        self.promptEditWidget.setObjectName(u"promptEditWidget")
        self.promptEditWidget.setGeometry(QRect(0, -390, 177, 1013))
        self.verticalLayout_7 = QVBoxLayout(self.promptEditWidget)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, -1, -1, -1)
        self.assiTitle = QLabel(self.promptEditWidget)
        self.assiTitle.setObjectName(u"assiTitle")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.assiTitle.sizePolicy().hasHeightForWidth())
        self.assiTitle.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.assiTitle)

        self.assiProfileTitle = QLabel(self.promptEditWidget)
        self.assiProfileTitle.setObjectName(u"assiProfileTitle")
        sizePolicy4.setHeightForWidth(self.assiProfileTitle.sizePolicy().hasHeightForWidth())
        self.assiProfileTitle.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.assiProfileTitle)

        self.assiProfilWidget = QWidget(self.promptEditWidget)
        self.assiProfilWidget.setObjectName(u"assiProfilWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.assiProfilWidget.sizePolicy().hasHeightForWidth())
        self.assiProfilWidget.setSizePolicy(sizePolicy5)
        self.assiProfilWidget.setMinimumSize(QSize(0, 100))
        self.assiProfilWidget.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_8 = QHBoxLayout(self.assiProfilWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, 0, 15, 0)
        self.assiProfileEdit = QTextEdit(self.assiProfilWidget)
        self.assiProfileEdit.setObjectName(u"assiProfileEdit")
        sizePolicy5.setHeightForWidth(self.assiProfileEdit.sizePolicy().hasHeightForWidth())
        self.assiProfileEdit.setSizePolicy(sizePolicy5)
        self.assiProfileEdit.setMinimumSize(QSize(0, 100))
        self.assiProfileEdit.setMaximumSize(QSize(16777215, 300))

        self.horizontalLayout_8.addWidget(self.assiProfileEdit)


        self.verticalLayout_7.addWidget(self.assiProfilWidget)

        self.styleTitle = QLabel(self.promptEditWidget)
        self.styleTitle.setObjectName(u"styleTitle")
        sizePolicy4.setHeightForWidth(self.styleTitle.sizePolicy().hasHeightForWidth())
        self.styleTitle.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.styleTitle)

        self.styleWidget = QWidget(self.promptEditWidget)
        self.styleWidget.setObjectName(u"styleWidget")
        sizePolicy5.setHeightForWidth(self.styleWidget.sizePolicy().hasHeightForWidth())
        self.styleWidget.setSizePolicy(sizePolicy5)
        self.styleWidget.setMinimumSize(QSize(0, 100))
        self.styleWidget.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_7 = QHBoxLayout(self.styleWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, 0, 15, 0)
        self.styleEdit = QTextEdit(self.styleWidget)
        self.styleEdit.setObjectName(u"styleEdit")
        sizePolicy5.setHeightForWidth(self.styleEdit.sizePolicy().hasHeightForWidth())
        self.styleEdit.setSizePolicy(sizePolicy5)
        self.styleEdit.setMinimumSize(QSize(0, 100))
        self.styleEdit.setMaximumSize(QSize(16777215, 300))

        self.horizontalLayout_7.addWidget(self.styleEdit)


        self.verticalLayout_7.addWidget(self.styleWidget)

        self.personalityTitle = QLabel(self.promptEditWidget)
        self.personalityTitle.setObjectName(u"personalityTitle")
        sizePolicy4.setHeightForWidth(self.personalityTitle.sizePolicy().hasHeightForWidth())
        self.personalityTitle.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.personalityTitle)

        self.personalityWidget = QWidget(self.promptEditWidget)
        self.personalityWidget.setObjectName(u"personalityWidget")
        sizePolicy5.setHeightForWidth(self.personalityWidget.sizePolicy().hasHeightForWidth())
        self.personalityWidget.setSizePolicy(sizePolicy5)
        self.personalityWidget.setMinimumSize(QSize(0, 100))
        self.personalityWidget.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_9 = QHBoxLayout(self.personalityWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, 0, 15, 0)
        self.personality = QTextEdit(self.personalityWidget)
        self.personality.setObjectName(u"personality")
        sizePolicy5.setHeightForWidth(self.personality.sizePolicy().hasHeightForWidth())
        self.personality.setSizePolicy(sizePolicy5)
        self.personality.setMinimumSize(QSize(0, 100))
        self.personality.setMaximumSize(QSize(16777215, 300))

        self.horizontalLayout_9.addWidget(self.personality)


        self.verticalLayout_7.addWidget(self.personalityWidget)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.dividerF = QWidget(self.promptEditWidget)
        self.dividerF.setObjectName(u"dividerF")
        sizePolicy4.setHeightForWidth(self.dividerF.sizePolicy().hasHeightForWidth())
        self.dividerF.setSizePolicy(sizePolicy4)
        self.dividerF.setMinimumSize(QSize(0, 1))
        self.dividerF.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_7.addWidget(self.dividerF)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.userTitle = QLabel(self.promptEditWidget)
        self.userTitle.setObjectName(u"userTitle")
        sizePolicy4.setHeightForWidth(self.userTitle.sizePolicy().hasHeightForWidth())
        self.userTitle.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.userTitle)

        self.baseInfoTitle = QLabel(self.promptEditWidget)
        self.baseInfoTitle.setObjectName(u"baseInfoTitle")
        sizePolicy4.setHeightForWidth(self.baseInfoTitle.sizePolicy().hasHeightForWidth())
        self.baseInfoTitle.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.baseInfoTitle)

        self.baseInfoWidget = QWidget(self.promptEditWidget)
        self.baseInfoWidget.setObjectName(u"baseInfoWidget")
        sizePolicy4.setHeightForWidth(self.baseInfoWidget.sizePolicy().hasHeightForWidth())
        self.baseInfoWidget.setSizePolicy(sizePolicy4)
        self.gridLayout_2 = QGridLayout(self.baseInfoWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(30, 0, 15, 0)
        self.userNicknameEdit = QLineEdit(self.baseInfoWidget)
        self.userNicknameEdit.setObjectName(u"userNicknameEdit")

        self.gridLayout_2.addWidget(self.userNicknameEdit, 1, 1, 1, 1)

        self.userAgeEdit = QLineEdit(self.baseInfoWidget)
        self.userAgeEdit.setObjectName(u"userAgeEdit")

        self.gridLayout_2.addWidget(self.userAgeEdit, 3, 1, 1, 1)

        self.userAge = QLabel(self.baseInfoWidget)
        self.userAge.setObjectName(u"userAge")

        self.gridLayout_2.addWidget(self.userAge, 3, 0, 1, 1)

        self.userNickname = QLabel(self.baseInfoWidget)
        self.userNickname.setObjectName(u"userNickname")

        self.gridLayout_2.addWidget(self.userNickname, 1, 0, 1, 1)

        self.userGender = QLabel(self.baseInfoWidget)
        self.userGender.setObjectName(u"userGender")

        self.gridLayout_2.addWidget(self.userGender, 2, 0, 1, 1)

        self.userNameEdit = QLineEdit(self.baseInfoWidget)
        self.userNameEdit.setObjectName(u"userNameEdit")

        self.gridLayout_2.addWidget(self.userNameEdit, 0, 1, 1, 1)

        self.userGenderEdit = QLineEdit(self.baseInfoWidget)
        self.userGenderEdit.setObjectName(u"userGenderEdit")

        self.gridLayout_2.addWidget(self.userGenderEdit, 2, 1, 1, 1)

        self.userBirthdayEdit = QLineEdit(self.baseInfoWidget)
        self.userBirthdayEdit.setObjectName(u"userBirthdayEdit")

        self.gridLayout_2.addWidget(self.userBirthdayEdit, 4, 1, 1, 1)

        self.userName = QLabel(self.baseInfoWidget)
        self.userName.setObjectName(u"userName")
        sizePolicy2.setHeightForWidth(self.userName.sizePolicy().hasHeightForWidth())
        self.userName.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.userName, 0, 0, 1, 1)

        self.userBirthday = QLabel(self.baseInfoWidget)
        self.userBirthday.setObjectName(u"userBirthday")

        self.gridLayout_2.addWidget(self.userBirthday, 4, 0, 1, 1)

        self.userIdentity = QLabel(self.baseInfoWidget)
        self.userIdentity.setObjectName(u"userIdentity")

        self.gridLayout_2.addWidget(self.userIdentity, 5, 0, 1, 1)

        self.userIdentityEdit = QLineEdit(self.baseInfoWidget)
        self.userIdentityEdit.setObjectName(u"userIdentityEdit")

        self.gridLayout_2.addWidget(self.userIdentityEdit, 5, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.baseInfoWidget)

        self.otherTitle = QLabel(self.promptEditWidget)
        self.otherTitle.setObjectName(u"otherTitle")
        sizePolicy4.setHeightForWidth(self.otherTitle.sizePolicy().hasHeightForWidth())
        self.otherTitle.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.otherTitle)

        self.otherWidget = QWidget(self.promptEditWidget)
        self.otherWidget.setObjectName(u"otherWidget")
        sizePolicy5.setHeightForWidth(self.otherWidget.sizePolicy().hasHeightForWidth())
        self.otherWidget.setSizePolicy(sizePolicy5)
        self.otherWidget.setMinimumSize(QSize(0, 100))
        self.otherWidget.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_10 = QHBoxLayout(self.otherWidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(50, 0, 15, 0)
        self.otherEdit = QTextEdit(self.otherWidget)
        self.otherEdit.setObjectName(u"otherEdit")

        self.horizontalLayout_10.addWidget(self.otherEdit)


        self.verticalLayout_7.addWidget(self.otherWidget)

        self.promptEditArea.setWidget(self.promptEditWidget)

        self.verticalLayout_4.addWidget(self.promptEditArea)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.widget = QWidget(self.page2)
        self.widget.setObjectName(u"widget")
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.widget.setMinimumSize(QSize(0, 30))
        self.widget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_11 = QHBoxLayout(self.widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, 30, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.promptSave = QPushButton(self.widget)
        self.promptSave.setObjectName(u"promptSave")
        sizePolicy2.setHeightForWidth(self.promptSave.sizePolicy().hasHeightForWidth())
        self.promptSave.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.promptSave)

        self.promptCancel = QPushButton(self.widget)
        self.promptCancel.setObjectName(u"promptCancel")
        sizePolicy2.setHeightForWidth(self.promptCancel.sizePolicy().hasHeightForWidth())
        self.promptCancel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.promptCancel)


        self.verticalLayout_4.addWidget(self.widget)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.stack.addWidget(self.page2)
        self.memoryWidget = QWidget(self.mainContainer)
        self.memoryWidget.setObjectName(u"memoryWidget")
        self.memoryWidget.setGeometry(QRect(40, 110, 250, 511))
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.memoryWidget.sizePolicy().hasHeightForWidth())
        self.memoryWidget.setSizePolicy(sizePolicy6)
        self.memoryWidget.setMinimumSize(QSize(250, 0))
        self.memoryWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.memoryWidget)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 15, 0, 0)
        self.memoryTitle = QWidget(self.memoryWidget)
        self.memoryTitle.setObjectName(u"memoryTitle")
        sizePolicy3.setHeightForWidth(self.memoryTitle.sizePolicy().hasHeightForWidth())
        self.memoryTitle.setSizePolicy(sizePolicy3)
        self.memoryTitle.setMinimumSize(QSize(0, 30))
        self.memoryTitle.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_12 = QHBoxLayout(self.memoryTitle)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(15, 0, 9, 0)
        self.memoryLabel = QLabel(self.memoryTitle)
        self.memoryLabel.setObjectName(u"memoryLabel")
        sizePolicy1.setHeightForWidth(self.memoryLabel.sizePolicy().hasHeightForWidth())
        self.memoryLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.memoryLabel)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_15)

        self.delMemoryBtn = QToolButton(self.memoryTitle)
        self.delMemoryBtn.setObjectName(u"delMemoryBtn")

        self.horizontalLayout_12.addWidget(self.delMemoryBtn)

        self.memoryMoreBtn = QToolButton(self.memoryTitle)
        self.memoryMoreBtn.setObjectName(u"memoryMoreBtn")

        self.horizontalLayout_12.addWidget(self.memoryMoreBtn)


        self.verticalLayout_8.addWidget(self.memoryTitle)

        self.memoryArea = QScrollArea(self.memoryWidget)
        self.memoryArea.setObjectName(u"memoryArea")
        self.memoryArea.setWidgetResizable(True)
        self.memoryAreaWidget = QWidget()
        self.memoryAreaWidget.setObjectName(u"memoryAreaWidget")
        self.memoryAreaWidget.setGeometry(QRect(0, 0, 248, 449))
        self.verticalLayout_10 = QVBoxLayout(self.memoryAreaWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.memoryLayout = QVBoxLayout()
        self.memoryLayout.setObjectName(u"memoryLayout")
        self.memoryLayout.setContentsMargins(-1, -1, -1, 15)
        self.noMemoryLabel = QLabel(self.memoryAreaWidget)
        self.noMemoryLabel.setObjectName(u"noMemoryLabel")
        self.noMemoryLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.memoryLayout.addWidget(self.noMemoryLabel)


        self.verticalLayout_10.addLayout(self.memoryLayout)

        self.memoryArea.setWidget(self.memoryAreaWidget)

        self.verticalLayout_8.addWidget(self.memoryArea)

        self.memoryMoreMenu = QWidget(self.mainContainer)
        self.memoryMoreMenu.setObjectName(u"memoryMoreMenu")
        self.memoryMoreMenu.setGeometry(QRect(420, 150, 91, 111))
        sizePolicy2.setHeightForWidth(self.memoryMoreMenu.sizePolicy().hasHeightForWidth())
        self.memoryMoreMenu.setSizePolicy(sizePolicy2)
        self.verticalLayout_9 = QVBoxLayout(self.memoryMoreMenu)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.manageBtn = QPushButton(self.memoryMoreMenu)
        self.manageBtn.setObjectName(u"manageBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.manageBtn.sizePolicy().hasHeightForWidth())
        self.manageBtn.setSizePolicy(sizePolicy7)

        self.verticalLayout_9.addWidget(self.manageBtn)

        self.clearBtn = QPushButton(self.memoryMoreMenu)
        self.clearBtn.setObjectName(u"clearBtn")
        sizePolicy7.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy7)

        self.verticalLayout_9.addWidget(self.clearBtn)

        self.titleBar.raise_()
        self.statusBar.raise_()
        self.moreMenu.raise_()
        self.avatarMenu.raise_()
        self.stack.raise_()
        self.memoryWidget.raise_()
        self.memoryMoreMenu.raise_()

        self.verticalLayout_3.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.avatarBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"\u6faa", None))
        self.statusDot.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u95f2\u4e2d", None))
        self.voiceBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.callBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.moreBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.minBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.maxBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.closeBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.statusDotA.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.statusLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u95f2\u4e2d", None))
        self.modelLabel.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
        self.envLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.quoteLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chooseAvatarBtn.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6362\u5f62\u8c61", None))
        self.Mio.setText("")
        self.zoomBtn1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.QMio.setText("")
        self.zoomBtn3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.MioCat.setText("")
        self.zoomBtn2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.QMioCat.setText("")
        self.zoomBtn4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.editPersonaBtn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u8bbe\u5b9a", None))
        self.memoryBtn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u8bb0\u5fc6", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.update.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.ComfyUI.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8ComfyUI", None))
        self.feedback.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u9988", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.reset.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.attachBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.imageBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.speechBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.sendBtn.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.PromptClose.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.assiTitle.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u6faa", None))
        self.assiProfileTitle.setText(QCoreApplication.translate("MainWindow", u" \u2022 \u57fa\u7840\u8bbe\u5b9a", None))
        self.styleTitle.setText(QCoreApplication.translate("MainWindow", u" \u2022 \u8bf4\u8bdd\u98ce\u683c", None))
        self.personalityTitle.setText(QCoreApplication.translate("MainWindow", u" \u2022 \u6027\u683c\u7279\u70b9", None))
        self.userTitle.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u4f60", None))
        self.baseInfoTitle.setText(QCoreApplication.translate("MainWindow", u" \u2022 \u57fa\u7840\u4fe1\u606f", None))
        self.userAge.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84\uff1a", None))
        self.userNickname.setText(QCoreApplication.translate("MainWindow", u"\u79f0\u547c\uff1a", None))
        self.userGender.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b\uff1a", None))
        self.userName.setText(QCoreApplication.translate("MainWindow", u"\u540d\u5b57\uff1a", None))
        self.userBirthday.setText(QCoreApplication.translate("MainWindow", u"\u751f\u65e5\uff1a", None))
        self.userIdentity.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u4efd\uff1a", None))
        self.otherTitle.setText(QCoreApplication.translate("MainWindow", u" \u2022 \u5176\u4ed6\u8bbe\u5b9a", None))
        self.promptSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.promptCancel.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.memoryLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5fc6", None))
        self.delMemoryBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.memoryMoreBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.noMemoryLabel.setText(QCoreApplication.translate("MainWindow", u"\u5c1a\u672a\u6307\u5b9a\u4efb\u4f55\u8bb0\u5fc6\u3002", None))
        self.manageBtn.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
    # retranslateUi

