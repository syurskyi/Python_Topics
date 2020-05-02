____ PySide.?C.. _____ _
____ PySide.?G.. _____ _

c_ simpleWindow(?W..
    ___  -  
        super(simpleWindow, self). - ()
        ly _ QVBoxLayout
        btn  _ ?PB..('Open')
        ly.addWidget(btn)
        resize(300,200)
        btn.c___.c..(showMessage2)

    ___ showMessage2 
        i _ ?ID...getItem , 'Enter text', 'Name:',
                                 [st.(x) ___ x __ range(10)])
        print i

    ___ showMessage 
        msgBox _ QMessageBox()
        msgBox.sT..("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setDetailedText('Detail text')
        ret _ msgBox.exec_()
        print ret __ QMessageBox.Save

__ __name__ __ '__main__':
    app _ ?A..([])
    w _ simpleWindow()
    w.s..
    app.exec_()