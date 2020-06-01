______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ QtCore __ qtc


c_ FormWindow(qtw.QWidget):

    submitted _ qtc.pyqtSignal([str], [int, str])

    ___ __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.edit _ qtw.QLineEdit()
        self.submit _ qtw.?PB..('Submit', c___self.onSubmit)

        self.layout().addWidget(self.edit)
        self.layout().addWidget(self.submit)

    ___ onSubmit(self):
        __ self.edit.text().isdigit
            text _ self.edit.text()
            self.submitted[int, str].emit(int(text), text)
        ____
            self.submitted[str].emit(self.edit.text())
        self.close()

c_ MainWindow(qtw.QWidget):

    ___ __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.label _ qtw.QLabel('Click "change" to change this text.')
        self.change _ qtw.?PB..("Change", c___self.onChange)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.change)
        self.s..

    @qtc.pyqtSlot()
    ___ onChange(self):
        self.formwindow _ FormWindow()
        #self.formwindow.submitted.connect(self.label.setText)
        self.formwindow.submitted[str].c..(self.onSubmittedStr)
        self.formwindow.submitted[int, str].c..(self.onSubmittedIntStr)
        self.formwindow.s..

    @qtc.pyqtSlot(str)
    ___ onSubmittedStr  string):
        self.label.sT..(string)

    @qtc.pyqtSlot(int, str)
    ___ onSubmittedIntStr  integer, string):
        text _ f'The string {string} becomes the number {integer}'
        self.label.sT..(text)


__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
