______ ___
____ ?.?S.. ______ ?SD.., QSqlQuery, ?STM.., QSqlQueryModel
____ ?.?C.. ______ *
____ ?.?W.. ______ *
______ re

c_ DataGrid(QWidget):
    ___  -   parent_None):
        super(DataGrid, self). - (parent)
        # Declare Database Connections
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
        # Current Page
        currentPage _ 1
        # PageCount
        totalPage _ N..
        # Total Records
        totalRecordCount _ N..
        # Number of records per page
        pageRecordCount _ 4

        initUI()
        initializedModel()
        setUpConnect()
        updateStatus()

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

    ___ setUpConnect 
        prevButton.c__.c..(onPrevPage)
        nextButton.c__.c..(onNextPage)
        switchPageButton.c__.c..(onSwitchPage)

    ___ initializedModel 
        db _ ?SD...aD..("QSQLITE")
        db.sDN..("/home/user/test.db")
        __ no. db.o..
            r_ False
        queryModel.setHeaderData(0, __.Horizontal, "ID")
        queryModel.setHeaderData(1, __.Horizontal, "Name")
        queryModel.setHeaderData(2, __.Horizontal, "Sex")
        queryModel.setHeaderData(3, __.Horizontal, "Age")
        # Get all the records of the table
        sql _ "SELECT * FROM student"
        queryModel.setQuery(sql, db)
        totalRecordCount _ queryModel.rowCount()
        __ totalRecordCount % pageRecordCount == 0:
            totalPage _ totalRecordCount / pageRecordCount
        ____
            totalPage _ int(totalRecordCount / pageRecordCount) + 1
        # Show Page 1
        sql _ "SELECT * FROM student limit %d,%d" % (0, pageRecordCount)
        queryModel.setQuery(sql, db)

    ___ onPrevPage 
        currentPage -_ 1
        limitIndex _ (currentPage - 1) * pageRecordCount
        queryRecord(limitIndex)
        updateStatus()

    ___ onNextPage 
        currentPage +_ 1
        limitIndex _ (currentPage - 1) * pageRecordCount
        queryRecord(limitIndex)
        updateStatus()

    ___ onSwitchPage 
        szText _ switchPageLineEdit.t__()
        pattern _ re.compile('^[0-9]+$')
        match _ pattern.match(szText)
        __ no. match:
            ?MB...information  "Tips", "please enter a number.")
            r_
        __ szText == "":
            ?MB...information  "Tips", "Please enter a jump page.")
            r_
        pageIndex _ int(szText)
        __ pageIndex > totalPage or pageIndex < 1:
            ?MB...information  "Tips", "No page specified, re-enter.")
            r_

        limitIndex _ (pageIndex - 1) * pageRecordCount
        queryRecord(limitIndex)
        currentPage _ pageIndex
        updateStatus()

    # Query records based on paging
    ___ queryRecord  limitIndex):
        sql _ "SELECT * FROM student limit %d,%d" % (limitIndex, pageRecordCount)
        queryModel.setQuery(sql)

    # Update Spatial Status
    ___ updateStatus 
        currentPageLabel.sT..(str(currentPage))
        totalPageLabel.sT..(str(totalPage))
        __ currentPage <_ 1:
            prevButton.setEnabled F..
        ____
            prevButton.setEnabled(True)

        __ currentPage >_ totalPage:
            nextButton.setEnabled F..
        ____
            nextButton.setEnabled(True)

    # Close database connection when interface is closed
    ___ closeEvent  event):
        db.close()

__ __name__ == "__main__":
    app _ ?A..(___.a..
    window _ DataGrid()
    window.s..
    ___.exit(app.exec_())