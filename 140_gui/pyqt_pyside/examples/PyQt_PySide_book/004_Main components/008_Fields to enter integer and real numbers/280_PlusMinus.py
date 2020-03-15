# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(spinBox.value())

app = QtGui.QApplication(sys.argv)
app.setStyle("windows")
window = QtGui.QWidget()
window.setWindowTitle("Класс QSpinBox")
window.resize(300, 70)
spinBox = QtGui.QSpinBox()
spinBox.setMinimumHeight(35)
spinBox.setRange(0, 100)
spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(spinBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())