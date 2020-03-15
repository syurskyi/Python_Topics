from PySide import QtGui, QtCore
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Horizontal Alignment")
        self.resize(450, 50)
        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button3 = QtGui.QPushButton("3")
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(button1, 10, QtCore.Qt.AlignRight)
        hbox.addWidget(button2, stretch=10)
        hbox.addWidget(button3, alignment=QtCore.Qt.AlignRight)
        self.setLayout(hbox)


def main():
    global c
    c = MyWindow()
    c.show()

main()