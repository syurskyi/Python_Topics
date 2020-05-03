____ PySide.?G.. _____ _
____ PySide.?C.. _____ _
_____ os
path _ os.path.dirname(__file__)

c_ simpleWindow(?W..
    path _ os.path.dirname(__file__)
    ___  -  
        super(simpleWindow, self). - 
        ly _ QHBoxLayout
        setLayout(ly)
        table _ QTableWidget
        ly.addWidget(table)
        table.verticalHeader.hide
        table.horizontalHeader.setResizeMode(QHeaderView.Stretch)
        # start
        resize(500,400)
        fillTable

    ___ fillTable 
        files _ os.listdir(path)
        table.setColumnCount(2)
        table.setRowCount(le.(files))
        table.setHorizontalHeaderLabels(['Name', 'Size'])
        ___ i, f __ enumerate(files
            item _ ?TWI..
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.sT..(f)
            table.sI..(i, 0, item)
            item _ ?TWI..
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.sT..(st.(os.stat(os.path.j..(path, f)).st_size) + ' bytes' )
            table.sI..(i, 1, item)


__ __name__ __ '__main__':
    app _ ?A..([])
    w _ simpleWindow
    w.s..
    app.exec_