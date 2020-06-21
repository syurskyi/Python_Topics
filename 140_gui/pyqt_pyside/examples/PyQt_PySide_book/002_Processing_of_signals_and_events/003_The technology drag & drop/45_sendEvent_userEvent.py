# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

class MyEvent(QtCore.QEvent):
    idType = QtCore.QEvent.registerEventType()
    def __init__(self, data):
        QtCore.QEvent.__init__(self, MyEvent.idType)
        self.data = data
    def get_data(self):
        return self.data

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtWidgets.QFrame.Box |
                           QtWidgets.QFrame.Plain)

    def customEvent(self, e):
        if e.type() == MyEvent.idType:
            self.setText("Получены данные: {0}".format(e.get_data()))

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = MyLabel("")
        self.button = QtWidgets.QPushButton("Отправить сообщение")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        QtCore.QCoreApplication.sendEvent(self.label,
                                          MyEvent("512"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("sendEvent")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())