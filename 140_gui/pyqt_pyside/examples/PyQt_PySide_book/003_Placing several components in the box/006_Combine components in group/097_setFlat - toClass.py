from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QGroupBox")
        self.resize(300, 80)
        radio1 = QtGui.QRadioButton("&Да")
        radio2 = QtGui.QRadioButton("&Нет")
        mainbox = QtGui.QVBoxLayout()
        box = QtGui.QGroupBox()
        box.setTitle("&Вы знаете язык Python?")
        box.setAlignment(QtCore.Qt.AlignHCenter)
        box.setFlat(True)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(radio1)
        hbox.addWidget(radio2)
        box.setLayout(hbox)
        mainbox.addWidget(box)
        self.setLayout(mainbox)
        radio1.setChecked(True)
