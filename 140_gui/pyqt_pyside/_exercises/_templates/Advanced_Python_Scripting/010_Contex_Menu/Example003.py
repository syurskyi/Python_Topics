_____ ___
____ PyQt4.?C.. _____ *
____ PyQt4.QtGui _____ *



c_ TableWidget(QTableWidget
    ___  -  , parent=None
        QTableWidget. -  , parent)
        setContextMenuPolicy(Qt.ActionsContextMenu)

        quitAction = QAction("Quit", self)
        quitAction.triggered.c..(qApp.quit)
        addAction(quitAction)


app = ?A..([])
tableWidget = TableWidget()
tableWidget.s..
___.e..(app.exec_())