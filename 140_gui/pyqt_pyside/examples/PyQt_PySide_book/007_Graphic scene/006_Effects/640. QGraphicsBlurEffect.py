# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


def on_clicked():
    view.setFocus()
    effect.setEnabled(not effect.isEnabled())
    effect.setBlurRadius(30)


def on_enabled_changed(status):
    print("on_enabled_changed", status)


def on_radius_changed(radius):
    print("on_radius_changed", radius)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsBlurEffect")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0),
                     pen=QtGui.QPen(QtCore.Qt.darkGreen, 1),
                     brush=QtGui.QBrush(QtCore.Qt.darkGreen))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)

effect = QtGui.QGraphicsBlurEffect()
effect.setBlurRadius(10)
effect.enabledChanged["bool"].connect(on_enabled_changed)
effect.blurRadiusChanged["qreal"].connect(on_radius_changed)
rect.setGraphicsEffect(effect)

view = QtGui.QGraphicsView(scene)

button = QtGui.QPushButton("Переключить статус и изменить параметры")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())