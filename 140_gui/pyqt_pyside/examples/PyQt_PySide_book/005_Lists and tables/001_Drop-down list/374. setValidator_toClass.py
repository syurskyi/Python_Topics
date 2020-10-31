# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui
import sys


class SetValidator(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i), i)
        ico = self.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxCritical)
        self.comboBox.setItemData(0, "Новое значение", role=QtCore.Qt.DisplayRole)
        self.comboBox.setItemData(0, ico, role=QtCore.Qt.DecorationRole)
        self.comboBox.setItemData(0, QtGui.QFont("Courier New", 16),
                             role=QtCore.Qt.FontRole)
        self.comboBox.setItemData(1, QtCore.Qt.AlignRight,
                             role=QtCore.Qt.TextAlignmentRole)
        self.comboBox.setItemData(2,
                             QtGui.QBrush(QtGui.QColor("#000000"), QtCore.Qt.SolidPattern),
                             role=QtCore.Qt.BackgroundRole)
        self.comboBox.setItemData(2,
                             QtGui.QBrush(QtGui.QColor("#FFFFFF"), QtCore.Qt.SolidPattern),
                             role=QtCore.Qt.ForegroundRole)
        self.comboBox.setItemData(3, QtCore.Qt.Checked,
                             role=QtCore.Qt.CheckStateRole)
        self.comboBox.setItemData(4, QtCore.Qt.PartiallyChecked,
                             role=QtCore.Qt.CheckStateRole)
        self.comboBox.setItemData(5, QtCore.Qt.Unchecked,
                             role=QtCore.Qt.CheckStateRole)
        self.comboBox.setItemData(0, 50, role=QtCore.Qt.UserRole)
        self.comboBox.setItemData(0, "Другие данные", role=QtCore.Qt.UserRole + 1)
        self.comboBox.setItemData(0, "Это текст всплывающей подсказки",
                             role=QtCore.Qt.ToolTipRole)
        button = QtWidgets.QPushButton("Получить значение")
        button.clicked.connect(on_clicked)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.comboBox)
        box.addWidget(button)
        self.setLayout(box)
        self.show()


    def on_clicked():
        print("Текст:", self.comboBox.currentText())
        print("Данные:", self.comboBox.itemData(self.comboBox.currentIndex(),
                                           role=QtCore.Qt.DisplayRole))
        print("Данные:", self.comboBox.itemData(0, role=QtCore.Qt.UserRole))
        print("Данные:", self.comboBox.itemData(0, role=QtCore.Qt.UserRole + 1))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SetValidator()
    sys.exit(app.exec_())