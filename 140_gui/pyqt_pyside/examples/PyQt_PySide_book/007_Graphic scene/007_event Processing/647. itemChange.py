# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

class MyRect(QtGui.QGraphicsRectItem):
    def __init__(self, r):
        QtGui.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
        self.setRect(r)

    def itemChange(self, signal, value):
        if signal == QtGui.QGraphicsItem.ItemEnabledChange:
            print("ItemEnabledChange", value)
        elif signal == QtGui.QGraphicsItem.ItemEnabledHasChanged:
            print("ItemEnabledHasChanged", value)
        elif signal == QtGui.QGraphicsItem.ItemSelectedChange:
            print("ItemSelectedChange", value)
        elif signal == QtGui.QGraphicsItem.ItemSelectedHasChanged:
            print("ItemSelectedHasChanged", value)
        elif signal == QtGui.QGraphicsItem.ItemPositionChange:
            print("ItemPositionChange", value)
        elif signal == QtGui.QGraphicsItem.ItemPositionHasChanged:
            print("ItemPositionHasChanged", value)
        elif signal == QtGui.QGraphicsItem.ItemScenePositionHasChanged:
            print("ItemScenePositionHasChanged", value)
        else:
            print("itemChange", signal)
        return QtGui.QGraphicsRectItem.itemChange(self, signal, value)

def on_clicked():
    view.setFocus()
    rect.setEnabled(not rect.isEnabled())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Обработка изменения состояния")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 200.0))
rect.setPos(QtCore.QPointF(50.0, 50.0))
rect.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
rect.setFlag(QtGui.QGraphicsItem.ItemSendsGeometryChanges)
rect.setFlag(QtGui.QGraphicsItem.ItemSendsScenePositionChanges)
scene.addItem(rect)

view = QtGui.QGraphicsView(scene)

button = QtGui.QPushButton("Переключить статус доступности")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())