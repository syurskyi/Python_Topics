# ______ ___
# ____ ?.?S.. ______ ?SD.., ?SQ.., ?STM.., QSqlQueryModel
# ____ ?.?C.. ______ *
# ____ ?.?W.. ______ *
# ______ re
#
# c_ DataGrid(?W..):
#     ___  -   parent_None):
#         s__(DataGrid, self). - (parent)
#         # Declare Database Connections
#         db _ N..
#         # Layout Manager
#         layout _ ?VBL..
#         # Query Model
#         queryModel _ QSqlQueryModel()
#         # Table View
#         tableView _ ?TV..
#         tableView.sM..(queryModel)
#         #
#         totalPageLabel _ ?L..
#         currentPageLabel _ ?L..
#         switchPageLineEdit _ ?LE..
#         prevButton _ ?PB..("Prev")
#         nextButton _ ?PB..("Next")
#         switchPageButton _ ?PB..("Switch")
#         # Current Page
#         currentPage _ 1
#         # PageCount
#         totalPage _ N..
#         # Total Records
#         totalRecordCount _ N..
#         # Number of records per page
#         pageRecordCount _ 4
#
#         initUI()
#         initializedModel()
#         setUpConnect()
#         updateStatus()
#
#     ___ initUI
#         tableView.hH.. .setStretchLastSection( st.
#         tableView.hH.. .sSRM..(?HV...Stretch)
#         layout.aW..(tableView)
#
#         hLayout _ ?HBL..
#         hLayout.aW..(prevButton)
#         hLayout.aW..(nextButton)
#         hLayout.aW..(QLabel("Jump To"))
#         switchPageLineEdit.setFixedWidth(40)
#         hLayout.aW..(switchPageLineEdit)
#         hLayout.aW..(QLabel("page"))
#         hLayout.aW..(switchPageButton)
#         hLayout.aW..(QLabel("Current page:"))
#         hLayout.aW..(currentPageLabel)
#         hLayout.aW..(QLabel("Total pages:"))
#         hLayout.aW..(totalPageLabel)
#         hLayout.addStretch(1)
#
#         layout.aL..(hLayout)
#         sL..(layout)
#
#         sWT..("DataGrid")
#         r..(600, 300)
#
#     ___ setUpConnect
#         prevButton.c__.c..(onPrevPage)
#         nextButton.c__.c..(onNextPage)
#         switchPageButton.c__.c..(onSwitchPage)
#
#     ___ initializedModel
#         db _ ?SD...aD..("QSQLITE")
#         db.sDN..("/home/user/test.db")
#         __ no. db.o..
#             r_ F..
#         queryModel.setHeaderData(0, __.H.., "ID")
#         queryModel.setHeaderData(1, __.H.., "Name")
#         queryModel.setHeaderData(2, __.H.., "Sex")
#         queryModel.setHeaderData(3, __.H.., "Age")
#         # Get all the records of the table
#         sql _ "SELECT * FROM student"
#         queryModel.setQuery(sql, db)
#         totalRecordCount _ queryModel.rowCount()
#         __ totalRecordCount % pageRecordCount __ 0:
#             totalPage _ totalRecordCount / pageRecordCount
#         ____
#             totalPage _ int(totalRecordCount / pageRecordCount) + 1
#         # Show Page 1
#         sql _ "SELECT * FROM student limit %d,%d" % (0, pageRecordCount)
#         queryModel.setQuery(sql, db)
#
#     ___ onPrevPage
#         currentPage -_ 1
#         limitIndex _ (currentPage - 1) * pageRecordCount
#         queryRecord(limitIndex)
#         updateStatus()
#
#     ___ onNextPage
#         currentPage +_ 1
#         limitIndex _ (currentPage - 1) * pageRecordCount
#         queryRecord(limitIndex)
#         updateStatus()
#
#     ___ onSwitchPage
#         szText _ switchPageLineEdit.t__()
#         pattern _ re.compile('^[0-9]+$')
#         match _ pattern.match(szText)
#         __ no. match:
#             ?MB...information  "Tips", "please enter a number.")
#             r_
#         __ szText __ "":
#             ?MB...information  "Tips", "Please enter a jump page.")
#             r_
#         pageIndex _ int(szText)
#         __ pageIndex > totalPage or pageIndex < 1:
#             ?MB...information  "Tips", "No page specified, re-enter.")
#             r_
#
#         limitIndex _ (pageIndex - 1) * pageRecordCount
#         queryRecord(limitIndex)
#         currentPage _ pageIndex
#         updateStatus()
#
#     # Query records based on paging
#     ___ queryRecord  limitIndex):
#         sql _ "SELECT * FROM student limit %d,%d" % (limitIndex, pageRecordCount)
#         queryModel.setQuery(sql)
#
#     # Update Spatial Status
#     ___ updateStatus
#         currentPageLabel.sT..(st.(currentPage))
#         totalPageLabel.sT..(st.(totalPage))
#         __ currentPage <_ 1:
#             prevButton.sE.. F..
#         ____
#             prevButton.sE..( st.
#
#         __ currentPage >_ totalPage:
#             nextButton.sE.. F..
#         ____
#             nextButton.sE..( st.
#
#     # Close database connection when interface is closed
#     ___ closeEvent  event):
#         db.c..
#
# __ __name__ __ "__main__":
#     app _ ?A..(___.a..
#     window _ DataGrid()
#     window.s..
#     ___.e.. ?.e..