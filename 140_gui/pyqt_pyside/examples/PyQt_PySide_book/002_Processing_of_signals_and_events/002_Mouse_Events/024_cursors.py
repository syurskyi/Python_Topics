# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

cursors = [
(QtCore.Qt.ArrowCursor, "ArrowCursor"),
(QtCore.Qt.UpArrowCursor, "UpArrowCursor"),
(QtCore.Qt.CrossCursor, "CrossCursor"),
(QtCore.Qt.WaitCursor, "WaitCursor"),
(QtCore.Qt.IBeamCursor, "IBeamCursor"),
(QtCore.Qt.SizeVerCursor, "SizeVerCursor"),
(QtCore.Qt.SizeHorCursor, "SizeHorCursor"),
(QtCore.Qt.SizeBDiagCursor, "SizeBDiagCursor"),
(QtCore.Qt.SizeFDiagCursor, "SizeFDiagCursor"),
(QtCore.Qt.SizeAllCursor, "SizeAllCursor"),
(QtCore.Qt.SplitVCursor, "SplitVCursor"),
(QtCore.Qt.SplitHCursor, "SplitHCursor"),
(QtCore.Qt.PointingHandCursor, "PointingHandCursor"),
(QtCore.Qt.ForbiddenCursor, "ForbiddenCursor"),
(QtCore.Qt.OpenHandCursor, "OpenHandCursor"),
(QtCore.Qt.ClosedHandCursor, "ClosedHandCursor"),
(QtCore.Qt.WhatsThisCursor, "WhatsThisCursor"),
(QtCore.Qt.BusyCursor, "BusyCursor")]

class MyLabel(QtWidgets.QLabel):
    def __init__(self, cur, nameCur, parent=None):
        QtWidgets.QLabel.__init__(self, nameCur, parent)
        self.setFixedSize(150, 40)
        self.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
        self.setCursor(cur)
        self.setAlignment(QtCore.Qt.AlignCenter)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.labels = []
        self.grid = QtWidgets.QGridLayout()
        i = 0
        for j in range(6):
            for k in range(3):
                item = MyLabel(cursors[i][0], cursors[i][1])
                self.labels.append(item)
                self.grid.addWidget(item, j, k)
                i += 1
        self.setLayout(self.grid)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Изменение внешнего вида указателя мыши")
    window.resize(500, 350)
    desktop = QtWidgets.QApplication.desktop()
    window.move(desktop.availableGeometry().center() -
                window.rect().center())
    window.show()
    sys.exit(app.exec_())