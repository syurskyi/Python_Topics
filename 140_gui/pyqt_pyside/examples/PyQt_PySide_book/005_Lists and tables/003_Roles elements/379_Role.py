# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


def on_clicked():
    print("Текст:", comboBox.currentText())
    print("Данные:", comboBox.itemData(comboBox.currentIndex(),
                                       role=QtCore.Qt.DisplayRole))
    print("Данные:", comboBox.itemData(0, role=QtCore.Qt.UserRole))
    print("Данные:", comboBox.itemData(0, role=QtCore.Qt.UserRole + 1))


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtGui.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i), i)
ico = window.style().standardIcon(QtGui.QStyle.SP_MessageBoxCritical)
comboBox.setItemData(0, "Новое значение", role=QtCore.Qt.DisplayRole)
comboBox.setItemData(0, ico, role=QtCore.Qt.DecorationRole)
comboBox.setItemData(0, QtGui.QFont("Courier New", 16),
                     role=QtCore.Qt.FontRole)
comboBox.setItemData(1, QtCore.Qt.AlignRight,
                     role=QtCore.Qt.TextAlignmentRole)
comboBox.setItemData(2,
                     QtGui.QBrush(QtGui.QColor("#000000"), QtCore.Qt.SolidPattern),
                     role=QtCore.Qt.BackgroundRole)
comboBox.setItemData(2,
                     QtGui.QBrush(QtGui.QColor("#FFFFFF"), QtCore.Qt.SolidPattern),
                     role=QtCore.Qt.ForegroundRole)
comboBox.setItemData(3, QtCore.Qt.Checked,
                     role=QtCore.Qt.CheckStateRole)
comboBox.setItemData(4, QtCore.Qt.PartiallyChecked,
                     role=QtCore.Qt.CheckStateRole)
comboBox.setItemData(5, QtCore.Qt.Unchecked,
                     role=QtCore.Qt.CheckStateRole)
comboBox.setItemData(0, 50, role=QtCore.Qt.UserRole)
comboBox.setItemData(0, "Другие данные", role=QtCore.Qt.UserRole + 1)
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