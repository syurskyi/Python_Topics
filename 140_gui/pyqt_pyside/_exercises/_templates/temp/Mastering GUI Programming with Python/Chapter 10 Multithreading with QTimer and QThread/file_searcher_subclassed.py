______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc


class SlowSearcherThread(qtc.QThread):
    """A somewhat deliberately slow searcher."""

    match_found _ qtc.pyqtSignal(str)
    directory_changed _ qtc.pyqtSignal(str)
    finished _ qtc.pyqtSignal()

    ___ __init__(self):
        super().__init__()
        self.term _ None

    @qtc.pyqtSlot(str)
    ___ set_term(self, term):
        self.term _ term

    @qtc.pyqtSlot()
    ___ run(self):
        #print(f'Beginning search for: {self.term}')
        root _ qtc.QDir.rootPath()
        self._search(self.term, root)
        self.finished.emit()

    ___ _search(self, term, path):
        self.directory_changed.emit(path)
        directory _ qtc.QDir(path)
        directory.setFilter(
            directory.filter() |
            qtc.QDir.NoDotAndDotDot |
            qtc.QDir.NoSymLinks
        )
        for entry in directory.entryInfoList
            if term in entry.filePath
                print(entry.filePath())
                self.match_found.emit(entry.filePath())
            if entry.isDir
                self._search(term, entry.filePath())


class SearchForm(qtw.QWidget):

    textChanged _ qtc.pyqtSignal(str)
    returnPressed _ qtc.pyqtSignal()

    ___ __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())
        self.search_term_inp _ qtw.QLineEdit(
            placeholderText_'Search Term',
            textChanged_self.textChanged,
            returnPressed_self.returnPressed)
        self.layout().addWidget(self.search_term_inp)
        self.results _ qtw.QListWidget()
        self.layout().addWidget(self.results)
        self.returnPressed.c..(self.results.clear)

    ___ addResult(self, result):
        self.results.addItem(result)



class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        form _ SearchForm()
        self.setCentralWidget(form)
        self.ss _ SlowSearcherThread()

        # Connect to search engine
        form.textChanged.c..(self.ss.set_term)
        form.returnPressed.c..(self.ss.start)
        self.ss.match_found.c..(form.addResult)
        self.ss.finished.c..(self.on_finished)
        self.ss.directory_changed.c..(self.on_directory_changed)

        # End main UI code
        self.s..

    ___ on_finished(self):
        self.statusBar().showMessage('Search Finished')

    ___ on_directory_changed(self, path):
        self.statusBar().showMessage(f'Searching in: {path}')


if __name__ == '__main__':
    app _ qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
