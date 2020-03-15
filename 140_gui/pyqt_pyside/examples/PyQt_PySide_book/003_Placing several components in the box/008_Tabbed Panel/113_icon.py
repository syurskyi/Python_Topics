# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 120)
tab = QtGui.QTabWidget()
style = window.style()
icon1 = style.standardIcon(QtGui.QStyle.SP_DriveHDIcon)
icon2 = style.standardIcon(QtGui.QStyle.SP_DriveCDIcon)
icon3 = style.standardIcon(QtGui.QStyle.SP_DriveNetIcon)
tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), icon1, "Вкладка &1")
tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), icon2, "Вкладка &2")
tab.addTab(QtGui.QLabel("Содержимое вкладки 3"), icon3, "Вкладка &3")
tab.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(tab)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())