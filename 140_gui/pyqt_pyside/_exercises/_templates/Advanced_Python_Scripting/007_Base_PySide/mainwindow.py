____ PySide.?C.. _____ *
____ PySide.QtGui _____ *


c_ WindowClass(QMainWindow
    ___  -  
        super(WindowClass, self). - ()
        w = ?W..()
        setCentralWidget(w)

        menuBar = QMenuBar()
        setMenuBar(menuBar)

        menu = QMenu('File')
        menuBar.addMenu(menu)

        act1 = QAction('Open', self)
        menu.addAction(act1)


__ __name__ __ '__main__':
    app = ?A..([])
    w = WindowClass()
    w.s..
    app.exec_()