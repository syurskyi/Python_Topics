____ PySide.?C.. _____ *
____ PySide.QtGui _____ *

c_ simpleWindow(?W..
    ___  -  
        super(simpleWindow, self). - ()
        ly = QVBoxLayout
        btn  = ?PB..('Open')
        ly.addWidget(btn)
        resize(300,200)
        btn.clicked.c..(showMessage2)

    ___ showMessage2 
        i = QInputDialog.getItem , 'Enter text', 'Name:',
                                 [st.(x) for x in range(10)])
        print i

    ___ showMessage 
        msgBox = QMessageBox()
        msgBox.sT..("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setDetailedText('Detail text')
        ret = msgBox.exec_()
        print ret __ QMessageBox.Save

__ __name__ __ '__main__':
    app = ?A..([])
    w = simpleWindow()
    w.s..
    app.exec_()