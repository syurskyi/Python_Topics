# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QToolBox")
window.resize(300, 250)
toolBox = QtGui.QToolBox()
toolBox.addItem(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
toolBox.addItem(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
toolBox.setItemToolTip(0, "Это текст подсказки для вкладки 1")
toolBox.setItemToolTip(1, "Это текст подсказки для вкладки 2")
toolBox.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(toolBox)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())