# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setFixedSize(330, 80)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        self.setStyleSheet(
        "background-image: url(pixmap.png);background-repeat:no-repeat")

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.acceptProposedAction()

    def dragMoveEvent(self, e):
        if e.mimeData().hasText():
            rect = QtCore.QRect(0, 0, 50, 50)
            if e.answerRect().intersects(rect):
                e.accept(rect)
            else:
                e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasText():
            self.setText(e.mimeData().text())
            e.accept()
        else:
            e.ignore()

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = MyLabel("Drag the text to an image")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("drop. dragMoveEvent")
    window.resize(350, 100)
    window.show()
    sys.exit(app.exec_())