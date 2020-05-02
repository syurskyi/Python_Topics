# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Class QLineEdit")
        self.resize(300, 100)
        self.lineEdit = QtGui.QLineEdit()
        self.lineEdit.cursorPositionChanged["int","int"].connect(self.on_changed)
        self.lineEdit.editingFinished.connect(self.on_finished)
        self.lineEdit.returnPressed.connect(self.on_return)
        self.lineEdit.selectionChanged.connect(self.on_selection)
        self.lineEdit.selectionChanged.connect(self.on_selection)
        self.lineEdit.tC..["const QString&"].connect(self.on_text_changed)
        self.lineEdit.textEdited["const QString&"].connect(self.on_text_edited)
        lineEdit2 = QtGui.QLineEdit()
        button = QtGui.QPushButton("Edit the text programmatically")
        button.clicked.connect(self.on_clicked)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.lineEdit)
        box.addWidget(lineEdit2)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        self.lineEdit.setText("New text")

    def on_changed(self, old_pos, new_pos):
        print("on_changed", old_pos, new_pos)

    def on_finished(self):
        print("on_finished")

    def on_return(self):
        print("on_return")

    def on_selection(self):
        print("on_selection")

    def on_text_changed(self, s):
        print("on_text_changed", s)

    def on_text_edited(self, s):
        print("on_text_edited", s)