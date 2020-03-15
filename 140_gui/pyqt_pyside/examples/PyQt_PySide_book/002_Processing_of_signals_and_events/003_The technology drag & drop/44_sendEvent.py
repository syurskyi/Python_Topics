# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)

    def mousePressEvent(self, e):
        if e.buttons() & QtCore.Qt.LeftButton:
            print("Left mouse button pressed")
        self.setText("X: {0}, Y: {1}".format(e.x(), e.y()))
        e.ignore()
        QtGui.QLabel.mousePressEvent(self, e)

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = MyLabel("")
        self.button = QtGui.QPushButton("send a message")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        e = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress,
                              QtCore.QPoint(5, 5), QtCore.Qt.LeftButton,
                              QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)
        QtCore.QCoreApplication.sendEvent(self.label, e)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    window = MyWindow()
    window.setWindowTitle("sendEvent")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())