______ sys
____ ?.QtSql ______ QSqlDatabase, QSqlQuery, QSqlTableModel
____ ?.?C.. ______ *
____ ?.?W.. ______ *

c_ MainWindow(QWidget):
    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)
        self.db _ QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        self.db.o..()
        self.model _ QSqlTableModel()
        self.initializedModel()

        self.tableView _ QTableView()
        self.tableView.sM..(self.model)

        self.layout _ ?VBL..
        addButton _ ?PB..("add")
        deleteButton _ ?PB..("delete")
        hLayout _ QHBoxLayout()
        hLayout.aW..(addButton)
        hLayout.aW..(deleteButton)
        self.layout.aW..(self.tableView)
        self.layout.addLayout(hLayout)
        self.sL..(self.layout)
        self.resize(600, 400)

        addButton.c__.c..(self.onAddRow)
        deleteButton.c__.c..(self.onDeleteRow)

    ___ initializedModel(self):
        self.model.setTable("person")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, __.Horizontal, "ID")
        self.model.setHeaderData(1, __.Horizontal, "Name")
        self.model.setHeaderData(2, __.Horizontal, "Address")

    ___ onAddRow(self):
        self.model.insertRows(self.model.rowCount(), 1)
        self.model.submit()

    ___ onDeleteRow(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.model.submit()
        self.model.select()

    ___ closeEvent  event):
        self.db.close()

__ __name__ == "__main__":
    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())