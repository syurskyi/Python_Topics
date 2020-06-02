______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ MainWindow(qtw.?MW..):

    ___  -  
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here

        widgets _ [
            ?.?L..("I am a label"),
            ?.?LE..(placeholderText_"I am a line edit"),
            qtw.SB..(),
            ?.?CB..("I am a checkbox"),
            qtw.?CB(editable_ st.
        ]
        container _ qtw.?W..
        sCW..(container)
        container.sL.. ?.?VBL..

        ___ widget __ widgets:
            container.la__ .aW..(widget)

        # Style switching combobox
        styles _ qtw.QStyleFactory.keys()
        style_combo _ ?.?CB..
        style_combo.aI..(styles)
        style_combo.currentTextChanged.c..(set_style)
        container.la__ .aW..(style_combo)

        # End main UI code
        s..

    ___ set_style  style):
        style _ qtw.QStyleFactory.create(style)
        qtw.?A...instance().setStyle(style)

__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
