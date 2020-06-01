______ ___
____ ?.?S.. ______ ?SD.., QSqlQuery, ?STM.., QSqlQueryModel
____ ?.?C.. ______ *
____ ?.?W.. ______ *

c_ DataGrid(QWidget):
    ___  -   parent_None):
        super(DataGrid, self). - (parent)
        # Database Connection
        db _ N..
        # Layout Manager
        layout _ ?VBL..
        # Query Model
        queryModel _ QSqlQueryModel()
        # Table View
        tableView _ QTableView()
        tableView.sM..(queryModel)
        #
        totalPageLabel _ QLabel()
        currentPageLabel _ QLabel()
        switchPageLineEdit _ ?LE..
        prevButton _ ?PB..("Prev")
        nextButton _ ?PB..("Next")
        switchPageButton _ ?PB..("Switch")
        currentPage _ 0
        totalPage _ 0
        totalRecordCount _ 0
        pageRecordCount _ 5

    ___ initUI 
        tableView.horizontalHeader().setStretchLastSection(True)
        tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.aW..(tableView)

        hLayout _ QHBoxLayout()
        hLayout.aW..(prevButton)
        hLayout.aW..(nextButton)
        hLayout.aW..(QLabel("Jump To"))
        switchPageLineEdit.setFixedWidth(40)
        hLayout.aW..(switchPageLineEdit)
        hLayout.aW..(QLabel("page"))
        hLayout.aW..(switchPageButton)
        hLayout.aW..(QLabel("Current page:"))
        hLayout.aW..(currentPageLabel)
        hLayout.aW..(QLabel("Total pages:"))
        hLayout.aW..(totalPageLabel)
        hLayout.addStretch(1)

        layout.aL..(hLayout)
        sL..(layout)

        setWindowTitle("DataGrid")
        resize(600, 300)

    ___ closeEvent  event):
        db.close()

__ __name__ == "__main__":
    app _ ?A..(___.a..
    window _ DataGrid()
    window.initUI()
    window.s..
    ___.exit(app.exec_())