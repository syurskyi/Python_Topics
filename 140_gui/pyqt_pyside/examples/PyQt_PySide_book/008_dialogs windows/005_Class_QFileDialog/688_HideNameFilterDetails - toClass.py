# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    dialog = QtGui.QFileDialog(parent=window,
                               filter="Images (*.png *.jpg)",
                               caption="This is name of window")
    dialog.setAcceptMode(QtGui.QFileDialog.AcceptOpen)
    dialog.setOption(QtGui.QFileDialog.HideNameFilterDetails)
    result = dialog.exec_()
    if result == QtGui.QDialog.Accepted:
        print(dialog.selectedFiles())
    else:
        print("Pushed button Cancel")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QFileDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Show dialog window...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())