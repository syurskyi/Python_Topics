# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(500, 300)

scene = QtGui.QGraphicsScene(0.0, 0.0, 475.0, 275.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect1 = scene.addRect(0.0, 0.0, 400.0, 100.0,
              pen=QtGui.QPen(QtCore.Qt.red, 3),
              brush=QtGui.QBrush(QtCore.Qt.yellow))
rect1.setPos(QtCore.QPointF(50.0, 30.0))
rect2 = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0),
              pen=QtGui.QPen(QtCore.Qt.blue, 3),
              brush=QtGui.QBrush(QtCore.Qt.green))
rect2.setPos(QtCore.QPointF(50.0, 150.0))

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())