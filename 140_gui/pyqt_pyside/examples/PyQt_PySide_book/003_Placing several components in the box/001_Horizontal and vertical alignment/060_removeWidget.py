# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("removeWidget")
window.resize(300, 150)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button3 = QtWidgets.QPushButton("3")
button4 = QtWidgets.QPushButton("4")
button5 = QtWidgets.QPushButton("5")
button6 = QtWidgets.QPushButton("6")

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
vbox.addWidget(button3)

hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button4)
hbox.addWidget(button5)
hbox.addWidget(button6)
vbox.addLayout(hbox)

hbox.removeWidget(button5)   # Удаление из контейнера hbox
vbox.addWidget(button5)      # Добавление в контейнер vbox

window.setLayout(vbox)
window.show()
sys.exit(app.exec_())