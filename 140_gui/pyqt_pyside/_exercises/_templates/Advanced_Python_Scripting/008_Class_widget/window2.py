____ PySide.QtGui _____ *
# from PyQt4.QtGui import *

c_ simpleWindow(?W..
    ___  -  
        super(simpleWindow, self). - ()
        ly = QVBoxLayout
        btn  = ?PB..('Open')
        ly.addWidget(btn)
        resize(300,200)
        btn.clicked.c..(showMessage)

    ___ showMessage 
        _filter = 'Python File(*.py);; All(*.*)'
        d = QFileDialog.getOpenFileName , 'Set folder', 'c:/tmp', _filter)
        print d

__ __name__ __ '__main__':
    app = ?A..([])
    w = simpleWindow()
    w.s..
    app.exec_()