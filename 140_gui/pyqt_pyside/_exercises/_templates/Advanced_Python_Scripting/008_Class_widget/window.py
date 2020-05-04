____ ?.?C.. _____ _
____ ?.?G.. _____ _

c_ simpleWindow(?W..
    ___  -  
        s__(simpleWindow, self). -
        ly _ QVBoxLayout
        btn  _ ?PB..('Open')
        ly.addWidget(btn)
        r..(300,200)
        btn.c___.c..(showMessage2)

    ___ showMessage2 
        i _ ?ID...getItem , 'Enter text', 'Name:',
                                 [st.(x) ___ x __ ra..(10)])
        print i

    ___ showMessage 
        msgBox _ QMessageBox
        msgBox.sT..("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setDetailedText('Detail text')
        ret _ msgBox.e..
        print ret __ QMessageBox.Save

__ _____ __ ______
    app _ ?A..
    w _ simpleWindow
    w.s..
    app.e..