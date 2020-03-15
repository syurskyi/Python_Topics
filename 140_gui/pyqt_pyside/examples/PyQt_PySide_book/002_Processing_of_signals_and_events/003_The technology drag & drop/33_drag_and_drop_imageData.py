# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.startPos = None

    def mousePressEvent(self, e):
        if e.buttons() & QtCore.Qt.LeftButton:
            self.startPos = e.pos()
        else:
            self.startPos = None
            e.ignore()
        QtGui.QLabel.mousePressEvent(self, e)

    def mouseMoveEvent(self, e):
        if self.startPos is None:
            e.ignore()
            QtGui.QLabel.mouseMoveEvent(self, e)
            return
        length = (e.pos() - self.startPos).manhattanLength()
        if length <= QtGui.QApplication.startDragDistance():
            e.ignore()
            QtGui.QLabel.mouseMoveEvent(self, e)
            return
        data = QtCore.QMimeData()
        data.setImageData(QtGui.QImage("pixmap.png"))
        drag = QtGui.QDrag(self)
        drag.setMimeData(data)
        drag.setPixmap(QtGui.QPixmap("pixmap.png"))
        drag.setHotSpot(QtCore.QPoint(1, 1))
        action = drag.exec_(QtCore.Qt.MoveAction | QtCore.Qt.CopyAction,
                            QtCore.Qt.MoveAction)
        if action == QtCore.Qt.CopyAction:
            print("Action completed CopyAction")
        elif action == QtCore.Qt.MoveAction:
            print("Action completed MoveAction")
        elif action == QtCore.Qt.IgnoreAction:
            print("Action canceled")
        QtGui.QLabel.mouseMoveEvent(self, e)

class MyLabel2(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasImage():
            e.acceptProposedAction()

    def dropEvent(self, e):
        if e.mimeData().hasImage():
            self.setPixmap(
                 QtGui.QPixmap.fromImage(e.mimeData().imageData()))
            e.accept()
        else:
            e.ignore()

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label1 = MyLabel("Click here with the mouse\n" +
             "and drag in the label below")
        self.label2 = MyLabel2("")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.label2)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("drag & drop. imageData")
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec_())