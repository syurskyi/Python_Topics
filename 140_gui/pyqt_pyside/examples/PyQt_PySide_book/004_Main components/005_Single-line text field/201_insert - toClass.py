# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Class QLineEdit")
        self.resize(300, 50)
        lineEdit = QtGui.QLineEdit("Default Text")
        lineEdit.insert("New text!")
        box = QtGui.QVBoxLayout()
        box.addWidget(lineEdit)
        self.setLayout(box)
        self.show()
