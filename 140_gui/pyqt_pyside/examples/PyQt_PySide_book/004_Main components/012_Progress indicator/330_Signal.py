# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    progressBar.setValue(70)

def on_value_changed(n):
    print("on_value_changed", n)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QProgressBar")
window.resize(300, 100)
progressBar = QtGui.QProgressBar()
progressBar.setRange(0, 100)
progressBar.setValue(30)
progressBar.valueChanged["int"].connect(on_value_changed)
button = QtGui.QPushButton("Изменить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(progressBar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())