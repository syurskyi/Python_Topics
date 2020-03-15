# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 150)
tab = QtGui.QTabWidget()
tab.setUsesScrollButtons(True)
tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.addTab(QtGui.QLabel("Содержимое вкладки 3"), "Вкладка &3")
tab.addTab(QtGui.QLabel("Содержимое вкладки 4"), "Вкладка &4")
tab.addTab(QtGui.QLabel("Содержимое вкладки 5"), "Вкладка &5")
tab.addTab(QtGui.QLabel("Содержимое вкладки 6"), "Вкладка &6")
tab.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(tab)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())