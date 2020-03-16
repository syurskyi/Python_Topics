from PySide import QtCore, QtGui


class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)

    def mousePressEvent(self, e):
        name = nuke.selectedNode().knob('name').getValue()
        if e.buttons() & QtCore.Qt.LeftButton:
            print("Нажата левая кнопка мыши")
        if e.buttons() & QtCore.Qt.RightButton:
            print("Нажата правая кнопка мыши")
        if e.buttons() & QtCore.Qt.MiddleButton:
            print("Нажата средняя кнопка мыши")
        if (e.buttons() & QtCore.Qt.LeftButton and
                    e.buttons() & QtCore.Qt.RightButton):
            print("Левая и правая кнопки нажаты")
        self.setText('Name of the Selected node is: ' + str(name))


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Name Window")

        self.resize(300, 150)
        self.label = MyLabel("Click here with the mouse")
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

