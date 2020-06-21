# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

class MyFilter(QtCore.QObject):
    def __init__(self, id, parent=None):
        QtCore.QObject.__init__(self, parent)
        self.id = id

    def eventFilter(self, obj, e):
        if e.type() == QtCore.QEvent.KeyPress:
            print("eventFilter", self.id, type(obj))
            if e.key() == QtCore.Qt.Key_B:
                print("Событие от клавиши <B> не дойдет до компонента")
                return True
        return QtCore.QObject.eventFilter(self, obj, e)

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtWidgets.QFrame.Box |
                           QtWidgets.QFrame.Plain)

    def event(self, e):
        if e.type() == QtCore.QEvent.KeyPress:
            self.setText(e.text())
            print("event")
        return QtWidgets.QLabel.event(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = MyLabel("Нажмите клавишу B на клавиатуре")
        # Назначаем фильтр
        self.label.installEventFilter(MyFilter(1, self.label))
        self.label.installEventFilter(MyFilter(2, self.label))
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Фильтрация событий")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())