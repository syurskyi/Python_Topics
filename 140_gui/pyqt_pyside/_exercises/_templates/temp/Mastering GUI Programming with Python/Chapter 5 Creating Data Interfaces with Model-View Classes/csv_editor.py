# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?C.. __ qtc
#
# ______ csv
#
#
# c_ CsvTableModel ?.?ATM..
#     """The model for a CSV table."""
#
#     ___  -   csv_file
#         s_. -
#         filename _ ?
#         w__ o.. ? __ fh
#             csvreader _ csv.reader ?
#             _headers _ n__ ?
#             _data _ li.. ?
#
#     # Minimum necessary methods:
#     ___ rowCount  parent
#         r_ le. _d..
#
#     ___ columnCount  parent
#         r_ le. _h..
#
#     ___ data  index role
#         # original if statement:
#         # if role == qtc.Qt.DisplayRole:
#         # Add EditRole so that the cell is not cleared when editing
#         __ role __ ?.__.DR.. ?.__.ER..
#             r_ _d..|i__.r.. i__.c..
#
#     # Additional features methods:
#
#     ___ hD..  section orientation role
#
#         __ orientation __ ?.__.H.. an. r.. __ ?.__.DR..
#             r_ _h..|s..
#         ____
#             r_ s_.hD.. s.. o.. r..
#
#     ___ s..  column, order
#         layoutAboutToBeChanged.e..  # needs to be emitted before a sort
#         _d__.s.. k_l.. x ?|c..
#         __ o.. __ ?.__.DO..
#             _d__.r..
#         lC__.e..  # needs to be emitted after a sort
#
#     # Methods for Read/Write
#
#     ___ flags  index
#         r_ s_.f.. ? | ?.__.IIE..
#
#     ___ setData  index value role
#         __ i__.iV.. an. r.. __ ?.__.ER..
#             _d..|i__.r.. i__.c.. _ v..
#             dC__.e.. i.. i.. |r..
#             r_ T..
#         ____
#             r_ F..
#
#     # Methods for inserting or deleting
#
#     ___ insertRows  position rows parent
#         beginInsertRows
#             pa.. o. ?.?MI..
#             po..
#             po.. + r.. - 1
#
#
#         ___ i __ ra.. r..
#             default_row _  '' * le. _h..
#             _d__.i.. p.. d_r..
#         eIR...
#
#     ___ removeRows  position rows parent
#         beginRemoveRows(
#             pa.. o. ?.?MI..
#             po..
#             po.. + r.. - 1
#         )
#         ___ i __ ra.. r..
#             de. _d..|p..
#         eRR..
#
#     # method for saving
#     ___ save_data
#         w__ o.. f.. _ e.._ utf-8 __ fh
#             writer _ ___.w.. ?
#             ?.w_r. ._h..
#             ?.w_r.. _d..
#
#
# c_ MainWindow ?.?MW..
#
#     model _ N..
#
#     ___  -
#         """MainWindow constructor.
#
#         This widget will be our main window.
#         We'll define all the UI components in here.
#         """
#         s_. -
#         # Main UI code goes here
#
#         tableview _ qtw.?TV..
#         ?.sSE.. st.
#         sCW.. ?
#
#         # Setup the menu
#         menu _ mB..
#         file_menu _ m__.aM.. File
#         ?.aA.. Open s_f..
#         ?.aA.. Save s_f..
#
#         edit_menu _ menu.aM..('Edit')
#         ?.aA.. Insert Above i_a..
#         ?.aA.. Insert Below i_b..
#         ?.aA.. Remove Row(s) r_r..
#
#         # End main UI code
#         s..
#
#     # File methods
#     ___ select_file
#         filename, _ _ ?.?FD...gOFN..(
#
#             'Select a CSV file to open…',
#             ?.?D.hP..
#             'CSV Files (*.csv) ;; All Files (*)'
#         )
#         __ filename
#             model _ CTM.. f..
#             t__.sM.. ?
#
#     ___ save_file
#         __ model:
#             model.save_data()
#
#     # Methods for insert/remove
#
#     ___ insert_above
#         selected _ tableview.sI..
#         row _ ? 0 .r.. __ ? ____ 0
#         m__.iR.. ? 1, N..
#
#     ___ insert_below
#         selected _ t__.sI..
#         row _ ? -1 .r.. __ ? ____ m__.rC.. N..
#         m__.iR.. ? + 1, 1, N..
#
#     ___ remove_rows
#         selected _ t__.sI..
#         __ ?
#             m__.rR.. ? 0 .r.. le. ? N..
#
#
# __ ______ __ ______
#     app _ qtw.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
