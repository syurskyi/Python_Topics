# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    toolBox.setCurrentIndex(1)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QToolBox")
window.resize(300, 250)
toolBox = QtGui.QToolBox()
button = QtGui.QPushButton("Сделать вкладку 2 видимой")
button.clicked.connect(on_clicked)
toolBox.addItem(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
toolBox.addItem(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
toolBox.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(toolBox)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())