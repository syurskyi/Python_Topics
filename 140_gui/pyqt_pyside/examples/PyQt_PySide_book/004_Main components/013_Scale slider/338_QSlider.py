# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print(slider.value())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QSlider")
window.resize(300, 100)
slider = QtGui.QSlider(QtCore.Qt.Horizontal)
slider.setRange(0, 100)
slider.setValue(50)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(slider)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())