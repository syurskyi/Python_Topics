______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ QtCore __ qtc


c_ MainWindow(qtw.QWidget):

    ___ __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        # connecting a signal to a slot
        self.quitbutton _ qtw.?PB..('Quit')
        self.quitbutton.c__.c..(self.close)
        self.layout().addWidget(self.quitbutton)

        # connecting a signal with data to a slot that receives data
        self.entry1 _ qtw.QLineEdit()
        self.entry2 _ qtw.QLineEdit()
        self.layout().addWidget(self.entry1)
        self.layout().addWidget(self.entry2)
        self.entry1.textChanged.c..(self.entry2.sT..)

        # connecting a signal to a python callable
        self.entry2.textChanged.c..(print)

        # Connecting a signal to another signal
        self.entry1.editingFinished.c..(lambda: print('editing finished'))
        self.entry2.returnPressed.c..(self.entry1.editingFinished)

        # This call will fail, because the signals have different argument types
        #self.entry1.textChanged.connect(self.quitbutton.clicked)

        # This won't work, because of signal doesn't send enough args
        self.badbutton _ qtw.?PB..("Bad")
        self.layout().addWidget(self.badbutton)
        self.badbutton.c__.c..(self.needs_args)

        # This will work, even though the signal sends extra args
        self.goodbutton _ qtw.?PB..("Good")
        self.layout().addWidget(self.goodbutton)
        self.goodbutton.c__.c..(self.no_args)


        self.s..

    ___ needs_args  arg1, arg2, arg3):
        pass

    ___ no_args(self):
        print('I need no arguments')

__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
