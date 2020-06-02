______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ SlowSearcherThread(qtc.QThread):
    """A somewhat deliberately slow searcher."""

    match_found _ qtc.pS.. st.
    directory_changed _ qtc.pS.. st.
    finished _ qtc.pS..()

    ___  -  
        s_. - ()
        term _ N..

    @qtc.pyqtSlot st.
    ___ set_term  term):
        term _ term

    ??.?
    ___ run 
        #print(f'Beginning search for: {self.term}')
        root _ qtc.QDir.rootPath()
        _search(term, root)
        finished.e..()

    ___ _search  term, path):
        directory_changed.e..(path)
        directory _ qtc.QDir(path)
        directory.setFilter(
            directory.filter() |
            qtc.QDir.NoDotAndDotDot |
            qtc.QDir.NoSymLinks
        )
        ___ entry __ directory.entryInfoList
            __ term __ entry.filePath
                print(entry.filePath())
                match_found.e..(entry.filePath())
            __ entry.isDir
                _search(term, entry.filePath())


c_ SearchForm ?.?W..

    tC.. _ qtc.pS.. st.
    rP__ _ qtc.pS..()

    ___  -  
        s_. - ()
        sL.. ?.?VBL..
        search_term_inp _ ?.?LE..(
            placeholderText_'Search Term',
            textChanged_self.tC..,
            returnPressed_self.rP__)
        la__ .aW..(search_term_inp)
        results _ ?.?LW..
        la__ .aW..(results)
        rP__.c..(results.clear)

    ___ addResult  result):
        results.aI..(result)



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
        ss _ SlowSearcherThread()

        # Connect to search engine
        form.tC...c..(ss.set_term)
        form.rP__.c..(ss.start)
        ss.match_found.c..(form.addResult)
        ss.finished.c..(on_finished)
        ss.directory_changed.c..(on_directory_changed)

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
