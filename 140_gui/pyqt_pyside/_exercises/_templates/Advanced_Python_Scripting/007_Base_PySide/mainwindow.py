____ PySide.?C.. _____ *
____ PySide.QtGui _____ *


c_ WindowClass(QMainWindow
    ___  -  
        super(WindowClass, self). - ()
        w _ ?W..()
        setCentralWidget(w)

        menuBar _ QMenuBar()
        setMenuBar(menuBar)

        menu _ QMenu('File')
        menuBar.addMenu(menu)

        act1 _ QAction('Open', self)
        menu.addAction(act1)


__ __name__ __ '__main__':
    app _ ?A..([])
    w _ WindowClass()
    w.s..
    app.exec_()