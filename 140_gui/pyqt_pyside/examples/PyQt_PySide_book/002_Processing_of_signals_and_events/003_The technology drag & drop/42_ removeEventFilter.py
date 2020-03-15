# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)

    def event(self, e):
        if e.type() == QtCore.QEvent.KeyPress:
            self.setText(e.text())
            print("event")
        return QtGui.QLabel.event(self, e)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = MyLabel("Press the B key on the keyboard")
        # Назначаем фильтр
        self.label.installEventFilter(self)
        self.button = QtGui.QPushButton("Remove Filter")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.label.removeEventFilter(self)

    def eventFilter(self, obj, e):
        if e.type() == QtCore.QEvent.KeyPress:
            print("eventFilter", type(obj))
            if e.key() == QtCore.Qt.Key_B:
                print("The event from the <B> key will not reach the component")
                return True
        return QtGui.QWidget.eventFilter(self, obj, e)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Filtering events")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())