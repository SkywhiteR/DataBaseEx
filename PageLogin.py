from PySide6.QtWidgets import *
from PageHome import *
import ui_login as login
import pymysql as sql

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = login.login_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)

        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM user WHERE Name = %s AND Password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            QMessageBox.information(self, '登陆成功', "登陆成功!")
            userType = user[3]
            self.homePage = HomePage(userType)
            self.homePage.show()
            self.close()
        else:
            QMessageBox.warning(self, '登录失败', '用户名或密码错误！')

        cursor.close()