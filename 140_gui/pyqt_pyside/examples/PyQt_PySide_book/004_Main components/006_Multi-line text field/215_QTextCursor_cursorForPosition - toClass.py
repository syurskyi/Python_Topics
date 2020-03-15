# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Class QTextCursor")
        self.resize(500, 250)
        self.textEdit = QtGui.QTextEdit("Default value")
        button = QtGui.QPushButton("Set the cursor")
        button.clicked.connect(self.on_clicked)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.textEdit)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        self.textEdit.setFocus()
        cur = self.textEdit.cursorForPosition(QtCore.QPoint(100, 5))
        self.textEdit.setTextCursor(cur)

if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QtGui.QApplication(sys.argv)
    main = SampleWindow()
    main.show()

    if app is not None:
        app.exec_()