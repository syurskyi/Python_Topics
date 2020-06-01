import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class DataGrid(QWidget):
    def __init__(self, parent=None):
        super(DataGrid, self).__init__(parent)
        # Database Connection
        self.db = None
        # Layout Manager
        self.layout = QVBoxLayout()
        # Query Model
        self.queryModel = QSqlQueryModel()
        # Table View
        self.tableView = QTableView()
        self.tableView.setModel(self.queryModel)
        #
        self.totalPageLabel = QLabel()
        self.currentPageLabel = QLabel()
        self.switchPageLineEdit = QLineEdit()
        self.prevButton = QPushButton("Prev")
        self.nextButton = QPushButton("Next")
        self.switchPageButton = QPushButton("Switch")
        self.currentPage = 0
        self.totalPage = 0
        self.totalRecordCount = 0
        self.pageRecordCount = 5

    def initUI(self):
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.tableView)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.prevButton)
        hLayout.addWidget(self.nextButton)
        hLayout.addWidget(QLabel("Jump To"))
        self.switchPageLineEdit.setFixedWidth(40)
        hLayout.addWidget(self.switchPageLineEdit)
        hLayout.addWidget(QLabel("page"))
        hLayout.addWidget(self.switchPageButton)
        hLayout.addWidget(QLabel("Current page:"))
        hLayout.addWidget(self.currentPageLabel)
        hLayout.addWidget(QLabel("Total pages:"))
        hLayout.addWidget(self.totalPageLabel)
        hLayout.addStretch(1)

        self.layout.addLayout(hLayout)
        self.setLayout(self.layout)

        self.setWindowTitle("DataGrid")
        self.resize(600, 300)

    def closeEvent(self, event):
        self.db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataGrid()
    window.initUI()
    window.show()
    sys.exit(app.exec_())