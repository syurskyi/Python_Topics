from PySide import QtGui, QtCore
import sys


class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Horizontal Alignment")
        self.resize(400, 50)
        button1 = QtGui.QPushButton("Right")
        button2 = QtGui.QPushButton("No")
        button3 = QtGui.QPushButton("Left")
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(button1, alignment=QtCore.Qt.AlignRight)
        hbox.addWidget(button2)
        hbox.addWidget(button3, alignment=QtCore.Qt.AlignLeft)
        self.setLayout(hbox)


def main():
    global c
    c = MyWindow()
    c.show()

main()