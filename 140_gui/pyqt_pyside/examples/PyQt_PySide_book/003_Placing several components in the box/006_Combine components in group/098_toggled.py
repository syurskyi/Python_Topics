# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys


def on_clicked_button():
    box.setChecked(False if box.isChecked() else True)


def on_clicked(flag):
    print("on_clicked", flag)


def on_toggled(flag):
    print("on_toggled", flag)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGroupBox")
window.resize(300, 80)
radio1 = QtGui.QRadioButton("&Да")
radio2 = QtGui.QRadioButton("&Нет")
button = QtGui.QPushButton("&Переключить флажок")
mainbox = QtGui.QVBoxLayout()
box = QtGui.QGroupBox()
box.setTitle("&Вы знаете язык Python?")
box.setCheckable(True)
hbox = QtGui.QHBoxLayout()
hbox.addWidget(radio1)
hbox.addWidget(radio2)
box.setLayout(hbox)
mainbox.addWidget(box)
mainbox.addWidget(button)
window.setLayout(mainbox)
radio1.setChecked(True)
box.clicked["bool"].connect(on_clicked)
box.toggled["bool"].connect(on_toggled)
button.clicked.connect(on_clicked_button)
window.show()

sys.exit(app.exec_())