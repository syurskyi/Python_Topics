# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

class SetDuplicatedEnabled(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.comboBox.setDuplicatesEnabled(True)
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i))
        button = QtWidgets.QPushButton("Получить индекс текущего элемента")
        button.clicked.connect(self.on_clicked)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.comboBox)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        print(self.comboBox.currentIndex())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SetDuplicatedEnabled()
    sys.exit(app.exec_())