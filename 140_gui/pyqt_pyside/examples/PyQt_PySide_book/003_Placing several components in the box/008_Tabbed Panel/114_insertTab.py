# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def insert_tab():
    tab.setUpdatesEnabled(False) # Для предотвращения мерцания
    ind = tab.insertTab(0, QtGui.QLabel("Содержимое вкладки 3"),
                        "Вкладка &3")
    tab.setCurrentIndex(ind)
    tab.setUpdatesEnabled(True) # Устанавливаем обратно
    button.setEnabled(False)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 150)
tab = QtGui.QTabWidget()
button = QtGui.QPushButton("Добавить вкладку")
button.clicked.connect(insert_tab)
tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(tab)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())