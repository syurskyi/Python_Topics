# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys


def on_toggled_button1(status):
    print("Кнопка переключена", status)


def on_clicked_button2():
    button1.toggle()


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button1 = QtGui.QPushButton("Кнопка")
button1.setCheckable(True)
button1.setChecked(True)
button2 = QtGui.QPushButton("Нажми меня")
button1.toggled["bool"].connect(on_toggled_button1)
button2.clicked.connect(on_clicked_button2)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())