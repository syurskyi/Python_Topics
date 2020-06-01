______ sys
____ ?.QtSql ______ QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
____ ?.?C.. ______ *
____ ?.?W.. ______ *
______ re

c_ DataGrid(QWidget):
    ___ __init__  parent_None):
        super(DataGrid, self).__init__(parent)
        # Declare Database Connections
        self.db _ N..
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
        self.totalPage _ N..
        # Total Records
        self.totalRecordCount _ N..
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
        __ no. self.db.o..
            r_ False
        self.queryModel.setHeaderData(0, __.Horizontal, "ID")
        self.queryModel.setHeaderData(1, __.Horizontal, "Name")
        self.queryModel.setHeaderData(2, __.Horizontal, "Sex")
        self.queryModel.setHeaderData(3, __.Horizontal, "Age")
        # Get all the records of the table
        sql _ "SELECT * FROM student"
        self.queryModel.setQuery(sql, self.db)
        self.totalRecordCount _ self.queryModel.rowCount()
        __ self.totalRecordCount % self.pageRecordCount == 0:
            self.totalPage _ self.totalRecordCount / self.pageRecordCount
        ____
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
        __ no. match:
            ?MB...information  "Tips", "please enter a number.")
            r_
        __ szText == "":
            ?MB...information  "Tips", "Please enter a jump page.")
            r_
        pageIndex _ int(szText)
        __ pageIndex > self.totalPage or pageIndex < 1:
            ?MB...information  "Tips", "No page specified, re-enter.")
            r_

        limitIndex _ (pageIndex - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.currentPage _ pageIndex
        self.updateStatus()

    # Query records based on paging
    ___ queryRecord  limitIndex):
        sql _ "SELECT * FROM student limit %d,%d" % (limitIndex, self.pageRecordCount)
        self.queryModel.setQuery(sql)

    # Update Spatial Status
    ___ updateStatus(self):
        self.currentPageLabel.sT..(str(self.currentPage))
        self.totalPageLabel.sT..(str(self.totalPage))
        __ self.currentPage <_ 1:
            self.prevButton.setEnabled F..
        ____
            self.prevButton.setEnabled(True)

        __ self.currentPage >_ self.totalPage:
            self.nextButton.setEnabled F..
        ____
            self.nextButton.setEnabled(True)

    # Close database connection when interface is closed
    ___ closeEvent  event):
        self.db.close()

__ __name__ == "__main__":
    app _ ?A..(sys.argv)
    window _ DataGrid()
    window.s..
    sys.exit(app.exec_())