# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'query.ui'
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
    QLabel, QPushButton, QSizePolicy, QWidget)
import background_image

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(394, 199)
        Dialog.setStyleSheet(u"background-image: url(:/back.jpg);")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 6, 0, 1, 1, Qt.AlignTop)

        self.doctorPre = QPushButton(Dialog)
        self.doctorPre.setObjectName(u"doctorPre")

        self.gridLayout.addWidget(self.doctorPre, 8, 1, 1, 1)

        self.departmentNum = QPushButton(Dialog)
        self.departmentNum.setObjectName(u"departmentNum")

        self.gridLayout.addWidget(self.departmentNum, 7, 1, 1, 1)

        self.IncomeButton = QPushButton(Dialog)
        self.IncomeButton.setObjectName(u"IncomeButton")

        self.gridLayout.addWidget(self.IncomeButton, 7, 0, 1, 1)

        self.departmentPre = QPushButton(Dialog)
        self.departmentPre.setObjectName(u"departmentPre")

        self.gridLayout.addWidget(self.departmentPre, 8, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(11)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, Qt.AlignLeft)

        self.returnHome = QPushButton(Dialog)
        self.returnHome.setObjectName(u"returnHome")

        self.gridLayout.addWidget(self.returnHome, 0, 1, 1, 1, Qt.AlignRight)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u67e5\u8be2\u7edf\u8ba1", None))
        self.doctorPre.setText(QCoreApplication.translate("Dialog", u"\u6307\u5b9a\u533b\u751f\u5904\u65b9\u60c5\u51b5", None))
        self.departmentNum.setText(QCoreApplication.translate("Dialog", u"\u5404\u79d1\u5ba4\u6302\u53f7\u4eba\u6570", None))
        self.IncomeButton.setText(QCoreApplication.translate("Dialog", u"\u6302\u53f7\u8d39\u6536\u5165", None))
        self.departmentPre.setText(QCoreApplication.translate("Dialog", u"\u5404\u79d1\u5ba4\u5904\u65b9\u91d1\u989d", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u67e5\u8be2\u7edf\u8ba1", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u67e5\u8be2\u65e5\u671f\uff1a", None))
        self.returnHome.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de\u4e3b\u754c\u9762", None))
    # retranslateUi

