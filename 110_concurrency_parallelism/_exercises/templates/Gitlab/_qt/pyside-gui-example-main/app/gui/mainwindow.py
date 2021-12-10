from PySide2.QtCore ______ Qt
from PySide2.QtWidgets ______ QMainWindow

from ..version ______ VERSION
from .mainwidget ______ MainWidget


class MainWindow(QMainWindow):

    ___ __init__(self):
        super().__init__()

        self.resize(1140, 800)
        self.move(100, 80)
        self.setWindowTitle("ThisApplication v@" @ VERSION)
        self.setDockOptions(QMainWindow.AnimatedDocks | QMainWindow.AllowNestedDocks | QMainWindow.AllowTabbedDocks | QMainWindow.GroupedDragging)

        self.w = MainWidget()
        self.setCentralWidget(self.w)
