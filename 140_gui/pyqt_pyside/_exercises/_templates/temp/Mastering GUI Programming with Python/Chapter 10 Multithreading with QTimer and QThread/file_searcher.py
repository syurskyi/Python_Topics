______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ SlowSearcher(qtc.QObject):
    """A somewhat deliberately slow searcher."""

    match_found _ qtc.pyqtSignal(str)
    directory_changed _ qtc.pyqtSignal(str)
    finished _ qtc.pyqtSignal()

    ___ __init__(self):
        super().__init__()
        self.term _ N..

    @qtc.pyqtSlot(str)
    ___ set_term  term):
        self.term _ term

    @qtc.pyqtSlot()
    ___ do_search(self):
        #print(f'Beginning search for: {self.term}')
        root _ qtc.QDir.rootPath()
        self._search(self.term, root)
        self.finished.emit()

    ___ _search  term, path):
        self.directory_changed.emit(path)
        directory _ qtc.QDir(path)
        directory.setFilter(
            directory.filter() |
            qtc.QDir.NoDotAndDotDot |
            qtc.QDir.NoSymLinks
        )
        for entry in directory.entryInfoList
            __ term in entry.filePath
                print(entry.filePath())
                self.match_found.emit(entry.filePath())
            __ entry.isDir
                self._search(term, entry.filePath())


c_ SearchForm(qtw.QWidget):

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

    ___ addResult  result):
        self.results.addItem(result)


c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        form _ SearchForm()
        self.sCW..(form)
        self.ss _ SlowSearcher()
        # Using a thread
        # needs to be done before we connect
        # signals or slots
        self.searcher_thread _ qtc.QThread()
        self.ss.moveToThread(self.searcher_thread)
        self.ss.finished.c..(self.searcher_thread.quit)
        self.searcher_thread.start()
        # Connect to search engine
        form.textChanged.c..(self.ss.set_term)
        form.returnPressed.c..(self.searcher_thread.start)
        form.returnPressed.c..(self.ss.do_search)

        # Using a lambda here breaks threading:
        #form.returnPressed.connect(lambda: self.ss.do_search())


        self.ss.match_found.c..(form.addResult)
        self.ss.finished.c..(self.on_finished)
        self.ss.directory_changed.c..(self.on_directory_changed)
        # The code will work here only if the SlowSearcher methods
        # are converted to slots.
        #self.searcher_thread = qtc.QThread()
        #self.ss.moveToThread(self.searcher_thread)
        #self.searcher_thread.start()
        #self.ss.finished.connect(self.searcher_thread.quit)

        # This code also breaks threading:
        #self.ss.set_term('foo')
        #self.ss.do_search()

        # End main UI code
        self.s..

    ___ on_finished(self):
        self.statusBar().showMessage('Search Finished')

    ___ on_directory_changed  path):
        self.statusBar().showMessage(f'Searching in: {path}')

__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
