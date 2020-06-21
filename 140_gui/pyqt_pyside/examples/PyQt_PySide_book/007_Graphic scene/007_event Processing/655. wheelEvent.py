# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

class MyRect(QtGui.QGraphicsRectItem):
    def __init__(self, r):
        QtGui.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
        self.setRect(r)

    def wheelEvent(self, e):
        print("wheelEvent")
        print("delta()", e.delta())
        if e.orientation() == QtCore.Qt.Horizontal:
            print("Колесико повернуто по горизонтали")
        elif e.orientation() == QtCore.Qt.Vertical:
            print("Колесико повернуто по вертикали")
        if e.buttons() & QtCore.Qt.LeftButton:
            print("Нажата левая кнопка мыши")
        if e.buttons() & QtCore.Qt.RightButton:
            print("Нажата правая кнопка мыши")
        if e.buttons() & QtCore.Qt.MiddleButton:
            print("Нажата средняя кнопка мыши")
        if (e.buttons() & QtCore.Qt.LeftButton and
            e.buttons() & QtCore.Qt.RightButton):
            print("Левая и правая кнопки нажаты")
        print("pos()", e.pos())
        print("scenePos()", e.scenePos())
        print("screenPos()", e.screenPos())
        modifiers = []
        if e.modifiers() & QtCore.Qt.ShiftModifier:
            modifiers.append("Shift")
        if e.modifiers() & QtCore.Qt.ControlModifier:
            modifiers.append("Ctrl")
        if e.modifiers() & QtCore.Qt.AltModifier:
            modifiers.append("Alt")
        if len(modifiers) == 0:
            modifiers.append("No")
        print("+".join(modifiers))
        QtGui.QGraphicsRectItem.wheelEvent(self, e)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("События мыши")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0))
rect.setPos(QtCore.QPointF(50.0, 150.0))
scene.addItem(rect)

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())