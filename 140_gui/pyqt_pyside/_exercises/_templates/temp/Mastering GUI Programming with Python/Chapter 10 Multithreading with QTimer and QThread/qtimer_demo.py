______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ AutoCloseDialog(qtw.QDialog):

    ___  -   parent, title, message, timeout):
        s_. - (parent)
        setModal F..
        setWindowTitle(title)
        sL.. ?.?VBL..
        layout().aW..(qtw.QLabel(message))
        timeout _ timeout

    ___ show
        s_.s..
        # Wrong:
        #from time import sleep
        #sleep(self.timeout)
        #self.hide()
        # Right:
        qtc.QTimer.singleShot(timeout * 1000, hide)


c_ MainWindow(qtw.QMainWindow):

    ___  -
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here

        # Using a singleshot timer
        dialog _ AutoCloseDialog(
            self,
            "Self-destructing message",
            "This message will self-destruct in 10 seconds",
            10
        )
        dialog.s..


        # Using an interval timer
        interval_seconds _ 10
        timer _ qtc.?T..
        timer.setInterval(interval_seconds * 1000)

        interval_dialog _ AutoCloseDialog(
            self, "It's time again",
            f"It has been {interval_seconds} seconds "
            "since this dialog was last shown.", 2000)
        timer.timeout.c..(interval_dialog.show)
        timer.start()
        toolbar _ addToolBar('Tools')
        toolbar.aA..('Stop Bugging Me', timer.stop)
        toolbar.aA..('Start Bugging Me', timer.start)

        # Getting data from a timer
        timer2 _ qtc.?T..
        timer2.setInterval(1000)
        timer2.timeout.c..(update_status)
        timer2.start()
        #self.show()
        #return

        # Does a blocking call in a timer block the UI?

        # create timer
        #qtc.QTimer.singleShot(1, self.long_blocking_callback)
        # Yes, yes it does.

        # End main UI code

        s..

    ___ update_status
        __ timer.isActive
            time_left _ (timer.remainingTime() // 1000) + 1
            statusBar().showMessage(
                f"Next dialog will be shown in {time_left} seconds.")
        ____
            statusBar().showMessage('Dialogs are off.')

    ___ long_blocking_callback
        ____ time ______ sl..
        statusBar().showMessage('Beginning a long blocking function.')
        sl..(30)
        statusBar().showMessage('Ending a long blocking function.')

__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.exit(app.exec())
