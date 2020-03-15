# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(comboBox.currentFont().family())

def on_font_changed(font):
    print("on_font_changed", font.family())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QFontComboBox")
window.resize(500, 90)
comboBox = QtGui.QFontComboBox()
comboBox.currentFontChanged["const QFont&"].connect(on_font_changed)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())