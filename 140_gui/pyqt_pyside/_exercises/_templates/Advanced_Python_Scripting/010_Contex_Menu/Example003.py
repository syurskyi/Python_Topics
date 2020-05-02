_____ ___
____ PyQt4.?C.. _____ *
____ PyQt4.QtGui _____ *



c_ TableWidget(QTableWidget
    ___  -  , parent_None
        QTableWidget. -  , parent)
        setContextMenuPolicy(Qt.ActionsContextMenu)

        quitAction _ QAction("Quit", self)
        quitAction.triggered.c..(qApp.quit)
        addAction(quitAction)


app _ ?A..([])
tableWidget _ TableWidget()
tableWidget.s..
___.e..(app.exec_())