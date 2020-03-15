from PySide import QtGui, QtCore
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Indent control")
        self.resize(400, 50)
        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button3 = QtGui.QPushButton("3")
        button4 = QtGui.QPushButton("4")
        button5 = QtGui.QPushButton("5")
        button6 = QtGui.QPushButton("6")
        vbox = QtGui.QVBoxLayout()

        hbox = QtGui.QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.setSpacing(0)
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        vbox.addLayout(hbox)

        hbox2 = QtGui.QHBoxLayout()
        hbox2.setContentsMargins(30, 30, 30, 30)
        hbox2.setSpacing(20)
        hbox2.addWidget(button4)
        hbox2.addWidget(button5)
        hbox2.addWidget(button6)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)


def main():
    global c
    c = MyWindow()
    c.show()

main()
# Result: