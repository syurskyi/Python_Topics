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
comboBox.setIconSize(QtCore.QSize(32, 32))
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i))
ico = window.style().standardIcon(QtGui.QStyle.SP_MessageBoxCritical)
comboBox.insertItem(0, ico, "Пункт 11")
button = QtGui.QPushButton("Получить индекс")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())