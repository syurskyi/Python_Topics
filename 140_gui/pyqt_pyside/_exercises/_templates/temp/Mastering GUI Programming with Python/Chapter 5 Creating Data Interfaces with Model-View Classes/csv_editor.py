______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc

______ csv


c_ CsvTableModel(qtc.QAbstractTableModel):
    """The model for a CSV table."""

    ___ __init__  csv_file):
        super().__init__()
        self.filename _ csv_file
        w__ o..(self.filename) __ fh:
            csvreader _ csv.reader(fh)
            self._headers _ next(csvreader)
            self._data _ list(csvreader)

    # Minimum necessary methods:
    ___ rowCount  parent):
        r_ len(self._data)

    ___ columnCount  parent):
        r_ len(self._headers)

    ___ data  index, role):
        # original if statement:
        # if role == qtc.Qt.DisplayRole:
        # Add EditRole so that the cell is not cleared when editing
        __ role in (qtc.__.DisplayRole, qtc.__.EditRole):
            r_ self._data[index.row()][index.column()]

    # Additional features methods:

    ___ headerData  section, orientation, role):

        __ orientation == qtc.__.Horizontal and role == qtc.__.DisplayRole:
            r_ self._headers[section]
        ____
            r_ super().headerData(section, orientation, role)

    ___ sort  column, order):
        self.layoutAboutToBeChanged.emit()  # needs to be emitted before a sort
        self._data.sort(key_lambda x: x[column])
        __ order == qtc.__.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()  # needs to be emitted after a sort

    # Methods for Read/Write

    ___ flags  index):
        r_ super().flags(index) | qtc.__.ItemIsEditable

    ___ setData  index, value, role):
        __ index.isValid() and role == qtc.__.EditRole:
            self._data[index.row()][index.column()] _ value
            self.dataChanged.emit(index, index, [role])
            r_ True
        ____
            r_ False

    # Methods for inserting or deleting

    ___ insertRows  position, rows, parent):
        self.beginInsertRows(
            parent or qtc.QModelIndex(),
            position,
            position + rows - 1
        )

        for i in range(rows):
            default_row _ [''] * len(self._headers)
            self._data.insert(position, default_row)
        self.endInsertRows()

    ___ removeRows  position, rows, parent):
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
        w__ o..(self.filename, 'w', encoding_'utf-8') __ fh:
            writer _ csv.writer(fh)
            writer.writerow(self._headers)
            writer.writerows(self._data)


c_ MainWindow(qtw.QMainWindow):

    model _ N..

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        self.tableview _ qtw.QTableView()
        self.tableview.setSortingEnabled(True)
        self.sCW..(self.tableview)

        # Setup the menu
        menu _ self.mB..
        file_menu _ menu.aM..('File')
        file_menu.aA..('Open', self.select_file)
        file_menu.aA..('Save', self.save_file)

        edit_menu _ menu.aM..('Edit')
        edit_menu.aA..('Insert Above', self.insert_above)
        edit_menu.aA..('Insert Below', self.insert_below)
        edit_menu.aA..('Remove Row(s)', self.remove_rows)

        # End main UI code
        self.s..

    # File methods
    ___ select_file(self):
        filename, _ _ qtw.?FD...gOFN..(
            self,
            'Select a CSV file to open…',
            qtc.QDir.homePath(),
            'CSV Files (*.csv) ;; All Files (*)'
        )
        __ filename:
            self.model _ CsvTableModel(filename)
            self.tableview.setModel(self.model)

    ___ save_file(self):
        __ self.model:
            self.model.save_data()

    # Methods for insert/remove

    ___ insert_above(self):
        selected _ self.tableview.selectedIndexes()
        row _ selected[0].row() __ selected else 0
        self.model.insertRows(row, 1, N..)

    ___ insert_below(self):
        selected _ self.tableview.selectedIndexes()
        row _ selected[-1].row() __ selected else self.model.rowCount(N..)
        self.model.insertRows(row + 1, 1, N..)

    ___ remove_rows(self):
        selected _ self.tableview.selectedIndexes()
        __ selected:
            self.model.removeRows(selected[0].row(), len(selected), N..)


__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
