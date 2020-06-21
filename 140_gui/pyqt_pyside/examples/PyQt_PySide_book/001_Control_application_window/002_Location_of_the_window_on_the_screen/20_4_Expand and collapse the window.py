# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.btnMin = QtGui.QPushButton("Collapse")
        self.btnMax = QtGui.QPushButton("Expand")
        self.btnFull = QtGui.QPushButton("Full Window")
        self.btnNormal = QtGui.QPushButton("Normal Size")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.btnMin)
        vbox.addWidget(self.btnMax)
        vbox.addWidget(self.btnFull)
        vbox.addWidget(self.btnNormal)
        self.setLayout(vbox)
        self.connect(self.btnMin, QtCore.SIGNAL("clicked()"),
                     self.on_min)
        self.connect(self.btnMax, QtCore.SIGNAL("clicked()"),
                     self.on_max)
        self.connect(self.btnFull, QtCore.SIGNAL("clicked()"),
                     self.on_full)
        self.connect(self.btnNormal, QtCore.SIGNAL("clicked()"),
                     self.on_normal)

    def on_min(self):
        self.showMinimized()

    def on_max(self):
        self.showMaximized()

    def on_full(self):
        self.showFullScreen()

    def on_normal(self):
        self.showNormal()



app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Maximize and minimize a window")
window.resize(300, 100)
window.show()
sys.exit(app.exec_())