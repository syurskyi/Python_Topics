from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QSplitter")
        self.resize(400, 250)
        splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        label1 = QtGui.QLabel("Содержимое 1")
        label2 = QtGui.QLabel("Содержимое 2")
        label3 = QtGui.QLabel("Содержимое 3")
        label1.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        label2.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        label3.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        splitter2.addWidget(label1)
        splitter2.addWidget(label2)
        splitter.addWidget(splitter2)
        splitter.addWidget(label3)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(splitter)
        self.setLayout(vbox)
