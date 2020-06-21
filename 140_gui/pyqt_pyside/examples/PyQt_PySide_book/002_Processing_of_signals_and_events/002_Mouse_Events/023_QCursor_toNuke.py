import os

from PySide import QtCore, QtGui

# path = 'C:/Users/serge/Dropbox/nuke/.nuke/example/PYSIDE/Books/PyQt - Sozdanie okonnuh
#  prilozenij na Python 3/PyQt/002_Processing_of_signals_and_events/002_Mouse_Events/'

icon = os.path.join('C:/Users/serge/Dropbox/nuke/.nuke/example/PYSIDE/Books/PyQt -'
                    ' Sozdanie okonnuh prilozenij na Python 3/PyQt/002_Processing_of_signals_and_events/'
                    '002_Mouse_Events/', 'Cursor.png')


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle("Custom Cursor")
        self.resize(300, 100)
        self.setCursor(QtGui.QCursor(QtGui.QPixmap(icon), 0, 0))
        self.label = QtGui.QLabel("Click in the window")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

    def mousePressEvent(self, e):
        self.label.setText("X: {0}, Y: {1}".format(e.x(), e.y()))
        e.ignore()
        QtGui.QWidget.mousePressEvent(self, e)


def main():
    global c
    c = MyWindow()
    c.raise_()
    c.show()

main()