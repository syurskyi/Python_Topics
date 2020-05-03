____ ?.?G.. _____ _
_____ dialog

c_ simpleWindow(?W..
    ___  -  
        s__(simpleWindow, self). -
        ly _ QVBoxLayout
        btn  _ ?PB..('Open')
        ly.addWidget(btn)
        resize(300,200)
        btn.c___.c..(showMessage)

    ___ showMessage 
        dial _ dialog.dialogClass
        r _ dial.exec_
        __ r:
            print dial.getData

__ _____ __ ______
    app _ ?A..([])
    w _ simpleWindow
    w.s..
    app.exec_