# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setDrugStock.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from PySide6.QtGui import QDoubleValidator, QIntValidator
import background_image

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-image: url(:/back.jpg);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignLeft)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.NowStock = QLineEdit(Dialog)
        self.NowStock.setObjectName(u"NowStock")
        self.NowStock.setValidator(QIntValidator())

        self.verticalLayout.addWidget(self.NowStock)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.minStock = QLineEdit(Dialog)
        self.minStock.setObjectName(u"minStock")
        self.minStock.setValidator(QIntValidator())

        self.verticalLayout.addWidget(self.minStock)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignLeft)

        self.maxStock = QLineEdit(Dialog)
        self.maxStock.setObjectName(u"maxStock")
        self.maxStock.setValidator(QIntValidator())

        self.verticalLayout.addWidget(self.maxStock)

        self.comfirmButton = QPushButton(Dialog)
        self.comfirmButton.setObjectName(u"comfirmButton")

        self.verticalLayout.addWidget(self.comfirmButton, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6539\u53d8\u836f\u54c1\u5e93\u5b58", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u540d\u79f0\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u73b0\u6709\u5e93\u5b58\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6700\u5c0f\u5e93\u5b58\u9608\u503c\u8bbe\u7f6e\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6700\u5927\u5e93\u5b58\u9608\u503c\u8bbe\u7f6e\uff1a", None))
        self.comfirmButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a\u4fee\u6539", None))
    # retranslateUi

