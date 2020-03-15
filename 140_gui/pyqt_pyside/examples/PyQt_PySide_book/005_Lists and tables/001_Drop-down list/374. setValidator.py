# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print(comboBox.currentIndex())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtGui.QComboBox()
comboBox.setEditable(True)
comboBox.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
validator = QtGui.QRegExpValidator(
                  QtCore.QRegExp("[а-яё]+"), window)
comboBox.setValidator(validator)
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i))
button = QtGui.QPushButton("Получить индекс текущего элемента")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())