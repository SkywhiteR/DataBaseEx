from PySide6.QtWidgets import *
from PySide6.QtCore import *
import ui_drugMangage as dm
import ui_addDrug as ad
import ui_deleteDrug as dd
import ui_setDrugPrice as sdp
import ui_setDrugStock as sds
import pymysql as sql
import PageHome

class DrugManagePage(QDialog):
    def __init__(self, userType):
        super().__init__()
        self.ui = dm.Ui_Dialog()
        self.ui.setupUi(self)
        self.privilige = userType
        self.bandButton()
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.add_Drug = AddDrug()
        self.delete_Drug = DeleteDrug()
        self.set_Price = SetDrugPrice()
        self.set_Stock = SetDrugStock()

    def bandButton(self):
        self.ui.addButton.clicked.connect(self.addDrug)
        self.ui.deleteButton.clicked.connect(self.deleteDrug)
        self.ui.setButton.clicked.connect(self.setPrice)
        self.ui.increaseButton.clicked.connect(self.addStock)
        self.ui.updateButton.clicked.connect(self.updateDrugData)
        self.ui.returnButton.clicked.connect(self.returnHome)

    def addDrug(self):
        self.add_Drug.show()

    def deleteDrug(self):
        self.delete_Drug.show()

    def setPrice(self):
        self.set_Price.show()

    def addStock(self):
        self.set_Stock.show()

    def getMinStockFromDrug(self, drugID):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MinStock FROM drug WHERE DrugID = %s", (drugID,))
        return cursor.fetchone()[0]

    def getMaxStockFromDrug(self, drugID):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MaxStock FROM drug WHERE DrugID = %s", (drugID,))
        return cursor.fetchone()[0]

    def updateDrugData(self):
        self.ui.tableWidget.clearContents()
        self.updateTable()

    def updateTable(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT DrugID, Name, UnitPrice, PrescriptionPrice, CurrentStock FROM drug")
        data = cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for column_index, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(value)))

                currentStock = row_data[4]
                minStock = self.getMinStockFromDrug(row_data[0])
                maxStock = self.getMaxStockFromDrug(row_data[0])

                if currentStock < minStock:
                    advice = "建议采购"
                elif currentStock > maxStock:
                    advice = "建议减少库存"
                else:
                    advice = ""

                self.ui.tableWidget.setItem(row_index, 5, QTableWidgetItem(advice))

        cursor.close()

    def returnHome(self):
        self.home = PageHome.HomePage(self.privilige)
        self.home.show()
        self.close()

class AddDrug(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ad.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.confirm)

    def getInfo(self):
        self.drugName = self.ui.nameLine.text()
        self.UnitPrice = self.ui.InPrice.text()
        self.PrescriptionPrice = self.ui.OutPrice.text()
        self.Stock = self.ui.InStock.text()
        self.minStock = self.ui.minStock.text()
        self.maxStock = self.ui.maxStock.text()

    def confirm(self):
        self.getInfo()
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MAX(DrugID) FROM drug")
        drugID = cursor.fetchone()[0] + 1

        insertSql = """
        INSERT INTO drug (DrugID, Name, UnitPrice, PrescriptionPrice, CurrentStock, MinStock, MaxStock)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(insertSql, (drugID, self.drugName, self.UnitPrice, self.PrescriptionPrice,
                                   self.Stock, self.minStock, self.maxStock))

        self.db_connection.commit()
        QMessageBox.information(self, '添加成功', '成功添加药品{}'.format(self.drugName))

        self.close()

class DeleteDrug(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = dd.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.deleteButton.clicked.connect(self.comfirm)
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.getInfo()

    def getInfo(self):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT Name FROM drug
        """
        cursor.execute(selectSql)
        self.ui.comboBox.clear()
        for name in cursor.fetchall():
            self.ui.comboBox.addItem(name[0])
        cursor.close()

    def delete(self, drugName):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT DrugID FROM drug WHERE Name = %s", (drugName,))
        drugId = cursor.fetchone()[0]

        deleteSql = """
        DELETE FROM prescriptiondetail WHERE DrugID = %s
        """
        cursor.execute(deleteSql, (drugId,))
        self.db_connection.commit()

        deleteSql = """
        DELETE FROM drug WHERE Name = %s
        """
        cursor.execute(deleteSql, (drugName,))
        self.db_connection.commit()

        cursor.close()

    def comfirm(self):
        drugName = self.ui.comboBox.currentText()
        self.delete(drugName)
        QMessageBox.information(self, "删除成功", "成功删除药品{}！".format(drugName))
        self.close()

class SetDrugPrice(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = sdp.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comfirmButton.clicked.connect(self.comfirm)
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.getDrugInfo()
        self.updateInfo()
        self.ui.comboBox.currentTextChanged.connect(self.updateInfo)

    def getDrugInfo(self):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT Name FROM drug
        """
        cursor.execute(selectSql)
        self.ui.comboBox.clear()
        for name in cursor.fetchall():
            self.ui.comboBox.addItem(name[0])
        cursor.close()

    def updateInfo(self):
        drugName = self.ui.comboBox.currentText()
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT UnitPrice FROM drug WHERE Name = %s", (drugName,))
        drugUnitPrice = cursor.fetchone()[0]

        cursor.execute("SELECT PrescriptionPrice FROM drug WHERE Name = %s", (drugName,))
        drugPresPrice = cursor.fetchone()[0]

        self.ui.UnitLine.setText(str(drugUnitPrice))
        self.ui.PPLine.setText(str(drugPresPrice))

        cursor.close()

    def comfirm(self):
        cursor = self.db_connection.cursor()
        drugUnitPrice = self.ui.UnitLine.text()
        drugPrepPrice = self.ui.PPLine.text()
        drugName = self.ui.comboBox.currentText()

        updateSql = """
        UPDATE drug SET UnitPrice = %s, PrescriptionPrice = %s
        WHERE Name = %s
        """

        cursor.execute(updateSql, (drugUnitPrice, drugPrepPrice, drugName))
        self.db_connection.commit()
        QMessageBox.information(self, "修改成功", "药品{}的进价与处方价修改成功!".format(drugName))
        cursor.close()
        self.close()

class SetDrugStock(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = sds.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comfirmButton.clicked.connect(self.comfirm)
        self.db_connection = sql.connect(
            host="localhost",
            user="root",
            password="2332341268hth",
            database="medcaredb"
        )
        self.getDrugInfo()
        self.updateInfo()
        self.ui.comboBox.currentTextChanged.connect(self.updateInfo)

    def getDrugInfo(self):
        cursor = self.db_connection.cursor()
        selectSql = """
        SELECT Name FROM drug
        """
        cursor.execute(selectSql)
        self.ui.comboBox.clear()
        for name in cursor.fetchall():
            self.ui.comboBox.addItem(name[0])
        cursor.close()

    def updateInfo(self):
        drugName = self.ui.comboBox.currentText()
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT CurrentStock FROM drug WHERE Name = %s", (drugName,))
        drugCurrentStock = cursor.fetchone()[0]

        cursor.execute("SELECT MinStock FROM drug WHERE Name = %s", (drugName,))
        drugminStock = cursor.fetchone()[0]

        cursor.execute("SELECT MaxStock FROM drug WHERE Name = %s", (drugName,))
        drugmaxStock = cursor.fetchone()[0]

        self.ui.NowStock.setText(str(drugCurrentStock))
        self.ui.minStock.setText(str(drugminStock))
        self.ui.maxStock.setText(str(drugmaxStock))

        cursor.close()

    def comfirm(self):
        cursor = self.db_connection.cursor()
        drugCurrentStock = self.ui.NowStock.text()
        drugminStock = self.ui.minStock.text()
        drugmaxStock = self.ui.maxStock.text()
        drugName = self.ui.comboBox.currentText()

        updateSql = """
                UPDATE drug SET CurrentStock = %s, MinStock = %s, MaxStock = %s
                WHERE Name = %s
                """

        cursor.execute(updateSql, (drugCurrentStock, drugminStock, drugmaxStock, drugName))
        self.db_connection.commit()
        QMessageBox.information(self, "修改成功", "药品{}的库存修改成功!".format(drugName))
        cursor.close()
        self.close()