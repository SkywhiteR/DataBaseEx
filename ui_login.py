# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class login_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"username")
        self.lineEdit.setGeometry(QRect(140, 99, 141, 21))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"password")
        self.lineEdit_2.setGeometry(QRect(140, 150, 141, 20))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 190, 75, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 90, 61, 41))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(11)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 150, 41, 20))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 30, 54, 51))
        self.label_3.setPixmap(QPixmap(u"login_up.png"))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 30, 211, 51))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(22)
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-260, -10, 741, 331))
        self.label_5.setPixmap(QPixmap(u"login_back.jpg"))
        self.label_5.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u767b\u5f55\u754c\u9762", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\uff1a", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6821\u533b\u9662\u7ba1\u7406\u7cfb\u7edf", None))
        self.label_5.setText("")
    # retranslateUi

