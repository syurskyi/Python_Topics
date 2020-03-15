# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys, time

def on_clicked():
    dialog = QtGui.QProgressDialog("Выполняется операция", "&Отмена",
             0, 20, window)
    dialog.setWindowTitle("Выполнение операции")
    dialog.setModal(True)
    dialog.setValue(0)
    dialog.show()
    dialog.resize(300, 100)
    for i in range(1, 21):
        dialog.setValue(i)
        if dialog.wasCanceled():
            break
        time.sleep(1)               # "Засыпаем" на 1 секунду
        QtGui.qApp.processEvents()  # Запускаем оборот цикла (если нужно)
        print("step -", i)
    dialog.close()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QProgressDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())