______ ___
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

        widgets _ [
            qtw.QLabel("I am a label"),
            ?.?LE..(placeholderText_"I am a line edit"),
            qtw.QSpinBox(),
            qtw.QCheckBox("I am a checkbox"),
            qtw.QComboBox(editable_True)
        ]
        container _ qtw.?W..
        sCW..(container)
        container.sL.. ?.?VBL..

        ___ widget __ widgets:
            container.layout().aW..(widget)

        # Style switching combobox
        styles _ qtw.QStyleFactory.keys()
        style_combo _ qtw.QComboBox()
        style_combo.addItems(styles)
        style_combo.currentTextChanged.c..(set_style)
        container.layout().aW..(style_combo)

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
    ___.exit(app.exec())
