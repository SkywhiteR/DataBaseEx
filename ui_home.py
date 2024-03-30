# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homePage.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import background_image

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 592)
        MainWindow.setStyleSheet(u"background-image: url(D:\\PyCharm\\pythonProject\\back.jpg);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, -20, 451, 131))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 90, 231, 41))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.PriviligeLabel = QLabel(self.centralwidget)
        self.PriviligeLabel.setObjectName(u"PriviligeLabel")
        self.PriviligeLabel.setGeometry(QRect(420, 80, 161, 61))
        self.PriviligeLabel.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 140, 91, 81))
        self.label_3.setFont(font)
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(-90, -20, 1031, 691))
        self.listView.setStyleSheet(u"background-image: url(:/back.jpg)")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(260, 230, 291, 221))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.registerButton = QPushButton(self.verticalLayoutWidget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setIconSize(QSize(16, 15))

        self.verticalLayout.addWidget(self.registerButton)

        self.PresciptionButton = QPushButton(self.verticalLayoutWidget)
        self.PresciptionButton.setObjectName(u"PresciptionButton")

        self.verticalLayout.addWidget(self.PresciptionButton)

        self.PayButton = QPushButton(self.verticalLayoutWidget)
        self.PayButton.setObjectName(u"PayButton")

        self.verticalLayout.addWidget(self.PayButton)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.SearchButton = QPushButton(self.verticalLayoutWidget)
        self.SearchButton.setObjectName(u"SearchButton")

        self.verticalLayout.addWidget(self.SearchButton)

        self.SettingButton = QPushButton(self.verticalLayoutWidget)
        self.SettingButton.setObjectName(u"SettingButton")

        self.verticalLayout.addWidget(self.SettingButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.listView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.PriviligeLabel.raise_()
        self.label_3.raise_()
        self.verticalLayoutWidget.raise_()
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u754c\u9762", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u6765\u5230\u6821\u533b\u9662\u6536\u8d39\u7ba1\u7406\u7cfb\u7edf", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u60a8\u7684\u8eab\u4efd\u6743\u9650\u662f\uff1a", None))
        self.PriviligeLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u83dc\u5355", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"\u6302\u53f7\u786e\u8bca", None))
        self.PresciptionButton.setText(QCoreApplication.translate("MainWindow", u"\u5904\u65b9\u7ba1\u7406", None))
        self.PayButton.setText(QCoreApplication.translate("MainWindow", u"\u7f34\u8d39\u7ed3\u7b97", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u836f\u54c1\u7ba1\u7406", None))
        self.SearchButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u7edf\u8ba1", None))
        self.SettingButton.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u8bbe\u7f6e\u4e0e\u4fee\u6539", None))
    # retranslateUi

