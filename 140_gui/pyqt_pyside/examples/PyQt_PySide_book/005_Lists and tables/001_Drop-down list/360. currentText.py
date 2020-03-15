# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print("Текст:", comboBox.currentText())
    print("Индекс:", comboBox.currentIndex())
    print("Данные:", comboBox.itemData(comboBox.currentIndex()))
    print("Текст подсказки:", comboBox.itemData(comboBox.currentIndex(),
                                                role=QtCore.Qt.ToolTipRole))

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtGui.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i), i)
comboBox.setItemData(0, 50, role=QtCore.Qt.UserRole)
comboBox.setItemData(0, "Это текст всплывающей подсказки",
                     role=QtCore.Qt.ToolTipRole)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())