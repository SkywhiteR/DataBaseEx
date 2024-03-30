from PySide6.QtWidgets import *
from PageRegister import *
from PagePrescriptionManage import *
from PagePayFee import *
from PageDrugManage import *
from PageQuery import *
from PageSetting import *
import ui_home as home
class HomePage(QMainWindow):
    def __init__(self, userType):
        super().__init__()
        self.ui = home.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PriviligeLabel.setText(userType)
        self.privilige = userType
        self.bandButton()

    def bandButton(self):
        self.ui.registerButton.clicked.connect(self.registerPage)
        self.ui.PayButton.clicked.connect(self.payPage)
        self.ui.PresciptionButton.clicked.connect(self.managePage)
        self.ui.SearchButton.clicked.connect(self.searchPage)
        self.ui.SettingButton.clicked.connect(self.settingPage)
        self.ui.pushButton.clicked.connect(self.DrugManage)

    def registerPage(self):
        if self.privilige == '医生' or self.privilige == '全能':
            self.register = Register(self.privilige)
            self.register.show()
            self.close()
        else:
            QMessageBox.warning(self, "权限不足", "该模块由医生进行操作，您的权限不足！")

    def payPage(self):
        if self.privilige == '收费员' or self.privilige == '全能':
            self.pay_page = PayPage(self.privilige)
            self.pay_page.show()
            self.close()
        else:
            QMessageBox.warning(self, "权限不足", "该模块由收费员进行操作，您的权限不足！")

    def managePage(self):
        if self.privilige == '医生' or self.privilige == '全能':
            self.manage = PrescriptionManagePage(self.privilige)
            self.manage.show()
            self.close()
        else:
            QMessageBox.warning(self, "权限不足", "该模块由医生进行操作，您的权限不足！")

    def DrugManage(self):
        if self.privilige == '药品管理员' or self.privilige == '全能':
            self.drugManage = DrugManagePage(self.privilige)
            self.drugManage.show()
            self.close()
        else:
            QMessageBox.warning(self, "权限不足", "该模块由药品管理员进行操作，您的权限不足！")

    def searchPage(self):
        self.queryPage = QueryPage(self.privilige)
        self.queryPage.show()
        self.close()

    def settingPage(self):
        if self.privilige == '系统管理员' or self.privilige == '全能':
            self.setPage = SettingPage(self.privilige)
            self.setPage.show()
            self.close()
        else:
            QMessageBox.warning(self, "权限不足", "该模块由系统管理员进行操作，您的权限不足！")