______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtCore as qtc

______ csv


class CsvTableModel(qtc.QAbstractTableModel):
    """The model for a CSV table."""

    ___ __init__(self, csv_file):
        super().__init__()
        self.filename _ csv_file
        with open(self.filename) as fh:
            csvreader _ csv.reader(fh)
            self._headers _ next(csvreader)
            self._data _ list(csvreader)

    # Minimum necessary methods:
    ___ rowCount(self, parent):
        return len(self._data)

    ___ columnCount(self, parent):
        return len(self._headers)

    ___ data(self, index, role):
        # original if statement:
        # if role == qtc.Qt.DisplayRole:
        # Add EditRole so that the cell is not cleared when editing
        if role in (qtc.Qt.DisplayRole, qtc.Qt.EditRole):
            return self._data[index.row()][index.column()]

    # Additional features methods:

    ___ headerData(self, section, orientation, role):

        if orientation == qtc.Qt.Horizontal and role == qtc.Qt.DisplayRole:
            return self._headers[section]
        else:
            return super().headerData(section, orientation, role)

    ___ sort(self, column, order):
        self.layoutAboutToBeChanged.emit()  # needs to be emitted before a sort
        self._data.sort(key_lambda x: x[column])
        if order == qtc.Qt.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()  # needs to be emitted after a sort

    # Methods for Read/Write

    ___ flags(self, index):
        return super().flags(index) | qtc.Qt.ItemIsEditable

    ___ setData(self, index, value, role):
        if index.isValid() and role == qtc.Qt.EditRole:
            self._data[index.row()][index.column()] _ value
            self.dataChanged.emit(index, index, [role])
            return True
        else:
            return False

    # Methods for inserting or deleting

    ___ insertRows(self, position, rows, parent):
        self.beginInsertRows(
            parent or qtc.QModelIndex(),
            position,
            position + rows - 1
        )

        for i in range(rows):
            default_row _ [''] * len(self._headers)
            self._data.insert(position, default_row)
        self.endInsertRows()

    ___ removeRows(self, position, rows, parent):
        self.beginRemoveRows(
            parent or qtc.QModelIndex(),
            position,
            position + rows - 1
        )
        for i in range(rows):
            del(self._data[position])
        self.endRemoveRows()

    # method for saving
    ___ save_data(self):
        with open(self.filename, 'w', encoding_'utf-8') as fh:
            writer _ csv.writer(fh)
            writer.writerow(self._headers)
            writer.writerows(self._data)


class MainWindow(qtw.QMainWindow):

    model _ None

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        self.tableview _ qtw.QTableView()
        self.tableview.setSortingEnabled(True)
        self.setCentralWidget(self.tableview)

        # Setup the menu
        menu _ self.menuBar()
        file_menu _ menu.addMenu('File')
        file_menu.addAction('Open', self.select_file)
        file_menu.addAction('Save', self.save_file)

        edit_menu _ menu.addMenu('Edit')
        edit_menu.addAction('Insert Above', self.insert_above)
        edit_menu.addAction('Insert Below', self.insert_below)
        edit_menu.addAction('Remove Row(s)', self.remove_rows)

        # End main UI code
        self.s..

    # File methods
    ___ select_file(self):
        filename, _ _ qtw.QFileDialog.getOpenFileName(
            self,
            'Select a CSV file to open…',
            qtc.QDir.homePath(),
            'CSV Files (*.csv) ;; All Files (*)'
        )
        if filename:
            self.model _ CsvTableModel(filename)
            self.tableview.setModel(self.model)

    ___ save_file(self):
        if self.model:
            self.model.save_data()

    # Methods for insert/remove

    ___ insert_above(self):
        selected _ self.tableview.selectedIndexes()
        row _ selected[0].row() if selected else 0
        self.model.insertRows(row, 1, None)

    ___ insert_below(self):
        selected _ self.tableview.selectedIndexes()
        row _ selected[-1].row() if selected else self.model.rowCount(None)
        self.model.insertRows(row + 1, 1, None)

    ___ remove_rows(self):
        selected _ self.tableview.selectedIndexes()
        if selected:
            self.model.removeRows(selected[0].row(), len(selected), None)


if __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
