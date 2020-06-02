______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ SlowSearcherThread(?.QThread
    """A somewhat deliberately slow searcher."""

    match_found _ ?.pS.. st.
    directory_changed _ ?.pS.. st.
    finished _ ?.pS..()

    ___  -  
        s_. - ()
        term _ N..

    @?.pyqtSlot st.
    ___ set_term  term):
        term _ term

    ??.?
    ___ run 
        #print(f'Beginning search for: {self.term}')
        root _ ?.?D...rootPath()
        _search(term, root)
        finished.e..()

    ___ _search  term, pa__):
        directory_changed.e..(pa__)
        directory _ ?.?D..(pa__)
        directory.setFilter(
            directory.f.. |
            ?.?D...NDADD.. |
            ?.?D...NSL..
        )
        ___ entry __ directory.eIL..
            __ term __ entry.fP..
                print(entry.fP..())
                match_found.e..(entry.fP..())
            __ entry.isDir
                _search(term, entry.fP..())


c_ SearchForm ?.?W..

    tC.. _ ?.pS.. st.
    rP__ _ ?.pS..()

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
        ss _ SlowSearcherThread()

        # Connect to search engine
        form.tC...c..(ss.set_term)
        form.rP__.c..(ss.start)
        ss.match_found.c..(form.addResult)
        ss.finished.c..(o_f..)
        ss.directory_changed.c..(on_directory_changed)

        # End main UI code
        s..

    ___ o_f..
        sB.. .sM..('Search Finished')

    ___ on_directory_changed  pa__):
        sB.. .sM..(f'Searching in: {pa__}')


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e.. ?.e..
