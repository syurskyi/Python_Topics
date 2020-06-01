______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc

______ csv


c_ CsvTableModel(qtc.QAbstractTableModel):
    """The model for a CSV table."""

    ___  -   csv_file):
        s_. - ()
        filename _ csv_file
        w__ o..(filename) __ fh:
            csvreader _ csv.reader(fh)
            _headers _ next(csvreader)
            _data _ list(csvreader)

    # Minimum necessary methods:
    ___ rowCount  parent):
        r_ le.(_data)

    ___ columnCount  parent):
        r_ le.(_headers)

    ___ data  index, role):
        # original if statement:
        # if role == qtc.Qt.DisplayRole:
        # Add EditRole so that the cell is not cleared when editing
        __ role __ (qtc.__.DisplayRole, qtc.__.EditRole):
            r_ _data[index.row()][index.column()]

    # Additional features methods:

    ___ headerData  section, orientation, role):

        __ orientation == qtc.__.Horizontal and role == qtc.__.DisplayRole:
            r_ _headers[section]
        ____
            r_ s_.headerData(section, orientation, role)

    ___ sort  column, order):
        layoutAboutToBeChanged.e..()  # needs to be emitted before a sort
        _data.sort(key_lambda x: x[column])
        __ order == qtc.__.DescendingOrder:
            _data.reverse()
        layoutChanged.e..()  # needs to be emitted after a sort

    # Methods for Read/Write

    ___ flags  index):
        r_ s_.flags(index) | qtc.__.ItemIsEditable

    ___ setData  index, value, role):
        __ index.isValid() and role == qtc.__.EditRole:
            _data[index.row()][index.column()] _ value
            dataChanged.e..(index, index, [role])
            r_ True
        ____
            r_ False

    # Methods for inserting or deleting

    ___ insertRows  position, rows, parent):
        beginInsertRows(
            parent or qtc.QModelIndex(),
            position,
            position + rows - 1
        )

        ___ i __ range(rows):
            default_row _ [''] * le.(_headers)
            _data.insert(position, default_row)
        endInsertRows()

    ___ removeRows  position, rows, parent):
        beginRemoveRows(
            parent or qtc.QModelIndex(),
            position,
            position + rows - 1
        )
        ___ i __ range(rows):
            del(_data[position])
        endRemoveRows()

    # method for saving
    ___ save_data
        w__ o..(filename, 'w', encoding_'utf-8') __ fh:
            writer _ csv.writer(fh)
            writer.writerow(_headers)
            writer.writerows(_data)


c_ MainWindow(qtw.QMainWindow):

    model _ N..

    ___  - 
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here

        tableview _ qtw.QTableView()
        tableview.setSortingEnabled( st.
        sCW..(tableview)

        # Setup the menu
        menu _ mB..
        file_menu _ menu.aM..('File')
        file_menu.aA..('Open', select_file)
        file_menu.aA..('Save', save_file)

        edit_menu _ menu.aM..('Edit')
        edit_menu.aA..('Insert Above', insert_above)
        edit_menu.aA..('Insert Below', insert_below)
        edit_menu.aA..('Remove Row(s)', remove_rows)

        # End main UI code
        s..

    # File methods
    ___ select_file
        filename, _ _ qtw.?FD...gOFN..(
            self,
            'Select a CSV file to open…',
            qtc.QDir.homePath(),
            'CSV Files (*.csv) ;; All Files (*)'
        )
        __ filename:
            model _ CsvTableModel(filename)
            tableview.sM..(model)

    ___ save_file
        __ model:
            model.save_data()

    # Methods for insert/remove

    ___ insert_above
        selected _ tableview.selectedIndexes()
        row _ selected[0].row() __ selected else 0
        model.insertRows(row, 1, N..)

    ___ insert_below
        selected _ tableview.selectedIndexes()
        row _ selected[-1].row() __ selected else model.rowCount(N..)
        model.insertRows(row + 1, 1, N..)

    ___ remove_rows
        selected _ tableview.selectedIndexes()
        __ selected:
            model.removeRows(selected[0].row(), le.(selected), N..)


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
