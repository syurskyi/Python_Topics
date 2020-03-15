# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print(scrollBar.value())
    print(scrollBar.sliderPosition())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QScrollBar")
window.resize(300, 100)
scrollBar = QtGui.QScrollBar(QtCore.Qt.Horizontal)
scrollBar.setRange(0, 100)
scrollBar.setValue(40)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(scrollBar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())