# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyRect(QtGui.QGraphicsRectItem):
    def __init__(self, r):
        QtGui.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
        self.setRect(r)

    def mousePressEvent(self, e):
        print("mousePressEvent")
        print("pos()", e.pos())
        print("scenePos()", e.scenePos())
        print("screenPos()", e.screenPos())
        print("lastPos()", e.lastPos())
        print("lastScenePos()", e.lastScenePos())
        print("lastScreenPos()", e.lastScreenPos())
        if e.buttons() & QtCore.Qt.LeftButton:
            print("Нажата левая кнопка мыши")
        if e.buttons() & QtCore.Qt.RightButton:
            print("Нажата правая кнопка мыши")
        if e.buttons() & QtCore.Qt.MiddleButton:
            print("Нажата средняя кнопка мыши")
        if (e.buttons() & QtCore.Qt.LeftButton and
                    e.buttons() & QtCore.Qt.RightButton):
            print("Левая и правая кнопки нажаты")
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
        e.accept()

    def mouseReleaseEvent(self, e):
        print("mouseReleaseEvent")
        print("pos()", e.pos())
        print("scenePos()", e.scenePos())
        print("screenPos()", e.screenPos())
        print("buttonDownPos()", e.buttonDownPos(QtCore.Qt.LeftButton))
        print("buttonDownScenePos()",
              e.buttonDownScenePos(QtCore.Qt.LeftButton))
        print("buttonDownScreenPos()",
              e.buttonDownScreenPos(QtCore.Qt.LeftButton))
        QtGui.QGraphicsRectItem.mouseReleaseEvent(self, e)

    def mouseMoveEvent(self, e):
        print("mouseMoveEvent")
        QtGui.QGraphicsRectItem.mouseMoveEvent(self, e)

    def mouseDoubleClickEvent(self, e):
        print("mouseDoubleClickEvent")
        QtGui.QGraphicsRectItem.mouseDoubleClickEvent(self, e)


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