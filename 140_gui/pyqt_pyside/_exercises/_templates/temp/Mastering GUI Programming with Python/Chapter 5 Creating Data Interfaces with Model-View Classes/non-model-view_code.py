______ sys
____ os ______ path

____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ QtCore __ qtc


c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        form _ qtw.QWidget()
        self.sCW..(form)
        form.setLayout(qtw.QVBoxLayout())
        self.filename _ qtw.QLineEdit()
        self.filecontent _ qtw.QTextEdit()
        self.savebutton _ qtw.?PB..(
            'Save',
            c___self.save
        )

        form.layout().addWidget(self.filename)
        form.layout().addWidget(self.filecontent)
        form.layout().addWidget(self.savebutton)

        # End main UI code
        self.s..

    ___ save(self):
        filename _ self.filename.text()
        error _ ''
        __ no. filename:
            error _ 'Filename empty'
        ____ path.exists(filename):
            error _ f'Will not overwrite {filename}'
        ____
            try:
                w__ o..(filename, 'w') __ fh:
                    fh.w..(self.filecontent.tPT..
            except Exception __ e:
                error _ f'Cannot write file: {e}'
        __ error:
            qtw.?MB...critical(N.., 'Error', error)

__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
