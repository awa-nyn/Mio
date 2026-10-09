# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_window.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(0, 0))
        Dialog.setMaximumSize(QSize(800, 600))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.messageWidget = QWidget(Dialog)
        self.messageWidget.setObjectName(u"messageWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.messageWidget.sizePolicy().hasHeightForWidth())
        self.messageWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.messageWidget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 15, 25, 15)
        self.titleWidget = QWidget(self.messageWidget)
        self.titleWidget.setObjectName(u"titleWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleWidget.sizePolicy().hasHeightForWidth())
        self.titleWidget.setSizePolicy(sizePolicy2)
        self.titleWidget.setMinimumSize(QSize(50, 35))
        self.titleWidget.setMaximumSize(QSize(16777215, 35))
        self.titleWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.titleWidget)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.title = QLabel(self.titleWidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.titleWidget)

        self.message = QLabel(self.messageWidget)
        self.message.setObjectName(u"message")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy3)
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.message)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnWidget = QWidget(self.messageWidget)
        self.btnWidget.setObjectName(u"btnWidget")
        sizePolicy2.setHeightForWidth(self.btnWidget.sizePolicy().hasHeightForWidth())
        self.btnWidget.setSizePolicy(sizePolicy2)
        self.btnWidget.setMinimumSize(QSize(0, 40))
        self.btnWidget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.btnWidget)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnLeft = QPushButton(self.btnWidget)
        self.btnLeft.setObjectName(u"btnLeft")
        sizePolicy.setHeightForWidth(self.btnLeft.sizePolicy().hasHeightForWidth())
        self.btnLeft.setSizePolicy(sizePolicy)
        self.btnLeft.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_3.addWidget(self.btnLeft)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btnMiddle = QPushButton(self.btnWidget)
        self.btnMiddle.setObjectName(u"btnMiddle")
        sizePolicy.setHeightForWidth(self.btnMiddle.sizePolicy().hasHeightForWidth())
        self.btnMiddle.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.btnMiddle)

        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.btnRight = QPushButton(self.btnWidget)
        self.btnRight.setObjectName(u"btnRight")
        sizePolicy.setHeightForWidth(self.btnRight.sizePolicy().hasHeightForWidth())
        self.btnRight.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.btnRight)


        self.verticalLayout.addWidget(self.btnWidget)


        self.horizontalLayout.addWidget(self.messageWidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Title", None))
        self.message.setText(QCoreApplication.translate("Dialog", u"Message", None))
        self.btnLeft.setText(QCoreApplication.translate("Dialog", u"Btn1", None))
        self.btnMiddle.setText(QCoreApplication.translate("Dialog", u"Btn2", None))
        self.btnRight.setText(QCoreApplication.translate("Dialog", u"Btn3", None))
    # retranslateUi

