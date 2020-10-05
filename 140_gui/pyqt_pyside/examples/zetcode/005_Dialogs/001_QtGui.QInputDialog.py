"""
ZetCode PyQt4 tutorial 

In this example, we receive data from
a QtGui.QInputDialog dialog. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PySide2 import QtGui
from PySide2 import QtWidgets


class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.btn = QtWidgets.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QtWidgets.QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog',
                                              'Enter your name:')

        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QtWidgets.QApplication(sys.argv)
    main = Example()
    main.show()

    if app is not None:
        app.exec_()