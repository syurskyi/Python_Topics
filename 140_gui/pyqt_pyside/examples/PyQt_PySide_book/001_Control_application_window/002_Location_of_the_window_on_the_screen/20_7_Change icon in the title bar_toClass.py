# -*- coding: utf-8 -*-
from PySide import QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Change the window title icon")
        self.resize(300, 100)
        # window.setWindowIcon(QtGui.QIcon("Camera.png"))  # Иконка для окна
        # app.setWindowIcon(QtGui.QIcon("NukeApp128.png"))  # Иконка приложения
        self.change_icon()

        self.show()

    def change_icon(self):
        self.setWindowIcon(QtGui.QIcon("Camera.png"))  # Иконка для окна
        # self.setWindowIcon(QtGui.QIcon("NukeApp128.png"))  # Иконка приложения


# app = QtGui.QApplication(sys.argv)
# window = QtGui.QWidget()
# window.setWindowTitle("Change the window title icon")
# window.resize(300, 100)
# window.setWindowIcon(QtGui.QIcon("Camera.png")) # Иконка для окна
# app.setWindowIcon(QtGui.QIcon("NukeApp128.png"))    # Иконка приложения
# window.show()
# sys.exit(app.exec_())



def main():
    app = None

    app = QtGui.QApplication(sys.argv)
    ex = SampleWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()