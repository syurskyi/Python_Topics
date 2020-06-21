# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

class MyClass(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
    @QtCore.pyqtSlot()
    def on_clicked(self):
        print("Кнопка нажата. Слот on_clicked()")
    @QtCore.pyqtSlot(bool, name="myslot")
    def on_clicked2(self, status):
        print("Кнопка нажата. Слот myslot(bool)", status)

obj = MyClass()
app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton("Нажми меня")
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"),
                       obj, QtCore.SLOT("on_clicked()"))
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked(bool)"),
                       obj, QtCore.SLOT("myslot(bool)"))
button.show()
sys.exit(app.exec_())