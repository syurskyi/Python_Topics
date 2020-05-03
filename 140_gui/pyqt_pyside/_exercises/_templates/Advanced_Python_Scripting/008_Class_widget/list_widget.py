____ ?.?G.. _____ _
_____ os
path _ os.path.dirname(__file__)

c_ simpleWindow(?W..
    ___  -  
        s__(simpleWindow, self). -
        ly _ QHBoxLayout
        setLayout(ly)
        list _ ?LW..
        ly.addWidget(list)
        textBrowser _ QTextBrowser
        ly.addWidget(textBrowser)
        # connect
        list.iC__.c..(updateText)
        list.itemDoubleClicked.c..(openFile)
        # start
        resize(500,400)
        fillList

    ___ fullPath , item
        r_ os.path.j..(path,item.t..())

    ___ fillList 
        ___ f __ os.listdir(path
            list.aI..(f)

    ___ updateText , item
        t.. _open(fullPath(item)).read
        textBrowser.sT..(t..)

    ___ openFile , item
        path _ fullPath(item)
        os.system(path)


__ _____ __ ______
    app _ ?A..([])
    w _ simpleWindow
    w.s..
    app.exec_