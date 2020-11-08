# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.id = None
    def event(self, e):
        if e.type() == QtCore.QEvent.Shortcut:
            if self.id == e.shortcutId():
                self.setFocus(QtCore.Qt.ShortcutFocusReason)
                return True
        return QtWidgets.QLineEdit.event(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)
        self.label = QtWidgets.QLabel("Устано&вить фокус на поле 1")
        self.lineEdit1 = QtWidgets.QLineEdit()
        self.label.setBuddy(self.lineEdit1)
        self.lineEdit2 = MyLineEdit()
        self.lineEdit2.id = self.lineEdit2.grabShortcut(
                            QtGui.QKeySequence.mnemonic("&е"))
        self.button = QtWidgets.QPushButton("&Убрать фокус с поля 1")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.lineEdit1)
        self.vbox.addWidget(self.lineEdit2)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.on_clicked)
    def on_clicked(self):
        self.lineEdit1.clearFocus()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

# self.lineEdit2 = QtWidgets.QLineEdit()
# self.shc = QtWidgets.QShortcut(QtGui.QKeySequence.mnemonic("&е"), self)
# self.shc.setContext(QtCore.Qt.WindowShortcut)
# self.shc.activated.connect(self.lineEdit2.setFocus)
#
#
# self.lineEdit2 = QtWidgets.QLineEdit()
# self.act = QtWidgets.QAction(self)
# self.act.setShortcut(QtGui.QKeySequence.mnemonic("&е"))
# self.act.triggered.connect(self.lineEdit2.setFocus)
# self.addAction(self.act)