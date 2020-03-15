# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Lock and removed handler")
        self.resize(300, 150)
        self.button1 = QtGui.QPushButton("Push me")
        self.button2 = QtGui.QPushButton("Lock")
        self.button3 = QtGui.QPushButton("Unlock")
        self.button4 = QtGui.QPushButton("Delete hamdler")
        self.button3.setEnabled(False)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)
        vbox.addWidget(self.button4)
        self.setLayout(vbox)
        self.connect(self.button1, QtCore.SIGNAL("clicked()"),
                     QtCore.SLOT("on_clicked_button1()"))
        self.connect(self.button2, QtCore.SIGNAL("clicked()"),
                     QtCore.SLOT("on_clicked_button2()"))
        self.connect(self.button3, QtCore.SIGNAL("clicked()"),
                     QtCore.SLOT("on_clicked_button3()"))
        self.connect(self.button4, QtCore.SIGNAL("clicked()"),
                     QtCore.SLOT("on_clicked_button4()"))
    @QtCore.pyqtSlot()
    def on_clicked_button1(self):
        print("Нажата кнопка button1")
    @QtCore.pyqtSlot()
    def on_clicked_button2(self):
        self.button1.blockSignals(True)
        self.button2.setEnabled(False)
        self.button3.setEnabled(True)
    @QtCore.pyqtSlot()
    def on_clicked_button3(self):
        self.button1.blockSignals(False)
        self.button2.setEnabled(True)
        self.button3.setEnabled(False)
    @QtCore.pyqtSlot()
    def on_clicked_button4(self):
        self.disconnect(self.button1,
                        QtCore.SIGNAL("clicked()"), self,
                        QtCore.SLOT("on_clicked_button1()"))
        self.button2.setEnabled(False)
        self.button3.setEnabled(False)
        self.button4.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())