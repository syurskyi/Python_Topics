# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    (font, ok) = QtGui.QFontDialog.getFont(QtGui.QFont("Tahoma", 16),
                                           window, "Заголовок окна")
    if ok:
        print(font.family(), font.pointSize(), font.weight(),
              font.italic(), font.underline())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QFontDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())