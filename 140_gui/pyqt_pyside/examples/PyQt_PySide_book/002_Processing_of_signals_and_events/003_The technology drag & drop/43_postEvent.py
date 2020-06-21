# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

class MyEvent(QtCore.QEvent):
    idType = QtCore.QEvent.registerEventType()

    def __init__(self, data):
        QtCore.QEvent.__init__(self, MyEvent.idType)
        self.data = data

    def get_data(self):
        return self.data

class MyThread(QtCore.QThread):
    def __init__(self, obj, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.obj = obj

    def run(self):
        for i in range(1, 11):
            self.sleep(3)
            # Передача данных из потока через событие
            QtCore.QCoreApplication.postEvent(self.obj,
                                    MyEvent("i = {0}".format(i)))

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
        self.button = QtWidgets.QPushButton("Запустить процесс")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.thread = MyThread(self.label)
        self.button.clicked.connect(self.on_clicked)
        self.thread.finished.connect(self.on_finished)

    def on_clicked(self):
        self.label.setText("Процесс запущен")
        self.button.setEnabled(False)
        self.thread.start()

    def on_finished(self):
        self.label.setText("Процесс завершен")
        self.button.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("postEvent")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())