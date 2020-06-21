# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_value_changed(s):
    print("on_value_changed", s)

def on_value_selected(s):
    print("on_value_selected", s)

def on_clicked():
    dialog = QtGui.QInputDialog(window)
    dialog.setWindowTitle("Это заголовок окна")
    dialog.setLabelText("Это текст подсказки")
    dialog.setOkButtonText("&Ввод")
    dialog.setCancelButtonText("&Отмена")
    dialog.setInputMode(QtGui.QInputDialog.TextInput)
    dialog.setTextValue("Значение по умолчанию")
    dialog.textValueChanged["const QString&"].connect(on_value_changed)
    dialog.textValueSelected["const QString&"].connect(on_value_selected)
    result = dialog.exec_()
    if result == QtGui.QDialog.Accepted:
        print(dialog.textValue())
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