_____ ___
____ PyQt4.?C.. _____ Qt
____ PyQt4.?G.. _____ _

app _ ?A..([])
tableWidget _ QTableWidget
tW__.setContextMenuPolicy(Qt.CustomContextMenu)

___ openMenu(position

    menu _ QMenu
    quitAction _ menu.addAction("Quit")
    action _ menu.exec_(tW__.mapToGlobal(position))
    __ action __ quitAction:
        qApp.quit

tW__.customContextMenuRequested.c..(openMenu)
tW__.s..
___.e.. ?.e