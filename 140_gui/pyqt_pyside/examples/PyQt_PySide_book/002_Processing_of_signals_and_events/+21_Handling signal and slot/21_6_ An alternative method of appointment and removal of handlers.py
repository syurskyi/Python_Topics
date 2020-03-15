# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    mysignal = QtCore.pyqtSignal([int], [str], name="mysignal")

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Signal Processing")
        self.resize(300, 100)
        self.button1 = QtGui.QPushButton("Click me")
        self.button2 = QtGui.QPushButton("Button 2")
        self.button3 = QtGui.QPushButton("Remove Handlers")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)
        self.setLayout(vbox)
        # Назначение обработчиков
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked["bool"].connect(self.on_clicked_button2)
        self.button3.clicked.connect(self.on_clicked_button3)
        self.mysignal[int].connect(self.on_mysignal)
        self.mysignal[str].connect(self.on_mysignal)

    def on_clicked_button1(self, status):
        print("Нажата кнопка button1", status)
        # Генерация сигнала
        self.button2.clicked["bool"].emit(False)
        self.mysignal[int].emit(10)
        self.mysignal[str].emit("строка")

    def on_clicked_button2(self, status):
        print("Нажата кнопка button2", status)

    def on_clicked_button3(self):
        print("Нажата кнопка button3")
        # Удаление обработчиков
        self.button1.clicked.disconnect()
        self.button2.clicked["bool"].disconnect(
                                     self.on_clicked_button2)
        self.mysignal[int].disconnect()
        self.mysignal[str].disconnect()
        self.button3.setEnabled(False)

    def on_mysignal(self, n):
        print("Обработан пользовательский сигнал\n n =", n)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())