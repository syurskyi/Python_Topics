# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    for sel in view.selectedIndexes():
        print(sel.data())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 200)

view = QtGui.QListView()
view.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)

L = []
for i in range(1, 101):
    L.append("Пункт {0}".format(i))
model = QtGui.QStringListModel(L)
view.setModel(model)

button = QtGui.QPushButton("Вывести текст выделенных элементов")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())