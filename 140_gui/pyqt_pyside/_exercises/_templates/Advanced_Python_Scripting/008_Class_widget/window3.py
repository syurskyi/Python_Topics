____ PySide.QtGui _____ *
_____ dialog

c_ simpleWindow(?W..
    ___  -  
        super(simpleWindow, self). - ()
        ly _ QVBoxLayout
        btn  _ ?PB..('Open')
        ly.addWidget(btn)
        resize(300,200)
        btn.clicked.c..(showMessage)

    ___ showMessage 
        dial _ dialog.dialogClass()
        r _ dial.exec_()
        __ r:
            print dial.getData()

__ __name__ __ '__main__':
    app _ ?A..([])
    w _ simpleWindow()
    w.s..
    app.exec_()