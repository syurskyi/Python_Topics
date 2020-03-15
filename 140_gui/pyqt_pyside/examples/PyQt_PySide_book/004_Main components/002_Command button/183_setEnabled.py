# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked_button2():
    print("Кнопка нажата")
    button1.setEnabled(not button1.isEnabled())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button1 = QtGui.QPushButton("Кнопка")
button2 = QtGui.QPushButton("Нажми меня")
button2.clicked.connect(on_clicked_button2)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())