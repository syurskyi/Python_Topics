# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

class SetDuplicatedEnabled(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

def on_clicked():
    print(comboBox.currentIndex())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtWidgets.QComboBox()
comboBox.setEditable(True)
comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
comboBox.setDuplicatesEnabled(True)
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i))
button = QtWidgets.QPushButton("Получить индекс текущего элемента")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SetDuplicatedEnabled()
    sys.exit(app.exec_())