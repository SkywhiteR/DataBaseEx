from PySide6.QtWidgets import *
from PySide6.QtCore import *
import pymysql as sql
import ui_query as qy
import ui_departNum as dn
import ui_departPresc as dp
import ui_doctorPrep as dpp
import PageHome

class QueryPage(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = qy.Ui_Dialog()
        self.ui.setupUi(self)
        self.privilige = userType
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.bandButton()
        self.updateDate()

    def bandButton(self):
        self.ui.returnHome.clicked.connect(self.returnHome)
        self.ui.IncomeButton.clicked.connect(self.registerFee)
        self.ui.departmentNum.clicked.connect(self.departNum)
        self.ui.departmentPre.clicked.connect(self.departPre)
        self.ui.doctorPre.clicked.connect(self.doctorPre)

    def updateDate(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT DISTINCT Date FROM patient")
        self.ui.comboBox.clear()
        for date in cursor.fetchall():
            self.ui.comboBox.addItem(str(date[0]))
        cursor.close()

    def returnHome(self):
        self.home = PageHome.HomePage(self.privilige)
        self.home.show()
        self.close()

    def registerFee(self):
        cursor = self.db_connection.cursor()
        date = self.ui.comboBox.currentText()
        if len(date) < 1:
            QMessageBox.warning(self, '错误', '选择日期不能为空！')
            return

        cursor.execute("SELECT COUNT(*) FROM patient WHERE Date = %s", (date,))
        patientNumber = cursor.fetchone()[0]
        register_fee = int(patientNumber) * 10
        QMessageBox.information(self, "挂号费用", "日期{}的挂号费用为：{}".format(date, register_fee))
        cursor.close()

    def departNum(self):
        self.depart_num = DepartmentPatient(self.ui.comboBox.currentText())
        self.depart_num.show()

    def departPre(self):
        self.depart_pre = DepartmentPrescriptionFee(self.ui.comboBox.currentText())
        self.depart_pre.show()

    def doctorPre(self):
        self.doctor_pre = DoctorPrescriptionInfo()
        self.doctor_pre.show()

class DepartmentPatient(QDialog):
    def __init__(self, day):
        super().__init__()
        self.ui = dn.Ui_Dialog()
        self.ui.setupUi(self)
        self.day = day
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.updateDepart()
        self.updateInfo()

    def updateDepart(self):
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

    def updateInfo(self):
        cursor = self.db_connection.cursor()
        for row in range(self.ui.tableWidget.rowCount()):
            departName = self.ui.tableWidget.item(row, 1).text()
            cursor.execute("SELECT COUNT(*) FROM patient WHERE Department = %s AND Date = %s", (departName, self.day))
            patientNum = cursor.fetchone()
            if patientNum is None:
                patientNum = 0
            else:
                patientNum = patientNum[0]
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(patientNum)))
        cursor.close()

class DepartmentPrescriptionFee(QDialog):
    def __init__(self, day):
        super().__init__()
        self.ui = dp.Ui_Dialog()
        self.ui.setupUi(self)
        self.day = day
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.updateDepart()
        self.updateInfo()

    def updateDepart(self):
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

    def updateInfo(self):
        cursor = self.db_connection.cursor()
        for row in range(self.ui.tableWidget.rowCount()):
            departName = self.ui.tableWidget.item(row, 1).text()
            selectSql = """
            SELECT PrescriptionPrice, Quantity
            FROM drug, patient, prescription pp, prescriptiondetail pd
            WHERE patient.Department = %s AND patient.PatientID = pp.PatientID
                AND pp.PrescriptionID = pd.PrescriptionID AND pd.DrugID = drug.DrugID
                AND patient.Date = %s
            """
            cursor.execute(selectSql, (departName, self.day))
            data = cursor.fetchall()
            totalPrice = 0

            if len(data) > 0:
                for tp in data:
                    prescriptionPrice = float(tp[0])
                    quantity = float(tp[1])
                    totalPrice += prescriptionPrice * quantity

            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(totalPrice)))
        cursor.close()

class DoctorPrescriptionInfo(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = dpp.Ui_Dialog()
        self.ui.setupUi(self)
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.ui.pushButton.clicked.connect(self.searchAndShow)
        self.updateDepartment()
        self.updateDoctor()
        self.ui.comboBox_2.currentTextChanged.connect(self.updateDoctor)

    def updateDepartment(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Name FROM department")
        self.ui.comboBox_2.clear()
        for departmentName in cursor.fetchall():
            self.ui.comboBox_2.addItem(departmentName[0])
        cursor.close()

    def updateDoctor(self):
        cursor = self.db_connection.cursor()
        depart = self.ui.comboBox_2.currentText()
        cursor.execute("SELECT doctor.Name FROM doctor, department\
                       WHERE doctor.DepartmentID = department.DepartmentID\
                            AND department.Name = %s", (depart,))
        self.ui.comboBox.clear()
        for departmentName in cursor.fetchall():
            self.ui.comboBox.addItem(departmentName[0])
        cursor.close()

    def searchAndShow(self):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT patient.DoctorID, patient.Doctor, patient.Name, pp.PrescriptionID, drug.Name, pd.Quantity
        FROM drug, patient, prescription pp, prescriptiondetail pd
        WHERE patient.Doctor = %s AND patient.patientID = pp.patientID AND
            pp.PrescriptionID = pd.PrescriptionID AND pd.DrugID = drug.DrugID
        """
        doctorName = self.ui.comboBox.currentText()
        cursor.execute(selectSql, (doctorName,))
        data = cursor.fetchall()

        if len(data) == 0:
            QMessageBox.warning(self, "查询失败", "该医生无处方信息!")
            return

        self.ui.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row_index)
            for column_index, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(value)))

        cursor.close()