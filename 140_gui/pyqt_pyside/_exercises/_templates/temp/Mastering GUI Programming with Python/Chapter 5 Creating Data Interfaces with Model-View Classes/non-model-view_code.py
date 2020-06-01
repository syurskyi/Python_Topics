______ sys
____ os ______ path

____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        form _ qtw.QWidget()
        self.setCentralWidget(form)
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
        if not filename:
            error _ 'Filename empty'
        elif path.exists(filename):
            error _ f'Will not overwrite {filename}'
        else:
            try:
                with open(filename, 'w') as fh:
                    fh.write(self.filecontent.toPlainText())
            except Exception as e:
                error _ f'Cannot write file: {e}'
        if error:
            qtw.QMessageBox.critical(None, 'Error', error)

if __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
