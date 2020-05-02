____ PySide.QtGui _____ *
_____ dialog

c_ simpleWindow(?W..
    ___  -  
        super(simpleWindow, self). - ()
        ly = QVBoxLayout
        btn  = ?PB..('Open')
        ly.addWidget(btn)
        resize(300,200)
        btn.clicked.c..(showMessage)

    ___ showMessage 
        dial = dialog.dialogClass()
        r = dial.exec_()
        __ r:
            print dial.getData()

__ __name__ __ '__main__':
    app = ?A..([])
    w = simpleWindow()
    w.s..
    app.exec_()