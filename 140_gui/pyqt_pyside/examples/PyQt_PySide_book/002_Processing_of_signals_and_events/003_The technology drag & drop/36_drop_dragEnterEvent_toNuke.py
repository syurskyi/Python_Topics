# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setFixedSize(280, 80)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            if e.proposedAction() == QtCore.Qt.CopyAction:
                e.acceptProposedAction()
                return
            if e.possibleActions() & QtCore.Qt.CopyAction:
                e.setDropAction(QtCore.Qt.CopyAction)
                e.accept()

    def dropEvent(self, e):
        if e.mimeData().hasText():
            self.setText(e.mimeData().text())
            e.accept()
        else:
            e.ignore()

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = MyLabel("Drag text here")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("drop. dragEnterEvent")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())