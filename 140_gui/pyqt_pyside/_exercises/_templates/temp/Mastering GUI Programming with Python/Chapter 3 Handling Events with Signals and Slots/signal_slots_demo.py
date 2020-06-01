______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc


c_ MainWindow ?.?W..

    ___  -
        s_. - ()
        sL.. ?.?VBL..

        # connecting a signal to a slot
        quitbutton _ qtw.?PB..('Quit')
        quitbutton.c__.c..(close)
        layout().aW..(quitbutton)

        # connecting a signal with data to a slot that receives data
        entry1 _ qtw.?LE..
        entry2 _ qtw.?LE..
        layout().aW..(entry1)
        layout().aW..(entry2)
        entry1.textChanged.c..(entry2.sT..)

        # connecting a signal to a python callable
        entry2.textChanged.c..(print)

        # Connecting a signal to another signal
        entry1.editingFinished.c..(lambda: print('editing finished'))
        entry2.rP__.c..(entry1.editingFinished)

        # This call will fail, because the signals have different argument types
        #self.entry1.textChanged.connect(self.quitbutton.clicked)

        # This won't work, because of signal doesn't send enough args
        badbutton _ qtw.?PB..("Bad")
        layout().aW..(badbutton)
        badbutton.c__.c..(needs_args)

        # This will work, even though the signal sends extra args
        goodbutton _ qtw.?PB..("Good")
        layout().aW..(goodbutton)
        goodbutton.c__.c..(no_args)


        s..

    ___ needs_args  arg1, arg2, arg3):
        pass

    ___ no_args 
        print('I need no arguments')

__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
