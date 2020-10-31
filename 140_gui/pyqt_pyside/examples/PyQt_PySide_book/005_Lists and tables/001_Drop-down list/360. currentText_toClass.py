# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys


class CurrentText(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i), i)
        self.comboBox.setItemData(0, 50, role=QtCore.Qt.UserRole)
        self.comboBox.setItemData(0, "Это текст всплывающей подсказки",
                             role=QtCore.Qt.ToolTipRole)
        button = QtWidgets.QPushButton("Получить значение")
        button.clicked.connect(self.on_clicked)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.comboBox)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        print("Текст:", self.comboBox.currentText())
        print("Индекс:", self.comboBox.currentIndex())
        print("Данные:", self.comboBox.itemData(self.comboBox.currentIndex()))
        print("Текст подсказки:", self.comboBox.itemData(
            self.comboBox.currentIndex(), role=QtCore.Qt.ToolTipRole))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = CurrentText()
    sys.exit(app.exec_())