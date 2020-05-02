____ PySide.?G.. _____ _
____ PySide.?C.. _____ _
_____ os
path _ os.path.dirname(__file__)

c_ simpleWindow(?W..
    path _ os.path.dirname(__file__)
    ___  -  
        super(simpleWindow, self). - ()
        ly _ QHBoxLayout()
        setLayout(ly)
        table _ QTableWidget()
        ly.addWidget(table)
        table.verticalHeader().hide()
        table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        # start
        resize(500,400)
        fillTable()

    ___ fillTable 
        files _ os.listdir(path)
        table.setColumnCount(2)
        table.setRowCount(len(files))
        table.setHorizontalHeaderLabels(['Name', 'Size'])
        for i, f in enumerate(files
            item _ QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.sT..(f)
            table.setItem(i, 0, item)
            item _ QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.sT..(st.(os.stat(os.path.join(path, f)).st_size) + ' bytes' )
            table.setItem(i, 1, item)


__ __name__ __ '__main__':
    app _ ?A..([])
    w _ simpleWindow()
    w.s..
    app.exec_()