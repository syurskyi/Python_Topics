from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QGroupBox")
        self.resize(300, 80)
        radio1 = QtGui.QRadioButton("&Yes")
        radio2 = QtGui.QRadioButton("&No")
        mainbox = QtGui.QVBoxLayout()
        box = QtGui.QGroupBox("&Do you know Python?")
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(radio1)
        hbox.addWidget(radio2)
        box.setLayout(hbox)
        mainbox.addWidget(box)
        self.setLayout(mainbox)
        radio1.setChecked(True)
