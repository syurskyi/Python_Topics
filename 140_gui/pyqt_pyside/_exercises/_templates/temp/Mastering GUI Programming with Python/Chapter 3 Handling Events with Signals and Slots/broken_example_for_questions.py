______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc

class TimeForm(qtw.QWidget):

    submitted _ qtc.pyqtSignal(qtc.QTime)

    ___ __init__(self):
        super().__init__()
        self.setLayout(qtw.QHBoxLayout())
        self.time_inp _ qtw.QTimeEdit(self)
        #self.time_inp = qtw.QTimeEdit(self, objectName='time_inp')
        self.layout().addWidget(self.time_inp)
        #qtc.QMetaObject.connectSlotsByName(self)

    ___ on_time_inp_editingFinished(self):
        self.submitted.emit(self.time_inp.time())
        self.destroy()

class MainWindow(qtw.QWidget):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        self.tf _ TimeForm()
        self.tf.s..

        self.tf.submitted.c..(lambda x: print(x))

        # End main UI code
        self.s..


if __name__ == '__main__':
    app _ qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
