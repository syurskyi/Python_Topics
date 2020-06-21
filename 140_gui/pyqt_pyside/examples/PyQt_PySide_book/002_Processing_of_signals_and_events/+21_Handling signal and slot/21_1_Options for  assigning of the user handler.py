# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print("Кнопка нажата. Функция on_clicked()")

class MyClass():
    def __init__(self, x=0):
        self.x = x
    def __call__(self):
        print("Кнопка нажата. Метод MyClass.__call__()")
        print("x =", self.x)
    def on_clicked(self):
        print("Кнопка нажата. Метод MyClass.on_clicked()")

obj = MyClass()
app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton("Push me")
# Назначаем обработчиком функцию

QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), on_clicked)
# Назначаем обработчиком метод класса
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"),
                       obj.on_clicked)
# Передача параметра в обработчик
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), MyClass(10))
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), MyClass(5))
button.show()
sys.exit(app.exec_())