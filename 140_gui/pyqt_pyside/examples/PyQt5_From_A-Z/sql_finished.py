import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from ui_modules.sql_ui import *
from ui_modules.sqlAdd_ui import *


class DlgMain(QDialog, Ui_dlgSql):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setupUi(self)
        self.setLayout(self.lytMain)

        self.lytMain.setStretch(0, 2)
        self.lytMain.setStretch(1, 8)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("data/employees.db")
        if db.open():
            query = QSqlQuery()
            print(db.tables())
            if "employee" not in db.tables():
                sql = """
                    CREATE TABLE IF NOT EXISTS employee (
                        emp_id INTEGER PRIMARY KEY,
                        fname TEXT NOT NULL,
                        lname TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        phone TEXT NOT NULL UNIQUE,
                        position TEXT,
                        supervisor INTEGER
                    )
                """
                query.exec_(sql)
                query.exec_("insert into employee values(101, 'Mike', 'Miller', 'mm@gmail.com', 'x452', 'CEO', 9999)")
                query.exec_("insert into employee values(102, 'Roger', 'Smith', 'rs@gmail.com', 'x645', 'VP-Sales', 101)")
                query.exec_("insert into employee values(103, 'Bill', 'Jones', 'bj@gmail.com', 'x632', 'VP-Marketing', 101)")
                query.exec_("insert into employee values(104, 'Joe', 'Smith', 'js@gmail.com', 'x657', 'PM', 102)")
                query.exec_("insert into employee values(105, 'Fred', 'White', 'fw@gmail.com', 'x275', 'PM', 103)")

            self.populateTable()
        else:
            QMessageBox.critical(self, "Database Error", "Could not open employee database")

        self.btnAdd.clicked.connect(self.evt_btnAdd_clicked)
        self.btnUpdate.clicked.connect(self.evt_btnUpdate_clicked)
        self.btnDelete.clicked.connect(self.evt_btnDelete_clicked)
        self.lstTables.itemDoubleClicked.connect(self.evt_btnUpdate_clicked)

    def populateTable(self):
            query = QSqlQuery()
            bOk = query.exec("SELECT * FROM employee ORDER BY lname, fname")
            if bOk:
                self.lstTables.clear()
                self.tblEmployees.clear()
                self.tblEmployees.setRowCount(0)
                self.tblEmployees.setColumnCount(7)
                self.tblEmployees.setHorizontalHeaderLabels(["ID", "First", "Last", "Email", "Phone", "Position", "Supervisor"])
                self.tblEmployees.setColumnWidth(0, 58)
                self.tblEmployees.setColumnWidth(1, 80)
                self.tblEmployees.setColumnWidth(2, 80)
                self.tblEmployees.setColumnWidth(3, 140)
                self.tblEmployees.setColumnWidth(4, 60)
                self.tblEmployees.setColumnWidth(5, 100)
                self.tblEmployees.setColumnWidth(6, 150)
                self.tblEmployees.setAlternatingRowColors(True)
                while query.next():
                    row = self.tblEmployees.rowCount()
                    self.tblEmployees.insertRow(row)
                    for col in range(6):
                        twi = QTableWidgetItem(str(query.value(col)))
                        if col in [0,6]:
                            twi.setTextAlignment(QtCore.Qt.AlignRight)
                        self.tblEmployees.setItem(row, col, twi)
                    self.tblEmployees.setItem(row, 6, QTableWidgetItem(self.returnEmpName(query.value(6))))
                    sList = "{}. {} : {}".format(query.value('lname'), query.value('fname'), query.value('position'))
                    lwi = QListWidgetItem(sList)
                    lwi.setData(QtCore.Qt.WhatsThisRole, query.value('emp_id'))
                    self.lstTables.addItem(lwi)
                    row += 1
            else:
                QMessageBox.warning(self, "Database Error", "Database error\n\n{}".format(query.lastError().text()))

    def returnEmpName(self, id):
        query=QSqlQuery()
        bOk = query.exec("SELECT fname, lname, position FROM employee WHERE emp_id = {}".format(id))
        if bOk:
            query.next()
            if query.isValid():
                return "{}, {} : {}".format(query.value('lname'), query.value('fname'), query.value('position'))
            else:
                return ""
        else:
            QMessageBox.warning(self, "Database Error", "Database error\n\n{}".format(query.lastError().text()))

    def returnEmployee(self, id):
        query=QSqlQuery()
        bOk = query.exec("SELECT * FROM employee WHERE emp_id = {}".format(id))
        if bOk:
            query.next()
            if query.isValid():
                return query
            else:
                return None
        else:
            QMessageBox.warning(self, "Database Error", "Database error\n\n{}".format(query.lastError().text()))

    def evt_btnAdd_clicked(self):
        dlgAdd = DlgAdd()
        dlgAdd.btnSubmit.clicked.connect(dlgAdd.evt_btnSubmit_clicked)
        dlgAdd.show()
        dlgAdd.exec_()
        self.populateTable()

    def evt_btnUpdate_clicked(self):
        if self.lstTables.currentRow()<0:
            QMessageBox.warning(self, "Warning", "No employee selected\n\nPlease select an employee and try again")
        else:
            dlgUpdate = DlgAdd()

            dlgUpdate.setWindowTitle("Update Existing Record")
            dlgUpdate.btnSubmit.setText("Update Text")
            id = self.lstTables.currentItem().data(QtCore.Qt.WhatsThisRole)
            emp = self.returnEmployee(id)
            dlgUpdate.ledId.setText(str(id))
            dlgUpdate.ledFName.setText(emp.value('fname'))
            dlgUpdate.ledLName.setText(emp.value('lname'))
            dlgUpdate.ledEmail.setText(emp.value('email'))
            dlgUpdate.ledPhone.setText(emp.value('phone'))
            dlgUpdate.ledPosition.setText(emp.value('position'))
            dlgUpdate.cmbSupervisor.setCurrentText(self.returnEmpName(emp.value('supervisor')))
            dlgUpdate.btnSubmit.clicked.connect(dlgUpdate.evt_btnUpdate_clicked)
            dlgUpdate.show()
            dlgUpdate.exec_()
            self.populateTable()

    def evt_btnDelete_clicked(self):
        if self.lstTables.currentRow() < 0:
            QMessageBox.warning(self, "Warning", "No employee selected\n\nPlease select an employee and try again")
        else:
            id = self.lstTables.currentItem().data(QtCore.Qt.WhatsThisRole)
            res = QMessageBox.question(self, "Delete", "Are you sure that you want to delete {}?".format(self.returnEmpName(id)))
            if res == QMessageBox.Yes:
                query = QSqlQuery()
                sSql="DELETE FROM employee WHERE emp_id ={}".format(id)
                print(sSql)
                bOk = query.exec(sSql)
                if bOk:
                    QMessageBox.information(self, "Success!!!", "Record deleted successfully")
                else:
                    QMessageBox.warning(self, "Database Error", "Database error\n\n{}".format(query.lastError().text()))
                self.populateTable()


class DlgAdd(QDialog, Ui_sqlAdd):
    def __init__(self):
        super(DlgAdd, self).__init__()
        self.setupUi(self)
        self.btnSubmit.setFocus()
        self.ledId.setAlignment(QtCore.Qt.AlignRight)

        if not QSqlDatabase.connectionNames():
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("data/employees.db")

        self.ledId.setText(str(self.getId()))
        self.populateSupervisor()

    def populateSupervisor(self):
        query = QSqlQuery()
        bOk = query.exec("SELECT emp_id, fname, lname, position FROM employee ORDER BY lname, fname, position")
        if bOk:
            self.cmbSupervisor.clear()
            self.cmbSupervisor.addItem("NONE", 9999)
            while query.next():
                fn = query.value('fname')
                ln = query.value('lname')
                pos = query.value('position')
                id = query.value('emp_id')

                self.cmbSupervisor.addItem("{}, {} : {}".format(ln, fn, pos), id)
        else:
            QMessageBox.warning(self, "Database Error", "Database error\n\n{}".format(query.lastError().text()))

    def getId(self):
        query = QSqlQuery()
        query.exec("SELECT max(emp_id) AS max FROM employee")
        query.next()
        return query.value('max')+1

    def evt_btnSubmit_clicked(self):
        query = QSqlQuery()
        query.prepare("INSERT into employee VALUES(:id, :fn, :ln, :em, :phn, :pos, :sup)")
        query.bindValue(":id", self.ledId.text())
        query.bindValue(":fn", self.ledFName.text())
        query.bindValue(":ln", self.ledLName.text())
        query.bindValue(":em", self.ledEmail.text())
        query.bindValue(":phn", self.ledPhone.text())
        query.bindValue(":pos", self.ledPosition.text())
        query.bindValue(":sup", self.cmbSupervisor.currentData())
        bOk = query.exec()
        if bOk:
            QMessageBox.information(self, "Success!!!", "Record added successfully")
            self.close()
        else:
            QMessageBox.warning(self, "Database Error", "Database error\n\n{}".format(query.lastError().text()))

    def evt_btnUpdate_clicked(self):
        sSql = "UPDATE employee SET fname='{}', lname='{}', email='{}', phone='{}', position='{}', supervisor={} WHERE emp_id={}".format(fn, ln, em, phn, pos, sup, id)
        query = QSqlQuery()
        query.prepare("UPDATE employee SET fname=:fn, lname=:ln, email=:em, phone=:phn, position=:pos, supervisor=:sup WHERE emp_id=:id")
        query.bindValue(":id", self.ledId.text())
        query.bindValue(":fn", self.ledFName.text())
        query.bindValue(":ln", self.ledLName.text())
        query.bindValue(":em", self.ledEmail.text())
        query.bindValue(":phn", self.ledPhone.text())
        query.bindValue(":pos", self.ledPosition.text())
        query.bindValue(":sup", self.cmbSupervisor.currentData())
        bOk = query.exec()
        if bOk:
            QMessageBox.information(self, "Success!!!", "Record updated successfully")
            self.close()
        else:
            QMessageBox.warning(self, "Database Error", "Database error\n\n{}".format(query.lastError().text()))
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
