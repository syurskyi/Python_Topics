______ ___
____ ?.?S.. ______ ?SD.., QSqlQuery, ?STM.., QSqlQueryModel
____ ?.?C.. ______ *
____ ?.?W.. ______ *

c_ DataGrid(QWidget):
    ___ __init__  parent_None):
        super(DataGrid, self).__init__(parent)
        # Database Connection
        self.db _ N..
        # Layout Manager
        self.layout _ ?VBL..
        # Query Model
        self.queryModel _ QSqlQueryModel()
        # Table View
        self.tableView _ QTableView()
        self.tableView.sM..(self.queryModel)
        #
        self.totalPageLabel _ QLabel()
        self.currentPageLabel _ QLabel()
        self.switchPageLineEdit _ ?LE..
        self.prevButton _ ?PB..("Prev")
        self.nextButton _ ?PB..("Next")
        self.switchPageButton _ ?PB..("Switch")
        self.currentPage _ 0
        self.totalPage _ 0
        self.totalRecordCount _ 0
        self.pageRecordCount _ 5

    ___ initUI(self):
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.aW..(self.tableView)

        hLayout _ QHBoxLayout()
        hLayout.aW..(self.prevButton)
        hLayout.aW..(self.nextButton)
        hLayout.aW..(QLabel("Jump To"))
        self.switchPageLineEdit.setFixedWidth(40)
        hLayout.aW..(self.switchPageLineEdit)
        hLayout.aW..(QLabel("page"))
        hLayout.aW..(self.switchPageButton)
        hLayout.aW..(QLabel("Current page:"))
        hLayout.aW..(self.currentPageLabel)
        hLayout.aW..(QLabel("Total pages:"))
        hLayout.aW..(self.totalPageLabel)
        hLayout.addStretch(1)

        self.layout.addLayout(hLayout)
        self.sL..(self.layout)

        self.setWindowTitle("DataGrid")
        self.resize(600, 300)

    ___ closeEvent  event):
        self.db.close()

__ __name__ == "__main__":
    app _ ?A..(___.argv)
    window _ DataGrid()
    window.initUI()
    window.s..
    ___.exit(app.exec_())