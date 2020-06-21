import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import re

class DataGrid(QWidget):
    def __init__(self, parent=None):
        super(DataGrid, self).__init__(parent)
        # Declare Database Connections
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
        # Current Page
        self.currentPage = 1
        # PageCount
        self.totalPage = None
        # Total Records
        self.totalRecordCount = None
        # Number of records per page
        self.pageRecordCount = 4

        self.initUI()
        self.initializedModel()
        self.setUpConnect()
        self.updateStatus()

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

    def setUpConnect(self):
        self.prevButton.clicked.connect(self.onPrevPage)
        self.nextButton.clicked.connect(self.onNextPage)
        self.switchPageButton.clicked.connect(self.onSwitchPage)

    def initializedModel(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("/home/user/test.db")
        if not self.db.open():
            return False
        self.queryModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "Name")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "Sex")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "Age")
        # Get all the records of the table
        sql = "SELECT * FROM student"
        self.queryModel.setQuery(sql, self.db)
        self.totalRecordCount = self.queryModel.rowCount()
        if self.totalRecordCount % self.pageRecordCount == 0:
            self.totalPage = self.totalRecordCount / self.pageRecordCount
        else:
            self.totalPage = int(self.totalRecordCount / self.pageRecordCount) + 1
        # Show Page 1
        sql = "SELECT * FROM student limit %d,%d" % (0, self.pageRecordCount)
        self.queryModel.setQuery(sql, self.db)

    def onPrevPage(self):
        self.currentPage -= 1
        limitIndex = (self.currentPage - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.updateStatus()

    def onNextPage(self):
        self.currentPage += 1
        limitIndex = (self.currentPage - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.updateStatus()

    def onSwitchPage(self):
        szText = self.switchPageLineEdit.text()
        pattern = re.compile('^[0-9]+$')
        match = pattern.match(szText)
        if not match:
            QMessageBox.information(self, "Tips", "please enter a number.")
            return
        if szText == "":
            QMessageBox.information(self, "Tips", "Please enter a jump page.")
            return
        pageIndex = int(szText)
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "Tips", "No page specified, re-enter.")
            return

        limitIndex = (pageIndex - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.currentPage = pageIndex
        self.updateStatus()

    # Query records based on paging
    def queryRecord(self, limitIndex):
        sql = "SELECT * FROM student limit %d,%d" % (limitIndex, self.pageRecordCount)
        self.queryModel.setQuery(sql)

    # Update Spatial Status
    def updateStatus(self):
        self.currentPageLabel.setText(str(self.currentPage))
        self.totalPageLabel.setText(str(self.totalPage))
        if self.currentPage <= 1:
            self.prevButton.setEnabled(False)
        else:
            self.prevButton.setEnabled(True)

        if self.currentPage >= self.totalPage:
            self.nextButton.setEnabled(False)
        else:
            self.nextButton.setEnabled(True)

    # Close database connection when interface is closed
    def closeEvent(self, event):
        self.db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataGrid()
    window.show()
    sys.exit(app.exec_())