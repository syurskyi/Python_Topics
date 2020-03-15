# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyEvent(QtCore.QEvent):
    idType = QtCore.QEvent.registerEventType()
    def __init__(self, data):
        QtCore.QEvent.__init__(self, MyEvent.idType)
        self.data = data
    def get_data(self):
        return self.data

class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)

    def customEvent(self, e):
        if e.type() == MyEvent.idType:
            self.setText("Received data: {0}".format(e.get_data()))

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
        QtCore.QCoreApplication.sendEvent(self.label, MyEvent("512"))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("sendEvent")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())