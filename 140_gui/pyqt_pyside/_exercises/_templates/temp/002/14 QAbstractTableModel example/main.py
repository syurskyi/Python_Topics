____ ?.?W.. ______ *
____ ?.QtCore ______ *

headers _ ["Scientist name", "Birthdate", "Contribution"]
rows _ [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]

class TableModel(QAbstractTableModel):
    ___ rowCount(self, parent):
        return len(rows)
    ___ columnCount(self, parent):
        return len(headers)
    ___ data(self, index, role):
        if role !_ Qt.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]
    ___ headerData(self, section, orientation, role):
        if role !_ Qt.DisplayRole or orientation !_ Qt.Horizontal:
            return QVariant()
        return headers[section]

app _ ?
model _ TableModel()
view _ QTableView()
view.setModel(model)
view.s..
app.e..