______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc


c_ FormWindow ?.?W..

    submitted _ qtc.pS..([str], [int, str])

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
            submitted[int, str].e..(int(t__), t__)
        ____
            submitted[str].e..(edit.t__())
        c..

c_ MainWindow ?.?W..

    ___  -
        s_. - ()
        sL.. ?.?VBL..

        label _ ?.?L..('Click "change" to change this text.')
        change _ qtw.?PB..("Change", c___self.onChange)
        layout().aW..(label)
        layout().aW..(change)
        s..

    ??.?
    ___ onChange
        formwindow _ FormWindow()
        #self.formwindow.submitted.connect(self.label.setText)
        formwindow.submitted[str].c..(onSubmittedStr)
        formwindow.submitted[int, str].c..(onSubmittedIntStr)
        formwindow.s..

    @qtc.pyqtSlot st.
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
    ___.e..(app.e..
