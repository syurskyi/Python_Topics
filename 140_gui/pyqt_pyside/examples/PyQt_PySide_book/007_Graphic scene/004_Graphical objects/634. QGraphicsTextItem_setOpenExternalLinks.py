# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_link_activated(s):
    print("on_link_activated", s)

def on_link_hovered(s):
    print("on_link_hovered", s)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsTextItem")
window.resize(600, 600)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.white)

item = QtGui.QGraphicsTextItem()
item.setHtml('<a href="http://google.ru/">Это гиперссылка</a>')
item.setDefaultTextColor(QtCore.Qt.darkBlue)
item.setFont(QtGui.QFont("Verdana", 16))
item.setPos(QtCore.QPointF(50.0, 150.0))
item.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
item.setOpenExternalLinks(True)
item.linkActivated["const QString&"].connect(on_link_activated)
item.linkHovered["const QString&"].connect(on_link_hovered)

item.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
item.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
item.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)
scene.addItem(item)

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())