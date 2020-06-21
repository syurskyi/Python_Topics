from PySide import QtGui, QtCore
import sys


class ToolExampleClass(QtGui.QWidget):


    # Constructor function
    def __init__(self):
        super(ToolExampleClass, self).__init__()
        self.setWindowTitle("Translucent window")
        self.resize(300, 100)
        self.setWindowOpacity(0.5)



def main():
    global c
    c = ToolExampleClass()
    desktop = QtGui.QApplication.desktop()
    x = (desktop.width() - c.width()) // 2
    y = (desktop.height() - c.height()) // 2
    c.move(x, y)

    c.show()

main()