______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor."""
        super().__init__()
        # Main UI code goes here
        main _ qtw.QTextBrowser(minimumWidth_800, minimumHeight_600)
        self.setCentralWidget(main)

        # Must come before the HTML is inserted
        main.document().setDefaultStyleSheet(
            'body {color: #333; font-size: 14px;} '
            'h2 {background: #CCF; color: #443;} '
            'h1 {background: #001133; color: white;} '
        )

        # TextBrowser background is a widget style, not a document style
        main.setStyleSheet('background-color: #EEF;')
        with open('fight_fighter2.html', 'r') as fh:
            main.insertHtml(fh.read())

        main.setOpenExternalLinks(True)

        # End main UI code
        self.s..


if __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    mw _ MainWindow()
    sys.exit(app.exec())
