from PySide6.QtWidgets import *
import PageHome
import ui_register as register
import ui_register_sec as register_sec
import ui_register_reg as register_reg
import pymysql as sql
from datetime import datetime
class Register(QMainWindow):
    def __init__(self, userType):
        super().__init__()
        self.ui = register.register_MainWindow()
        self.ui.setupUi(self)
        self.privilige = userType
        self.bandButton()

    def bandButton(self):
        self.ui.ReturnHome0.clicked.connect(self.returnHome)
        self.ui.updateInfo.clicked.connect(self.updateInfo)
        self.ui.register_2.clicked.connect(self.register)
        self.ui.searchPatient.clicked.connect(self.search)

    def returnHome(self):
        self.home = PageHome.HomePage(self.privilige)
        self.home.show()
        self.close()

    def register(self):
        self.reg = Register_reg()
        self.reg.show()

    def search(self):
        self.sec = Register_sec()
        self.sec.show()

    def updateInfo(self):
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Name, PatientID, Department FROM patient ")
        data = cursor.fetchall()

        self.ui.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row_index)
            for column_index, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(value)))

        cursor.close()

class Register_reg(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = register_reg.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register)
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.updateDepartment()
        self.updateDoctor()
        self.updateSex()
        self.ui.ComboBox.currentTextChanged.connect(self.updateDoctor)

    def updateSex(self):
        genders = ['男', '女']
        self.ui.comboBox.clear()
        for gender in genders:
            self.ui.comboBox.addItem(gender)

    def updateDepartment(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Name FROM department")
        self.ui.ComboBox.clear()
        for departmentName in cursor.fetchall():
            self.ui.ComboBox.addItem(departmentName[0])
        cursor.close()

    def updateDoctor(self):
        cursor = self.db_connection.cursor()
        depart = self.ui.ComboBox.currentText()
        cursor.execute("SELECT doctor.Name FROM doctor, department\
                       WHERE doctor.DepartmentID = department.DepartmentID\
                            AND department.Name = %s", (depart,))
        self.ui.ComboBox_2.clear()
        for departmentName in cursor.fetchall():
            self.ui.ComboBox_2.addItem(departmentName[0])
        cursor.close()

    def register(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MAX(PatientID) FROM patient")
        patientid = cursor.fetchone()[0] + 1
        name = self.ui.lineEdit.text()
        age = self.ui.LineEdit_3.text()
        sex = self.ui.comboBox.currentText()
        phone = self.ui.LineEdit_4.text()
        address = self.ui.LineEdit_5.text()
        department = self.ui.ComboBox.currentText()
        currentDate = datetime.now().strftime("%Y-%m-%d")

        doctor = self.ui.ComboBox_2.currentText()

        cursor.execute("SELECT DoctorID FROM doctor WHERE Name = %s", (doctor,))
        doctorID = cursor.fetchone()[0]

        cursor.execute("SELECT DepartmentID FROM department WHERE Name = %s", (department,))
        departmentID = cursor.fetchone()[0]

        insertSql = """
        INSERT INTO patient (PatientID, Name, age, Sex, Phone, Doctor, DoctorID, Department, DepartmentID, Address, Date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insertSql,
                       (patientid, name, age, sex, phone, doctor, doctorID, department, departmentID, address, currentDate))
        self.db_connection.commit()
        QMessageBox.information(self, '挂号成功', '挂号成功！')
        cursor.close()
        self.close()

class Register_sec(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = register_sec.register_sec_Form()
        self.ui.setupUi(self)
        self.ui.SearchButton.clicked.connect(self.search)

    def search(self):
        info = self.ui.lineEdit.text()
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT patient.Name, patient.Sex, age, Phone, Address, Department, doctor.Name\
                       FROM patient, doctor\
                       WHERE patient.DoctorID = doctor.DoctorID AND\
                            (%s = patient.Name OR %s = PatientID)", (info, info))
        data = cursor.fetchall()
        if len(data) < 1:
            QMessageBox.information(self, '查询失败', '数据库中无该患者信息!')
            return
        self.ui.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row_index)
            for column_index, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(value)))
        cursor.close()