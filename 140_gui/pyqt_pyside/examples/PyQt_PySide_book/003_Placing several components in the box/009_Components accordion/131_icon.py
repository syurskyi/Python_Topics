# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QToolBox")
window.resize(300, 150)
toolBox = QtGui.QToolBox()
style = window.style()
icon1 = style.standardIcon(QtGui.QStyle.SP_DriveHDIcon)
icon2 = style.standardIcon(QtGui.QStyle.SP_DriveCDIcon)
icon3 = style.standardIcon(QtGui.QStyle.SP_DriveNetIcon)
toolBox.addItem(QtGui.QLabel("Содержимое вкладки 1"), icon1, "Вкладка &1")
toolBox.addItem(QtGui.QLabel("Содержимое вкладки 2"), icon2, "Вкладка &2")
toolBox.addItem(QtGui.QLabel("Содержимое вкладки 3"), icon3, "Вкладка &3")
toolBox.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(toolBox)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())