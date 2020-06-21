from PySide import QtCore, QtGui


class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        # Обрабатываем любые перемещения мыши
        self.setMouseTracking(True)
        # в пределах всего окна, а не комопонета
        self.grabMouse()

    def mouseMoveEvent(self, e):
        self.setText(
             "X: {0}, Y: {1}, globalX: {2}, globalY: {3}".format(
             e.x(), e.y(), e.globalX(), e.globalY()))
        e.ignore()
        QtGui.QLabel.mouseMoveEvent(self, e)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Move the mouse")
        self.label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)


def main():
    global c
    c = MyWindow()
    c.raise_()
    c.show()

main()