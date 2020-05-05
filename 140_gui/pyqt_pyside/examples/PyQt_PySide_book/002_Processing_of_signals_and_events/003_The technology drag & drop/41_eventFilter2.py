# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

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
        self.label.installEventFilter(self)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

    def eventFilter(self, obj, e):
        if e.type() == QtCore.QEvent.KeyPress:
            print("eventFilter", type(obj))
            if e.key() == QtCore.Qt.Key_B:
                print("Событие от клавиши <B> не дойдет до компонента")
                return True
        return QtWidgets.QWidget.eventFilter(self, obj, e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Фильтрация событий")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())