______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc


c_ FormWindow ?.?W..

    submitted _ qtc.pyqtSignal([str], [int, str])

    ___  -
        s_. - ()
        sL.. ?.?VBL..

        edit _ qtw.?LE..
        submit _ qtw.?PB..('Submit', c___self.onSubmit)

        layout().aW..(edit)
        layout().aW..(submit)

    ___ onSubmit
        __ edit.t__().isdigit
            t__ _ edit.t__()
            submitted[int, str].emit(int(t__), t__)
        ____
            submitted[str].emit(edit.t__())
        close()

c_ MainWindow ?.?W..

    ___  -
        s_. - ()
        sL.. ?.?VBL..

        label _ qtw.QLabel('Click "change" to change this text.')
        change _ qtw.?PB..("Change", c___self.onChange)
        layout().aW..(label)
        layout().aW..(change)
        s..

    @qtc.pyqtSlot()
    ___ onChange
        formwindow _ FormWindow()
        #self.formwindow.submitted.connect(self.label.setText)
        formwindow.submitted[str].c..(onSubmittedStr)
        formwindow.submitted[int, str].c..(onSubmittedIntStr)
        formwindow.s..

    @qtc.pyqtSlot(str)
    ___ onSubmittedStr  string):
        label.sT..(string)

    @qtc.pyqtSlot(int, str)
    ___ onSubmittedIntStr  integer, string):
        t__ _ f'The string {string} becomes the number {integer}'
        label.sT..(t__)


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.exit(app.exec())
