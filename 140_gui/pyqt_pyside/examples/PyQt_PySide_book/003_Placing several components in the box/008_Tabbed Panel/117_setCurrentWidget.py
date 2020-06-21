# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    tab.setCurrentWidget(label2)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 150)
tab = QtGui.QTabWidget()
button = QtGui.QPushButton("Сделать вкладку 2 видимой")
button.clicked.connect(on_clicked)
label1 = QtGui.QLabel("Содержимое вкладки 1")
label2 = QtGui.QLabel("Содержимое вкладки 2")
tab.addTab(label1, "Вкладка &1")
tab.addTab(label2, "Вкладка &2")
tab.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(tab)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())