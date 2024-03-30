# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addOperator.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import background_image

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(267, 252)
        Dialog.setStyleSheet(u"background-image: url(:/back.jpg);")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 6, 0, 1, 1)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1, Qt.AlignLeft)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft)

        self.comfirmButton = QPushButton(Dialog)
        self.comfirmButton.setObjectName(u"comfirmButton")

        self.gridLayout.addWidget(self.comfirmButton, 7, 0, 1, 1, Qt.AlignHCenter)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft)

        self.returnButton = QPushButton(Dialog)
        self.returnButton.setObjectName(u"returnButton")

        self.gridLayout.addWidget(self.returnButton, 8, 0, 1, 1, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u589e\u52a0\u64cd\u4f5c\u5458", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6743\u9650\u8bbe\u5b9a\uff1a", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u589e\u52a0\u64cd\u4f5c\u5458", None))
        self.comfirmButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u8d26\u53f7\uff1a", None))
        self.returnButton.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de", None))
    # retranslateUi

