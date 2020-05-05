# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtWidgets.QFrame.Box |
                           QtWidgets.QFrame.Plain)
        self.startPos = None

    def mousePressEvent(self, e):
        if e.buttons() & QtCore.Qt.LeftButton:
            self.startPos = e.pos()
        else:
            self.startPos = None
            e.ignore()
        QtWidgets.QLabel.mousePressEvent(self, e)

    def mouseMoveEvent(self, e):
        if self.startPos is None:
            e.ignore()
            QtWidgets.QLabel.mouseMoveEvent(self, e)
            return
        length = (e.pos() - self.startPos).manhattanLength()
        if length <= QtWidgets.QApplication.startDragDistance():
            e.ignore()
            QtWidgets.QLabel.mouseMoveEvent(self, e)
            return
        data = QtCore.QMimeData()
        data.setText("Перетаскиваемый текст")
        drag = QtGui.QDrag(self)
        drag.setMimeData(data)
        drag.actionChanged.connect(self.on_action_changed)
        drag.targetChanged.connect(self.on_target_changed)
        action = drag.exec_(QtCore.Qt.MoveAction |
                            QtCore.Qt.CopyAction,
                            QtCore.Qt.MoveAction)
        if action == QtCore.Qt.CopyAction:
            print("Завершено действие CopyAction")
        elif action == QtCore.Qt.MoveAction:
            print("Завершено действие MoveAction")
        elif action == QtCore.Qt.IgnoreAction:
            print("Действие отменено")
        QtWidgets.QLabel.mouseMoveEvent(self, e)

    def on_action_changed(self, action):
        if action == QtCore.Qt.CopyAction:
            print("Действие изменено на CopyAction")
        elif action == QtCore.Qt.MoveAction:
            print("Действие изменено на MoveAction")

    def on_target_changed(self, target):
        print("Изменен компонент-приемник", type(target))

class MyLabel2(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setFixedSize(280, 80)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtWidgets.QFrame.Box |
                           QtWidgets.QFrame.Plain)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.acceptProposedAction()

    def dropEvent(self, e):
        if e.mimeData().hasText():
            self.setText(e.mimeData().text())
            e.accept()
        else:
            e.ignore()

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label1 = MyLabel("Щелкните здесь мышью\n" +
             "и перетащите в текстовый редактор\n(например, в WordPad)" +
             "\nили на надпись ниже")
        self.label2 = MyLabel2("Перетащите сюда текст")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.label2)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("drag & drop")
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec_())