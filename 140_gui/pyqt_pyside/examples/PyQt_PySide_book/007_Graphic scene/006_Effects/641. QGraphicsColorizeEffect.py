# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


def on_clicked():
    view.setFocus()
    effect.setEnabled(not effect.isEnabled())
    effect.setColor(QtGui.QColor(128, 128, 128, 255))
    effect.setStrength(0.8)


def on_enabled_changed(status):
    print("on_enabled_changed", status)


def on_strength_changed(strength):
    print("on_strength_changed", strength)


def on_color_changed(color):
    print("on_color_changed", color.getRgb())


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsColorizeEffect")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0),
                     pen=QtGui.QPen(QtCore.Qt.red, 3),
                     brush=QtGui.QBrush(QtCore.Qt.darkGreen))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)

effect = QtGui.QGraphicsColorizeEffect()
effect.setStrength(0.5)
effect.enabledChanged["bool"].connect(on_enabled_changed)
effect.colorChanged["const QColor&"].connect(on_color_changed)
effect.strengthChanged["qreal"].connect(on_strength_changed)
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