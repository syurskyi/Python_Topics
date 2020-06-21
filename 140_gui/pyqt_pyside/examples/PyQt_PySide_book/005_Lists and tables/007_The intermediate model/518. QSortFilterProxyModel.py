# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QSortFilterProxyModel")
window.resize(600, 500)
view1 = QtGui.QTableView()
view2 = QtGui.QTableView()
view1.setSortingEnabled(True)

model = QtGui.QStandardItemModel(4, 4)
for row in range(0, 4):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)

proxyModel = QtGui.QSortFilterProxyModel()
proxyModel.setSourceModel(model)

view1.setModel(proxyModel)
view2.setModel(model)

box = QtGui.QVBoxLayout()
box.addWidget(view1)
box.addWidget(view2)
window.setLayout(box)
window.show()
sys.exit(app.exec_())