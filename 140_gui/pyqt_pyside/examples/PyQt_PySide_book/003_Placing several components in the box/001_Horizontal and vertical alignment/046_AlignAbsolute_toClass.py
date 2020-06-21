from PyQt5 import QtCore, QtWidgets, QtGui
import sys

class SampleWindow(QtWidgets.QWidget):

    def __init__(self):
        super(SampleWindow, self).__init__()

        self.initUI()

    def initUI(self):

        button1 = QtWidgets.QPushButton("1")
        button2 = QtWidgets.QPushButton("2")
        button3 = QtWidgets.QPushButton("3")
        button4 = QtWidgets.QPushButton("4")
        button5 = QtWidgets.QPushButton("5")
        button6 = QtWidgets.QPushButton("6")
        #
        self.setLayoutDirection(QtCore.Qt.RightToLeft)
        vbox = QtWidgets.QVBoxLayout()

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3, alignment=QtCore.Qt.AlignLeft)
        vbox.addLayout(hbox)

        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.addWidget(button4)
        hbox2.addWidget(button5)
        hbox2.addWidget(button6,
                        alignment=QtCore.Qt.AlignAbsolute | QtCore.Qt.AlignLeft)
        vbox.addLayout(hbox2)
        # window = QtWidgets.QWidget()
        self.setWindowTitle("AlignAbsolute")
        self.resize(400, 150)
        self.setLayout(vbox)
        self.show()
