____ ?.?W.. ______ *
____ ?.QtCore ______ *

headers _ ["Scientist name", "Birthdate", "Contribution"]
rows _ [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]

c_ TableModel(QAbstractTableModel):
    ___ rowCount  parent):
        r_ len(rows)
    ___ columnCount  parent):
        r_ len(headers)
    ___ data  index, role):
        __ role !_ Qt.DisplayRole:
            r_ QVariant()
        r_ rows[index.row()][index.column()]
    ___ headerData  section, orientation, role):
        __ role !_ Qt.DisplayRole or orientation !_ Qt.Horizontal:
            r_ QVariant()
        r_ headers[section]

app _ ?
model _ TableModel()
view _ QTableView()
view.setModel(model)
view.s..
app.e..