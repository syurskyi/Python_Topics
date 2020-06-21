from PySide import QtCore, QtGui


class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        # Запрет передачи события родителю
        self.setAttribute(QtCore.Qt.WA_NoMousePropagation, True)

    def mousePressEvent(self, e):
        if e.buttons() & QtCore.Qt.LeftButton:
            print("Нажата левая кнопка мыши")
        if e.buttons() & QtCore.Qt.RightButton:
            print("Нажата правая кнопка мыши")
        if e.buttons() & QtCore.Qt.MiddleButton:
            print("Нажата средняя кнопка мыши")
        if (e.buttons() & QtCore.Qt.LeftButton and
            e.buttons() & QtCore.Qt.RightButton):
            print("Левая и правая кнопки нажаты")
        self.setText(
             "X: {0}, Y: {1}, globalX: {2}, globalY: {3}".format(
             e.x(), e.y(), e.globalX(), e.globalY()))
        e.ignore()
        QtGui.QLabel.mousePressEvent(self, e)

    def mouseReleaseEvent(self, e):
        print("Отпускание кнопки")
        QtGui.QLabel.mouseReleaseEvent(self, e)

    def mouseDoubleClickEvent(self, e):
        print("Двойной щелчок")
        QtGui.QLabel.mouseDoubleClickEvent(self, e)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

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