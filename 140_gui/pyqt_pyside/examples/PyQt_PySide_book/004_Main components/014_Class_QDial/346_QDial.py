# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(dial.value())
    print(dial.sliderPosition())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QDial")
window.resize(300, 300)
dial = QtGui.QDial()
dial.setRange(0, 100)
dial.setValue(40)
dial.setNotchesVisible(True)
dial.setNotchTarget(2.0)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(dial)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())