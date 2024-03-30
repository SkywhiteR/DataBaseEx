# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_reg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
from PySide6.QtGui import QIntValidator
import background_image

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(276, 252)
        Form.setStyleSheet(u"background-image: url(:/back.jpg);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LineEdit_5 = QLineEdit(Form)
        self.LineEdit_5.setObjectName(u"LineEdit_5")

        self.gridLayout.addWidget(self.LineEdit_5, 5, 1, 1, 1)

        self.Label_6 = QLabel(Form)
        self.Label_6.setObjectName(u"Label_6")

        self.gridLayout.addWidget(self.Label_6, 7, 0, 1, 1, Qt.AlignLeft)

        self.ComboBox = QComboBox(Form)
        self.ComboBox.setObjectName(u"ComboBox")

        self.gridLayout.addWidget(self.ComboBox, 6, 1, 1, 1)

        self.LineEdit_4 = QLineEdit(Form)
        self.LineEdit_4.setObjectName(u"LineEdit_4")

        self.gridLayout.addWidget(self.LineEdit_4, 4, 1, 1, 1)

        self.Label = QLabel(Form)
        self.Label.setObjectName(u"Label")

        self.gridLayout.addWidget(self.Label, 3, 0, 1, 1, Qt.AlignLeft)

        self.Label_1 = QLabel(Form)
        self.Label_1.setObjectName(u"1")

        self.gridLayout.addWidget(self.Label_1, 1, 0, 1, 1, Qt.AlignLeft)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.Label_3 = QLabel(Form)
        self.Label_3.setObjectName(u"Label_3")

        self.gridLayout.addWidget(self.Label_3, 4, 0, 1, 1, Qt.AlignLeft)

        self.Label_2 = QLabel(Form)
        self.Label_2.setObjectName(u"Label_2")

        self.gridLayout.addWidget(self.Label_2, 2, 0, 1, 1)

        self.ComboBox_2 = QComboBox(Form)
        self.ComboBox_2.setObjectName(u"ComboBox_2")

        self.gridLayout.addWidget(self.ComboBox_2, 7, 1, 1, 1)

        self.Label_4 = QLabel(Form)
        self.Label_4.setObjectName(u"Label_4")

        self.gridLayout.addWidget(self.Label_4, 5, 0, 1, 1, Qt.AlignLeft)

        self.Label_5 = QLabel(Form)
        self.Label_5.setObjectName(u"Label_5")

        self.gridLayout.addWidget(self.Label_5, 6, 0, 1, 1, Qt.AlignLeft)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)

        self.LineEdit_3 = QLineEdit(Form)
        self.LineEdit_3.setObjectName(u"LineEdit_3")
        self.LineEdit_3.setInputMethodHints(Qt.ImhDigitsOnly | Qt.ImhPreferNumbers)
        self.LineEdit_3.setValidator(QIntValidator())

        self.gridLayout.addWidget(self.LineEdit_3, 2, 1, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6302\u53f7", None))
        self.Label_6.setText(QCoreApplication.translate("Form", u"\u533b\u751f\u9009\u62e9", None))
        self.Label.setText(QCoreApplication.translate("Form", u"\u6027\u522b", None))
        self.Label_1.setText(QCoreApplication.translate("Form", u"\u59d3\u540d", None))
        self.Label_3.setText(QCoreApplication.translate("Form", u"\u8054\u7cfb\u7535\u8bdd", None))
        self.Label_2.setText(QCoreApplication.translate("Form", u"\u5e74\u9f84", None))
        self.Label_4.setText(QCoreApplication.translate("Form", u"\u4f4f\u5740", None))
        self.Label_5.setText(QCoreApplication.translate("Form", u"\u5019\u8bca\u79d1\u5ba4", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6302\u53f7\u7cfb\u7edf", None))
    # retranslateUi

