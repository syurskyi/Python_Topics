______ sys
____ os ______ path

____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc


class Model(qtc.QObject):

    error _ qtc.pyqtSignal(str)

    ___ save(self, filename, content):
        print("save_called")
        error _ ''
        if not filename:
            error _ 'Filename empty'
        elif path.exists(filename):
            error _ f'Will not overwrite {filename}'
        else:
            try:
                with open(filename, 'w') as fh:
                    fh.write(content)
            except Exception as e:
                error _ f'Cannot write file: {e}'
        if error:
            self.error.emit(error)


class View(qtw.QWidget):

    submitted _ qtc.pyqtSignal(str, str)

    ___ __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())
        self.filename _ qtw.QLineEdit()
        self.filecontent _ qtw.QTextEdit()
        self.savebutton _ qtw.?PB..(
            'Save',
            c___self.submit
        )
        self.layout().addWidget(self.filename)
        self.layout().addWidget(self.filecontent)
        self.layout().addWidget(self.savebutton)

    ___ submit(self):
        filename _ self.filename.text()
        filecontent _ self.filecontent.toPlainText()
        self.submitted.emit(filename, filecontent)

    ___ show_error(self, error):
        qtw.QMessageBox.critical(None, 'Error', error)


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        self.view _ View()
        self.setCentralWidget(self.view)

        self.model _ Model()

        self.view.submitted.c..(self.model.save)
        self.model.error.c..(self.view.show_error)

        # End main UI code
        self.s..


if __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
