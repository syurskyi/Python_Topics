# -*- coding: utf-8 -*-
from PyQt4 import QtGui
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

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtGui.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i))
comboBox.setEditable(True)
comboBox.activated["int"].connect(on_activated)
comboBox.activated["const QString&"].connect(on_activated)
comboBox.currentIndexChanged["int"].connect(on_index_changed)
comboBox.currentIndexChanged["const QString&"].connect(on_index_changed)
comboBox.editTextChanged["const QString&"].connect(on_text_changed)
comboBox.highlighted["int"].connect(on_highlighted)
comboBox.highlighted["const QString&"].connect(on_highlighted)
button = QtGui.QPushButton("Выбрать элемент с индексом 3")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())