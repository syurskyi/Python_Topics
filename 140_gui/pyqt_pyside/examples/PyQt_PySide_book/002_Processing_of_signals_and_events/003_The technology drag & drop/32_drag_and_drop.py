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
        self.connect(drag, QtCore.SIGNAL("actionChanged(Qt::DropAction)"),
                     self.on_action_changed)
        self.connect(drag, QtCore.SIGNAL("targetChanged(QWidget *)"),
                     self.on_target_changed)
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

    def on_target_changed(self, target):
        print("Component-receiver is changed", type(target))

class MyLabel2(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setFixedSize(280, 80)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.acceptProposedAction()

    def dropEvent(self, e):
        if e.mimeData().hasText():
            self.setText(e.mimeData().text())
            e.accept()
        else:
            e.ignore()

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label1 = MyLabel("Click here with the mouse\n" +
             "and drag to a text editor\n(for example, to WordPad)" +
             "\nor on the label below")
        self.label2 = MyLabel2("Drag text here")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.label2)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("drag & drop")
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec_())