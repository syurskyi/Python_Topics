# -*- coding: utf-8 -*-
"""
- Щелкните мышью на надписи, чтобы установить фокус ввода
- Нажмите любую клавишу
- Нажмите обычную клавишу вместе с модификаторами
- Нажмите комбинацию клавиш <Ctrl>+<C>
- Нажмите клавишу <B>
"""
from PyQt5 import QtCore, QtWidgets, QtGui


class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAlignment(QtCore.Qt.AlignCenter)

    def focusInEvent(self, e):
        self.grabKeyboard()
        QtWidgets.QLabel.focusInEvent(self, e)

    def focusOutEvent(self, e):
        self.releaseKeyboard()
        QtWidgets.QLabel.focusOutEvent(self, e)

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
            msg.append("Нажата комбинация <Ctrl>+<C>")
        if e.key() == QtCore.Qt.Key_B:
            msg.append("Нажата клавиша <B>")
        self.setText(
            "Код: {0}, символ: {1}\nmodifiers: {2}\n{3}".format(
                e.key(), e.text(), "+".join(modifiers), "\n".join(msg)))
        e.ignore()
        QtWidgets.QLabel.keyPressEvent(self, e)

    def keyReleaseEvent(self, e):
        print("Клавиша отпущена")
        QtWidgets.QLabel.keyReleaseEvent(self, e)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Нажмите любую клавишу")
        self.label.setFrameStyle(QtWidgets.QFrame.Box |
                                 QtWidgets.QFrame.Plain)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())