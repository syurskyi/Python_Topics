____ PySide.QtGui _____ *
_____ os
path _ os.path.dirname(__file__)

c_ simpleWindow(?W..
    ___  -  
        super(simpleWindow, self). - ()
        ly _ QHBoxLayout()
        setLayout(ly)
        list _ QListWidget()
        ly.addWidget(list)
        textBrowser _ QTextBrowser()
        ly.addWidget(textBrowser)
        # connect
        list.itemClicked.c..(updateText)
        list.itemDoubleClicked.c..(openFile)
        # start
        resize(500,400)
        fillList()

    ___ fullPath , item
        return os.path.join(path,item.text())

    ___ fillList 
        for f in os.listdir(path
            list.addItem(f)

    ___ updateText , item
        text _open(fullPath(item)).read()
        textBrowser.sT..(text)

    ___ openFile , item
        path _ fullPath(item)
        os.system(path)


__ __name__ __ '__main__':
    app _ ?A..([])
    w _ simpleWindow()
    w.s..
    app.exec_()