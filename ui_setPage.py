# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setPage.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)
import background_image

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(194, 196)
        Dialog.setAcceptDrops(True)
        Dialog.setStyleSheet(u"background-image: url(:/back.jpg);")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.setDepart = QPushButton(Dialog)
        self.setDepart.setObjectName(u"setDepart")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(11)
        self.setDepart.setFont(font1)

        self.gridLayout.addWidget(self.setDepart, 2, 0, 1, 1)

        self.setOperator = QPushButton(Dialog)
        self.setOperator.setObjectName(u"setOpeartor")
        self.setOperator.setFont(font1)

        self.gridLayout.addWidget(self.setOperator, 4, 0, 1, 1)

        self.setDoctor = QPushButton(Dialog)
        self.setDoctor.setObjectName(u"setDoctor")
        self.setDoctor.setFont(font1)

        self.gridLayout.addWidget(self.setDoctor, 5, 0, 1, 1)

        self.returnHome = QPushButton(Dialog)
        self.returnHome.setObjectName(u"returnHome")
        self.returnHome.setFont(font1)

        self.gridLayout.addWidget(self.returnHome, 6, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7cfb\u7edf\u8bbe\u7f6e\u4e0e\u4fee\u6539", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7cfb\u7edf\u8bbe\u7f6e\u4e0e\u4fee\u6539", None))
        self.setDepart.setText(QCoreApplication.translate("Dialog", u"\u79d1\u5ba4\u8bbe\u7f6e", None))
        self.setOperator.setText(QCoreApplication.translate("Dialog", u"\u64cd\u4f5c\u5458\u7ba1\u7406", None))
        self.setDoctor.setText(QCoreApplication.translate("Dialog", u"\u533b\u751f\u7ba1\u7406", None))
        self.returnHome.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de\u4e3b\u754c\u9762", None))
    # retranslateUi

