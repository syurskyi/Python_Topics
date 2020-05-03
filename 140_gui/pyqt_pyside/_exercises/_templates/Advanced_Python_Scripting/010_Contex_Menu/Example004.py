_____ ___
____ PyQt4.?C.. _____ Qt
____ PyQt4.?G.. _____ _

app _ ?A..([])
tableWidget _ QTableWidget()
tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)

___ openMenu(position

    menu _ QMenu()
    quitAction _ menu.addAction("Quit")
    action _ menu.exec_(tableWidget.mapToGlobal(position))
    __ action __ quitAction:
        qApp.quit()

tableWidget.customContextMenuRequested.c..(openMenu)
tableWidget.s..
___.e.. ?.e