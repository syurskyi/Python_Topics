______ sys
____ ?.QtSql ______ QSqlDatabase, QSqlQuery, QSqlTableModel
____ ?.QtCore ______ *
____ ?.?W.. ______ *

class MainWindow(QWidget):
    ___ __init__(self, parent_None):
        super(MainWindow, self).__init__(parent)
        self.db _ QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        self.db.open()
        self.model _ QSqlTableModel()
        self.initializedModel()

        self.tableView _ QTableView()
        self.tableView.setModel(self.model)

        self.layout _ QVBoxLayout()
        addButton _ ?PB..("add")
        deleteButton _ ?PB..("delete")
        hLayout _ QHBoxLayout()
        hLayout.addWidget(addButton)
        hLayout.addWidget(deleteButton)
        self.layout.addWidget(self.tableView)
        self.layout.addLayout(hLayout)
        self.setLayout(self.layout)
        self.resize(600, 400)

        addButton.c__.c..(self.onAddRow)
        deleteButton.c__.c..(self.onDeleteRow)

    ___ initializedModel(self):
        self.model.setTable("person")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Address")

    ___ onAddRow(self):
        self.model.insertRows(self.model.rowCount(), 1)
        self.model.submit()

    ___ onDeleteRow(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.model.submit()
        self.model.select()

    ___ closeEvent(self, event):
        self.db.close()

if __name__ == "__main__":
    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())