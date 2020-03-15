# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyThread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        for i in range(1, 26):
            self.sleep(1)
            self.emit(QtCore.SIGNAL("mysignal(int)"), i * 4)


def on_clicked():
    thread.start()
    button.setEnabled(False)


def on_finished():
    button.setEnabled(True)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QProgressBar")
window.resize(300, 70)
progressBar = QtGui.QProgressBar()
progressBar.setMinimum(0)
progressBar.setMaximum(100)
thread = MyThread()
thread.finished.connect(on_finished)
QtCore.QObject.connect(thread, QtCore.SIGNAL("mysignal(int)"),
                       progressBar, QtCore.SLOT("setValue(int)"))
button = QtGui.QPushButton("Запустить процесс")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(progressBar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())