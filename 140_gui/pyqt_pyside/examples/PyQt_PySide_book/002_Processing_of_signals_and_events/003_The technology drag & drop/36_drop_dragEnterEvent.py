# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setFixedSize(280, 80)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtWidgets.QFrame.Box |
                           QtWidgets.QFrame.Plain)
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

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = MyLabel("Перетащите сюда текст")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("drop. dragEnterEvent")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())