

def on_clicked_group1(id_button):
    print("group1", id_button)

def on_clicked_group2(id_button):
    print("group2", id_button)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Класс QButtonGroup")
window.resize(300, 80)
radio1 = QtGui.QRadioButton("Да")
radio2 = QtGui.QRadioButton("Нет")
radio3 = QtGui.QRadioButton("Да")
radio4 = QtGui.QRadioButton("Нет")
buttonGroup1 = QtGui.QButtonGroup(window)
buttonGroup1.addButton(radio1, 1)
buttonGroup1.addButton(radio2, 2)
buttonGroup1.buttonClicked["int"].connect(on_clicked_group1)
buttonGroup2 = QtGui.QButtonGroup(window)
buttonGroup2.addButton(radio3, 1)
buttonGroup2.addButton(radio4, 2)
buttonGroup2.buttonClicked["int"].connect(on_clicked_group2)
label1 = QtGui.QLabel("Вы знаете язык Python?")
label2 = QtGui.QLabel("Вы знаете язык PyQt?")
box = QtGui.QVBoxLayout()
box.addWidget(label1)
box.addWidget(radio1)
box.addWidget(radio2)
box.addWidget(label2)
box.addWidget(radio3)
box.addWidget(radio4)
window.setLayout(box)
radio1.setChecked(True)
radio3.setChecked(True)
