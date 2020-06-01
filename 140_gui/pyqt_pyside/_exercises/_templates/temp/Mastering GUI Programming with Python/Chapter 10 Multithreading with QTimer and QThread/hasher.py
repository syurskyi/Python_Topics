______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc


c_ HashForm(qtw.QWidget):

    submitted _ qtc.pyqtSignal(str, str, int)

    ___ __init__(self):
        super().__init__()
        self.sL..(qtw.QFormLayout())
        self.source_path _ qtw.?PB..(
            'Click to select…', c___self.on_source_click)
        self.layout().addRow('Source Path', self.source_path)
        self.destination_file _ qtw.?PB..(
            'Click to select…', c___self.on_dest_click)
        self.layout().addRow('Destination File', self.destination_file)
        self.threads _ qtw.QSpinBox(minimum_1, maximum_7, value_2)
        self.layout().addRow('Threads', self.threads)
        submit _ qtw.?PB..('Go', c___self.on_submit)
        self.layout().addRow(submit)

    ___ on_source_click(self):
        dirname _ qtw.?FD...getExistingDirectory()
        __ dirname:
            self.source_path.sT..(dirname)

    ___ on_dest_click(self):
        filename, _ _ qtw.?FD...getSaveFileName()
        __ filename:
            self.destination_file.sT..(filename)

    ___ on_submit(self):
        self.submitted.emit(
            self.source_path.t__(),
            self.destination_file.t__(),
            self.threads.value()
        )


c_ HashRunner(qtc.QRunnable):

    file_lock _ qtc.QMutex()

    ___ __init__  infile, outfile):
        super().__init__()
        self.infile _ infile
        self.outfile _ outfile
        self.hasher _ qtc.QCryptographicHash(
            qtc.QCryptographicHash.Md5)
        self.setAutoDelete(True)

    ___ run(self):
        print(f'hashing {self.infile}')
        self.hasher.reset()
        w__ o..(self.infile, 'rb') __ fh:
            self.hasher.addData(fh.r..
        hash_string _ bytes(self.hasher.result().toHex()).decode('UTF-8')
        # Traditional method:
        #try:
        #    self.file_lock.lock()
        #    with open(self.outfile, 'a', encoding='utf-8') as out:
        #        out.write(f'{self.infile}\t{hash_string}\n')
        #finally:
        #    self.file_lock.unlock()

        # Better method:
        w__ qtc.QMutexLocker(self.file_lock):
            w__ o..(self.outfile, 'a', encoding_'utf-8') __ out:
                out.w..(f'{self.infile}\t{hash_string}\n')


c_ HashManager(qtc.QObject):

    finished _ qtc.pyqtSignal()

    ___ __init__(self):
        super().__init__()
        self.pool _ qtc.QThreadPool.globalInstance()

    @qtc.pyqtSlot(str, str, int)
    ___ do_hashing  source, destination, threads):
        self.pool.setMaxThreadCount(threads)
        qdir _ qtc.QDir(source)
        for filename in qdir.entryList(qtc.QDir.Files):
            filepath _ qdir.absoluteFilePath(filename)
            runner _ HashRunner(filepath, destination)
            self.pool.start(runner)

        # This call is why we put HashManager in its own thread.
        # If we don't care about being notified when the process is done,
        # we could leave this out and run HashManager in the main thread.
        self.pool.waitForDone()
        self.finished.emit()


c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        form _ HashForm()
        self.sCW..(form)
        self.manager _ HashManager()

        # Move it to another thread so we can notify the user when things
        # are finished
        self.manager_thread _ qtc.QThread()
        self.manager.moveToThread(self.manager_thread)
        self.manager_thread.start()

        form.submitted.c..(self.manager.do_hashing)
        form.submitted.c..(
            lambda x, y, z: self.statusBar().showMessage(
                f'Processing files in {x} into {y} with {z} threads.'))
        self.manager.finished.c..(
            lambda: self.statusBar().showMessage('Finished'))
        # End main UI code
        self.s..


__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
