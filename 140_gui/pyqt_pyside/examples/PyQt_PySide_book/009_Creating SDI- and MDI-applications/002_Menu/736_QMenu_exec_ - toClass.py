# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Содержимое страницы")
        self.box = QtGui.QVBoxLayout()
        self.box.addWidget(self.label)
        self.setLayout(self.box)

    def contextMenuEvent(self, event):
        act1 = QtGui.QAction("Пункт &1", self)
        act1.triggered.connect(self.on_act1)
        act2 = QtGui.QAction("Пункт &2", self)
        act2.triggered.connect(self.on_act2)
        QtGui.QMenu.exec_([act1, act2], event.globalPos(),
                          act2, self)

    def on_act1(self):
        print("on_act1")

    def on_act2(self):
        print("on_act2")


class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.w = MyWidget()
        self.setCentralWidget(self.w)


app = QtGui.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QMenu")
window.resize(500, 350)

window.show()
sys.exit(app.exec_())