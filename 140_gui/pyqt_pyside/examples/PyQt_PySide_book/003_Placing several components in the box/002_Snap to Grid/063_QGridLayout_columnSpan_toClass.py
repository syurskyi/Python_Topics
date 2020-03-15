from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()


        self.setWindowTitle("Выравнивание по сетке")
        self.resize(300, 50)
        button1 = QtGui.QPushButton("1")
        button3 = QtGui.QPushButton("3")
        button4 = QtGui.QPushButton("4")
        grid = QtGui.QGridLayout()
        grid.addWidget(button1, 0, 0, 1, 2)
        grid.addWidget(button3, 1, 0)
        grid.addWidget(button4, 1, 1)
        self.setLayout(grid)
