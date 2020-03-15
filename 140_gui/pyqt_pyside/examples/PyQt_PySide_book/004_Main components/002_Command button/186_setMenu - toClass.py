

def on_menu_item1():
    print("Выбран пункт 1")

def on_menu_item2():
    print("Выбран пункт 2")

def on_menu_item3():
    print("Выбран пункт 3")

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

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
