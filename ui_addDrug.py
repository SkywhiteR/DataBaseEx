# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addDrug.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from PySide6.QtGui import QIntValidator, QDoubleValidator
import background_image

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(287, 357)
        Dialog.setStyleSheet(u"background-image: url(:/back.jpg);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.nameLine = QLineEdit(Dialog)
        self.nameLine.setObjectName(u"nameLine")

        self.verticalLayout.addWidget(self.nameLine)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.InPrice = QLineEdit(Dialog)
        self.InPrice.setObjectName(u"InPrice")
        self.InPrice.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.InPrice.setValidator(QDoubleValidator())

        self.verticalLayout.addWidget(self.InPrice)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.OutPrice = QLineEdit(Dialog)
        self.OutPrice.setObjectName(u"OutPrice")
        self.OutPrice.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.OutPrice.setValidator(QDoubleValidator())

        self.verticalLayout.addWidget(self.OutPrice)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.InStock = QLineEdit(Dialog)
        self.InStock.setObjectName(u"InStock")
        self.InStock.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.InStock.setValidator(QIntValidator())

        self.verticalLayout.addWidget(self.InStock)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.minStock = QLineEdit(Dialog)
        self.minStock.setObjectName(u"minStock")
        self.minStock.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.minStock.setValidator(QIntValidator())

        self.verticalLayout.addWidget(self.minStock)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.maxStock = QLineEdit(Dialog)
        self.maxStock.setObjectName(u"maxStock")
        self.maxStock.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.maxStock.setValidator(QIntValidator())

        self.verticalLayout.addWidget(self.maxStock)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u836f\u54c1", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u65b0\u589e\u836f\u54c1\u540d\u79f0", None))
        self.nameLine.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u8fdb\u4ef7", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u5904\u65b9\u4ef7", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u8fdb\u8d27\u91cf", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u6700\u5c0f\u5e93\u5b58\u9608\u503c\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u6700\u5927\u5e93\u5b58\u9608\u503c\u8bbe\u7f6e", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
    # retranslateUi

