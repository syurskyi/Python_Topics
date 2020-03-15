# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    scene.setFocus()
    myPath = QtGui.QPainterPath()
    myPath.addEllipse(5.0, 50.0, 500.0, 200.0)
    scene.setSelectionArea(myPath, QtCore.Qt.IntersectsItemShape)
    print(scene.selectedItems())
    scene.addPath(myPath, pen=QtGui.QPen(QtCore.Qt.red))
    button.setEnabled(False)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)
scene.setStickyFocus(True)

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

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0),
                     pen=QtGui.QPen(QtCore.Qt.blue, 3),
                     brush=QtGui.QBrush(QtCore.Qt.green))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)

line1.setSelected(True)

view = QtGui.QGraphicsView(scene)

button = QtGui.QPushButton("Выделить")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())