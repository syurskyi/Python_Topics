____ ?.?G.. _____ _
_____ __
path _ __.path.d_n..(__file__)

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
        r..(500,400)
        fillList

    ___ fullPath , item
        r_ __.path.j..(path,item.t..())

    ___ fillList 
        ___ f __ __.listdir(path
            list.aI..(f)

    ___ updateText , item
        t.. _open(fullPath(item)).read
        textBrowser.sT..(t..)

    ___ openFile , item
        path _ fullPath(item)
        __.system(path)


__ _____ __ ______
    app _ ?A..
    w _ simpleWindow
    w.s..
    app.e..