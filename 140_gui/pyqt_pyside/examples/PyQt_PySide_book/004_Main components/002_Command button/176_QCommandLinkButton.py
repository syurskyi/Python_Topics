# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print("Кнопка нажата")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QCommandLinkButton")
window.resize(300, 70)
button = QtGui.QCommandLinkButton("The text on the button")
button.setDescription("Additional text")
button.clicked.connect(on_clicked)
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())