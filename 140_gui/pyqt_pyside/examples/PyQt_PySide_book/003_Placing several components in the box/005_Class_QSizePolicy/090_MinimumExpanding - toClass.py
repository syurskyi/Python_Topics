from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("QSizePolicy")
        self.resize(300, 150)
        label = QtGui.QLabel("Текст надписи")
        button = QtGui.QPushButton("1")

        policy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding,
                                   QtGui.QSizePolicy.MinimumExpanding)
        label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        label.setSizePolicy(policy)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(button)
        self.setLayout(vbox)
