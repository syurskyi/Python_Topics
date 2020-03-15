# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(comboBox.currentIndex())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtGui.QComboBox()
comboBox.setEditable(True)
comboBox.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
comboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
comboBox.setMinimumContentsLength(30)
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i))
button = QtGui.QPushButton("Получить индекс")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())