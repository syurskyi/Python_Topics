_____ ___
____ PyQt4.?C.. _____ Qt
____ PyQt4.QtGui _____ *

app = ?A..([])
tableWidget = QTableWidget()
tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)

___ openMenu(position

    menu = QMenu()
    quitAction = menu.addAction("Quit")
    action = menu.exec_(tableWidget.mapToGlobal(position))
    __ action __ quitAction:
        qApp.quit()

tableWidget.customContextMenuRequested.c..(openMenu)
tableWidget.s..
___.e..(app.exec_())