# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

class MyRect(QtGui.QGraphicsRectItem):
    def __init__(self, r):
        QtGui.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
        self.setRect(r)
        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, e):
        print("hoverEnterEvent")
        print("pos()", e.pos())
        print("scenePos()", e.scenePos())
        print("screenPos()", e.screenPos())
        print("lastPos()", e.lastPos())
        print("lastScenePos()", e.lastScenePos())
        print("lastScreenPos()", e.lastScreenPos())
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
        self.setPen(QtGui.QPen(QtCore.Qt.red, 3))
        QtGui.QGraphicsRectItem.hoverEnterEvent(self, e)

    def hoverLeaveEvent(self, e):
        print("hoverLeaveEvent")
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        QtGui.QGraphicsRectItem.hoverLeaveEvent(self, e)

    def hoverMoveEvent(self, e):
        print("hoverMoveEvent")
        QtGui.QGraphicsRectItem.hoverMoveEvent(self, e)

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