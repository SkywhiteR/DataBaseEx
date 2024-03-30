from PySide6.QtWidgets import *
import ui_pay as pay
import pymysql as sql
import PageHome

class PayPage(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = pay.Ui_Dialog()
        self.ui.setupUi(self)
        self.privilige = userType
        self.bandButton()
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )

    def bandButton(self):
        self.ui.returnHome.clicked.connect(self.returnHome)
        self.ui.pushButton_2.clicked.connect(self.pay)
        self.ui.pushButton.clicked.connect(self.showInfo)

    def returnHome(self):
        self.home = PageHome.HomePage(self.privilige)
        self.home.show()
        self.close()

    def getInfo(self):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT pp.PrescriptionID, pt.Name, dg.Name, pd.quantity, dg.PrescriptionPrice
        FROM prescription pp, prescriptiondetail pd, drug dg, patient pt
        WHERE pp.PrescriptionID = pd.PrescriptionID AND pp.PatientId = pt.PatientID
            AND pd.DrugID = dg.DrugID AND pp.PrescriptionID = %s
        """
        cursor.execute(selectSql, (self.prescriptionId,))
        data = cursor.fetchall()
        cursor.close()
        return data

    def showInfo(self):
        self.prescriptionId = self.ui.lineEdit.text()
        if len(self.prescriptionId) == 0:
            QMessageBox.warning(self, "警告", "输入处方号不能为空！")
            return
        Info = self.getInfo()
        if len(Info) == 0:
            QMessageBox.warning(self, "警告", "该处方号不存在！")
            return

        self.ui.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(Info):
            self.ui.tableWidget.insertRow(row_index)
            for column_index, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(value)))

        totalPrice = 0
        for row in range(self.ui.tableWidget.rowCount()):
            quantity = self.ui.tableWidget.item(row, 3).text()
            price = self.ui.tableWidget.item(row, 4).text()
            totalPrice += float(quantity) * float(price)
        self.ui.TotalPrice.setText(str(totalPrice) + "元")

    def check(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT PrescriptionID FROM prescription WHERE PrescriptionID = %s", (self.prescriptionId))
        flag = cursor.fetchall()
        if len(flag) == 0:
            QMessageBox.warning(self, '错误', '该处方不存在或已缴费！')
            return True
        return False

    def updateDrugInfo(self):
        cursor = self.db_connection.cursor()
        for row in range(self.ui.tableWidget.rowCount()):
            drugName = self.ui.tableWidget.item(row, 2).text()
            quantity = self.ui.tableWidget.item(row, 3).text()
            quantity = float(quantity)

            cursor.execute("SELECT CurrentStock FROM drug WHERE Name = %s", (drugName,))
            currentQuantity = cursor.fetchone()[0]
            currentQuantity = float(currentQuantity) - quantity
            cursor.execute("UPDATE drug SET CurrentStock = %s WHERE Name = %s", (str(currentQuantity), drugName))
            self.db_connection.commit()
        cursor.close()


    def pay(self):
        self.prescriptionId = self.ui.lineEdit.text()
        if self.check():
            return
        cursor = self.db_connection.cursor()

        self.updateDrugInfo()

        deleteSql = """
                        DELETE FROM prescriptiondetail WHERE PrescriptionID = %s
                        """
        cursor.execute(deleteSql, (self.prescriptionId,))
        self.db_connection.commit()

        deleteSql = """
                DELETE FROM prescription WHERE PrescriptionID = %s
                """
        cursor.execute(deleteSql, (self.prescriptionId,))
        self.db_connection.commit()

        cursor.close()

        QMessageBox.information(self, '缴费成功', '该处方已缴费成功！')

        self.close()

        self.returnHome()