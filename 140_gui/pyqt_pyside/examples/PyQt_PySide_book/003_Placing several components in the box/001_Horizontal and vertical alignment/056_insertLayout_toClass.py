# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Container Containment")
        self.resize(300, 150)
        button1 = QtWidgets.QPushButton("1")
        button2 = QtWidgets.QPushButton("2")
        button3 = QtWidgets.QPushButton("3")
        button4 = QtWidgets.QPushButton("4")
        button5 = QtWidgets.QPushButton("5")
        button6 = QtWidgets.QPushButton("6")

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(button4)
        hbox.addWidget(button5)
        hbox.addWidget(button6)

        vbox.insertLayout(1, hbox)
        self.setLayout(vbox)


if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.show()

    if app is not None:
        app.exec_()