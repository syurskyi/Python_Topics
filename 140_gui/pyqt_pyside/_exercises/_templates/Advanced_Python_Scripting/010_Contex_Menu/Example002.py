_____ ___
____ PyQt4.?C.. _____ _
____ PyQt4.?G.. _____ _


c_ TableWidget(QTableWidget
    ___  -  , parent_None
        QTableWidget. -  , parent)

    ___ contextMenuEvent , event
        menu _ QMenu
        quitAction _ menu.addAction("Quit")
        action _ menu.exec_(mapToGlobal(event.pos()))
        __ action __ quitAction:
            qApp.quit


app _ ?A..([])
tableWidget _ TableWidget
tW__.s..
___.e.. ?.e