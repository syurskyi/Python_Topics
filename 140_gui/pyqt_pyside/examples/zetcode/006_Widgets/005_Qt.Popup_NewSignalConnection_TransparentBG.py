from PySide import QtCore, QtGui
import sys



class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        # self.setWindowFlags(QtCore.Qt.Popup)
        self.setWindowTitle("Window Title")
        self.resize(300, 50)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        btn = QtGui.QPushButton("Print", self)
        btn.setGeometry(50, 10, 200, 30)

        btn.clicked.connect(self.action)

    def action(self):
        nuke.createNode('Blur')

def main():
    global c
    c = Example()
    desktop = QtGui.QApplication.desktop()
    x = (desktop.width() - c.width()) // 2
    y = (desktop.height() - c.height()) // 2
    c.move(x, y)

    c.show()


main()