# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys

def on_clicked():
    print("Текст:", comboBox.currentText())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtWidgets.QComboBox()
L = []
for i in range(1, 11):
    L.append("Пункт {0}".format(i))
model = QtCore.QStringListModel(L)
comboBox.setModel(model)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())