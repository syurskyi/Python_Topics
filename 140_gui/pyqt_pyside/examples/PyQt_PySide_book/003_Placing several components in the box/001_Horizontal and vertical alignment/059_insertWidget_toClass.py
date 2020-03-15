from PySide import QtGui, QtCore
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Horizonatl aligment")
        self.resize(300, 50)
        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button3 = QtGui.QPushButton("3")
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(button1)
        hbox.insertWidget(-1, button2) # Добавление в конец
        hbox.insertWidget(0, button3)  # Добавление в начало
        self.setLayout(hbox)


def main():
    global c
    c = MyWindow()
    c.show()

main()