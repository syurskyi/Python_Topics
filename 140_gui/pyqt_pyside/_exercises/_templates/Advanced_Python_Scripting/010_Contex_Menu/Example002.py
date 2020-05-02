_____ ___
____ PyQt4.?C.. _____ *
____ PyQt4.QtGui _____ *


c_ TableWidget(QTableWidget
    ___  -  , parent=None
        QTableWidget. -  , parent)

    ___ contextMenuEvent , event
        menu = QMenu
        quitAction = menu.addAction("Quit")
        action = menu.exec_(mapToGlobal(event.pos()))
        __ action __ quitAction:
            qApp.quit()


app = ?A..([])
tableWidget = TableWidget()
tableWidget.s..
___.e..(app.exec_())