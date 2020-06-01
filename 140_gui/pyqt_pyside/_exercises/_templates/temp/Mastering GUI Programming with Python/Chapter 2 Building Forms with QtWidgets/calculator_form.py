______ sys
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
        lcd _ qtw.QLCDNumber(self)
        self.layout().aW..(lcd)

        history _ qtw.QLineEdit  placeholderText_'History')
        self.layout().aW..(history)

        button_texts _ [
            'Clear', 'BackSpace', 'Mem', 'Mem Clear',
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '×',
            '.', '0', '=', '÷'
        ]
        button_layout _ qtw.QGridLayout()
        self.layout().addLayout(button_layout)
        buttons _ []
        for num, button_text in enumerate(button_texts):
            button _ qtw.?PB..(button_text, self)
            button.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
            buttons.append(button)
            row _ num // 4
            column _ num % 4
            button_layout.aW..(button, row, column)
        # End main UI code
        self.s..


__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
