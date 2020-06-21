# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_menu_item1():
    print("Выбран пункт 1")

def on_menu_item2():
    print("Выбран пункт 2")

def on_menu_item3():
    print("Выбран пункт 3")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button = QtGui.QPushButton("Кнопка с меню")
menu = QtGui.QMenu()
menu.addAction("Пункт 1", on_menu_item1)
menu.addAction("Пункт 2", on_menu_item2)
menu.addAction("Пункт 3", on_menu_item3)
button.setMenu(menu)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())