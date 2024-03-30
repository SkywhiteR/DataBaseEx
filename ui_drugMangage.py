# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drugManage.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
import background_image

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(627, 600)
        Dialog.setStyleSheet(u"background-image:url(:/back.jpg)")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, Qt.AlignLeft)

        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 2)

        self.addButton = QPushButton(Dialog)
        self.addButton.setObjectName(u"addButton")

        self.gridLayout.addWidget(self.addButton, 2, 0, 1, 1)

        self.setButton = QPushButton(Dialog)
        self.setButton.setObjectName(u"setButton")

        self.gridLayout.addWidget(self.setButton, 3, 0, 1, 1)

        self.deleteButton = QPushButton(Dialog)
        self.deleteButton.setObjectName(u"deleteButton")

        self.gridLayout.addWidget(self.deleteButton, 2, 1, 1, 1)

        self.increaseButton = QPushButton(Dialog)
        self.increaseButton.setObjectName(u"increaseButton")

        self.gridLayout.addWidget(self.increaseButton, 3, 1, 1, 1)

        self.updateButton = QPushButton(Dialog)
        self.updateButton.setObjectName(u"updateButton")

        self.gridLayout.addWidget(self.updateButton, 4, 0, 1, 1)

        self.returnButton = QPushButton(Dialog)
        self.returnButton.setObjectName(u"returnButton")

        self.gridLayout.addWidget(self.returnButton, 4, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u7ba1\u7406", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u7ba1\u7406", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u6807\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u8fdb\u5355\u4ef7", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u5904\u65b9\u5355\u4ef7", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u5e93\u5b58", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u5efa\u8bae", None));
        self.addButton.setText(QCoreApplication.translate("Dialog", u"\u65b0\u589e\u836f\u54c1", None))
        self.setButton.setText(QCoreApplication.translate("Dialog", u"\u8bbe\u5b9a\u8fdb\u4ef7\u4e0e\u5904\u65b9\u4ef7", None))
        self.deleteButton.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664\u836f\u54c1", None))
        self.increaseButton.setText(QCoreApplication.translate("Dialog", u"改变药品库存", None))
        self.updateButton.setText(QCoreApplication.translate("Dialog", u"\u66f4\u65b0\u5217\u8868", None))
        self.returnButton.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de\u4e3b\u754c\u9762", None))
    # retranslateUi

