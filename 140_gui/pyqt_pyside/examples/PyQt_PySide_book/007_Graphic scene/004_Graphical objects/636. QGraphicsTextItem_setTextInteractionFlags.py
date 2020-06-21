# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsTextItem")
window.resize(600, 600)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.white)

item = QtGui.QGraphicsTextItem()
item.setHtml("<u>Редактируемый <b>текст</b></u>")
item.setDefaultTextColor(QtCore.Qt.darkBlue)
item.setFont(QtGui.QFont("Verdana", 16))
item.setPos(QtCore.QPointF(50.0, 150.0))
item.setTextWidth(300)
item.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
item.setTabChangesFocus(False)

item.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
item.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
item.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)
scene.addItem(item)

print(item.toHtml(), item.toPlainText())
view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())