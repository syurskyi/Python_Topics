____ ?.QtWidgets ______ *
____ ?.?C.. ______ *

headers = ["Scientist name", "Birthdate", "Contribution"]
rows = [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]

c_ TableModel(QAbstractTableModel):
    ___ rowCount(self, parent):
        return len(rows)
    ___ columnCount(self, parent):
        return len(headers)
    ___ data(self, index, role):
        if role != __.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]
    ___ headerData(self, section, orientation, role):
        if role != __.DisplayRole or orientation != __.Horizontal:
            return QVariant()
        return headers[section]

app = ?A..([])
model = TableModel()
view = QTableView()
view.sM..(model)
view.s..
app.exec_()