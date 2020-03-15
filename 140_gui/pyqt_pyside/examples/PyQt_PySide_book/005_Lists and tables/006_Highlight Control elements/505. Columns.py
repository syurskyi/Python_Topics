# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    view.setFocus()
    sel = view.selectionModel()
    ind = view.model().index(0, 0)
    sel.select(ind,
     QtGui.QItemSelectionModel.Columns | QtGui.QItemSelectionModel.Select)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QItemSelectionModel")
window.resize(400, 300)
view = QtGui.QTableView()

model = QtGui.QStandardItemModel(4, 2)
for row in range(0, 4):
    for column in range(0, 2):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)
model.setHorizontalHeaderLabels(["A", "B"])
model.setVerticalHeaderLabels(["01", "02", "03", "04"])
view.setModel(model)

selModel = QtGui.QItemSelectionModel(model)
view.setSelectionModel(selModel)

button = QtGui.QPushButton("Изменить выделение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())