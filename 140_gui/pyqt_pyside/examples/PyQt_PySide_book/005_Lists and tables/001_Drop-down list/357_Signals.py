# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

def on_clicked():
    comboBox.setCurrentIndex(3)

def on_activated(v):
    print("on_activated", v)

def on_index_changed(v):
    print("on_index_changed", v)

def on_text_changed(s):
    print("on_text_changed", s)

def on_highlighted(v):
    print("on_highlighted", v)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtWidgets.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i))
comboBox.setEditable(True)
comboBox.activated[int].connect(on_activated)
comboBox.activated[str].connect(on_activated)
comboBox.currentIndexChanged[int].connect(on_index_changed)
comboBox.currentIndexChanged[str].connect(on_index_changed)
comboBox.editTextChanged[str].connect(on_text_changed)
comboBox.highlighted[int].connect(on_highlighted)
comboBox.highlighted[str].connect(on_highlighted)
button = QtWidgets.QPushButton("Выбрать элемент с индексом 3")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())