# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Horizontal Alignment")
        self.resize(450, 50)
        button1 = QtWidgets.QPushButton("1")
        button2 = QtWidgets.QPushButton("2")
        button3 = QtWidgets.QPushButton("3")
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(button1, 10, QtCore.Qt.AlignRight)
        hbox.addWidget(button2, stretch=10)
        hbox.addWidget(button3, alignment=QtCore.Qt.AlignRight)
        self.setLayout(hbox)


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