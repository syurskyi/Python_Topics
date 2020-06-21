# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.grabMouse()

    def wheelEvent(self, e):
        if e.angleDelta().y() > 0:
            print("Колесико повернуто от пользователя")
        elif e.angleDelta().y() < 0:
            print("Колесико повернуто к пользователю")
        if e.buttons() & QtCore.Qt.LeftButton:
            print("Нажата левая кнопка мыши")
        if e.buttons() & QtCore.Qt.RightButton:
            print("Нажата правая кнопка мыши")
        if e.buttons() & QtCore.Qt.MiddleButton:
            print("Нажата средняя кнопка мыши")
        if (e.buttons() & QtCore.Qt.LeftButton and
            e.buttons() & QtCore.Qt.RightButton):
            print("Левая и правая кнопки нажаты")
        self.setText(
        "X: {0}, Y: {1}, globalX: {2}, globalY: {3}\ndelta: {4}".format(
        e.x(), e.y(), e.globalX(), e.globalY(), e.angleDelta().y()))
        e.ignore()
        QtWidgets.QLabel.wheelEvent(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Поверните колесико мыши")
        self.label.setFrameStyle(QtWidgets.QFrame.Box |
                                 QtWidgets.QFrame.Plain)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())