import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        self.db.open()
        self.model = QSqlTableModel()
        self.initializedModel()

        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        self.layout = QVBoxLayout()
        addButton = QPushButton("add")
        deleteButton = QPushButton("delete")
        hLayout = QHBoxLayout()
        hLayout.addWidget(addButton)
        hLayout.addWidget(deleteButton)
        self.layout.addWidget(self.tableView)
        self.layout.addLayout(hLayout)
        self.setLayout(self.layout)
        self.resize(600, 400)

        addButton.clicked.connect(self.onAddRow)
        deleteButton.clicked.connect(self.onDeleteRow)

    def initializedModel(self):
        self.model.setTable("person")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Address")

    def onAddRow(self):
        self.model.insertRows(self.model.rowCount(), 1)
        self.model.submit()

    def onDeleteRow(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.model.submit()
        self.model.select()

    def closeEvent(self, event):
        self.db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())