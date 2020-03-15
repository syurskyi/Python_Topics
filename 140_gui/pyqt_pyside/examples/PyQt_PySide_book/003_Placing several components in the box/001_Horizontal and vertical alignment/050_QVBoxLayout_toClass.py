from PySide import QtGui, QtCore
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Vertical alignment")
        self.resize(300, 150)
        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button3 = QtGui.QPushButton("3")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        self.setLayout(vbox)


def main():
    global c
    c = MyWindow()
    c.show()

main()