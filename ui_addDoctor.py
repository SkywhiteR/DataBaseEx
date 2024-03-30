# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addDoctor.ui'
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
        Dialog.resize(190, 291)
        Dialog.setStyleSheet(u"background-image: url(:/back.jpg);")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft)

        self.nameLine = QLineEdit(Dialog)
        self.nameLine.setObjectName(u"nameLine")

        self.gridLayout.addWidget(self.nameLine, 2, 0, 1, 1)

        self.sexBox = QComboBox(Dialog)
        self.sexBox.setObjectName(u"sexBox")

        self.gridLayout.addWidget(self.sexBox, 4, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1, Qt.AlignLeft)

        self.DepartBox = QComboBox(Dialog)
        self.DepartBox.setObjectName(u"DepartBox")

        self.gridLayout.addWidget(self.DepartBox, 7, 0, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 1, Qt.AlignHCenter)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1, Qt.AlignLeft)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.returnButton = QPushButton(Dialog)
        self.returnButton.setObjectName(u"returnButton")

        self.gridLayout.addWidget(self.returnButton, 9, 0, 1, 1, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u589e\u52a0\u533b\u751f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u65b0\u589e\u533b\u751f\u59d3\u540d\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u65b0\u589e\u533b\u751f\u6240\u5c5e\u79d1\u5ba4\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u65b0\u589e\u533b\u751f\u6027\u522b\uff1a", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u589e\u52a0\u533b\u751f", None))
        self.returnButton.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de", None))
    # retranslateUi

