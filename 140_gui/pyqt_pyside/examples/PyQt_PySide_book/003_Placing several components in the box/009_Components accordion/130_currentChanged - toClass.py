
def on_current_changed(index):
    print("on_current_changed", index)
from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Class QToolBox")
        self.resize(300, 250)
        toolBox = QtGui.QToolBox()
        toolBox.currentChanged["int"].connect(on_current_changed)
        toolBox.addItem(QtGui.QLabel("Content tab 1"), "inset &1")
        toolBox.addItem(QtGui.QLabel("Content tab 2"), "inset &2")
        toolBox.setCurrentIndex(0)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(toolBox)
        self.setLayout(vbox)
