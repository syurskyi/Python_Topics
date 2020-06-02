______ ___
____ os ______ path

____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ MainWindow(qtw.QMainWindow):

    ___  -  
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here

        form _ qtw.?W..
        sCW..(form)
        form.sL.. ?.?VBL..
        filename _ qtw.?LE..
        filecontent _ ?.?TE..)
        savebutton _ qtw.?PB..(
            'Save',
            c___self.save
        )

        form.la__ .aW..(filename)
        form.la__ .aW..(filecontent)
        form.la__ .aW..(savebutton)

        # End main UI code
        s..

    ___ save 
        filename _ filename.t__()
        error _ ''
        __ no. filename:
            error _ 'Filename empty'
        ____ path.exists(filename):
            error _ f'Will not overwrite {filename}'
        ____
            ___
                w__ o..(filename, 'w') __ fh:
                    fh.w..(filecontent.tPT..
            _____ Exception __ e:
                error _ f'Cannot write file: {e}'
        __ error:
            qtw.?MB...critical(N.., 'Error', error)

__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
