# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editPrescription.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import background_image

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(417, 394)
        Dialog.setStyleSheet(u"background-image:url(:/back.jpg)")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.addButton = QPushButton(Dialog)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout.addWidget(self.addButton, 0, Qt.AlignHCenter)

        self.deleteButton = QPushButton(Dialog)
        self.deleteButton.setObjectName(u"deleteButton")

        self.verticalLayout.addWidget(self.deleteButton, 0, Qt.AlignHCenter)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7f16\u8f91\u5904\u65b9", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u533b\u751f\u59d3\u540d\uff1a", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u60a3\u8005\u59d3\u540d\uff1a", None))
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u836f\u54c1\u548c\u6570\u91cf\uff1a", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u6570\u91cf", None));
        self.addButton.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u836f\u54c1", None))
        self.deleteButton.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664\u9009\u5b9a\u836f\u54c1", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
    # retranslateUi

