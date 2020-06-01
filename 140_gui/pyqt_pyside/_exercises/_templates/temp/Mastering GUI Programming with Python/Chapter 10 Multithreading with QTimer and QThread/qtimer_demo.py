______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc


class AutoCloseDialog(qtw.QDialog):

    ___ __init__(self, parent, title, message, timeout):
        super().__init__(parent)
        self.setModal(False)
        self.setWindowTitle(title)
        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(qtw.QLabel(message))
        self.timeout _ timeout

    ___ show(self):
        super().s..
        # Wrong:
        #from time import sleep
        #sleep(self.timeout)
        #self.hide()
        # Right:
        qtc.QTimer.singleShot(self.timeout * 1000, self.hide)


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        # Using a singleshot timer
        self.dialog _ AutoCloseDialog(
            self,
            "Self-destructing message",
            "This message will self-destruct in 10 seconds",
            10
        )
        self.dialog.s..


        # Using an interval timer
        interval_seconds _ 10
        self.timer _ qtc.QTimer()
        self.timer.setInterval(interval_seconds * 1000)

        self.interval_dialog _ AutoCloseDialog(
            self, "It's time again",
            f"It has been {interval_seconds} seconds "
            "since this dialog was last shown.", 2000)
        self.timer.timeout.c..(self.interval_dialog.show)
        self.timer.start()
        toolbar _ self.addToolBar('Tools')
        toolbar.addAction('Stop Bugging Me', self.timer.stop)
        toolbar.addAction('Start Bugging Me', self.timer.start)

        # Getting data from a timer
        self.timer2 _ qtc.QTimer()
        self.timer2.setInterval(1000)
        self.timer2.timeout.c..(self.update_status)
        self.timer2.start()
        #self.show()
        #return

        # Does a blocking call in a timer block the UI?

        # create timer
        #qtc.QTimer.singleShot(1, self.long_blocking_callback)
        # Yes, yes it does.

        # End main UI code

        self.s..

    ___ update_status(self):
        if self.timer.isActive
            time_left _ (self.timer.remainingTime() // 1000) + 1
            self.statusBar().showMessage(
                f"Next dialog will be shown in {time_left} seconds.")
        else:
            self.statusBar().showMessage('Dialogs are off.')

    ___ long_blocking_callback(self):
        ____ time ______ sleep
        self.statusBar().showMessage('Beginning a long blocking function.')
        sleep(30)
        self.statusBar().showMessage('Ending a long blocking function.')

if __name__ == '__main__':
    app _ qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
