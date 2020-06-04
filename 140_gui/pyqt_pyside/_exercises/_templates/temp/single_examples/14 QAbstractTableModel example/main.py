____ ?.QtWidgets ______ *
____ ?.?C.. ______ *

headers _ ["Scientist name", "Birthdate", "Contribution"]
rows _ [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]

c_ TableModel(QAbstractTableModel):
    ___ rowCount  parent):
        r_ le.(rows)
    ___ columnCount  parent):
        r_ le.(headers)
    ___ data  index, role):
        __ role !_ __.DisplayRole:
            r_ QVariant()
        r_ rows[i...row()][i...column()]
    ___ headerData  section, orientation, role):
        __ role !_ __.DisplayRole or orientation !_ __.Horizontal:
            r_ QVariant()
        r_ headers[section]

app _ ?A..([])
model _ TableModel()
view _ QTableView()
view.sM..(model)
view.s..
app.exec_()