______ sys
____ ?.QtSql ______ QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
____ ?.QtCore ______ *
____ ?.?W.. ______ *
______ re

class DataGrid(QWidget):
    ___ __init__(self, parent_None):
        super(DataGrid, self).__init__(parent)
        # Declare Database Connections
        self.db _ None
        # Layout Manager
        self.layout _ QVBoxLayout()
        # Query Model
        self.queryModel _ QSqlQueryModel()
        # Table View
        self.tableView _ QTableView()
        self.tableView.setModel(self.queryModel)
        #
        self.totalPageLabel _ QLabel()
        self.currentPageLabel _ QLabel()
        self.switchPageLineEdit _ QLineEdit()
        self.prevButton _ ?PB..("Prev")
        self.nextButton _ ?PB..("Next")
        self.switchPageButton _ ?PB..("Switch")
        # Current Page
        self.currentPage _ 1
        # PageCount
        self.totalPage _ None
        # Total Records
        self.totalRecordCount _ None
        # Number of records per page
        self.pageRecordCount _ 4

        self.initUI()
        self.initializedModel()
        self.setUpConnect()
        self.updateStatus()

    ___ initUI(self):
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.tableView)

        hLayout _ QHBoxLayout()
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

    ___ setUpConnect(self):
        self.prevButton.c__.c..(self.onPrevPage)
        self.nextButton.c__.c..(self.onNextPage)
        self.switchPageButton.c__.c..(self.onSwitchPage)

    ___ initializedModel(self):
        self.db _ QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("/home/user/test.db")
        if not self.db.open
            return False
        self.queryModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "Name")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "Sex")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "Age")
        # Get all the records of the table
        sql _ "SELECT * FROM student"
        self.queryModel.setQuery(sql, self.db)
        self.totalRecordCount _ self.queryModel.rowCount()
        if self.totalRecordCount % self.pageRecordCount == 0:
            self.totalPage _ self.totalRecordCount / self.pageRecordCount
        else:
            self.totalPage _ int(self.totalRecordCount / self.pageRecordCount) + 1
        # Show Page 1
        sql _ "SELECT * FROM student limit %d,%d" % (0, self.pageRecordCount)
        self.queryModel.setQuery(sql, self.db)

    ___ onPrevPage(self):
        self.currentPage -_ 1
        limitIndex _ (self.currentPage - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.updateStatus()

    ___ onNextPage(self):
        self.currentPage +_ 1
        limitIndex _ (self.currentPage - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.updateStatus()

    ___ onSwitchPage(self):
        szText _ self.switchPageLineEdit.text()
        pattern _ re.compile('^[0-9]+$')
        match _ pattern.match(szText)
        if not match:
            QMessageBox.information(self, "Tips", "please enter a number.")
            return
        if szText == "":
            QMessageBox.information(self, "Tips", "Please enter a jump page.")
            return
        pageIndex _ int(szText)
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "Tips", "No page specified, re-enter.")
            return

        limitIndex _ (pageIndex - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.currentPage _ pageIndex
        self.updateStatus()

    # Query records based on paging
    ___ queryRecord(self, limitIndex):
        sql _ "SELECT * FROM student limit %d,%d" % (limitIndex, self.pageRecordCount)
        self.queryModel.setQuery(sql)

    # Update Spatial Status
    ___ updateStatus(self):
        self.currentPageLabel.sT..(str(self.currentPage))
        self.totalPageLabel.sT..(str(self.totalPage))
        if self.currentPage <_ 1:
            self.prevButton.setEnabled(False)
        else:
            self.prevButton.setEnabled(True)

        if self.currentPage >_ self.totalPage:
            self.nextButton.setEnabled(False)
        else:
            self.nextButton.setEnabled(True)

    # Close database connection when interface is closed
    ___ closeEvent(self, event):
        self.db.close()

if __name__ == "__main__":
    app _ ?A..(sys.argv)
    window _ DataGrid()
    window.s..
    sys.exit(app.exec_())