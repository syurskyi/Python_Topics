______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc

c_ TimeForm ?.?W..

    submitted _ qtc.pyqtSignal(qtc.QTime)

    ___  -  
        s_. - ()
        sL..(qtw.QHBoxLayout())
        time_inp _ qtw.QTimeEdit
        #self.time_inp = qtw.QTimeEdit(self, objectName='time_inp')
        layout().aW..(time_inp)
        #qtc.QMetaObject.connectSlotsByName(self)

    ___ on_time_inp_editingFinished 
        submitted.emit(time_inp.time())
        destroy()

c_ MainWindow ?.?W..

    ___  -  
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here
        tf _ TimeForm()
        tf.s..

        tf.submitted.c..(lambda x: print(x))

        # End main UI code
        s..


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
