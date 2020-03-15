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
        data.setText("Drag and drop text")
        drag = QtGui.QDrag(self)
        drag.setMimeData(data)
        drag.setPixmap(QtGui.QPixmap("pixmap.png"))
        drag.setHotSpot(QtCore.QPoint(40, 40))
        drag.setDragCursor(QtGui.QPixmap("cursor.png"),
                           QtCore.Qt.MoveAction)
        drag.setDragCursor(QtGui.QPixmap("cursor.png"),
                           QtCore.Qt.CopyAction)
        self.connect(drag, QtCore.SIGNAL("actionChanged(Qt::DropAction)"),
                     self.on_action_changed)
        action = drag.exec_(QtCore.Qt.MoveAction | QtCore.Qt.CopyAction,
                            QtCore.Qt.MoveAction)
        if action == QtCore.Qt.CopyAction:
            print("Action completed CopyAction")
        elif action == QtCore.Qt.MoveAction:
            print("Action completed MoveAction")
        elif action == QtCore.Qt.IgnoreAction:
            print("Action canceled")
        QtGui.QLabel.mouseMoveEvent(self, e)

    def on_action_changed(self, action):
        if action == QtCore.Qt.CopyAction:
            print("Action changed to CopyAction")
        elif action == QtCore.Qt.MoveAction:
            print("Action changed to MoveAction")

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = MyLabel("Click here with the mouse\n" +
             "and drag it to a text editor\n(for example, to WordPad)")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("drag")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())