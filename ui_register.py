# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
import background_image

class register_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(-10, -10, 821, 621))
        self.listView.setStyleSheet(u"background: url(:/back.jpg);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 0, 131, 131))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.ReturnHome0 = QPushButton(self.centralwidget)
        self.ReturnHome0.setObjectName(u"ReturnHome0")
        self.ReturnHome0.setGeometry(QRect(530, 370, 121, 51))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(11)
        self.ReturnHome0.setFont(font1)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 111, 331, 451))
        self.updateInfo = QPushButton(self.centralwidget)
        self.updateInfo.setObjectName(u"updateInfo")
        self.updateInfo.setGeometry(QRect(530, 310, 121, 51))
        font2 = QFont()
        font2.setPointSize(11)
        self.updateInfo.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 60, 161, 51))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(12)
        self.label_2.setFont(font3)
        self.register_2 = QPushButton(self.centralwidget)
        self.register_2.setObjectName(u"register_2")
        self.register_2.setGeometry(QRect(530, 190, 121, 51))
        self.register_2.setFont(font1)
        self.searchPatient = QPushButton(self.centralwidget)
        self.searchPatient.setObjectName(u"searchPatient")
        self.searchPatient.setGeometry(QRect(530, 250, 121, 51))
        self.searchPatient.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6302\u53f7\u5019\u8bca", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6302\u53f7\u5019\u8bca", None))
        self.ReturnHome0.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u4e3b\u83dc\u5355", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6302\u53f7\u53f7\u7801", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5019\u8bca\u79d1\u5ba4", None));
        self.updateInfo.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u60a3\u8005\u5217\u8868", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5728\u5019\u8bca\u60a3\u8005\u4fe1\u606f", None))
        self.register_2.setText(QCoreApplication.translate("MainWindow", u"\u6302\u53f7", None))
        self.searchPatient.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627e\u60a3\u8005", None))
    # retranslateUi

