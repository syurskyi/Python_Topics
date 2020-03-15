# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys


def on_clicked():
    view.setFocus()
    view.selectionModel().clearSelection()


def on_current_changed(ind1, ind2):
    print("on_current_changed")


def on_current_column_changed(ind1, ind2):
    print("on_current_column_changed")


def on_current_row_changed(ind1, ind2):
    print("on_current_row_changed")


def on_selection_changed(sel1, sel2):
    print("on_selection_changed")


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

selModel.currentChanged["const QModelIndex&", "const QModelIndex&"].connect(on_current_changed)
selModel.currentColumnChanged["const QModelIndex&", "const QModelIndex&"].connect(on_current_column_changed)
selModel.currentRowChanged["const QModelIndex&", "const QModelIndex&"].connect(on_current_row_changed)
selModel.selectionChanged["const QItemSelection&", "const QItemSelection&"].connect(on_selection_changed)

button = QtGui.QPushButton("Снять выделение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())