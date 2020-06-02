______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc

c_ MainWindow ?.?W..

    ___  -
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here
        sL.. ?.?VBL..

        data _ [
            'Hamburger', 'Cheeseburger',
            'Chicken Nuggets', 'Hot Dog', 'Fish Sandwich'
        ]

        listwidget _ ?.?LW..
        listwidget.aI..(data)
        combobox _ ?.?CB..
        combobox.aI..(data)
        layout().aW..(listwidget)
        layout().aW..(combobox)

        # make the list widget editable
        ___ i __ ra..(listwidget.count()):
            item _ listwidget.item(i)
            item.setFlags(item.flags() | qtc.__.IIE..)


        # The same, but with a model

        model _ qtc.QStringListModel(data)

        listview _ qtw.QListView()
        listview.sM..(model)
        model_combobox _ ?.?CB..
        model_combobox.sM..(model)

        layout().aW..(listview)
        layout().aW..(model_combobox)

        # End main UI code
        s..



__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
