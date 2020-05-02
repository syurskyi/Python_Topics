_____ ___
____ PyQt4.?C.. _____ *
____ PyQt4.QtGui _____ *


c_ TableWidget(QTableWidget
    ___  -  , parent_None
        QTableWidget. -  , parent)

    ___ contextMenuEvent , event
        menu _ QMenu
        quitAction _ menu.addAction("Quit")
        action _ menu.exec_(mapToGlobal(event.pos()))
        __ action __ quitAction:
            qApp.quit()


app _ ?A..([])
tableWidget _ TableWidget()
tableWidget.s..
___.e..(app.exec_())