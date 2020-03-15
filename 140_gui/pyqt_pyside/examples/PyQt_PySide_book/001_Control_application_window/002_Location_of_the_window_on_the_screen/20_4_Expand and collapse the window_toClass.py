# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui
import sys


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Maximize and minimize a window")
        self.resize(300, 100)
        self.set_buttons()
        self.show()

    def set_buttons(self):

        self.btn_min = QtGui.QPushButton("Collapse")
        self.btn_max = QtGui.QPushButton("Expand")
        self.btn_full = QtGui.QPushButton("Full Window")
        self.btn_normal = QtGui.QPushButton("Normal Size")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.btn_min)
        vbox.addWidget(self.btn_max)
        vbox.addWidget(self.btn_full)
        vbox.addWidget(self.btn_normal)
        self.setLayout(vbox)

        # self.connect(self.btn_min, QtCore.SIGNAL("clicked()"), self.on_min)
        self.btn_min.clicked.connect(self.on_min)

        # self.connect(self.btn_max, QtCore.SIGNAL("clicked()"), self.on_max)
        self.btn_max.clicked.connect(self.on_max)

        # self.connect(self.btn_full, QtCore.SIGNAL("clicked()"), self.on_full)
        self.btn_full.clicked.connect(self.on_full)

        # self.connect(self.btn_normal, QtCore.SIGNAL("clicked()"), self.on_normal)
        self.btn_normal.clicked.connect(self.on_normal)

    def on_min(self):
        self.showMinimized()

    def on_max(self):
        self.showMaximized()

    def on_full(self):
        self.showFullScreen()

    def on_normal(self):
        self.showNormal()

def main():
    app = None

    app = QtGui.QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()