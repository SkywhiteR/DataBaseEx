from PySide6.QtWidgets import *
from PySide6.QtCore import *
import pymysql as sql
import ui_setPage as sp
import ui_setDepart as sd
import ui_addDepart as ad
import ui_setOperator as so
import ui_addOperator as ao
import ui_setDoctor as sdt
import ui_addDoctor as adt
import PageHome

class SettingPage(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = sp.Ui_Dialog()
        self.ui.setupUi(self)
        self.privilige = userType
        self.bandButton()

    def bandButton(self):
        self.ui.setDepart.clicked.connect(self.setDepart)
        self.ui.setOperator.clicked.connect(self.setOperator)
        self.ui.setDoctor.clicked.connect(self.setDoctor)
        self.ui.returnHome.clicked.connect(self.returnHome)

    def setDepart(self):
        self.set_depart = SettingDepartPage(self.privilige)
        self.set_depart.show()
        self.close()

    def setOperator(self):
        self.set_operator = SettingOperatorPage(self.privilige)
        self.set_operator.show()
        self.close()

    def setDoctor(self):
        self.set_doctor = SettingDoctorPage(self.privilige)
        self.set_doctor.show()
        self.close()

    def returnHome(self):
        self.home = PageHome.HomePage(self.privilige)
        self.home.show()
        self.close()

class SettingDepartPage(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = sd.Ui_Dialog()
        self.ui.setupUi(self)
        self.privilige = userType
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.bandButton()
        self.showDepartInfo()
        self.ui.tableWidget.setSelectionMode(QTableWidget.MultiSelection)

    def bandButton(self):
        self.ui.addDepart.clicked.connect(self.addDepart)
        self.ui.deletDepart.clicked.connect(self.deleteDepart)
        self.ui.returnButton.clicked.connect(self.returnPage)

    def showDepartInfo(self):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT DepartmentID, Name FROM department
        """
        cursor.execute(selectSql)
        data = cursor.fetchall()

        self.ui.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row_index)
            for column_index, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(value)))

        cursor.close()

    def addDepart(self):
        self.add_depart = AddDepartment(self.privilige)
        self.add_depart.show()
        self.close()

    def deleteDepart(self):
        selectedRows = self.ui.tableWidget.selectionModel().selectedRows()
        if len(selectedRows) < 1:
            QMessageBox.warning(self, '错误', '请选择一行数据进行删除！')
            return

        for rows in selectedRows:
            row = rows.row()
            departmentId = self.ui.tableWidget.item(row, 0).text()
            departName = self.getDepartName(departmentId)
            try:
                self.deleteDepartInDB(departmentId)
                self.ui.tableWidget.removeRow(row)
            except:
                QMessageBox.warning(self, '错误', '该科室仍有医生和患者，无法被删除！')
            QMessageBox.information(self, '删除成功', '成功删除科室{}'.format(departName))

    def getDepartName(self, departId):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Name FROM department WHERE DepartmentID = %s", (departId,))
        departName = cursor.fetchone()[0]
        cursor.close()
        return departName

    def deleteDepartInDB(self, departmentId):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM department WHERE DepartmentID = %s", (departmentId,))
        self.db_connection.commit()
        cursor.close()

    def returnPage(self):
        self.return_page = SettingPage(self.privilige)
        self.return_page.show()
        self.close()

class AddDepartment(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = ad.Ui_Dialog()
        self.ui.setupUi(self)
        self.privilige = userType
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.ui.pushButton.clicked.connect(self.comfirm)
        self.ui.returnButton.clicked.connect(self.returnToPage)

    def updateDB(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MAX(DepartmentID) FROM department")
        departmentId = cursor.fetchone()[0] + 1
        insertSql = """
        INSERT INTO department (DepartmentID, Name)
        VALUES (%s, %s)
        """
        cursor.execute(insertSql, (departmentId, self.newDepartName))
        self.db_connection.commit()
        cursor.close()

    def comfirm(self):
        self.newDepartName = self.ui.lineEdit.text()

        if len(self.newDepartName) < 1:
            QMessageBox.information(self, '错误', '科室名称不能为空!')
            return

        self.updateDB()
        QMessageBox.information(self, "添加成功", "成功添加科室:{}!".format(self.newDepartName))
        self.returnToPage()

    def returnToPage(self):
        self.returnPage = SettingDepartPage(self.privilige)
        self.returnPage.show()
        self.close()

class SettingOperatorPage(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = so.Ui_Dialog()
        self.ui.setupUi(self)
        self.privilige = userType
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.bandButton()
        self.showOperatorInfo()
        self.ui.tableWidget.setSelectionMode(QTableWidget.MultiSelection)

    def bandButton(self):
        self.ui.addButton.clicked.connect(self.addOperator)
        self.ui.deleteButton.clicked.connect(self.deleteOperator)
        self.ui.returnButton.clicked.connect(self.returnPage)

    def showOperatorInfo(self):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT UserID, Name, Password, UserType FROM user
        """
        cursor.execute(selectSql)
        data = cursor.fetchall()

        self.ui.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row_index)
            for column_index, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(value)))

        cursor.close()

    def addOperator(self):
        self.add_operator = AddOperatorPage(self.privilige)
        self.add_operator.show()
        self.close()

    def deleteOperator(self):
        selectedRows = self.ui.tableWidget.selectionModel().selectedRows()
        if len(selectedRows) < 1:
            QMessageBox.warning(self, '错误', '请选择一行数据进行删除！')
            return
        for rows in selectedRows:
            row = rows.row()
            userId = self.ui.tableWidget.item(row, 0).text()
            self.deleteOperatorInDB(userId)
            self.ui.tableWidget.removeRow(row)
        QMessageBox.information(self, '删除成功', '该账号成功删除！')

    def deleteOperatorInDB(self, userId):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM user WHERE UserID = %s", (userId,))
        self.db_connection.commit()
        cursor.close()

    def returnPage(self):
        self.return_page = SettingPage(self.privilige)
        self.return_page.show()
        self.close()

class AddOperatorPage(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = ao.Ui_Dialog()
        self.ui.setupUi(self)
        self.privilige = userType
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.ui.comfirmButton.clicked.connect(self.comfirm)
        self.ui.returnButton.clicked.connect(self.returnToPage)
        self.updateBox()

    def updateBox(self):
        priviliges = ['医生', '收费员', '药品管理员', '系统管理员', '全能']
        self.ui.comboBox.clear()
        for privilige in priviliges:
            self.ui.comboBox.addItem(privilige)

    def updateDB(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MAX(UserID) FROM user")
        userId = cursor.fetchone()[0] + 1
        insertSql = """
                INSERT INTO user (UserID, Name, PassWord, UserType)
                VALUES (%s, %s, %s, %s)
                """
        cursor.execute(insertSql, (userId, self.userName, self.password, self.userType))
        self.db_connection.commit()
        cursor.close()

    def comfirm(self):
        self.userName = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()
        self.userType = self.ui.comboBox.currentText()

        if len(self.userName) < 1 or len(self.password) < 1:
            QMessageBox.information(self, '错误', '用户名或密码不能为空！')
            return

        self.updateDB()
        QMessageBox.information(self, '添加成功', '操作员添加成功！')
        self.returnToPage()

    def returnToPage(self):
        self.returnPage = SettingOperatorPage(self.privilige)
        self.returnPage.show()
        self.close()

class SettingDoctorPage(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = sdt.Ui_Dialog()
        self.ui.setupUi(self)
        self.privilige = userType
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.bandButton()
        self.showDoctorInfo()
        self.ui.tableWidget.setSelectionMode(QTableWidget.MultiSelection)

    def bandButton(self):
        self.ui.addButton.clicked.connect(self.addDoctor)
        self.ui.deleteButton.clicked.connect(self.deleteDoctor)
        self.ui.returnButton.clicked.connect(self.returnPage)

    def showDoctorInfo(self):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT dt.DoctorID, dt.Name, Sex, dm.Name 
        FROM doctor dt, department dm
        WHERE dt.DepartmentID = dm.DepartmentID
        """
        cursor.execute(selectSql)
        data = cursor.fetchall()

        self.ui.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row_index)
            for column_index, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(value)))

        cursor.close()

    def addDoctor(self):
        self.add_doctor = AddDoctorPage(self.privilige)
        self.add_doctor.show()
        self.close()

    def deleteDoctor(self):
        selectedRows = self.ui.tableWidget.selectionModel().selectedRows()
        if len(selectedRows) < 1:
            QMessageBox.warning(self, '错误', '请选择一行数据进行删除！')
            return
        for rows in selectedRows:
            row = rows.row()
            doctorId = self.ui.tableWidget.item(row, 0).text()
            doctorName = self.ui.tableWidget.item(row, 1).text()
            try:
                self.deleteDoctorInDB(doctorId)
                self.ui.tableWidget.removeRow(row)
            except:
                QMessageBox.warning(self, '错误', '该医生仍有患者未处理，无法被删除！')
            QMessageBox.information(self, '删除成功', '医生{}信息删除成功！'.format(doctorName))

    def deleteDoctorInDB(self, doctorId):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM doctor WHERE DoctorID = %s", (doctorId,))
        self.db_connection.commit()
        cursor.close()

    def returnPage(self):
        self.return_page = SettingPage(self.privilige)
        self.return_page.show()
        self.close()

class AddDoctorPage(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = adt.Ui_Dialog()
        self.ui.setupUi(self)
        self.privilige = userType
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.ui.pushButton.clicked.connect(self.comfirm)
        self.ui.returnButton.clicked.connect(self.returnToPage)
        self.updateSexBox()
        self.updateDepartBox()

    def updateSexBox(self):
        genders = ['男', '女']
        self.ui.sexBox.clear()
        for gender in genders:
            self.ui.sexBox.addItem(gender)

    def updateDepartBox(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Name FROM department")
        self.ui.DepartBox.clear()
        for departmentName in cursor.fetchall():
            self.ui.DepartBox.addItem(departmentName[0])
        cursor.close()

    def updateDB(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MAX(DoctorID) FROM doctor")
        doctorId = cursor.fetchone()[0] + 1
        cursor.execute("SELECT DepartmentID FROM department WHERE Name = %s", (self.depart,))
        departId = cursor.fetchone()[0]

        insertSql = """
                        INSERT INTO doctor (DoctorID, Name, Sex, DepartmentID)
                        VALUES (%s, %s, %s, %s)
                        """
        cursor.execute(insertSql, (doctorId, self.doctorName, self.sex, departId))
        self.db_connection.commit()

        cursor.close()

    def comfirm(self):
        self.doctorName = self.ui.nameLine.text()
        self.sex = self.ui.sexBox.currentText()
        self.depart = self.ui.DepartBox.currentText()

        if len(self.doctorName) < 1:
            QMessageBox.information(self, '错误', '医生姓名不能为空！')
            return

        self.updateDB()
        QMessageBox.information(self, '添加成功', '医生添加成功！')
        self.returnToPage()

    def returnToPage(self):
        self.returnPage = SettingDoctorPage(self.privilige)
        self.returnPage.show()
        self.close()