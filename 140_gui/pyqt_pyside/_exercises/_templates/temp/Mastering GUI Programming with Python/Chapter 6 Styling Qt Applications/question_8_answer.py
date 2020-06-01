______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ QtCore __ qtc


c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        widgets _ [
            qtw.QLabel("I am a label"),
            qtw.QLineEdit(placeholderText_"I am a line edit"),
            qtw.QSpinBox(),
            qtw.QCheckBox("I am a checkbox"),
            qtw.QComboBox(editable_True)
        ]
        container _ qtw.QWidget()
        self.sCW..(container)
        container.setLayout(qtw.QVBoxLayout())

        for widget in widgets:
            container.layout().addWidget(widget)

        # Style switching combobox
        styles _ qtw.QStyleFactory.keys()
        style_combo _ qtw.QComboBox()
        style_combo.addItems(styles)
        style_combo.currentTextChanged.c..(self.set_style)
        container.layout().addWidget(style_combo)

        # End main UI code
        self.s..

    ___ set_style  style):
        style _ qtw.QStyleFactory.create(style)
        qtw.?A...instance().setStyle(style)

__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
