from PySide import QtCore, QtGui


class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.grabMouse()

    def wheelEvent(self, e):
        if e.orientation() == QtCore.Qt.Horizontal:
            print("The wheel rotated Horizontal")
        elif e.orientation() == QtCore.Qt.Vertical:
            print("The wheel rotated Vertical")
        if e.buttons() & QtCore.Qt.LeftButton:
            print("Left button is pressed")
        if e.buttons() & QtCore.Qt.RightButton:
            print("Right button is pressed")
        if e.buttons() & QtCore.Qt.MiddleButton:
            print("Middle button is pressed")
        if (e.buttons() & QtCore.Qt.LeftButton and
            e.buttons() & QtCore.Qt.RightButton):
            print("The left and right buttons are pressed")
        self.setText(
        "X: {0}, Y: {1}, globalX: {2}, globalY: {3}\ndelta: {4}".format(
        e.x(), e.y(), e.globalX(), e.globalY(), e.delta()))
        e.ignore()
        QtGui.QLabel.wheelEvent(self, e)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Turn the mouse wheel")
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
