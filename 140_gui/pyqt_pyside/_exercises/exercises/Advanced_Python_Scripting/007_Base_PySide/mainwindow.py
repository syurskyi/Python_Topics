____ ?.?C.. _____ _
____ ?.?G.. _____ _


c_ WindowClass(?M..
    ___  -  
        s__(WindowClass, self). -
        w _ ?W..
        setCentralWidget(w)

        menuBar _ QMenuBar
        setMenuBar(menuBar)

        menu _ QMenu('File')
        menuBar.addMenu(menu)

        act1 _ ?A__('Open', self)
        menu.addAction(act1)


__ _____ __ ______
    app _ ?A..
    w _ WindowClass
    w.s..
    app.e..