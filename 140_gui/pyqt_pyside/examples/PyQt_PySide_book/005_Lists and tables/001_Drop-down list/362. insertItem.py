# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print("Текст:", comboBox.currentText())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtGui.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i), i)
ico = window.style().standardIcon(QtGui.QStyle.SP_MessageBoxCritical)
comboBox.insertItem(0, ico, "Пункт 11", 11)
comboBox.insertItem(1, "Пункт 12", 12)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())