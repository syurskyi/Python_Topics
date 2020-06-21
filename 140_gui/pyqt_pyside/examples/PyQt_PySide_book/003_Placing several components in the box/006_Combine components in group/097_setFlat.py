# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGroupBox")
window.resize(300, 80)
radio1 = QtGui.QRadioButton("&Да")
radio2 = QtGui.QRadioButton("&Нет")
mainbox = QtGui.QVBoxLayout()
box = QtGui.QGroupBox()
box.setTitle("&Вы знаете язык Python?")
box.setAlignment(QtCore.Qt.AlignHCenter)
box.setFlat(True)
hbox = QtGui.QHBoxLayout()
hbox.addWidget(radio1)
hbox.addWidget(radio2)
box.setLayout(hbox)
mainbox.addWidget(box)
window.setLayout(mainbox)
radio1.setChecked(True)
window.show()
sys.exit(app.exec_())