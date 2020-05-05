# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, prnt, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.grabMouse()
        self.prnt = prnt

    def mousePressEvent(self, e):
        self.setText(
             "X: {0}, Y: {1}, globalX: {2}, globalY: {3}".format(
             e.x(), e.y(), e.globalX(), e.globalY()))
        # Преобразование из глобальных координат в координаты компонента
        p1 = self.mapFromGlobal(e.globalPos())
        print("mapFromGlobal - X: {0}, Y: {1}".format(p1.x(), p1.y()))
        # Преобразование из координат компонента в глобальные координаты
        p2 = self.mapToGlobal(e.pos())
        print("mapToGlobal - X: {0}, Y: {1}".format(p2.x(), p2.y()))
        # Преобразование в координаты родителя
        p3 = self.mapToParent(e.pos())
        print("mapToParent - X: {0}, Y: {1}".format(p3.x(), p3.y()))
        # Преобразование координат родителя в координаты компонента
        p4 = self.mapFromParent(p3)
        print("mapFromParent - X: {0}, Y: {1}".format(p4.x(), p4.y()))
        # Преобразование в координаты родителя
        p5 = self.mapTo(self.prnt, e.pos())
        print("mapTo - X: {0}, Y: {1}".format(p5.x(), p5.y()))
        # Преобразование координат родителя в координаты компонента
        p6 = self.mapFrom(self.prnt, p5)
        print("mapFrom - X: {0}, Y: {1}".format(p6.x(), p6.y()))
        e.ignore()
        QtWidgets.QLabel.mousePressEvent(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Щелкните мышью в окне", self)
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