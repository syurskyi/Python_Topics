# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    style = window.style()
    icon = style.standardIcon(QtGui.QStyle.SP_DriveNetIcon)
    tab.setTabIcon(0, icon)
    button.setEnabled(False)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 150)
tab = QtGui.QTabWidget()
button = QtGui.QPushButton("Установить иконку")
button.clicked.connect(on_clicked)
tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(tab)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())