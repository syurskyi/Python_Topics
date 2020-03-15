# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTreeView")
window.resize(500, 400)
view = QtGui.QTreeView()

model = QtGui.QStandardItemModel()
model.setColumnCount(4)
parent = model.invisibleRootItem()
for i in range(0, 4):
    item = QtGui.QStandardItem("Пункт {0}-1".format(i))
    parent.appendRow(item)
    parent = item

parent = QtGui.QStandardItem(3, 4)
parent.setText("Элемент-родитель")
for row in range(0, 3):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        parent.setChild(row, column, item)
model.appendRow(parent)

view.setModel(model)

view.setColumnWidth(0, 200)
view.expandAll()
view.setSortingEnabled(True)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)
window.show()
sys.exit(app.exec_())