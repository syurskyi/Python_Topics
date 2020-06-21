from PySide import QtCore, QtGui

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


class MyLabel(QtGui.QLabel):
    def __init__(self, cur, nameCur, parent=None):
        QtGui.QLabel.__init__(self, nameCur, parent)
        self.setFixedSize(150, 40)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.setCursor(cur)
        self.setAlignment(QtCore.Qt.AlignCenter)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Change the appearance of the mouse pointer")
        self.resize(500, 350)
        self.labels = []
        self.grid = QtGui.QGridLayout()
        i = 0
        for j in range(6):
            for k in range(3):
                item = MyLabel(cursors[i][0], cursors[i][1])
                self.labels.append(item)
                self.grid.addWidget(item, j, k)
                i += 1
        self.setLayout(self.grid)


def main():
    global c
    c = MyWindow()
    desktop = QtGui.QApplication.desktop()
    c.move(desktop.availableGeometry().center() - c.rect().center())

    c.show()
