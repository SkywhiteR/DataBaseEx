from PySide6.QtWidgets import *
from datetime import datetime
import ui_prescriptionManage as preManage
import ui_addPrescription as addPre
import ui_editPrescription as editPre
import pymysql as sql
import PageHome

class PrescriptionManagePage(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = preManage.Ui_Dialog()
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
        self.ui.pushButton.clicked.connect(self.returnHome)
        self.ui.addPre.clicked.connect(self.add)
        self.ui.editPre.clicked.connect(self.edit)
        self.ui.pushButton_3.clicked.connect(self.delete)
        self.ui.fresh.clicked.connect(self.fresh)

    def check(self, id):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT PrescriptionID FROM prescription 
        WHERE PrescriptionID = %s
        """
        cursor.execute(selectSql, (id,))
        data = cursor.fetchone()
        if data is None:
            QMessageBox.warning(self, "查询失败", "该处方号不存在!")
            cursor.close()
            return False
        else:
            cursor.close()
            return True

    def returnHome(self):
        self.home = PageHome.HomePage(self.privilige)
        self.home.show()
        self.close()

    def fresh(self):
        cursor = self.db_connection.cursor()
        prescriptionId = self.ui.lineEdit.text()
        if not self.check(prescriptionId):
            self.ui.tableWidget.setRowCount(0)
            return

        selectSql = """
        SELECT prep.PrescriptionID, pt.Name, dt.Name, drug.Name, pdt.Quantity
        FROM doctor dt, patient pt, drug, prescription prep, prescriptiondetail pdt
        WHERE prep.PatientID = pt.PatientID AND prep.DoctorID = dt.DoctorID AND
            pdt.PrescriptionID = prep.PrescriptionID AND pdt.DrugID = drug.DrugID AND
            prep.PrescriptionID = %s
        """

        cursor.execute(selectSql, (prescriptionId,))
        data = cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row_index)
            for column_index, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(value)))
        cursor.close()

    def add(self):
        self.addPage = AddPrescription()
        self.addPage.show()

    def edit(self):
        prescriptionID = self.ui.lineEdit.text()
        if not self.check(prescriptionID):
            return
        self.editPage = EditPrescription(prescriptionID)
        self.editPage.show()

    def delete(self):
        cursor = self.db_connection.cursor()
        prescriptionID = self.ui.lineEdit.text()
        if len(prescriptionID) < 1:
            QMessageBox.warning(self, '错误', '处方号不能为空！')
            return

        deleteSql = """
                DELETE FROM prescriptiondetail WHERE PrescriptionID = %s
                """
        cursor.execute(deleteSql, (prescriptionID,))
        self.db_connection.commit()

        deleteSql = """
        DELETE FROM prescription WHERE PrescriptionID = %s
        """
        cursor.execute(deleteSql, (prescriptionID,))
        self.db_connection.commit()

        QMessageBox.information(self, '删除成功', '处方号为{}的处方删除成功!'.format(prescriptionID))

        cursor.close()

class AddPrescription(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = addPre.Ui_Dialog()
        self.ui.setupUi(self)
        self.bandButton()
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.ui.lineEdit_2.textChanged.connect(self.updatePatientInfo)
        self.ui.tableWidget.setSelectionMode(QTableWidget.MultiSelection)

    def bandButton(self):
        self.ui.pushButton_2.clicked.connect(self.addRow)
        self.ui.pushButton.clicked.connect(self.commit)
        self.ui.pushButton_3.clicked.connect(self.deleteRow)

    def getDrugName(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT NAME FROM drug")
        data = cursor.fetchall()
        cursor.close()
        return data

    def addRow(self):
        rowPosition = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPosition)
        comboBox = QComboBox()
        for name in self.getDrugName():
            comboBox.addItem(name[0])
        self.ui.tableWidget.setCellWidget(rowPosition, 0, comboBox)
        spinBox = QSpinBox()
        self.ui.tableWidget.setCellWidget(rowPosition, 1, spinBox)

    def deleteRow(self):
        selectedRows = self.ui.tableWidget.selectionModel().selectedRows()
        for row in selectedRows:
            self.ui.tableWidget.removeRow(row.row())

    def getInfo(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MAX(PrescriptionID) FROM prescription")
        self.prescriptionID = cursor.fetchone()[0]
        self.prescriptionID = 1 if self.prescriptionID is None else self.prescriptionID + 1

        cursor.execute("SELECT MAX(DetailID) FROM prescriptiondetail")
        self.detailID = cursor.fetchone()[0]
        self.detailID = 1 if self.detailID is None else self.detailID + 1

        self.doctorName = self.ui.lineEdit_2.text()
        cursor.execute("SELECT DoctorID FROM doctor WHERE Name = %s", (self.doctorName,))
        self.doctorID = cursor.fetchone()
        if self.doctorID is not None:
            self.doctorID = self.doctorID[0]

        self.patientName = self.ui.comboBox.currentText()
        cursor.execute("SELECT PatientID FROM patient WHERE Name = %s", (self.patientName,))
        self.patientID = cursor.fetchone()
        if self.patientID is not None:
            self.patientID = self.patientID[0]

        currentDate = datetime.now()
        self.formattedDate = currentDate.strftime("%Y-%m-%d")

    def commit(self):
        self.getInfo()
        if not self.doctorName:
            QMessageBox.warning(self, "警告", "医生姓名不能为空！")
            return
        if not self.patientName:
            QMessageBox.warning(self, "警告", "患者姓名不能为空！")
            return
        if not self.ui.tableWidget.rowCount():
            QMessageBox.warning(self, "警告", "药品选择不能为空！")
            return

        cursor = self.db_connection.cursor()
        flag = True

        for row in range(self.ui.tableWidget.rowCount()):
            drugName = self.ui.tableWidget.cellWidget(row, 0).currentText()
            quantity = self.ui.tableWidget.cellWidget(row, 1).value()

            if not drugName:
                QMessageBox.warning(self, "警告", "药品选择不能为空！")
                return
            if quantity == 0:
                QMessageBox.warning(self, "警告", "药品数量不能为零！")
                return
            if flag:
                insertSql = """
                                INSERT INTO prescription (PrescriptionID, PatientID, DoctorID, PrescriptionData)
                                VALUES (%s, %s, %s, %s)
                                """
                cursor.execute(insertSql, (self.prescriptionID, self.patientID, self.doctorID, self.formattedDate))
                self.db_connection.commit()
                flag = False

            cursor.execute("SELECT DrugID FROM drug WHERE Name = %s", (drugName,))
            drugID = cursor.fetchone()[0]
            insertSql = """
            INSERT INTO prescriptiondetail (DetailID, PrescriptionID, DrugID, Quantity)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insertSql, (self.detailID, self.prescriptionID, drugID, quantity))
            self.db_connection.commit()
            self.detailID += 1

        QMessageBox.information(self, '添加成功', '新处方添加成功，处方号为{}'.format(self.prescriptionID))
        self.close()

    def updatePatientInfo(self):
        doctorName = self.ui.lineEdit_2.text()
        self.ui.comboBox.clear()
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Name FROM patient WHERE doctor = %s", (doctorName,))

        for patientName in cursor.fetchall():
            self.ui.comboBox.addItem(patientName[0])

        cursor.close()

class EditPrescription(QDialog):
    def __init__(self, prescriptionID):
        super().__init__()
        self.ui = editPre.Ui_Dialog()
        self.ui.setupUi(self)
        self.prescriptionID = prescriptionID
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.bandButton()
        self.showInfo()
        self.ui.tableWidget.setSelectionMode(QTableWidget.MultiSelection)

    def bandButton(self):
        self.ui.addButton.clicked.connect(self.addRow)
        self.ui.deleteButton.clicked.connect(self.deleteRow)
        self.ui.pushButton_3.clicked.connect(self.commit)

    def getPrescriptionDetail(self):
        prescriptionDetail = []
        try:
            cursor = self.db_connection.cursor()
            selectSql = """
            SELECT DrugID, Quantity FROM prescriptiondetail
            WHERE PrescriptionID = %s
            """
            cursor.execute(selectSql, (self.prescriptionID,))
            results = cursor.fetchall()
            for row in results:
                drugID, quantity = row
                prescriptionDetail.append((drugID, quantity))
            cursor.close()
        except Exception as e:
            QMessageBox.warning(self, "查询失败", "获取处方明细失败!")

        return prescriptionDetail

    def getDrugName_ID(self, drugId):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT Name FROM drug WHERE DrugID = %s
        """
        cursor.execute(selectSql, (drugId,))
        drugName = cursor.fetchone()[0]
        cursor.close()
        return drugName

    def getDrugName(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT NAME FROM drug")
        data = cursor.fetchall()
        cursor.close()
        return data

    def showInfo(self):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT PatientID, DoctorID FROM prescription
        WHERE PrescriptionID = %s 
        """
        cursor.execute(selectSql, (self.prescriptionID,))
        data = cursor.fetchone()
        if data is None:
            QMessageBox.warning(self, "警告", "处方号不能为空！")
            return

        patientId = data[0]
        doctorId = data[1]

        cursor.execute("SELECT Name FROM patient WHERE PatientID = %s", (patientId,))
        patientName = cursor.fetchone()[0]
        cursor.execute("SELECT Name FROM doctor WHERE DoctorID = %s", (doctorId,))
        doctorName = cursor.fetchone()[0]

        self.ui.label_4.setText(doctorName)
        self.ui.label_5.setText(patientName)

        self.ui.tableWidget.setRowCount(0)
        prescriptionDetial = self.getPrescriptionDetail()
        for drugId, quantity in prescriptionDetial:
            drugName = self.getDrugName_ID(drugId)
            if drugName:
                rowPosition = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(rowPosition)
                self.ui.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(drugName))
                self.ui.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(quantity)))

    def addRow(self):
        rowPosition = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPosition)
        comboBox = QComboBox()
        for name in self.getDrugName():
            comboBox.addItem(name[0])
        self.ui.tableWidget.setCellWidget(rowPosition, 0, comboBox)

        spinBox = QSpinBox()
        self.ui.tableWidget.setCellWidget(rowPosition, 1, spinBox)

    def deleteRow(self):
        cursor = self.db_connection.cursor()
        selectedRows = self.ui.tableWidget.selectionModel().selectedRows()
        for row in selectedRows:
            dname = self.ui.tableWidget.item(row.row(), 0).text()
            cursor.execute("SELECT DrugID from drug WHERE Name = %s", (dname,))
            dID = cursor.fetchone()[0]
            deleteSql = """
                            DELETE FROM prescriptiondetail 
                            WHERE PrescriptionID = %s AND DrugID = %s
                            """
            cursor.execute(deleteSql, (self.prescriptionID, dID))
            self.db_connection.commit()
            self.ui.tableWidget.removeRow(row.row())
        cursor.close()

    def deleteOriginalPrescription(self):
        cursor = self.db_connection.cursor()
        deleteSql = """
        DELETE FROM prescriptiondetail WHERE PrescriptionID = %s
        """
        cursor.execute(deleteSql, (self.prescriptionID,))
        self.db_connection.commit()
        cursor.close()

    def commit(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MAX(DetailID) FROM prescriptiondetail WHERE PrescriptionID = %s",
                       (self.prescriptionID,))
        detailId = cursor.fetchone()[0] + 1
        cursor.execute("SELECT COUNT(*) FROM prescriptiondetail WHERE PrescriptionID = %s", (self.prescriptionID,))
        originalNum = cursor.fetchone()[0]
        for row in range(originalNum, self.ui.tableWidget.rowCount()):
            drugName = self.ui.tableWidget.cellWidget(row, 0).currentText()
            quantity = self.ui.tableWidget.cellWidget(row, 1).value()

            if not drugName:
                QMessageBox.warning(self, "警告", "药品选择不能为空！")
                return
            if quantity == 0:
                QMessageBox.warning(self, "警告", "药品数量不能为零！")
                return

            cursor.execute("SELECT DrugID FROM drug WHERE Name = %s", (drugName,))
            drugID = cursor.fetchone()[0]
            insertSql = """
            INSERT INTO prescriptiondetail (DetailID, PrescriptionID, DrugID, Quantity)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insertSql, (detailId, self.prescriptionID, drugID, quantity))
            detailId += 1
            self.db_connection.commit()

        currentDate = datetime.now()
        formattedDate = currentDate.strftime("%Y-%m-%d")
        updateSql = "UPDATE prescription SET PrescriptionData = %s WHERE PrescriptionID = %s"
        cursor.execute(updateSql, (formattedDate, self.prescriptionID))
        self.db_connection.commit()

        QMessageBox.information(self, '编辑成功', '编辑处方成功!')
        self.close()