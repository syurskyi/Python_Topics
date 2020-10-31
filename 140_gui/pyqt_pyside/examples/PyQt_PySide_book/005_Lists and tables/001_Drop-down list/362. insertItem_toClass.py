# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

def on_clicked():
    print("Текст:", comboBox.currentText())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtWidgets.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i), i)
ico = window.style().standardIcon(
    QtWidgets.QStyle.SP_MessageBoxCritical)
comboBox.insertItem(0, ico, "Пункт 11", 11)
comboBox.insertItem(1, "Пункт 12", 12)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())