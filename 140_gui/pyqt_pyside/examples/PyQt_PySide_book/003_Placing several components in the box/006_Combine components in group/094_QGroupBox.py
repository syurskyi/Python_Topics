# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGroupBox")
window.resize(300, 80)
radio1 = QtGui.QRadioButton("&Yes")
radio2 = QtGui.QRadioButton("&No")
mainbox = QtGui.QVBoxLayout()
box = QtGui.QGroupBox("&Do you know Python?")
hbox = QtGui.QHBoxLayout()
hbox.addWidget(radio1)
hbox.addWidget(radio2)
box.setLayout(hbox)
mainbox.addWidget(box)
window.setLayout(mainbox)
radio1.setChecked(True)
window.show()
sys.exit(app.exec_())