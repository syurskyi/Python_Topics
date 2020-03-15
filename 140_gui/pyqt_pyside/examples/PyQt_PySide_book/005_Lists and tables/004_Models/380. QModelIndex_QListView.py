# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys


def on_clicked():
    ind = listView.currentIndex()
    if ind.isValid():
        print("Данные:", ind.data())
        print("row:", ind.row(), "column:", ind.column())

        ind_sibling = ind.sibling(0, 0)
        if ind_sibling.isValid():
            print("sibling:", ind_sibling.data())
        else:
            print("Нет sibling")

    else:
        print("Нет текущего элемента")


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 200)
listView = QtGui.QListView()
L = []
for i in range(1, 11):
    L.append("Пункт {0}".format(i))
model = QtGui.QStringListModel(L)
listView.setModel(model)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(listView)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())