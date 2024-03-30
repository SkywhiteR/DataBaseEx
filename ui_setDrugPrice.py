# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setDrugPrice.ui'
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
from PySide6.QtGui import QDoubleValidator
import background_image

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 260)
        Dialog.setStyleSheet(u"background-image: url(:/back.jpg);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.UnitLine = QLineEdit(Dialog)
        self.UnitLine.setObjectName(u"UnitLine")
        self.UnitLine.setValidator(QDoubleValidator())

        self.verticalLayout.addWidget(self.UnitLine)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.PPLine = QLineEdit(Dialog)
        self.PPLine.setObjectName(u"PPLine")
        self.PPLine.setValidator(QDoubleValidator())

        self.verticalLayout.addWidget(self.PPLine)

        self.comfirmButton = QPushButton(Dialog)
        self.comfirmButton.setObjectName(u"comfirmButton")

        self.verticalLayout.addWidget(self.comfirmButton, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bbe\u5b9a\u8fdb\u4ef7\u4e0e\u5904\u65b9\u4ef7", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u540d\u79f0\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u8fdb\u4ef7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u5904\u65b9\u4ef7\uff1a", None))
        self.comfirmButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
    # retranslateUi

