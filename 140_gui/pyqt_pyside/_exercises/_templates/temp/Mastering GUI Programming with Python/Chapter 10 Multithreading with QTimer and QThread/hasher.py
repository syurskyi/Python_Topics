______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc


c_ HashForm ?.?W..

    submitted _ qtc.pS..(str, str, int)

    ___  - 
        s_. - ()
        sL..(qtw.QFormLayout())
        source_path _ qtw.?PB..(
            'Click to select…', c___self.on_source_click)
        la__ .aR..('Source Path', source_path)
        destination_file _ qtw.?PB..(
            'Click to select…', c___self.on_dest_click)
        la__ .aR..('Destination File', destination_file)
        threads _ qtw.SB..(minimum_1, maximum_7, value_2)
        la__ .aR..('Threads', threads)
        submit _ qtw.?PB..('Go', c___self.on_submit)
        la__ .aR..(submit)

    ___ on_source_click
        dirname _ qtw.?FD...getExistingDirectory()
        __ dirname:
            source_path.sT..(dirname)

    ___ on_dest_click
        filename, _ _ qtw.?FD...getSaveFileName()
        __ filename:
            destination_file.sT..(filename)

    ___ on_submit
        submitted.e..(
            source_path.t__(),
            destination_file.t__(),
            threads.value()
        )


c_ HashRunner(qtc.QRunnable):

    file_lock _ qtc.QMutex()

    ___  -   infile, outfile):
        s_. - ()
        infile _ infile
        outfile _ outfile
        hasher _ qtc.QCryptographicHash(
            qtc.QCryptographicHash.Md5)
        setAutoDelete( st.

    ___ run
        print(f'hashing {infile}')
        hasher.reset()
        w__ o..(infile, 'rb') __ fh:
            hasher.addData(fh.r..
        hash_string _ bytes(hasher.result().toHex()).decode('UTF-8')
        # Traditional method:
        #try:
        #    self.file_lock.lock()
        #    with open(self.outfile, 'a', encoding='utf-8') as out:
        #        out.write(f'{self.infile}\t{hash_string}\n')
        #finally:
        #    self.file_lock.unlock()

        # Better method:
        w__ qtc.QMutexLocker(file_lock):
            w__ o..(outfile, 'a', encoding_'utf-8') __ out:
                out.w..(f'{infile}\t{hash_string}\n')


c_ HashManager(qtc.?O..):

    finished _ qtc.pS..()

    ___  - 
        s_. - ()
        pool _ qtc.QThreadPool.globalInstance()

    @qtc.pyqtSlot(str, str, int)
    ___ do_hashing  source, destination, threads):
        pool.setMaxThreadCount(threads)
        qdir _ qtc.?D..(source)
        ___ filename __ qdir.entryList(qtc.?D...Files):
            filepath _ qdir.absoluteFilePath(filename)
            runner _ HashRunner(filepath, destination)
            pool.start(runner)

        # This call is why we put HashManager in its own thread.
        # If we don't care about being notified when the process is done,
        # we could leave this out and run HashManager in the main thread.
        pool.waitForDone()
        finished.e..()


c_ MainWindow(qtw.?MW..):

    ___  - 
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here
        form _ HashForm()
        sCW..(form)
        manager _ HashManager()

        # Move it to another thread so we can notify the user when things
        # are finished
        manager_thread _ qtc.QThread()
        manager.moveToThread(manager_thread)
        manager_thread.start()

        form.submitted.c..(manager.do_hashing)
        form.submitted.c..(
            l___ x, y, z: statusBar().showMessage(
                f'Processing files in {x} into {y} with {z} threads.'))
        manager.finished.c..(
            l___: statusBar().showMessage('Finished'))
        # End main UI code
        s..


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e.. ?.e..
