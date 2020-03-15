# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_value_changed(n):
    print("on_value_changed", n)

def on_value_selected(n):
    print("on_value_selected", n)

def on_clicked():
    dialog = QtGui.QInputDialog(window)
    dialog.setWindowTitle("Это заголовок окна")
    dialog.setLabelText("Это текст подсказки")
    dialog.setOkButtonText("&Ввод")
    dialog.setCancelButtonText("&Отмена")
    dialog.setInputMode(QtGui.QInputDialog.DoubleInput)
    dialog.setDoubleRange(0.0, 100.0)
    dialog.setDoubleDecimals(2)
    dialog.setDoubleValue(50.0)
    dialog.doubleValueChanged["double"].connect(on_value_changed)
    dialog.doubleValueSelected["double"].connect(on_value_selected)
    result = dialog.exec_()
    if result == QtGui.QDialog.Accepted:
        print(dialog.doubleValue())
    else:
        print("Нажата кнопка Cancel")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QInputDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())