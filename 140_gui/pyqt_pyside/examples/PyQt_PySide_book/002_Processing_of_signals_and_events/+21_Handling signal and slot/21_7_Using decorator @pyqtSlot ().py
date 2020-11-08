# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
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
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Нажми меня")
button.clicked.connect(obj.on_clicked)
button.clicked.connect(obj.myslot)
button.show()
sys.exit(app.exec_())


# Эти два обработчика будут успешно назначены и выполнены
button.clicked.connect(on_clicked)
button.clicked.connect(on_clicked)
# А эти два обработчика назначены не будут
button.clicked.connect(on_clicked, Qt.Core.Qt.AutoConnection | QtCore.Qt.UniqueConnection)
button.clicked.connect(on_clicked, Qt.Core.Qt.AutoConnection | QtCore.Qt.UniqueConnection)
# Тем не менее, эти два обработчика будут назначены,
# поскольку они разные
button.clicked.connect(on_clicked, Qt.Core.Qt.AutoConnection | QtCore.Qt.UniqueConnection)
button.clicked.connect(obj.on_clicked, Qt.Core.Qt.AutoConnection | QtCore.Qt.UniqueConnection)