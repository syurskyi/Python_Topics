# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

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

class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)

    def customEvent(self, e):
        if e.type() == MyEvent.idType:
            self.setText("Got data: {0}".format(e.get_data()))

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = MyLabel("")
        self.button = QtGui.QPushButton("Start the process")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.thread = MyThread(self.label)
        self.button.clicked.connect(self.on_clicked)
        self.thread.finished.connect(self.on_finished)

    def on_clicked(self):
        self.label.setText("The process launched")
        self.button.setEnabled(False)
        self.thread.start()

    def on_finished(self):
        self.label.setText("The process completed")
        self.button.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("postEvent")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())