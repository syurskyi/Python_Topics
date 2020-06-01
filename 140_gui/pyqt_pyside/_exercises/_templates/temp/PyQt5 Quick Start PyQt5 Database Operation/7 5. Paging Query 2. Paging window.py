______ sys
____ ?.QtSql ______ QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
____ ?.QtCore ______ *
____ ?.?W.. ______ *

class DataGrid(QWidget):
    ___ __init__(self, parent_None):
        super(DataGrid, self).__init__(parent)
        # Database Connection
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
        self.currentPage _ 0
        self.totalPage _ 0
        self.totalRecordCount _ 0
        self.pageRecordCount _ 5

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

    ___ closeEvent(self, event):
        self.db.close()

if __name__ == "__main__":
    app _ QApplication(sys.argv)
    window _ DataGrid()
    window.initUI()
    window.s..
    sys.exit(app.exec_())