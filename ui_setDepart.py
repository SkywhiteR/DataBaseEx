# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setDepart.ui'
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
        Dialog.resize(337, 465)
        Dialog.setStyleSheet(u"background-image: url(:/back.jpg);")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.addDepart = QPushButton(Dialog)
        self.addDepart.setObjectName(u"addDepart")

        self.gridLayout.addWidget(self.addDepart, 3, 0, 1, 1, Qt.AlignHCenter)

        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)

        self.deletDepart = QPushButton(Dialog)
        self.deletDepart.setObjectName(u"deletDepart")

        self.gridLayout.addWidget(self.deletDepart, 4, 0, 1, 1, Qt.AlignHCenter)

        self.returnButton = QPushButton(Dialog)
        self.returnButton.setObjectName(u"returnButton")

        self.gridLayout.addWidget(self.returnButton, 5, 0, 1, 1, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u79d1\u5ba4\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u79d1\u5ba4\u8bbe\u7f6e", None))
        self.addDepart.setText(QCoreApplication.translate("Dialog", u"\u589e\u52a0\u79d1\u5ba4", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u79d1\u5ba4\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u79d1\u5ba4\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u5176\u4ed6", None));
        self.deletDepart.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664\u9009\u4e2d\u79d1\u5ba4", None))
        self.returnButton.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de", None))
    # retranslateUi

