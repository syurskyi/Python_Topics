from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Class QFrame. StyledPanel")
        self.resize(300, 250)
        frame1 = QtGui.QFrame()
        frame2 = QtGui.QFrame()
        frame3 = QtGui.QFrame()
        frame1.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Plain)
        frame2.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Raised)
        frame3.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Sunken)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(frame1)
        vbox.addWidget(frame2)
        vbox.addWidget(frame3)
        self.setLayout(vbox)
