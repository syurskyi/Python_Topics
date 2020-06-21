from PySide import QtCore, QtGui


class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAlignment(QtCore.Qt.AlignCenter)

    def focusInEvent(self, e):
        self.grabKeyboard()
        QtGui.QLabel.focusInEvent(self, e)

    def focusOutEvent(self, e):
        self.releaseKeyboard()
        QtGui.QLabel.focusOutEvent(self, e)

    def keyPressEvent(self, e):
        msg, modifiers = [], []
        if e.modifiers() & QtCore.Qt.ShiftModifier:
            modifiers.append("Shift")
        if e.modifiers() & QtCore.Qt.ControlModifier:
            modifiers.append("Ctrl")
        if e.modifiers() & QtCore.Qt.AltModifier:
            modifiers.append("Alt")
        if len(modifiers) == 0:
            modifiers.append("No")
        if e.matches(QtGui.QKeySequence.Copy):
            msg.append("Pressed combination <Ctrl>+<C>")
        if e.key() == QtCore.Qt.Key_B:
            msg.append("Pressed key <B>")
        self.setText(
            "Code: {0}, symbol: {1}\nmodifiers: {2}\n{3}".format(
                e.key(), e.text(), "+".join(modifiers), "\n".join(msg)))
        e.ignore()
        QtGui.QLabel.keyPressEvent(self, e)

    def keyReleaseEvent(self, e):
        print("key released")
        QtGui.QLabel.keyReleaseEvent(self, e)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Press any key")
        self.label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.lineEdit = QtGui.QLineEdit()
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.lineEdit)
        self.setLayout(self.vbox)



def main():
    main.panel = MyWindow()
    main.panel.show()

main()