# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    dialog = QtGui.QInputDialog(window)
    dialog.setWindowTitle("Это заголовок окна")
    dialog.setLabelText("Это текст подсказки")
    dialog.setOkButtonText("&Ввод")
    dialog.setCancelButtonText("&Отмена")
    dialog.setOption(QtGui.QInputDialog.UseListViewForComboBoxItems,
                     on=True)
    dialog.setComboBoxItems(["Пункт 1", "Пункт 2", "Пункт 3"])
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