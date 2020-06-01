______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ SlowSearcher(qtc.QObject):
    """A somewhat deliberately slow searcher."""

    match_found _ qtc.pyqtSignal(str)
    directory_changed _ qtc.pyqtSignal(str)
    finished _ qtc.pyqtSignal()

    ___  -  
        s_. - ()
        term _ N..

    @qtc.pyqtSlot(str)
    ___ set_term  term):
        term _ term

    @qtc.pyqtSlot()
    ___ do_search 
        #print(f'Beginning search for: {self.term}')
        root _ qtc.QDir.rootPath()
        _search(term, root)
        finished.emit()

    ___ _search  term, path):
        directory_changed.emit(path)
        directory _ qtc.QDir(path)
        directory.setFilter(
            directory.filter() |
            qtc.QDir.NoDotAndDotDot |
            qtc.QDir.NoSymLinks
        )
        ___ entry __ directory.entryInfoList
            __ term __ entry.filePath
                print(entry.filePath())
                match_found.emit(entry.filePath())
            __ entry.isDir
                _search(term, entry.filePath())


c_ SearchForm ?.?W..

    textChanged _ qtc.pyqtSignal(str)
    rP__ _ qtc.pyqtSignal()

    ___  -  
        s_. - ()
        sL.. ?.?VBL..
        search_term_inp _ ?.?LE..(
            placeholderText_'Search Term',
            textChanged_self.textChanged,
            returnPressed_self.rP__)
        layout().aW..(search_term_inp)
        results _ ?.?LW..
        layout().aW..(results)
        rP__.c..(results.clear)

    ___ addResult  result):
        results.addItem(result)


c_ MainWindow(qtw.QMainWindow):

    ___  -  
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here

        form _ SearchForm()
        sCW..(form)
        ss _ SlowSearcher()
        # Using a thread
        # needs to be done before we connect
        # signals or slots
        searcher_thread _ qtc.QThread()
        ss.moveToThread(searcher_thread)
        ss.finished.c..(searcher_thread.quit)
        searcher_thread.start()
        # Connect to search engine
        form.textChanged.c..(ss.set_term)
        form.rP__.c..(searcher_thread.start)
        form.rP__.c..(ss.do_search)

        # Using a lambda here breaks threading:
        #form.returnPressed.connect(lambda: self.ss.do_search())


        ss.match_found.c..(form.addResult)
        ss.finished.c..(on_finished)
        ss.directory_changed.c..(on_directory_changed)
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
        s..

    ___ on_finished 
        statusBar().showMessage('Search Finished')

    ___ on_directory_changed  path):
        statusBar().showMessage(f'Searching in: {path}')

__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
