# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import time

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Clock in the window")
        self.resize(200, 100)
        self.timer_id = 0
        self.label = QtGui.QLabel("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button1 = QtGui.QPushButton("Launch")
        self.button2 = QtGui.QPushButton("Stop")
        self.button2.setEnabled(False)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)
        self.connect(self.button1, QtCore.SIGNAL("clicked()"),
                     self.on_clicked_button1)
        self.connect(self.button2, QtCore.SIGNAL("clicked()"),
                     self.on_clicked_button2)

    def on_clicked_button1(self):
        self.timer_id = self.startTimer(1000) # 1 секунда
        self.button1.setEnabled(False)
        self.button2.setEnabled(True)

    def on_clicked_button2(self):
        if self.timer_id:
            self.killTimer(self.timer_id)
            self.timer_id = 0
        self.button1.setEnabled(True)
        self.button2.setEnabled(False)

    def timerEvent(self, event):
        self.label.setText(time.strftime("%H:%M:%S"))

def main():
    main.panel = MyWindow()
    main.panel.show()

main()