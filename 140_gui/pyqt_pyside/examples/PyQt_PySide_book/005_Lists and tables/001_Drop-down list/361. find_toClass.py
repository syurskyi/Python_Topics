# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys

def on_clicked():
    print(comboBox.findText("пункт 3",
                        flags=QtCore.Qt.MatchFixedString))
    print(comboBox.findText("[а-яёА-ЯЁ]+",
                             flags=QtCore.Qt.MatchRegExp))
    print(comboBox.findText("Пункт 80"))
    print(comboBox.findData(10))

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtWidgets.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i), i)
comboBox.addItem("Пункт".format(i), 11)
button = QtWidgets.QPushButton("Найти элементы")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())