from PySide import QtGui, QtCore
import sys


class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Vertical alignment")
        self.resize(300, 150)
        button1 = QtGui.QPushButton("Bottom")
        button2 = QtGui.QPushButton("No")
        button3 = QtGui.QPushButton("Top")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(button1, alignment=QtCore.Qt.AlignBottom)
        vbox.addWidget(button2)
        vbox.addWidget(button3, alignment=QtCore.Qt.AlignTop)
        self.setLayout(vbox)


def main():
    global c
    c = MyWindow()
    c.show()

main()