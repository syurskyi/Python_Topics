____ ?.?G.. _____ _
____ ?.?C.. _____ _
_____ __
path _ __.path.d_n..(__file__)

c_ simpleWindow(?W..
    path _ __.path.d_n..(__file__)
    ___  -  
        s__(simpleWindow, self). -
        ly _ QHBoxLayout
        setLayout(ly)
        table _ QTableWidget
        ly.addWidget(table)
        table.verticalHeader.h..
        table.horizontalHeader.setResizeMode(QHeaderView.Stretch)
        # start
        r..(500,400)
        fillTable

    ___ fillTable 
        files _ __.listdir(path)
        table.setColumnCount(2)
        table.setRowCount(le.(files))
        table.setHorizontalHeaderLabels(['Name', 'Size'])
        ___ i, f __ enumerate(files
            item _ ?TWI..
            item.setFlags(__.ItemIsEnabled | __.ItemIsSelectable)
            item.sT..(f)
            table.sI..(i, 0, item)
            item _ ?TWI..
            item.setFlags(__.ItemIsEnabled | __.ItemIsSelectable)
            item.sT..(st.(__.stat(__.path.j..(path, f)).st_size) + ' bytes' )
            table.sI..(i, 1, item)


__ _____ __ ______
    app _ ?A..
    w _ simpleWindow
    w.s..
    app.e..