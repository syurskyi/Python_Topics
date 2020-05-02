# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print(textBrowser.source().tS..())
    textBrowser.home()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextBrowser")
window.resize(800, 600)
textBrowser = QtGui.QTextBrowser()
textBrowser.setSource(QtCore.QUrl("file:///C:/Python32/Lib/site-packages/PyQt4/doc/html/classes.html"))
button = QtGui.QPushButton("Вывести адрес и перейти домой")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textBrowser)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())