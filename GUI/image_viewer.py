# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1300, 1300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(1300, 1300))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainContainer = QWidget(Dialog)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.mainContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QWidget(self.mainContainer)
        self.titleBar.setObjectName(u"titleBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleBar.sizePolicy().hasHeightForWidth())
        self.titleBar.setSizePolicy(sizePolicy2)
        self.titleBar.setMinimumSize(QSize(0, 40))
        self.titleBar.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 3, -1, 3)
        self.horizontalSpacer = QSpacerItem(1225, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.minBtn = QToolButton(self.titleBar)
        self.minBtn.setObjectName(u"minBtn")

        self.horizontalLayout.addWidget(self.minBtn)

        self.maxBtn = QToolButton(self.titleBar)
        self.maxBtn.setObjectName(u"maxBtn")

        self.horizontalLayout.addWidget(self.maxBtn)

        self.closeBtn = QToolButton(self.titleBar)
        self.closeBtn.setObjectName(u"closeBtn")

        self.horizontalLayout.addWidget(self.closeBtn)


        self.verticalLayout_2.addWidget(self.titleBar)

        self.image = QLabel(self.mainContainer)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(1254, 1254))
        self.image.setMaximumSize(QSize(16777215, 16777215))
        self.image.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_2.addWidget(self.image)


        self.verticalLayout.addWidget(self.mainContainer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.minBtn.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.maxBtn.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.closeBtn.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.image.setText("")
    # retranslateUi

