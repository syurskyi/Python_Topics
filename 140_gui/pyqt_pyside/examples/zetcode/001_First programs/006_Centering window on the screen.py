"""
ZetCode PyQt4 tutorial 

This program centers a window 
on the screen. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PySide2.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QApplication(sys.argv)
    main = Example()
    main.show()

    if app is not None:
        app.exec_()