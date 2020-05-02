____ PySide.QtGui _____ *
_____ os
path = os.path.dirname(__file__)

c_ simpleWindow(?W..
    ___  -  
        super(simpleWindow, self). - ()
        ly = QHBoxLayout()
        setLayout(ly)
        list = QListWidget()
        ly.addWidget(list)
        textBrowser = QTextBrowser()
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
        text =open(fullPath(item)).read()
        textBrowser.sT..(text)

    ___ openFile , item
        path = fullPath(item)
        os.system(path)


__ __name__ __ '__main__':
    app = ?A..([])
    w = simpleWindow()
    w.s..
    app.exec_()