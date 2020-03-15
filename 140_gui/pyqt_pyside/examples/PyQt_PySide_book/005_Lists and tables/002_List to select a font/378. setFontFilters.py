# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print(comboBox.currentFont().family())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QFontComboBox")
window.resize(500, 90)
comboBox = QtGui.QFontComboBox()
comboBox.setFontFilters(QtGui.QFontComboBox.MonospacedFonts)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())