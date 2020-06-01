______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc

c_ MainWindow(qtw.QWidget):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        self.sL..(qtw.QVBoxLayout())

        data _ [
            'Hamburger', 'Cheeseburger',
            'Chicken Nuggets', 'Hot Dog', 'Fish Sandwich'
        ]

        listwidget _ qtw.QListWidget()
        listwidget.addItems(data)
        combobox _ qtw.QComboBox()
        combobox.addItems(data)
        self.layout().aW..(listwidget)
        self.layout().aW..(combobox)

        # make the list widget editable
        for i in range(listwidget.count()):
            item _ listwidget.item(i)
            item.setFlags(item.flags() | qtc.__.ItemIsEditable)


        # The same, but with a model

        model _ qtc.QStringListModel(data)

        listview _ qtw.QListView()
        listview.sM..(model)
        model_combobox _ qtw.QComboBox()
        model_combobox.sM..(model)

        self.layout().aW..(listview)
        self.layout().aW..(model_combobox)

        # End main UI code
        self.s..



__ __name__ == '__main__':
    app _ qtw.?A..(___.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.exit(app.exec())
