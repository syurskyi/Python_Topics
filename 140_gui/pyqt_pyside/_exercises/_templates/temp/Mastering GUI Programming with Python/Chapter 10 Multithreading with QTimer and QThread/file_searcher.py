______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ SlowSearcher(qtc.?O..):
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
    ___ do_search 
        #print(f'Beginning search for: {self.term}')
        root _ qtc.?D...rootPath()
        _search(term, root)
        finished.e..()

    ___ _search  term, pa__):
        directory_changed.e..(pa__)
        directory _ qtc.?D..(pa__)
        directory.setFilter(
            directory.filter() |
            qtc.?D...NoDotAndDotDot |
            qtc.?D...NoSymLinks
        )
        ___ entry __ directory.entryInfoList
            __ term __ entry.fP..
                print(entry.fP..())
                match_found.e..(entry.fP..())
            __ entry.isDir
                _search(term, entry.fP..())


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


c_ MainWindow(qtw.?MW..):

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
        form.tC...c..(ss.set_term)
        form.rP__.c..(searcher_thread.start)
        form.rP__.c..(ss.do_search)

        # Using a lambda here breaks threading:
        #form.returnPressed.connect(lambda: self.ss.do_search())


        ss.match_found.c..(form.addResult)
        ss.finished.c..(o_f..)
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

    ___ o_f..
        statusBar().showMessage('Search Finished')

    ___ on_directory_changed  pa__):
        statusBar().showMessage(f'Searching in: {pa__}')

__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e.. ?.e..
