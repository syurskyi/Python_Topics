# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui
import sys


class MyClass(object):
    def __init__(self, x=0):
        self.x = x
    def __call__(self):
        print("Кнопка нажата. Метод MyClass.__call__()")
        print("x =", self.x)
    def on_clicked_in_class(self):
        print("Кнопка нажата. Метод MyClass.on_clicked()")


class UserHanderClass(QtGui.QWidget, MyClass):
    def __init__(self):
        super(UserHanderClass, self).__init__()
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout_2")
        self.button = QtGui.QPushButton("Push me")
        self.button.setObjectName("button")
        self.verticalLayout.addWidget(self.button)
        self.items_ly = QtGui.QVBoxLayout()
        self.items_ly.setObjectName("items_ly")
        self.verticalLayout.addLayout(self.items_ly)
        spacer_item = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_item)

        self.setWindowTitle('Options for assigning of the user handler')

        # Назначаем обработчиком функцию
        QtCore.QObject.connect(self.button, QtCore.SIGNAL("clicked()"), self.on_clicked)

    def on_clicked(self):
        print("Кнопка нажата. Функция on_clicked()")

        # Назначаем обработчиком метод класса
        QtCore.QObject.connect(self.button, QtCore.SIGNAL("clicked()"),
                               MyClass.on_clicked_in_class)

        # Передача параметра в обработчик
        QtCore.QObject.connect(self.button, QtCore.SIGNAL("clicked()"), MyClass(10))
        QtCore.QObject.connect(self.button, QtCore.SIGNAL("clicked()"), MyClass(5))

if __name__ == '__main__':
    app = QtGui.QApplication([])
    w = UserHanderClass()
    w.show()
    app.exec_()
