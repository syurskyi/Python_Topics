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
        lineEdit = QtGui.QLineEdit()
        validator = QtGui.QDoubleValidator(0.0, 100.0, 2, self)
        validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        lineEdit.setValidator(validator)
        button = QtGui.QPushButton("Get Value")
        button.clicked.connect(self.on_clicked)
        box = QtGui.QVBoxLayout()
        box.addWidget(lineEdit)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        if self.lineEdit.hasAcceptableInput():
            print(self.lineEdit.text())
        else:
            print("The value does not match the condition")
