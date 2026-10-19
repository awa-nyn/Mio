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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStackedWidget, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)

from switch_button import SwitchButton
from widgets import AvatarButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(985, 802)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy1)
        self.mainContainer.setMinimumSize(QSize(896, 672))
        self.titleBar = QWidget(self.mainContainer)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setGeometry(QRect(0, 0, 896, 80))
        sizePolicy1.setHeightForWidth(self.titleBar.sizePolicy().hasHeightForWidth())
        self.titleBar.setSizePolicy(sizePolicy1)
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
        icon.addFile(u"../../../../../../../../../../../../../../../../../../../../../../../../../../\u4e0b\u8f7d/Mio.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
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

        self.divider6 = QWidget(self.titleBar)
        self.divider6.setObjectName(u"divider6")
        sizePolicy.setHeightForWidth(self.divider6.sizePolicy().hasHeightForWidth())
        self.divider6.setSizePolicy(sizePolicy)
        self.divider6.setMinimumSize(QSize(1, 50))
        self.divider6.setMaximumSize(QSize(1, 50))
        self.divider6.setSizeIncrement(QSize(0, 0))
        self.divider6.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.divider6)

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

        self.divider5 = QWidget(self.titleBar)
        self.divider5.setObjectName(u"divider5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.divider5.sizePolicy().hasHeightForWidth())
        self.divider5.setSizePolicy(sizePolicy2)
        self.divider5.setMinimumSize(QSize(1, 50))
        self.divider5.setMaximumSize(QSize(1, 50))

        self.horizontalLayout.addWidget(self.divider5)

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
        self.divider6.raise_()
        self.divider5.raise_()
        self.voiceBtn.raise_()
        self.statusBar = QWidget(self.mainContainer)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setGeometry(QRect(-80, 710, 896, 28))
        sizePolicy1.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy1)
        self.statusBar.setMinimumSize(QSize(0, 28))
        self.statusBar.setMaximumSize(QSize(16777215, 28))
        self.horizontalLayout_4 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.statusDotBottom = QLabel(self.statusBar)
        self.statusDotBottom.setObjectName(u"statusDotBottom")
        self.statusDotBottom.setMaximumSize(QSize(10, 16777215))

        self.horizontalLayout_4.addWidget(self.statusDotBottom)

        self.statusLabelBottom = QLabel(self.statusBar)
        self.statusLabelBottom.setObjectName(u"statusLabelBottom")
        self.statusLabelBottom.setMinimumSize(QSize(0, 0))
        self.statusLabelBottom.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.statusLabelBottom)

        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.divider3 = QWidget(self.statusBar)
        self.divider3.setObjectName(u"divider3")
        self.divider3.setMinimumSize(QSize(1, 20))
        self.divider3.setMaximumSize(QSize(1, 20))

        self.horizontalLayout_4.addWidget(self.divider3)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.modelLabel = QLabel(self.statusBar)
        self.modelLabel.setObjectName(u"modelLabel")

        self.horizontalLayout_4.addWidget(self.modelLabel)

        self.horizontalSpacer_7 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.divider4 = QWidget(self.statusBar)
        self.divider4.setObjectName(u"divider4")
        self.divider4.setMinimumSize(QSize(1, 21))
        self.divider4.setMaximumSize(QSize(1, 20))

        self.horizontalLayout_4.addWidget(self.divider4)

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
        sizePolicy1.setHeightForWidth(self.avatarMenu.sizePolicy().hasHeightForWidth())
        self.avatarMenu.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.avatarMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chooseAvatarBtn = QPushButton(self.avatarMenu)
        self.chooseAvatarBtn.setObjectName(u"chooseAvatarBtn")

        self.verticalLayout.addWidget(self.chooseAvatarBtn)

        self.avatarPicker = QWidget(self.avatarMenu)
        self.avatarPicker.setObjectName(u"avatarPicker")
        sizePolicy1.setHeightForWidth(self.avatarPicker.sizePolicy().hasHeightForWidth())
        self.avatarPicker.setSizePolicy(sizePolicy1)
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
        self.moreMenu.setGeometry(QRect(500, 550, 121, 181))
        self.verticalLayout_6 = QVBoxLayout(self.moreMenu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.fileBtn = QPushButton(self.moreMenu)
        self.fileBtn.setObjectName(u"fileBtn")

        self.verticalLayout_6.addWidget(self.fileBtn)

        self.logBtn = QPushButton(self.moreMenu)
        self.logBtn.setObjectName(u"logBtn")

        self.verticalLayout_6.addWidget(self.logBtn)

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
        self.stack.setGeometry(QRect(150, 70, 816, 734))
        sizePolicy1.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy1)
        self.stack.setMinimumSize(QSize(800, 700))
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
        sizePolicy1.setHeightForWidth(self.chatWidget.sizePolicy().hasHeightForWidth())
        self.chatWidget.setSizePolicy(sizePolicy1)
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

        self.divider1 = QWidget(self.inputArea)
        self.divider1.setObjectName(u"divider1")
        self.divider1.setMinimumSize(QSize(1, 38))
        self.divider1.setMaximumSize(QSize(1, 38))

        self.horizontalLayout_3.addWidget(self.divider1)

        self.inputEdit = QTextEdit(self.inputArea)
        self.inputEdit.setObjectName(u"inputEdit")
        self.inputEdit.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_3.addWidget(self.inputEdit)

        self.speechBtn = QToolButton(self.inputArea)
        self.speechBtn.setObjectName(u"speechBtn")

        self.horizontalLayout_3.addWidget(self.speechBtn)

        self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.divider2 = QWidget(self.inputArea)
        self.divider2.setObjectName(u"divider2")
        self.divider2.setMinimumSize(QSize(1, 35))
        self.divider2.setMaximumSize(QSize(1, 35))

        self.horizontalLayout_3.addWidget(self.divider2)

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

        self.promptClose = QToolButton(self.topBar)
        self.promptClose.setObjectName(u"promptClose")

        self.horizontalLayout_6.addWidget(self.promptClose)


        self.verticalLayout_4.addWidget(self.topBar)

        self.promptEditArea = QScrollArea(self.page2)
        self.promptEditArea.setObjectName(u"promptEditArea")
        self.promptEditArea.setWidgetResizable(True)
        self.promptEditWidget = QWidget()
        self.promptEditWidget.setObjectName(u"promptEditWidget")
        self.promptEditWidget.setGeometry(QRect(0, 0, 177, 1013))
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

        self.assiProfileWidget = QWidget(self.promptEditWidget)
        self.assiProfileWidget.setObjectName(u"assiProfileWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.assiProfileWidget.sizePolicy().hasHeightForWidth())
        self.assiProfileWidget.setSizePolicy(sizePolicy5)
        self.assiProfileWidget.setMinimumSize(QSize(0, 100))
        self.assiProfileWidget.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_8 = QHBoxLayout(self.assiProfileWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, 0, 15, 0)
        self.assiProfileEdit = QTextEdit(self.assiProfileWidget)
        self.assiProfileEdit.setObjectName(u"assiProfileEdit")
        sizePolicy5.setHeightForWidth(self.assiProfileEdit.sizePolicy().hasHeightForWidth())
        self.assiProfileEdit.setSizePolicy(sizePolicy5)
        self.assiProfileEdit.setMinimumSize(QSize(0, 100))
        self.assiProfileEdit.setMaximumSize(QSize(16777215, 300))

        self.horizontalLayout_8.addWidget(self.assiProfileEdit)


        self.verticalLayout_7.addWidget(self.assiProfileWidget)

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
        self.personalityEdit = QTextEdit(self.personalityWidget)
        self.personalityEdit.setObjectName(u"personalityEdit")
        sizePolicy5.setHeightForWidth(self.personalityEdit.sizePolicy().hasHeightForWidth())
        self.personalityEdit.setSizePolicy(sizePolicy5)
        self.personalityEdit.setMinimumSize(QSize(0, 100))
        self.personalityEdit.setMaximumSize(QSize(16777215, 300))

        self.horizontalLayout_9.addWidget(self.personalityEdit)


        self.verticalLayout_7.addWidget(self.personalityWidget)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.divider7 = QWidget(self.promptEditWidget)
        self.divider7.setObjectName(u"divider7")
        sizePolicy4.setHeightForWidth(self.divider7.sizePolicy().hasHeightForWidth())
        self.divider7.setSizePolicy(sizePolicy4)
        self.divider7.setMinimumSize(QSize(0, 1))
        self.divider7.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_7.addWidget(self.divider7)

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

        self.promptOptionWidget = QWidget(self.page2)
        self.promptOptionWidget.setObjectName(u"promptOptionWidget")
        sizePolicy4.setHeightForWidth(self.promptOptionWidget.sizePolicy().hasHeightForWidth())
        self.promptOptionWidget.setSizePolicy(sizePolicy4)
        self.promptOptionWidget.setMinimumSize(QSize(0, 30))
        self.promptOptionWidget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_11 = QHBoxLayout(self.promptOptionWidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, 30, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.promptSave = QPushButton(self.promptOptionWidget)
        self.promptSave.setObjectName(u"promptSave")
        sizePolicy2.setHeightForWidth(self.promptSave.sizePolicy().hasHeightForWidth())
        self.promptSave.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.promptSave)

        self.promptCancel = QPushButton(self.promptOptionWidget)
        self.promptCancel.setObjectName(u"promptCancel")
        sizePolicy2.setHeightForWidth(self.promptCancel.sizePolicy().hasHeightForWidth())
        self.promptCancel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.promptCancel)


        self.verticalLayout_4.addWidget(self.promptOptionWidget)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.stack.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.verticalLayout_11 = QVBoxLayout(self.page3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 15, 0, -1)
        self.settingTitleBar = QWidget(self.page3)
        self.settingTitleBar.setObjectName(u"settingTitleBar")
        self.settingTitleBar.setMinimumSize(QSize(0, 40))
        self.settingTitleBar.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_13 = QHBoxLayout(self.settingTitleBar)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_17 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)

        self.searchBar = QLineEdit(self.settingTitleBar)
        self.searchBar.setObjectName(u"searchBar")

        self.horizontalLayout_13.addWidget(self.searchBar)

        self.horizontalSpacer_16 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.closeSettingBtn = QToolButton(self.settingTitleBar)
        self.closeSettingBtn.setObjectName(u"closeSettingBtn")

        self.horizontalLayout_13.addWidget(self.closeSettingBtn)


        self.verticalLayout_11.addWidget(self.settingTitleBar)

        self.settingContent = QWidget(self.page3)
        self.settingContent.setObjectName(u"settingContent")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.settingContent.sizePolicy().hasHeightForWidth())
        self.settingContent.setSizePolicy(sizePolicy6)
        self.horizontalLayout_15 = QHBoxLayout(self.settingContent)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.settingMenu = QWidget(self.settingContent)
        self.settingMenu.setObjectName(u"settingMenu")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.settingMenu.sizePolicy().hasHeightForWidth())
        self.settingMenu.setSizePolicy(sizePolicy7)
        self.settingMenu.setMinimumSize(QSize(150, 0))
        self.settingMenu.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.settingMenu)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 15, 9, 0)
        self.connSettingBtn = QPushButton(self.settingMenu)
        self.connSettingBtn.setObjectName(u"connSettingBtn")
        self.connSettingBtn.setCheckable(True)
        self.connSettingBtn.setChecked(True)

        self.verticalLayout_12.addWidget(self.connSettingBtn)

        self.generalSettingBtn = QPushButton(self.settingMenu)
        self.generalSettingBtn.setObjectName(u"generalSettingBtn")

        self.verticalLayout_12.addWidget(self.generalSettingBtn)

        self.paintSettingBtn = QPushButton(self.settingMenu)
        self.paintSettingBtn.setObjectName(u"paintSettingBtn")

        self.verticalLayout_12.addWidget(self.paintSettingBtn)

        self.voiceSettingBtn = QPushButton(self.settingMenu)
        self.voiceSettingBtn.setObjectName(u"voiceSettingBtn")

        self.verticalLayout_12.addWidget(self.voiceSettingBtn)

        self.confirmSettingBtn = QPushButton(self.settingMenu)
        self.confirmSettingBtn.setObjectName(u"confirmSettingBtn")

        self.verticalLayout_12.addWidget(self.confirmSettingBtn)

        self.searchSettingBtn = QPushButton(self.settingMenu)
        self.searchSettingBtn.setObjectName(u"searchSettingBtn")

        self.verticalLayout_12.addWidget(self.searchSettingBtn)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)


        self.horizontalLayout_15.addWidget(self.settingMenu)

        self.settingWidget = QWidget(self.settingContent)
        self.settingWidget.setObjectName(u"settingWidget")
        self.verticalLayout_13 = QVBoxLayout(self.settingWidget)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 15, 0, 0)
        self.settingTitle = QLabel(self.settingWidget)
        self.settingTitle.setObjectName(u"settingTitle")
        sizePolicy4.setHeightForWidth(self.settingTitle.sizePolicy().hasHeightForWidth())
        self.settingTitle.setSizePolicy(sizePolicy4)
        self.settingTitle.setMargin(0)
        self.settingTitle.setIndent(15)

        self.verticalLayout_13.addWidget(self.settingTitle)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)

        self.divider8 = QWidget(self.settingWidget)
        self.divider8.setObjectName(u"divider8")
        sizePolicy4.setHeightForWidth(self.divider8.sizePolicy().hasHeightForWidth())
        self.divider8.setSizePolicy(sizePolicy4)
        self.divider8.setMinimumSize(QSize(0, 1))
        self.divider8.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_13.addWidget(self.divider8)

        self.settingStack = QStackedWidget(self.settingWidget)
        self.settingStack.setObjectName(u"settingStack")
        self.connSettingPage = QWidget()
        self.connSettingPage.setObjectName(u"connSettingPage")
        self.horizontalLayout_16 = QHBoxLayout(self.connSettingPage)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.connScroll = QScrollArea(self.connSettingPage)
        self.connScroll.setObjectName(u"connScroll")
        self.connScroll.setMaximumSize(QSize(1000, 16777215))
        self.connScroll.setWidgetResizable(True)
        self.connScrollWidget = QWidget()
        self.connScrollWidget.setObjectName(u"connScrollWidget")
        self.connScrollWidget.setGeometry(QRect(0, 0, 619, 922))
        self.verticalLayout_14 = QVBoxLayout(self.connScrollWidget)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 15, 9, 15)
        self.APIKeyTitle = QLabel(self.connScrollWidget)
        self.APIKeyTitle.setObjectName(u"APIKeyTitle")
        sizePolicy4.setHeightForWidth(self.APIKeyTitle.sizePolicy().hasHeightForWidth())
        self.APIKeyTitle.setSizePolicy(sizePolicy4)
        self.APIKeyTitle.setIndent(16)

        self.verticalLayout_14.addWidget(self.APIKeyTitle)

        self.APIKeySetting = QWidget(self.connScrollWidget)
        self.APIKeySetting.setObjectName(u"APIKeySetting")
        sizePolicy4.setHeightForWidth(self.APIKeySetting.sizePolicy().hasHeightForWidth())
        self.APIKeySetting.setSizePolicy(sizePolicy4)
        self.verticalLayout_15 = QVBoxLayout(self.APIKeySetting)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.APIKeyWidget = QWidget(self.APIKeySetting)
        self.APIKeyWidget.setObjectName(u"APIKeyWidget")
        sizePolicy4.setHeightForWidth(self.APIKeyWidget.sizePolicy().hasHeightForWidth())
        self.APIKeyWidget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_17 = QHBoxLayout(self.APIKeyWidget)
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(15, 15, 15, 15)
        self.APIKeyEdit = QLineEdit(self.APIKeyWidget)
        self.APIKeyEdit.setObjectName(u"APIKeyEdit")
        self.APIKeyEdit.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_17.addWidget(self.APIKeyEdit)

        self.horizontalSpacer_19 = QSpacerItem(6, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_19)

        self.removeAPIKeyBtn = QToolButton(self.APIKeyWidget)
        self.removeAPIKeyBtn.setObjectName(u"removeAPIKeyBtn")

        self.horizontalLayout_17.addWidget(self.removeAPIKeyBtn)

        self.addAPIKeyBtn = QToolButton(self.APIKeyWidget)
        self.addAPIKeyBtn.setObjectName(u"addAPIKeyBtn")

        self.horizontalLayout_17.addWidget(self.addAPIKeyBtn)


        self.verticalLayout_15.addWidget(self.APIKeyWidget)


        self.verticalLayout_14.addWidget(self.APIKeySetting)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_7)

        self.APISettingTitle = QLabel(self.connScrollWidget)
        self.APISettingTitle.setObjectName(u"APISettingTitle")
        sizePolicy4.setHeightForWidth(self.APISettingTitle.sizePolicy().hasHeightForWidth())
        self.APISettingTitle.setSizePolicy(sizePolicy4)
        self.APISettingTitle.setIndent(16)

        self.verticalLayout_14.addWidget(self.APISettingTitle)

        self.APISettingWidget = QWidget(self.connScrollWidget)
        self.APISettingWidget.setObjectName(u"APISettingWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.APISettingWidget.sizePolicy().hasHeightForWidth())
        self.APISettingWidget.setSizePolicy(sizePolicy8)
        self.verticalLayout_16 = QVBoxLayout(self.APISettingWidget)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(15, 15, 15, 15)
        self.baseUrlWidget = QWidget(self.APISettingWidget)
        self.baseUrlWidget.setObjectName(u"baseUrlWidget")
        sizePolicy4.setHeightForWidth(self.baseUrlWidget.sizePolicy().hasHeightForWidth())
        self.baseUrlWidget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_18 = QHBoxLayout(self.baseUrlWidget)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.baseUrlLabel = QLabel(self.baseUrlWidget)
        self.baseUrlLabel.setObjectName(u"baseUrlLabel")
        sizePolicy2.setHeightForWidth(self.baseUrlLabel.sizePolicy().hasHeightForWidth())
        self.baseUrlLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_18.addWidget(self.baseUrlLabel)

        self.horizontalSpacer_20 = QSpacerItem(15, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_20)

        self.baseUrl = QLineEdit(self.baseUrlWidget)
        self.baseUrl.setObjectName(u"baseUrl")
        sizePolicy2.setHeightForWidth(self.baseUrl.sizePolicy().hasHeightForWidth())
        self.baseUrl.setSizePolicy(sizePolicy2)
        self.baseUrl.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_18.addWidget(self.baseUrl)


        self.verticalLayout_16.addWidget(self.baseUrlWidget)

        self.divider9 = QWidget(self.APISettingWidget)
        self.divider9.setObjectName(u"divider9")
        sizePolicy3.setHeightForWidth(self.divider9.sizePolicy().hasHeightForWidth())
        self.divider9.setSizePolicy(sizePolicy3)
        self.divider9.setMinimumSize(QSize(0, 1))
        self.divider9.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_16.addWidget(self.divider9)

        self.modelWidget = QWidget(self.APISettingWidget)
        self.modelWidget.setObjectName(u"modelWidget")
        sizePolicy4.setHeightForWidth(self.modelWidget.sizePolicy().hasHeightForWidth())
        self.modelWidget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_19 = QHBoxLayout(self.modelWidget)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.modelSettingLabel = QLabel(self.modelWidget)
        self.modelSettingLabel.setObjectName(u"modelSettingLabel")
        sizePolicy2.setHeightForWidth(self.modelSettingLabel.sizePolicy().hasHeightForWidth())
        self.modelSettingLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_19.addWidget(self.modelSettingLabel)

        self.horizontalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_21)

        self.modelCombo = QComboBox(self.modelWidget)
        self.modelCombo.addItem("")
        self.modelCombo.setObjectName(u"modelCombo")
        sizePolicy2.setHeightForWidth(self.modelCombo.sizePolicy().hasHeightForWidth())
        self.modelCombo.setSizePolicy(sizePolicy2)

        self.horizontalLayout_19.addWidget(self.modelCombo)

        self.listModel = QPushButton(self.modelWidget)
        self.listModel.setObjectName(u"listModel")

        self.horizontalLayout_19.addWidget(self.listModel)


        self.verticalLayout_16.addWidget(self.modelWidget)

        self.divider10 = QWidget(self.APISettingWidget)
        self.divider10.setObjectName(u"divider10")
        sizePolicy3.setHeightForWidth(self.divider10.sizePolicy().hasHeightForWidth())
        self.divider10.setSizePolicy(sizePolicy3)
        self.divider10.setMinimumSize(QSize(0, 1))
        self.divider10.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_16.addWidget(self.divider10)

        self.enableToolWidget = QWidget(self.APISettingWidget)
        self.enableToolWidget.setObjectName(u"enableToolWidget")
        sizePolicy3.setHeightForWidth(self.enableToolWidget.sizePolicy().hasHeightForWidth())
        self.enableToolWidget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_20 = QHBoxLayout(self.enableToolWidget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.enableToolLabel = QLabel(self.enableToolWidget)
        self.enableToolLabel.setObjectName(u"enableToolLabel")
        sizePolicy.setHeightForWidth(self.enableToolLabel.sizePolicy().hasHeightForWidth())
        self.enableToolLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_20.addWidget(self.enableToolLabel)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_22)

        self.enableTool = SwitchButton(self.enableToolWidget)
        self.enableTool.setObjectName(u"enableTool")
        self.enableTool.setChecked(True)

        self.horizontalLayout_20.addWidget(self.enableTool)


        self.verticalLayout_16.addWidget(self.enableToolWidget)

        self.divider11 = QWidget(self.APISettingWidget)
        self.divider11.setObjectName(u"divider11")
        sizePolicy4.setHeightForWidth(self.divider11.sizePolicy().hasHeightForWidth())
        self.divider11.setSizePolicy(sizePolicy4)
        self.divider11.setMinimumSize(QSize(0, 1))
        self.divider11.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_16.addWidget(self.divider11)

        self.reasoningEffortWidget = QWidget(self.APISettingWidget)
        self.reasoningEffortWidget.setObjectName(u"reasoningEffortWidget")
        sizePolicy4.setHeightForWidth(self.reasoningEffortWidget.sizePolicy().hasHeightForWidth())
        self.reasoningEffortWidget.setSizePolicy(sizePolicy4)
        self.gridLayout_10 = QGridLayout(self.reasoningEffortWidget)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.reasoningEffortLabel = QLabel(self.reasoningEffortWidget)
        self.reasoningEffortLabel.setObjectName(u"reasoningEffortLabel")
        sizePolicy.setHeightForWidth(self.reasoningEffortLabel.sizePolicy().hasHeightForWidth())
        self.reasoningEffortLabel.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.reasoningEffortLabel, 0, 0, 1, 1)

        self.reasoningEffortComboWidget = QWidget(self.reasoningEffortWidget)
        self.reasoningEffortComboWidget.setObjectName(u"reasoningEffortComboWidget")
        self.horizontalLayout_21 = QHBoxLayout(self.reasoningEffortComboWidget)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_23)

        self.reasoningEffort = QComboBox(self.reasoningEffortComboWidget)
        self.reasoningEffort.addItem("")
        self.reasoningEffort.addItem("")
        self.reasoningEffort.addItem("")
        self.reasoningEffort.addItem("")
        self.reasoningEffort.addItem("")
        self.reasoningEffort.addItem("")
        self.reasoningEffort.addItem("")
        self.reasoningEffort.setObjectName(u"reasoningEffort")
        sizePolicy2.setHeightForWidth(self.reasoningEffort.sizePolicy().hasHeightForWidth())
        self.reasoningEffort.setSizePolicy(sizePolicy2)
        self.reasoningEffort.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_21.addWidget(self.reasoningEffort)


        self.gridLayout_10.addWidget(self.reasoningEffortComboWidget, 0, 1, 1, 1)

        self.defaultReasoningEffortWidget = QWidget(self.reasoningEffortWidget)
        self.defaultReasoningEffortWidget.setObjectName(u"defaultReasoningEffortWidget")
        self.horizontalLayout_22 = QHBoxLayout(self.defaultReasoningEffortWidget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_24)

        self.defaultReasoningEffort = SwitchButton(self.defaultReasoningEffortWidget)
        self.defaultReasoningEffort.setObjectName(u"defaultReasoningEffort")
        self.defaultReasoningEffort.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.defaultReasoningEffort.setTristate(False)

        self.horizontalLayout_22.addWidget(self.defaultReasoningEffort)


        self.gridLayout_10.addWidget(self.defaultReasoningEffortWidget, 1, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.reasoningEffortWidget)

        self.divider12 = QWidget(self.APISettingWidget)
        self.divider12.setObjectName(u"divider12")
        self.divider12.setMinimumSize(QSize(0, 1))
        self.divider12.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_16.addWidget(self.divider12)

        self.extraBodyWidget = QWidget(self.APISettingWidget)
        self.extraBodyWidget.setObjectName(u"extraBodyWidget")
        self.horizontalLayout_23 = QHBoxLayout(self.extraBodyWidget)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.extraBodyLabel = QLabel(self.extraBodyWidget)
        self.extraBodyLabel.setObjectName(u"extraBodyLabel")
        sizePolicy.setHeightForWidth(self.extraBodyLabel.sizePolicy().hasHeightForWidth())
        self.extraBodyLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_23.addWidget(self.extraBodyLabel)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_25)

        self.extraBody = QLineEdit(self.extraBodyWidget)
        self.extraBody.setObjectName(u"extraBody")
        sizePolicy2.setHeightForWidth(self.extraBody.sizePolicy().hasHeightForWidth())
        self.extraBody.setSizePolicy(sizePolicy2)
        self.extraBody.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_23.addWidget(self.extraBody)


        self.verticalLayout_16.addWidget(self.extraBodyWidget)


        self.verticalLayout_14.addWidget(self.APISettingWidget)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_9)

        self.proxyLabel = QLabel(self.connScrollWidget)
        self.proxyLabel.setObjectName(u"proxyLabel")
        sizePolicy4.setHeightForWidth(self.proxyLabel.sizePolicy().hasHeightForWidth())
        self.proxyLabel.setSizePolicy(sizePolicy4)
        self.proxyLabel.setIndent(16)

        self.verticalLayout_14.addWidget(self.proxyLabel)

        self.proxyWidget = QWidget(self.connScrollWidget)
        self.proxyWidget.setObjectName(u"proxyWidget")
        sizePolicy4.setHeightForWidth(self.proxyWidget.sizePolicy().hasHeightForWidth())
        self.proxyWidget.setSizePolicy(sizePolicy4)
        self.verticalLayout_17 = QVBoxLayout(self.proxyWidget)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(15, 15, 15, 15)
        self.enableProxyWidget = QWidget(self.proxyWidget)
        self.enableProxyWidget.setObjectName(u"enableProxyWidget")
        self.horizontalLayout_25 = QHBoxLayout(self.enableProxyWidget)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.enableProxyLabel = QLabel(self.enableProxyWidget)
        self.enableProxyLabel.setObjectName(u"enableProxyLabel")
        sizePolicy.setHeightForWidth(self.enableProxyLabel.sizePolicy().hasHeightForWidth())
        self.enableProxyLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_25.addWidget(self.enableProxyLabel)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_27)

        self.enableProxy = SwitchButton(self.enableProxyWidget)
        self.enableProxy.setObjectName(u"enableProxy")
        sizePolicy2.setHeightForWidth(self.enableProxy.sizePolicy().hasHeightForWidth())
        self.enableProxy.setSizePolicy(sizePolicy2)

        self.horizontalLayout_25.addWidget(self.enableProxy)


        self.verticalLayout_17.addWidget(self.enableProxyWidget)

        self.divider15 = QWidget(self.proxyWidget)
        self.divider15.setObjectName(u"divider15")
        self.divider15.setMinimumSize(QSize(0, 1))
        self.divider15.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_17.addWidget(self.divider15)

        self.sysProxyWidget = QWidget(self.proxyWidget)
        self.sysProxyWidget.setObjectName(u"sysProxyWidget")
        sizePolicy4.setHeightForWidth(self.sysProxyWidget.sizePolicy().hasHeightForWidth())
        self.sysProxyWidget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_24 = QHBoxLayout(self.sysProxyWidget)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.sysProxyLabel = QLabel(self.sysProxyWidget)
        self.sysProxyLabel.setObjectName(u"sysProxyLabel")
        sizePolicy.setHeightForWidth(self.sysProxyLabel.sizePolicy().hasHeightForWidth())
        self.sysProxyLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_24.addWidget(self.sysProxyLabel)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_26)

        self.sysProxy = SwitchButton(self.sysProxyWidget)
        self.sysProxy.setObjectName(u"sysProxy")
        sizePolicy2.setHeightForWidth(self.sysProxy.sizePolicy().hasHeightForWidth())
        self.sysProxy.setSizePolicy(sizePolicy2)
        self.sysProxy.setChecked(True)

        self.horizontalLayout_24.addWidget(self.sysProxy)


        self.verticalLayout_17.addWidget(self.sysProxyWidget)


        self.verticalLayout_14.addWidget(self.proxyWidget)

        self.verticalSpacer_10 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_10)

        self.manualProxyLabel = QLabel(self.connScrollWidget)
        self.manualProxyLabel.setObjectName(u"manualProxyLabel")
        sizePolicy3.setHeightForWidth(self.manualProxyLabel.sizePolicy().hasHeightForWidth())
        self.manualProxyLabel.setSizePolicy(sizePolicy3)
        self.manualProxyLabel.setIndent(16)

        self.verticalLayout_14.addWidget(self.manualProxyLabel)

        self.manualProxyWidget = QWidget(self.connScrollWidget)
        self.manualProxyWidget.setObjectName(u"manualProxyWidget")
        sizePolicy4.setHeightForWidth(self.manualProxyWidget.sizePolicy().hasHeightForWidth())
        self.manualProxyWidget.setSizePolicy(sizePolicy4)
        self.verticalLayout_18 = QVBoxLayout(self.manualProxyWidget)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(15, 15, 15, 15)
        self.proxyAddressWidget = QWidget(self.manualProxyWidget)
        self.proxyAddressWidget.setObjectName(u"proxyAddressWidget")
        sizePolicy3.setHeightForWidth(self.proxyAddressWidget.sizePolicy().hasHeightForWidth())
        self.proxyAddressWidget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_26 = QHBoxLayout(self.proxyAddressWidget)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.proxyAddressLabel = QLabel(self.proxyAddressWidget)
        self.proxyAddressLabel.setObjectName(u"proxyAddressLabel")
        sizePolicy.setHeightForWidth(self.proxyAddressLabel.sizePolicy().hasHeightForWidth())
        self.proxyAddressLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_26.addWidget(self.proxyAddressLabel)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_28)

        self.proxyAddress = QLineEdit(self.proxyAddressWidget)
        self.proxyAddress.setObjectName(u"proxyAddress")
        self.proxyAddress.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_26.addWidget(self.proxyAddress)


        self.verticalLayout_18.addWidget(self.proxyAddressWidget)

        self.divider13 = QWidget(self.manualProxyWidget)
        self.divider13.setObjectName(u"divider13")
        sizePolicy3.setHeightForWidth(self.divider13.sizePolicy().hasHeightForWidth())
        self.divider13.setSizePolicy(sizePolicy3)
        self.divider13.setMinimumSize(QSize(0, 1))
        self.divider13.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_18.addWidget(self.divider13)

        self.proxyPortWidget = QWidget(self.manualProxyWidget)
        self.proxyPortWidget.setObjectName(u"proxyPortWidget")
        self.horizontalLayout_27 = QHBoxLayout(self.proxyPortWidget)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.proxyPortLabel = QLabel(self.proxyPortWidget)
        self.proxyPortLabel.setObjectName(u"proxyPortLabel")
        sizePolicy.setHeightForWidth(self.proxyPortLabel.sizePolicy().hasHeightForWidth())
        self.proxyPortLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_27.addWidget(self.proxyPortLabel)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_29)

        self.proxyPort = QSpinBox(self.proxyPortWidget)
        self.proxyPort.setObjectName(u"proxyPort")
        self.proxyPort.setMaximum(65535)

        self.horizontalLayout_27.addWidget(self.proxyPort)


        self.verticalLayout_18.addWidget(self.proxyPortWidget)

        self.divider14 = QWidget(self.manualProxyWidget)
        self.divider14.setObjectName(u"divider14")
        sizePolicy3.setHeightForWidth(self.divider14.sizePolicy().hasHeightForWidth())
        self.divider14.setSizePolicy(sizePolicy3)
        self.divider14.setMinimumSize(QSize(0, 1))
        self.divider14.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_18.addWidget(self.divider14)

        self.proxyTypeWidget = QWidget(self.manualProxyWidget)
        self.proxyTypeWidget.setObjectName(u"proxyTypeWidget")
        self.horizontalLayout_28 = QHBoxLayout(self.proxyTypeWidget)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.proxyTypeLabel = QLabel(self.proxyTypeWidget)
        self.proxyTypeLabel.setObjectName(u"proxyTypeLabel")
        sizePolicy.setHeightForWidth(self.proxyTypeLabel.sizePolicy().hasHeightForWidth())
        self.proxyTypeLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_28.addWidget(self.proxyTypeLabel)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_30)

        self.proxyType = QComboBox(self.proxyTypeWidget)
        self.proxyType.addItem("")
        self.proxyType.addItem("")
        self.proxyType.addItem("")
        self.proxyType.addItem("")
        self.proxyType.setObjectName(u"proxyType")

        self.horizontalLayout_28.addWidget(self.proxyType)


        self.verticalLayout_18.addWidget(self.proxyTypeWidget)


        self.verticalLayout_14.addWidget(self.manualProxyWidget)

        self.verticalSpacer_11 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_11)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_8)

        self.connScroll.setWidget(self.connScrollWidget)

        self.horizontalLayout_16.addWidget(self.connScroll)

        self.settingStack.addWidget(self.connSettingPage)
        self.generalSettingPage = QWidget()
        self.generalSettingPage.setObjectName(u"generalSettingPage")
        self.horizontalLayout_29 = QHBoxLayout(self.generalSettingPage)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.generalScroll = QScrollArea(self.generalSettingPage)
        self.generalScroll.setObjectName(u"generalScroll")
        self.generalScroll.setWidgetResizable(True)
        self.generalScrollWidget = QWidget()
        self.generalScrollWidget.setObjectName(u"generalScrollWidget")
        self.generalScrollWidget.setGeometry(QRect(0, -499, 650, 1073))
        self.verticalLayout_19 = QVBoxLayout(self.generalScrollWidget)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 15, 9, 15)
        self.locationSeetingLabel = QLabel(self.generalScrollWidget)
        self.locationSeetingLabel.setObjectName(u"locationSeetingLabel")
        sizePolicy3.setHeightForWidth(self.locationSeetingLabel.sizePolicy().hasHeightForWidth())
        self.locationSeetingLabel.setSizePolicy(sizePolicy3)
        self.locationSeetingLabel.setIndent(16)

        self.verticalLayout_19.addWidget(self.locationSeetingLabel)

        self.locationSettingWidget = QWidget(self.generalScrollWidget)
        self.locationSettingWidget.setObjectName(u"locationSettingWidget")
        sizePolicy3.setHeightForWidth(self.locationSettingWidget.sizePolicy().hasHeightForWidth())
        self.locationSettingWidget.setSizePolicy(sizePolicy3)
        self.verticalLayout_22 = QVBoxLayout(self.locationSettingWidget)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, 15, 15, 15)
        self.enableLocationWidget = QWidget(self.locationSettingWidget)
        self.enableLocationWidget.setObjectName(u"enableLocationWidget")
        sizePolicy3.setHeightForWidth(self.enableLocationWidget.sizePolicy().hasHeightForWidth())
        self.enableLocationWidget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_34 = QHBoxLayout(self.enableLocationWidget)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.enableLocationLabel = QLabel(self.enableLocationWidget)
        self.enableLocationLabel.setObjectName(u"enableLocationLabel")
        sizePolicy.setHeightForWidth(self.enableLocationLabel.sizePolicy().hasHeightForWidth())
        self.enableLocationLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_34.addWidget(self.enableLocationLabel)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_35)

        self.enableLocation = SwitchButton(self.enableLocationWidget)
        self.enableLocation.setObjectName(u"enableLocation")

        self.horizontalLayout_34.addWidget(self.enableLocation)


        self.verticalLayout_22.addWidget(self.enableLocationWidget)

        self.divider18 = QWidget(self.locationSettingWidget)
        self.divider18.setObjectName(u"divider18")
        self.divider18.setMinimumSize(QSize(0, 1))
        self.divider18.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_22.addWidget(self.divider18)

        self.locationWidget = QWidget(self.locationSettingWidget)
        self.locationWidget.setObjectName(u"locationWidget")
        self.gridLayout_4 = QGridLayout(self.locationWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.countriesCombo = QComboBox(self.locationWidget)
        self.countriesCombo.setObjectName(u"countriesCombo")
        sizePolicy2.setHeightForWidth(self.countriesCombo.sizePolicy().hasHeightForWidth())
        self.countriesCombo.setSizePolicy(sizePolicy2)
        self.countriesCombo.setMinimumSize(QSize(120, 0))
        self.countriesCombo.setMaximumSize(QSize(125, 16777215))
        self.countriesCombo.setEditable(True)

        self.gridLayout_4.addWidget(self.countriesCombo, 0, 2, 1, 1)

        self.adm1Combo = QComboBox(self.locationWidget)
        self.adm1Combo.setObjectName(u"adm1Combo")
        self.adm1Combo.setMinimumSize(QSize(120, 0))
        self.adm1Combo.setMaximumSize(QSize(125, 16777215))
        self.adm1Combo.setEditable(True)

        self.gridLayout_4.addWidget(self.adm1Combo, 0, 3, 1, 1)

        self.adm2Combo = QComboBox(self.locationWidget)
        self.adm2Combo.setObjectName(u"adm2Combo")
        self.adm2Combo.setMinimumSize(QSize(120, 0))
        self.adm2Combo.setEditable(True)

        self.gridLayout_4.addWidget(self.adm2Combo, 0, 4, 1, 1)

        self.adm3Combo = QComboBox(self.locationWidget)
        self.adm3Combo.setObjectName(u"adm3Combo")
        self.adm3Combo.setMinimumSize(QSize(120, 0))
        self.adm3Combo.setEditable(True)

        self.gridLayout_4.addWidget(self.adm3Combo, 0, 5, 1, 1)

        self.locationLabel = QLabel(self.locationWidget)
        self.locationLabel.setObjectName(u"locationLabel")
        sizePolicy.setHeightForWidth(self.locationLabel.sizePolicy().hasHeightForWidth())
        self.locationLabel.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.locationLabel, 0, 0, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_34, 0, 1, 1, 1)

        self.showLocationInfo = QLabel(self.locationWidget)
        self.showLocationInfo.setObjectName(u"showLocationInfo")
        sizePolicy3.setHeightForWidth(self.showLocationInfo.sizePolicy().hasHeightForWidth())
        self.showLocationInfo.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.showLocationInfo, 2, 0, 1, 4)

        self.autoGetLocation = QPushButton(self.locationWidget)
        self.autoGetLocation.setObjectName(u"autoGetLocation")
        sizePolicy2.setHeightForWidth(self.autoGetLocation.sizePolicy().hasHeightForWidth())
        self.autoGetLocation.setSizePolicy(sizePolicy2)
        self.autoGetLocation.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_4.addWidget(self.autoGetLocation, 2, 4, 1, 2)


        self.verticalLayout_22.addWidget(self.locationWidget)


        self.verticalLayout_19.addWidget(self.locationSettingWidget)

        self.verticalSpacer_16 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_16)

        self.uiSettingTitle = QLabel(self.generalScrollWidget)
        self.uiSettingTitle.setObjectName(u"uiSettingTitle")
        sizePolicy4.setHeightForWidth(self.uiSettingTitle.sizePolicy().hasHeightForWidth())
        self.uiSettingTitle.setSizePolicy(sizePolicy4)
        self.uiSettingTitle.setMargin(0)
        self.uiSettingTitle.setIndent(16)

        self.verticalLayout_19.addWidget(self.uiSettingTitle)

        self.uiSettingWidget = QWidget(self.generalScrollWidget)
        self.uiSettingWidget.setObjectName(u"uiSettingWidget")
        self.verticalLayout_21 = QVBoxLayout(self.uiSettingWidget)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(15, 15, 15, 15)
        self.themeWidge = QWidget(self.uiSettingWidget)
        self.themeWidge.setObjectName(u"themeWidge")
        sizePolicy4.setHeightForWidth(self.themeWidge.sizePolicy().hasHeightForWidth())
        self.themeWidge.setSizePolicy(sizePolicy4)
        self.gridLayout_3 = QGridLayout(self.themeWidge)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_31, 0, 1, 1, 1)

        self.followSysTheme = SwitchButton(self.themeWidge)
        self.followSysTheme.setObjectName(u"followSysTheme")
        sizePolicy2.setHeightForWidth(self.followSysTheme.sizePolicy().hasHeightForWidth())
        self.followSysTheme.setSizePolicy(sizePolicy2)
        self.followSysTheme.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.followSysTheme.setChecked(True)

        self.gridLayout_3.addWidget(self.followSysTheme, 0, 2, 1, 1)

        self.themeLabel = QLabel(self.themeWidge)
        self.themeLabel.setObjectName(u"themeLabel")
        sizePolicy2.setHeightForWidth(self.themeLabel.sizePolicy().hasHeightForWidth())
        self.themeLabel.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.themeLabel, 0, 0, 1, 1)

        self.theme = QComboBox(self.themeWidge)
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.setObjectName(u"theme")
        self.theme.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.theme, 1, 2, 1, 1)


        self.verticalLayout_21.addWidget(self.themeWidge)

        self.showWeatherWidget = QWidget(self.uiSettingWidget)
        self.showWeatherWidget.setObjectName(u"showWeatherWidget")
        self.horizontalLayout_33 = QHBoxLayout(self.showWeatherWidget)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_21.addWidget(self.showWeatherWidget)

        self.divider21 = QWidget(self.uiSettingWidget)
        self.divider21.setObjectName(u"divider21")
        self.divider21.setMinimumSize(QSize(0, 1))
        self.divider21.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_21.addWidget(self.divider21)

        self.setBackgroundWidget = QWidget(self.uiSettingWidget)
        self.setBackgroundWidget.setObjectName(u"setBackgroundWidget")
        self.horizontalLayout_36 = QHBoxLayout(self.setBackgroundWidget)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.setBackgroundLabel = QLabel(self.setBackgroundWidget)
        self.setBackgroundLabel.setObjectName(u"setBackgroundLabel")
        sizePolicy.setHeightForWidth(self.setBackgroundLabel.sizePolicy().hasHeightForWidth())
        self.setBackgroundLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_36.addWidget(self.setBackgroundLabel)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_45)

        self.setBackground = QPushButton(self.setBackgroundWidget)
        self.setBackground.setObjectName(u"setBackground")

        self.horizontalLayout_36.addWidget(self.setBackground)


        self.verticalLayout_21.addWidget(self.setBackgroundWidget)


        self.verticalLayout_19.addWidget(self.uiSettingWidget)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_14)

        self.statusBarComponentTitle = QLabel(self.generalScrollWidget)
        self.statusBarComponentTitle.setObjectName(u"statusBarComponentTitle")
        self.statusBarComponentTitle.setIndent(16)

        self.verticalLayout_19.addWidget(self.statusBarComponentTitle)

        self.statusBarComponentWidget = QWidget(self.generalScrollWidget)
        self.statusBarComponentWidget.setObjectName(u"statusBarComponentWidget")
        self.gridLayout_9 = QGridLayout(self.statusBarComponentWidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(6)
        self.gridLayout_9.setVerticalSpacing(10)
        self.gridLayout_9.setContentsMargins(15, 15, 15, 15)
        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_48, 0, 1, 1, 1)

        self.divider26 = QWidget(self.statusBarComponentWidget)
        self.divider26.setObjectName(u"divider26")
        self.divider26.setMinimumSize(QSize(0, 1))
        self.divider26.setMaximumSize(QSize(16777215, 1))

        self.gridLayout_9.addWidget(self.divider26, 3, 0, 1, 3)

        self.divider20 = QWidget(self.statusBarComponentWidget)
        self.divider20.setObjectName(u"divider20")
        self.divider20.setMinimumSize(QSize(0, 1))
        self.divider20.setMaximumSize(QSize(16777215, 1))

        self.gridLayout_9.addWidget(self.divider20, 1, 0, 1, 3)

        self.roundTokensComponent = SwitchButton(self.statusBarComponentWidget)
        self.roundTokensComponent.setObjectName(u"roundTokensComponent")
        self.roundTokensComponent.setChecked(True)

        self.gridLayout_9.addWidget(self.roundTokensComponent, 0, 2, 1, 1)

        self.roundTokensComponentLabel = QLabel(self.statusBarComponentWidget)
        self.roundTokensComponentLabel.setObjectName(u"roundTokensComponentLabel")
        sizePolicy.setHeightForWidth(self.roundTokensComponentLabel.sizePolicy().hasHeightForWidth())
        self.roundTokensComponentLabel.setSizePolicy(sizePolicy)

        self.gridLayout_9.addWidget(self.roundTokensComponentLabel, 0, 0, 1, 1)

        self.divider27 = QWidget(self.statusBarComponentWidget)
        self.divider27.setObjectName(u"divider27")
        self.divider27.setMinimumSize(QSize(0, 1))
        self.divider27.setMaximumSize(QSize(16777215, 1))

        self.gridLayout_9.addWidget(self.divider27, 4, 0, 1, 3)

        self.totalTokensComponent = SwitchButton(self.statusBarComponentWidget)
        self.totalTokensComponent.setObjectName(u"totalTokensComponent")
        self.totalTokensComponent.setChecked(True)

        self.gridLayout_9.addWidget(self.totalTokensComponent, 2, 2, 1, 1)

        self.totalTokensComponentLabel = QLabel(self.statusBarComponentWidget)
        self.totalTokensComponentLabel.setObjectName(u"totalTokensComponentLabel")

        self.gridLayout_9.addWidget(self.totalTokensComponentLabel, 2, 0, 1, 1)

        self.weatherComponentlabel = QLabel(self.statusBarComponentWidget)
        self.weatherComponentlabel.setObjectName(u"weatherComponentlabel")

        self.gridLayout_9.addWidget(self.weatherComponentlabel, 5, 0, 1, 1)

        self.weatherComponent = SwitchButton(self.statusBarComponentWidget)
        self.weatherComponent.setObjectName(u"weatherComponent")
        self.weatherComponent.setChecked(True)

        self.gridLayout_9.addWidget(self.weatherComponent, 5, 2, 1, 1)


        self.verticalLayout_19.addWidget(self.statusBarComponentWidget)

        self.verticalSpacer_19 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_19)

        self.chatSettingTitle = QLabel(self.generalScrollWidget)
        self.chatSettingTitle.setObjectName(u"chatSettingTitle")
        self.chatSettingTitle.setTextFormat(Qt.TextFormat.AutoText)
        self.chatSettingTitle.setIndent(16)

        self.verticalLayout_19.addWidget(self.chatSettingTitle)

        self.chatSettingWidget = QWidget(self.generalScrollWidget)
        self.chatSettingWidget.setObjectName(u"chatSettingWidget")
        sizePolicy3.setHeightForWidth(self.chatSettingWidget.sizePolicy().hasHeightForWidth())
        self.chatSettingWidget.setSizePolicy(sizePolicy3)
        self.verticalLayout_20 = QVBoxLayout(self.chatSettingWidget)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(15, 15, 15, 15)
        self.sendSettingWidget = QWidget(self.chatSettingWidget)
        self.sendSettingWidget.setObjectName(u"sendSettingWidget")
        sizePolicy4.setHeightForWidth(self.sendSettingWidget.sizePolicy().hasHeightForWidth())
        self.sendSettingWidget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_31 = QHBoxLayout(self.sendSettingWidget)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.sendSettingLabel = QLabel(self.sendSettingWidget)
        self.sendSettingLabel.setObjectName(u"sendSettingLabel")
        sizePolicy.setHeightForWidth(self.sendSettingLabel.sizePolicy().hasHeightForWidth())
        self.sendSettingLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_31.addWidget(self.sendSettingLabel)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_33)

        self.sendSetting = QComboBox(self.sendSettingWidget)
        self.sendSetting.addItem("")
        self.sendSetting.addItem("")
        self.sendSetting.setObjectName(u"sendSetting")
        sizePolicy2.setHeightForWidth(self.sendSetting.sizePolicy().hasHeightForWidth())
        self.sendSetting.setSizePolicy(sizePolicy2)

        self.horizontalLayout_31.addWidget(self.sendSetting)


        self.verticalLayout_20.addWidget(self.sendSettingWidget)

        self.divider17 = QWidget(self.chatSettingWidget)
        self.divider17.setObjectName(u"divider17")
        sizePolicy4.setHeightForWidth(self.divider17.sizePolicy().hasHeightForWidth())
        self.divider17.setSizePolicy(sizePolicy4)
        self.divider17.setMinimumSize(QSize(0, 1))
        self.divider17.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_20.addWidget(self.divider17)

        self.renderSettingWidget = QWidget(self.chatSettingWidget)
        self.renderSettingWidget.setObjectName(u"renderSettingWidget")
        sizePolicy4.setHeightForWidth(self.renderSettingWidget.sizePolicy().hasHeightForWidth())
        self.renderSettingWidget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_30 = QHBoxLayout(self.renderSettingWidget)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.renderSettingLabel = QLabel(self.renderSettingWidget)
        self.renderSettingLabel.setObjectName(u"renderSettingLabel")
        sizePolicy.setHeightForWidth(self.renderSettingLabel.sizePolicy().hasHeightForWidth())
        self.renderSettingLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_30.addWidget(self.renderSettingLabel)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_32)

        self.renderSetting = SwitchButton(self.renderSettingWidget)
        self.renderSetting.setObjectName(u"renderSetting")

        self.horizontalLayout_30.addWidget(self.renderSetting)


        self.verticalLayout_20.addWidget(self.renderSettingWidget)

        self.divider16 = QWidget(self.chatSettingWidget)
        self.divider16.setObjectName(u"divider16")
        sizePolicy3.setHeightForWidth(self.divider16.sizePolicy().hasHeightForWidth())
        self.divider16.setSizePolicy(sizePolicy3)
        self.divider16.setMinimumSize(QSize(0, 1))
        self.divider16.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_20.addWidget(self.divider16)

        self.msgWithLocationWidget = QWidget(self.chatSettingWidget)
        self.msgWithLocationWidget.setObjectName(u"msgWithLocationWidget")
        self.horizontalLayout_32 = QHBoxLayout(self.msgWithLocationWidget)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.msgWithLocationLabel = QLabel(self.msgWithLocationWidget)
        self.msgWithLocationLabel.setObjectName(u"msgWithLocationLabel")
        sizePolicy.setHeightForWidth(self.msgWithLocationLabel.sizePolicy().hasHeightForWidth())
        self.msgWithLocationLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_32.addWidget(self.msgWithLocationLabel)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_37)

        self.megWithLocation = SwitchButton(self.msgWithLocationWidget)
        self.megWithLocation.setObjectName(u"megWithLocation")

        self.horizontalLayout_32.addWidget(self.megWithLocation)


        self.verticalLayout_20.addWidget(self.msgWithLocationWidget)


        self.verticalLayout_19.addWidget(self.chatSettingWidget)

        self.verticalSpacer_15 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_15)

        self.textStyleTitle = QLabel(self.generalScrollWidget)
        self.textStyleTitle.setObjectName(u"textStyleTitle")
        sizePolicy4.setHeightForWidth(self.textStyleTitle.sizePolicy().hasHeightForWidth())
        self.textStyleTitle.setSizePolicy(sizePolicy4)
        self.textStyleTitle.setIndent(16)

        self.verticalLayout_19.addWidget(self.textStyleTitle)

        self.textStyleWidget = QWidget(self.generalScrollWidget)
        self.textStyleWidget.setObjectName(u"textStyleWidget")
        sizePolicy3.setHeightForWidth(self.textStyleWidget.sizePolicy().hasHeightForWidth())
        self.textStyleWidget.setSizePolicy(sizePolicy3)
        self.verticalLayout_23 = QVBoxLayout(self.textStyleWidget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(15, 15, 15, 15)
        self.fontWidget = QWidget(self.textStyleWidget)
        self.fontWidget.setObjectName(u"fontWidget")
        self.horizontalLayout_35 = QHBoxLayout(self.fontWidget)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.fontLabel = QLabel(self.fontWidget)
        self.fontLabel.setObjectName(u"fontLabel")
        sizePolicy.setHeightForWidth(self.fontLabel.sizePolicy().hasHeightForWidth())
        self.fontLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_35.addWidget(self.fontLabel)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_38)

        self.font = QComboBox(self.fontWidget)
        self.font.addItem("")
        self.font.addItem("")
        self.font.setObjectName(u"font")
        sizePolicy2.setHeightForWidth(self.font.sizePolicy().hasHeightForWidth())
        self.font.setSizePolicy(sizePolicy2)

        self.horizontalLayout_35.addWidget(self.font)


        self.verticalLayout_23.addWidget(self.fontWidget)

        self.divider19 = QWidget(self.textStyleWidget)
        self.divider19.setObjectName(u"divider19")
        self.divider19.setMinimumSize(QSize(0, 1))
        self.divider19.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_23.addWidget(self.divider19)

        self.fontSizeWidget = QWidget(self.textStyleWidget)
        self.fontSizeWidget.setObjectName(u"fontSizeWidget")
        sizePolicy3.setHeightForWidth(self.fontSizeWidget.sizePolicy().hasHeightForWidth())
        self.fontSizeWidget.setSizePolicy(sizePolicy3)
        self.gridLayout_5 = QGridLayout(self.fontSizeWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.fontSizeLabel = QLabel(self.fontSizeWidget)
        self.fontSizeLabel.setObjectName(u"fontSizeLabel")
        sizePolicy.setHeightForWidth(self.fontSizeLabel.sizePolicy().hasHeightForWidth())
        self.fontSizeLabel.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.fontSizeLabel, 1, 0, 1, 3)

        self.standardSizeExample = QLabel(self.fontSizeWidget)
        self.standardSizeExample.setObjectName(u"standardSizeExample")

        self.gridLayout_5.addWidget(self.standardSizeExample, 0, 6, 1, 1)

        self.smallestSizeExample = QLabel(self.fontSizeWidget)
        self.smallestSizeExample.setObjectName(u"smallestSizeExample")
        self.smallestSizeExample.setIndent(2)

        self.gridLayout_5.addWidget(self.smallestSizeExample, 0, 4, 1, 1)

        self.fontSize = QSlider(self.fontSizeWidget)
        self.fontSize.setObjectName(u"fontSize")
        self.fontSize.setMinimumSize(QSize(500, 0))
        self.fontSize.setMaximumSize(QSize(500, 16777215))
        self.fontSize.setMinimum(50)
        self.fontSize.setMaximum(200)
        self.fontSize.setSingleStep(25)
        self.fontSize.setValue(100)
        self.fontSize.setOrientation(Qt.Orientation.Horizontal)
        self.fontSize.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.fontSize.setTickInterval(25)

        self.gridLayout_5.addWidget(self.fontSize, 1, 4, 1, 5)

        self.largestSizeExample = QLabel(self.fontSizeWidget)
        self.largestSizeExample.setObjectName(u"largestSizeExample")

        self.gridLayout_5.addWidget(self.largestSizeExample, 0, 8, 1, 1)

        self.horizontalSpacer_40 = QSpacerItem(130, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_40, 0, 5, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(290, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_39, 0, 7, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_41, 1, 3, 1, 1)


        self.verticalLayout_23.addWidget(self.fontSizeWidget)


        self.verticalLayout_19.addWidget(self.textStyleWidget)

        self.verticalSpacer_12 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_12)

        self.generalScroll.setWidget(self.generalScrollWidget)

        self.horizontalLayout_29.addWidget(self.generalScroll)

        self.settingStack.addWidget(self.generalSettingPage)
        self.paintSettingPage = QWidget()
        self.paintSettingPage.setObjectName(u"paintSettingPage")
        self.verticalLayout_24 = QVBoxLayout(self.paintSettingPage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.paintSettingScroll = QScrollArea(self.paintSettingPage)
        self.paintSettingScroll.setObjectName(u"paintSettingScroll")
        self.paintSettingScroll.setWidgetResizable(True)
        self.paintSettingWidget = QWidget()
        self.paintSettingWidget.setObjectName(u"paintSettingWidget")
        self.paintSettingWidget.setGeometry(QRect(0, 0, 499, 565))
        self.verticalLayout_25 = QVBoxLayout(self.paintSettingWidget)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 15, -1, 15)
        self.paintSettingTipMsgWidget = QWidget(self.paintSettingWidget)
        self.paintSettingTipMsgWidget.setObjectName(u"paintSettingTipMsgWidget")
        self.horizontalLayout_37 = QHBoxLayout(self.paintSettingTipMsgWidget)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(15, 5, 15, 5)
        self.paintSettingTipMsg = QLabel(self.paintSettingTipMsgWidget)
        self.paintSettingTipMsg.setObjectName(u"paintSettingTipMsg")

        self.horizontalLayout_37.addWidget(self.paintSettingTipMsg)


        self.verticalLayout_25.addWidget(self.paintSettingTipMsgWidget)

        self.verticalSpacer_18 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_18)

        self.comfyuiSettingTitle = QLabel(self.paintSettingWidget)
        self.comfyuiSettingTitle.setObjectName(u"comfyuiSettingTitle")
        sizePolicy4.setHeightForWidth(self.comfyuiSettingTitle.sizePolicy().hasHeightForWidth())
        self.comfyuiSettingTitle.setSizePolicy(sizePolicy4)
        self.comfyuiSettingTitle.setIndent(16)

        self.verticalLayout_25.addWidget(self.comfyuiSettingTitle)

        self.comfyuiSettingWidget = QWidget(self.paintSettingWidget)
        self.comfyuiSettingWidget.setObjectName(u"comfyuiSettingWidget")
        self.gridLayout_6 = QGridLayout(self.comfyuiSettingWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(10)
        self.gridLayout_6.setContentsMargins(15, 15, 15, 15)
        self.divider24 = QWidget(self.comfyuiSettingWidget)
        self.divider24.setObjectName(u"divider24")
        self.divider24.setMinimumSize(QSize(0, 1))
        self.divider24.setMaximumSize(QSize(16777215, 1))

        self.gridLayout_6.addWidget(self.divider24, 5, 0, 1, 3)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_42, 0, 1, 1, 1)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_44, 4, 1, 1, 1)

        self.divider23 = QWidget(self.comfyuiSettingWidget)
        self.divider23.setObjectName(u"divider23")
        self.divider23.setMinimumSize(QSize(0, 1))
        self.divider23.setMaximumSize(QSize(0, 1))

        self.gridLayout_6.addWidget(self.divider23, 3, 0, 1, 3)

        self.pushButton = QPushButton(self.comfyuiSettingWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.pushButton, 6, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.comfyuiSettingWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_6.addWidget(self.pushButton_2, 6, 3, 1, 1)

        self.updateComfyui = QPushButton(self.comfyuiSettingWidget)
        self.updateComfyui.setObjectName(u"updateComfyui")
        sizePolicy2.setHeightForWidth(self.updateComfyui.sizePolicy().hasHeightForWidth())
        self.updateComfyui.setSizePolicy(sizePolicy2)
        self.updateComfyui.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_6.addWidget(self.updateComfyui, 4, 2, 1, 2)

        self.getModelLabel = QLabel(self.comfyuiSettingWidget)
        self.getModelLabel.setObjectName(u"getModelLabel")

        self.gridLayout_6.addWidget(self.getModelLabel, 6, 0, 1, 1)

        self.installComfyuiLabel = QLabel(self.comfyuiSettingWidget)
        self.installComfyuiLabel.setObjectName(u"installComfyuiLabel")
        sizePolicy.setHeightForWidth(self.installComfyuiLabel.sizePolicy().hasHeightForWidth())
        self.installComfyuiLabel.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.installComfyuiLabel, 0, 0, 1, 1)

        self.divider22 = QWidget(self.comfyuiSettingWidget)
        self.divider22.setObjectName(u"divider22")
        sizePolicy3.setHeightForWidth(self.divider22.sizePolicy().hasHeightForWidth())
        self.divider22.setSizePolicy(sizePolicy3)
        self.divider22.setMinimumSize(QSize(0, 1))
        self.divider22.setMaximumSize(QSize(16777215, 1))

        self.gridLayout_6.addWidget(self.divider22, 1, 0, 1, 3)

        self.updateComfyuiLabel = QLabel(self.comfyuiSettingWidget)
        self.updateComfyuiLabel.setObjectName(u"updateComfyuiLabel")
        sizePolicy.setHeightForWidth(self.updateComfyuiLabel.sizePolicy().hasHeightForWidth())
        self.updateComfyuiLabel.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.updateComfyuiLabel, 4, 0, 1, 1)

        self.installComfyui = QPushButton(self.comfyuiSettingWidget)
        self.installComfyui.setObjectName(u"installComfyui")
        sizePolicy2.setHeightForWidth(self.installComfyui.sizePolicy().hasHeightForWidth())
        self.installComfyui.setSizePolicy(sizePolicy2)
        self.installComfyui.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_6.addWidget(self.installComfyui, 0, 2, 1, 2)

        self.chooseComfyuiPathWidget = QWidget(self.comfyuiSettingWidget)
        self.chooseComfyuiPathWidget.setObjectName(u"chooseComfyuiPathWidget")
        sizePolicy3.setHeightForWidth(self.chooseComfyuiPathWidget.sizePolicy().hasHeightForWidth())
        self.chooseComfyuiPathWidget.setSizePolicy(sizePolicy3)
        self.chooseComfyuiPathWidget.setMinimumSize(QSize(0, 20))
        self.gridLayout_7 = QGridLayout(self.chooseComfyuiPathWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.chooseComfyuiPathLabel = QLabel(self.chooseComfyuiPathWidget)
        self.chooseComfyuiPathLabel.setObjectName(u"chooseComfyuiPathLabel")
        sizePolicy.setHeightForWidth(self.chooseComfyuiPathLabel.sizePolicy().hasHeightForWidth())
        self.chooseComfyuiPathLabel.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.chooseComfyuiPathLabel, 0, 0, 1, 1)

        self.showComfyuiPathLabel = QLabel(self.chooseComfyuiPathWidget)
        self.showComfyuiPathLabel.setObjectName(u"showComfyuiPathLabel")

        self.gridLayout_7.addWidget(self.showComfyuiPathLabel, 1, 0, 1, 2)

        self.chooseComfyuiPath = QPushButton(self.chooseComfyuiPathWidget)
        self.chooseComfyuiPath.setObjectName(u"chooseComfyuiPath")
        sizePolicy2.setHeightForWidth(self.chooseComfyuiPath.sizePolicy().hasHeightForWidth())
        self.chooseComfyuiPath.setSizePolicy(sizePolicy2)
        self.chooseComfyuiPath.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_7.addWidget(self.chooseComfyuiPath, 0, 2, 2, 1)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_43, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.chooseComfyuiPathWidget, 2, 0, 1, 4)


        self.verticalLayout_25.addWidget(self.comfyuiSettingWidget)

        self.verticalSpacer_17 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_17)

        self.paintManageTitle = QLabel(self.paintSettingWidget)
        self.paintManageTitle.setObjectName(u"paintManageTitle")
        self.paintManageTitle.setIndent(16)

        self.verticalLayout_25.addWidget(self.paintManageTitle)

        self.paintManageWidget = QWidget(self.paintSettingWidget)
        self.paintManageWidget.setObjectName(u"paintManageWidget")
        self.gridLayout_8 = QGridLayout(self.paintManageWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(10)
        self.gridLayout_8.setContentsMargins(15, 15, 15, 15)
        self.enablePaint = SwitchButton(self.paintManageWidget)
        self.enablePaint.setObjectName(u"enablePaint")
        self.enablePaint.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_8.addWidget(self.enablePaint, 1, 2, 1, 1)

        self.showImageSavePathLabel = QLabel(self.paintManageWidget)
        self.showImageSavePathLabel.setObjectName(u"showImageSavePathLabel")

        self.gridLayout_8.addWidget(self.showImageSavePathLabel, 5, 0, 1, 2)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_47, 1, 1, 1, 1)

        self.chooseImageSavePath = QPushButton(self.paintManageWidget)
        self.chooseImageSavePath.setObjectName(u"chooseImageSavePath")
        sizePolicy2.setHeightForWidth(self.chooseImageSavePath.sizePolicy().hasHeightForWidth())
        self.chooseImageSavePath.setSizePolicy(sizePolicy2)
        self.chooseImageSavePath.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_8.addWidget(self.chooseImageSavePath, 5, 2, 1, 1)

        self.divider25 = QWidget(self.paintManageWidget)
        self.divider25.setObjectName(u"divider25")
        self.divider25.setMinimumSize(QSize(0, 1))
        self.divider25.setMaximumSize(QSize(16777215, 1))

        self.gridLayout_8.addWidget(self.divider25, 3, 0, 1, 3)

        self.defaultImageSavePath = SwitchButton(self.paintManageWidget)
        self.defaultImageSavePath.setObjectName(u"defaultImageSavePath")
        self.defaultImageSavePath.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.defaultImageSavePath.setChecked(True)

        self.gridLayout_8.addWidget(self.defaultImageSavePath, 4, 2, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_46, 4, 1, 1, 1)

        self.imageSavePathLabel = QLabel(self.paintManageWidget)
        self.imageSavePathLabel.setObjectName(u"imageSavePathLabel")
        sizePolicy.setHeightForWidth(self.imageSavePathLabel.sizePolicy().hasHeightForWidth())
        self.imageSavePathLabel.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.imageSavePathLabel, 4, 0, 1, 1)

        self.enablePaintLabel = QLabel(self.paintManageWidget)
        self.enablePaintLabel.setObjectName(u"enablePaintLabel")

        self.gridLayout_8.addWidget(self.enablePaintLabel, 1, 0, 1, 1)


        self.verticalLayout_25.addWidget(self.paintManageWidget)

        self.verticalSpacer_13 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_13)

        self.paintSettingScroll.setWidget(self.paintSettingWidget)

        self.verticalLayout_24.addWidget(self.paintSettingScroll)

        self.settingStack.addWidget(self.paintSettingPage)
        self.voiceSettingPage = QWidget()
        self.voiceSettingPage.setObjectName(u"voiceSettingPage")
        self.verticalLayout_26 = QVBoxLayout(self.voiceSettingPage)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 15, -1, 15)
        self.label = QLabel(self.voiceSettingPage)
        self.label.setObjectName(u"label")

        self.verticalLayout_26.addWidget(self.label)

        self.settingStack.addWidget(self.voiceSettingPage)
        self.confirmSettingPage = QWidget()
        self.confirmSettingPage.setObjectName(u"confirmSettingPage")
        self.settingStack.addWidget(self.confirmSettingPage)
        self.searchSettingPage = QWidget()
        self.searchSettingPage.setObjectName(u"searchSettingPage")
        self.settingStack.addWidget(self.searchSettingPage)

        self.verticalLayout_13.addWidget(self.settingStack)


        self.horizontalLayout_15.addWidget(self.settingWidget)


        self.verticalLayout_11.addWidget(self.settingContent)

        self.defaultSettingWidget = QWidget(self.page3)
        self.defaultSettingWidget.setObjectName(u"defaultSettingWidget")
        self.defaultSettingWidget.setMinimumSize(QSize(0, 40))
        self.defaultSettingWidget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_14 = QHBoxLayout(self.defaultSettingWidget)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 20, 0)
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_18)

        self.defaultSettingBtn = QPushButton(self.defaultSettingWidget)
        self.defaultSettingBtn.setObjectName(u"defaultSettingBtn")
        sizePolicy2.setHeightForWidth(self.defaultSettingBtn.sizePolicy().hasHeightForWidth())
        self.defaultSettingBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.defaultSettingBtn)


        self.verticalLayout_11.addWidget(self.defaultSettingWidget)

        self.stack.addWidget(self.page3)
        self.memoryWidget = QWidget(self.mainContainer)
        self.memoryWidget.setObjectName(u"memoryWidget")
        self.memoryWidget.setGeometry(QRect(-140, 130, 250, 511))
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.memoryWidget.sizePolicy().hasHeightForWidth())
        self.memoryWidget.setSizePolicy(sizePolicy9)
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
        sizePolicy.setHeightForWidth(self.memoryLabel.sizePolicy().hasHeightForWidth())
        self.memoryLabel.setSizePolicy(sizePolicy)

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
        self.memoryMoreMenu.setGeometry(QRect(110, 280, 41, 51))
        sizePolicy2.setHeightForWidth(self.memoryMoreMenu.sizePolicy().hasHeightForWidth())
        self.memoryMoreMenu.setSizePolicy(sizePolicy2)
        self.verticalLayout_9 = QVBoxLayout(self.memoryMoreMenu)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.manageBtn = QPushButton(self.memoryMoreMenu)
        self.manageBtn.setObjectName(u"manageBtn")
        sizePolicy8.setHeightForWidth(self.manageBtn.sizePolicy().hasHeightForWidth())
        self.manageBtn.setSizePolicy(sizePolicy8)

        self.verticalLayout_9.addWidget(self.manageBtn)

        self.clearBtn = QPushButton(self.memoryMoreMenu)
        self.clearBtn.setObjectName(u"clearBtn")
        sizePolicy8.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy8)

        self.verticalLayout_9.addWidget(self.clearBtn)

        self.titleBar.raise_()
        self.moreMenu.raise_()
        self.avatarMenu.raise_()
        self.memoryWidget.raise_()
        self.memoryMoreMenu.raise_()
        self.statusBar.raise_()
        self.stack.raise_()

        self.verticalLayout_3.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stack.setCurrentIndex(2)
        self.settingStack.setCurrentIndex(1)


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
        self.statusDotBottom.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.statusLabelBottom.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u95f2\u4e2d", None))
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
        self.fileBtn.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5e93", None))
        self.logBtn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u65e5\u5fd7", None))
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
        self.promptClose.setText(QCoreApplication.translate("MainWindow", u"...", None))
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
        self.closeSettingBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.connSettingBtn.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.generalSettingBtn.setText(QCoreApplication.translate("MainWindow", u"\u5e38\u89c4", None))
        self.paintSettingBtn.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u753b", None))
        self.voiceSettingBtn.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u97f3", None))
        self.confirmSettingBtn.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u786e\u8ba4", None))
        self.searchSettingBtn.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7f51\u641c\u7d22", None))
        self.settingTitle.setText("")
        self.APIKeyTitle.setText(QCoreApplication.translate("MainWindow", u"API Key <span style=\"color: red;\">*</span>", None))
        self.removeAPIKeyBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.addAPIKeyBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.APISettingTitle.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u53c2\u6570", None))
        self.baseUrlLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Base URL <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.modelSettingLabel.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u540d\u79f0 <span style=\"color: red\";>*</span>", None))
        self.modelCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5728API Key\u4e0eBase URL\u586b\u5199\u5b8c\u6bd5\u540e\u70b9\u51fb\u53f3\u4fa7\u6309\u94ae", None))

        self.listModel.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6a21\u578b\u5217\u8868", None))
        self.enableToolLabel.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\u5de5\u5177\u8c03\u7528", None))
        self.enableTool.setText("")
        self.reasoningEffortLabel.setText(QCoreApplication.translate("MainWindow", u"\u601d\u8003\u5f3a\u5ea6", None))
        self.reasoningEffort.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0(\u672a\u9a8c\u8bc1)", None))
        self.reasoningEffort.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6700\u4f4e(\u672a\u9a8c\u8bc1)", None))
        self.reasoningEffort.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4f4e(\u672a\u9a8c\u8bc1)", None))
        self.reasoningEffort.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e2d(\u672a\u9a8c\u8bc1)", None))
        self.reasoningEffort.setItemText(4, QCoreApplication.translate("MainWindow", u"\u9ad8(\u672a\u9a8c\u8bc1)", None))
        self.reasoningEffort.setItemText(5, QCoreApplication.translate("MainWindow", u"\u6781\u9ad8(\u672a\u9a8c\u8bc1)", None))
        self.reasoningEffort.setItemText(6, QCoreApplication.translate("MainWindow", u"\u6700\u9ad8(\u672a\u9a8c\u8bc1)", None))

        self.defaultReasoningEffort.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u9ed8\u8ba4\u601d\u8003\u5f3a\u5ea6(\u62a5\u9519\u65f6\u8bf7\u9009\u62e9)", None))
        self.extraBodyLabel.setText(QCoreApplication.translate("MainWindow", u"\u989d\u5916\u53c2\u6570(extra_body)", None))
        self.proxyLabel.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406", None))
        self.enableProxyLabel.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\u7f51\u7edc\u4ee3\u7406", None))
        self.enableProxy.setText("")
        self.sysProxyLabel.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u7cfb\u7edf\u4ee3\u7406", None))
        self.sysProxy.setText("")
        self.manualProxyLabel.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u914d\u7f6e\u4ee3\u7406", None))
        self.proxyAddressLabel.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u5730\u5740", None))
        self.proxyPortLabel.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u7aef\u53e3", None))
        self.proxyTypeLabel.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u7c7b\u578b", None))
        self.proxyType.setItemText(0, QCoreApplication.translate("MainWindow", u"HTTP", None))
        self.proxyType.setItemText(1, QCoreApplication.translate("MainWindow", u"HTTPS", None))
        self.proxyType.setItemText(2, QCoreApplication.translate("MainWindow", u"FTP", None))
        self.proxyType.setItemText(3, QCoreApplication.translate("MainWindow", u"SOCKS", None))

        self.locationSeetingLabel.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None))
        self.enableLocationLabel.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\u5730\u7406\u4f4d\u7f6e\u4fe1\u606f", None))
        self.enableLocation.setText("")
        self.locationLabel.setText(QCoreApplication.translate("MainWindow", u"\u5730\u7406\u4f4d\u7f6e", None))
        self.showLocationInfo.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e\uff1a", None))
        self.autoGetLocation.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u83b7\u53d6\u5730\u7406\u4f4d\u7f6e", None))
        self.uiSettingTitle.setText(QCoreApplication.translate("MainWindow", u"\u754c\u9762", None))
        self.followSysTheme.setText(QCoreApplication.translate("MainWindow", u"\u8ddf\u968f\u7cfb\u7edf", None))
        self.themeLabel.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e3b\u9898", None))
        self.theme.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6d45\u8272\u6a21\u5f0f", None))
        self.theme.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6df1\u8272\u6a21\u5f0f", None))

        self.setBackgroundLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u5bf9\u8bdd\u533a\u80cc\u666f", None))
        self.setBackground.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247...", None))
        self.statusBarComponentTitle.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u90e8\u72b6\u6001\u680f\u7ec4\u4ef6", None))
        self.roundTokensComponent.setText("")
        self.roundTokensComponentLabel.setText(QCoreApplication.translate("MainWindow", u"\u672c\u8f6eTokens", None))
        self.totalTokensComponent.setText("")
        self.totalTokensComponentLabel.setText(QCoreApplication.translate("MainWindow", u"\u603b\u8ba1Tokens", None))
        self.weatherComponentlabel.setText(QCoreApplication.translate("MainWindow", u"\u5929\u6c14", None))
        self.weatherComponent.setText("")
        self.chatSettingTitle.setText(QCoreApplication.translate("MainWindow", u"\u804a\u5929", None))
        self.sendSettingLabel.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6d88\u606f", None))
        self.sendSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Shift + Enter", None))
        self.sendSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Enter", None))

        self.renderSettingLabel.setText(QCoreApplication.translate("MainWindow", u"\u6e32\u67d3\u7528\u6237\u6d88\u606f", None))
        self.renderSetting.setText("")
        self.msgWithLocationLabel.setText(QCoreApplication.translate("MainWindow", u"\u6d88\u606f\u9644\u5e26\u5730\u7406\u4f4d\u7f6e\u4fe1\u606f", None))
        self.megWithLocation.setText("")
        self.textStyleTitle.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u4f53\u5b57\u53f7", None))
        self.fontLabel.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u4f53\u9009\u62e9", None))
        self.font.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u9ed8\u8ba4\u5b57\u4f53", None))
        self.font.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u7cfb\u7edf\u5b57\u4f53", None))

        self.fontSizeLabel.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u53f7\u5927\u5c0f", None))
        self.standardSizeExample.setText(QCoreApplication.translate("MainWindow", u"\u6807\u51c6", None))
        self.smallestSizeExample.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.largestSizeExample.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.paintSettingTipMsg.setText(QCoreApplication.translate("MainWindow", u"\u975e\u591a\u6a21\u6001\u6a21\u578b\u5728\u7ed8\u5236\u5b8c\u6210\u540e\u65e0\u6cd5\u770b\u5230\u7ed8\u5236\u540e\u7684\u56fe\u7247", None))
        self.comfyuiSettingTitle.setText(QCoreApplication.translate("MainWindow", u"ComfyUI", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6a21\u578b...", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4ece CivitAI \u83b7\u53d6\u6a21\u578b", None))
        self.updateComfyui.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.getModelLabel.setText(QCoreApplication.translate("MainWindow", u"\u5411\u6a21\u578b\u5b58\u50a8\u8def\u5f84\u4e2d\u6dfb\u52a0\u6a21\u578b", None))
        self.installComfyuiLabel.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u88c5ComfyUI", None))
        self.updateComfyuiLabel.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5ComfyUI\u66f4\u65b0", None))
        self.installComfyui.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84\u4ee5\u5b89\u88c5", None))
        self.chooseComfyuiPathLabel.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9ComfyUI\u8def\u5f84(main.py)", None))
        self.showComfyuiPathLabel.setText("")
        self.chooseComfyuiPath.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84...", None))
        self.paintManageTitle.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u753b\u7ba1\u7406", None))
        self.enablePaint.setText("")
        self.showImageSavePathLabel.setText("")
        self.chooseImageSavePath.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84...", None))
        self.defaultImageSavePath.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u9ed8\u8ba4\u8def\u5f84", None))
        self.imageSavePathLabel.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247\u4fdd\u5b58\u8def\u5f84", None))
        self.enablePaintLabel.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\u7ed8\u753b\u529f\u80fd", None))
        self.label.setText("")
        self.defaultSettingBtn.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u9ed8\u8ba4\u8bbe\u7f6e", None))
        self.memoryLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5fc6", None))
        self.delMemoryBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.memoryMoreBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.noMemoryLabel.setText(QCoreApplication.translate("MainWindow", u"\u5c1a\u672a\u6307\u5b9a\u4efb\u4f55\u8bb0\u5fc6\u3002", None))
        self.manageBtn.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
    # retranslateUi

