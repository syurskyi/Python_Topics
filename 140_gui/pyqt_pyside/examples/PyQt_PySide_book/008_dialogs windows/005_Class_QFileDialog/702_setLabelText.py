# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    dialog = QtGui.QFileDialog(parent=window,
                               filter="Images (*.png *.jpg)",
                               caption="Это заголовок окна")
    dialog.setLabelText(QtGui.QFileDialog.LookIn, "Текущий каталог")
    dialog.setLabelText(QtGui.QFileDialog.FileName, "Название файла:")
    dialog.setLabelText(QtGui.QFileDialog.FileType, "Типы файлов:")
    dialog.setLabelText(QtGui.QFileDialog.Accept, "&Открыть")
    dialog.setLabelText(QtGui.QFileDialog.Reject, "О&тмена")

    result = dialog.exec_()
    if result == QtGui.QDialog.Accepted:
        print(dialog.selectedFiles())
    else:
        print("Нажата кнопка Cancel")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QFileDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())