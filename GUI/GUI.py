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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)

from widgets import AvatarButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(985, 802)
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
        icon.addFile(u"../../../../../../../../../../../../\u4e0b\u8f7d/Mio.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
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

        self.callBtn = QToolButton(self.titleBar)
        self.callBtn.setObjectName(u"callBtn")

        self.horizontalLayout.addWidget(self.callBtn)

        self.voiceBtn = QToolButton(self.titleBar)
        self.voiceBtn.setObjectName(u"voiceBtn")

        self.horizontalLayout.addWidget(self.voiceBtn)

        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.dividerD = QWidget(self.titleBar)
        self.dividerD.setObjectName(u"dividerD")
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
        self.divider.raise_()
        self.minBtn.raise_()
        self.maxBtn.raise_()
        self.closeBtn.raise_()
        self.avatarBtn.raise_()
        self.callBtn.raise_()
        self.voiceBtn.raise_()
        self.dividerD.raise_()
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

        self.chatScroll = QScrollArea(self.mainContainer)
        self.chatScroll.setObjectName(u"chatScroll")
        self.chatScroll.setGeometry(QRect(0, 70, 941, 551))
        self.chatScroll.setMaximumSize(QSize(16777215, 16777215))
        self.chatScroll.setWidgetResizable(True)
        self.chatWidget = QWidget()
        self.chatWidget.setObjectName(u"chatWidget")
        self.chatWidget.setGeometry(QRect(0, 0, 939, 549))
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
        self.inputRow = QWidget(self.mainContainer)
        self.inputRow.setObjectName(u"inputRow")
        self.inputRow.setGeometry(QRect(940, 20, 919, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputRow.sizePolicy().hasHeightForWidth())
        self.inputRow.setSizePolicy(sizePolicy1)
        self.inputRow.setMinimumSize(QSize(0, 50))
        self.inputRow.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.inputRow)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(50, 0, 50, 0)
        self.inputArea = QWidget(self.inputRow)
        self.inputArea.setObjectName(u"inputArea")
        sizePolicy1.setHeightForWidth(self.inputArea.sizePolicy().hasHeightForWidth())
        self.inputArea.setSizePolicy(sizePolicy1)
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

        self.sendBtn = QPushButton(self.inputArea)
        self.sendBtn.setObjectName(u"sendBtn")

        self.horizontalLayout_3.addWidget(self.sendBtn)


        self.horizontalLayout_5.addWidget(self.inputArea)

        self.fadeMask = QWidget(self.mainContainer)
        self.fadeMask.setObjectName(u"fadeMask")
        self.fadeMask.setGeometry(QRect(540, 650, 120, 82))
        sizePolicy1.setHeightForWidth(self.fadeMask.sizePolicy().hasHeightForWidth())
        self.fadeMask.setSizePolicy(sizePolicy1)
        self.fadeMask.setMinimumSize(QSize(0, 82))
        self.fadeMask.setMaximumSize(QSize(16777215, 82))
        self.avatarMenu = QWidget(self.mainContainer)
        self.avatarMenu.setObjectName(u"avatarMenu")
        self.avatarMenu.setGeometry(QRect(370, 709, 121, 91))
        self.verticalLayout = QVBoxLayout(self.avatarMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chooseAvatarBtn = QPushButton(self.avatarMenu)
        self.chooseAvatarBtn.setObjectName(u"chooseAvatarBtn")

        self.verticalLayout.addWidget(self.chooseAvatarBtn)

        self.editPersonaBtn = QPushButton(self.avatarMenu)
        self.editPersonaBtn.setObjectName(u"editPersonaBtn")

        self.verticalLayout.addWidget(self.editPersonaBtn)

        self.memoryBtn = QPushButton(self.avatarMenu)
        self.memoryBtn.setObjectName(u"memoryBtn")

        self.verticalLayout.addWidget(self.memoryBtn)

        self.moreMenu = QWidget(self.mainContainer)
        self.moreMenu.setObjectName(u"moreMenu")
        self.moreMenu.setGeometry(QRect(800, 569, 121, 181))
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

        self.titleBar.raise_()
        self.statusBar.raise_()
        self.chatScroll.raise_()
        self.fadeMask.raise_()
        self.inputRow.raise_()
        self.avatarMenu.raise_()
        self.moreMenu.raise_()

        self.verticalLayout_3.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.avatarBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"\u6faa", None))
        self.statusDot.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u95f2\u4e2d", None))
        self.callBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.voiceBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
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
        self.attachBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.imageBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.sendBtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.chooseAvatarBtn.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6362\u5f62\u8c61", None))
        self.editPersonaBtn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u8bbe\u5b9a", None))
        self.memoryBtn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u8bb0\u5fc6", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.update.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.ComfyUI.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8ComfyUI", None))
        self.feedback.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u9988", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.reset.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
    # retranslateUi

