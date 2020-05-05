# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtWidgets.QFrame.Box |
                           QtWidgets.QFrame.Plain)

    def mousePressEvent(self, e):
        if e.buttons() & QtCore.Qt.LeftButton:
            print("Нажата левая кнопка мыши")
        self.setText("X: {0}, Y: {1}".format(e.x(), e.y()))
        e.ignore()
        QtWidgets.QLabel.mousePressEvent(self, e)

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
        e = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress,
                      QtCore.QPoint(5, 5), QtCore.Qt.LeftButton,
                      QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)
        QtCore.QCoreApplication.sendEvent(self.label, e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("sendEvent")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())