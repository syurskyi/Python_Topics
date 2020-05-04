import sys
from PySide2.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PySide2.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    #
    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QApplication(sys.argv)
    main =Example()
    main.show()

    if app is not None:
        app.exec_()