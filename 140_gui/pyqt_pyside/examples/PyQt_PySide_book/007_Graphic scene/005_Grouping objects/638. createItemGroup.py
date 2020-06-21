# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    scene.setFocus()
    scene.destroyItemGroup(group)
    button.setEnabled(False)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsItemGroup")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

line1 = scene.addLine(50.0, 50.0, 450.0, 50.0,
                     pen=QtGui.QPen(QtCore.Qt.red, 3))
line1.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
line1.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
line1.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)

line2 = scene.addLine(QtCore.QLineF(50.0, 100.0, 450.0, 100.0),
                      pen=QtGui.QPen(QtCore.Qt.blue, 3))
line2.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
line2.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
line2.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)

group = scene.createItemGroup([line1, line2])
group.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
group.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0),
                     pen=QtGui.QPen(QtCore.Qt.blue, 3),
                     brush=QtGui.QBrush(QtCore.Qt.green))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)

view = QtGui.QGraphicsView(scene)

button = QtGui.QPushButton("Разгруппировать")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())