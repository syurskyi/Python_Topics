# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def changeEvent(self, e):
        if e.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                print("Окно свернуто")
            elif self.isMaximized():
                print("Окно раскрыто до максимальных размеров")
            elif self.isFullScreen():
                print("Полноэкранный режим")
            elif self.isActiveWindow():
                print("Окно находится в фокусе ввода")
        QtGui.QWidget.changeEvent(self, e) # Отправляем дальше

    def showEvent(self, e):
        print("Окно отображено")
        QtGui.QWidget.showEvent(self, e)   # Отправляем дальше

    def hideEvent(self, e):
        print("Окно скрыто")
        QtGui.QWidget.hideEvent(self, e)   # Отправляем дальше

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())