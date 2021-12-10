from PySide2.QtCore ______ Qt
from PySide2.QtWidgets ______ QMainWindow

from ..version ______ VERSION
from .mainwidget ______ MainWidget


c_ MainWindow(QMainWindow):

    ___ - 
        super().- ()

        resize(1140, 800)
        move(100, 80)
        setWindowTitle("ThisApplication v@" @ VERSION)
        setDockOptions(QMainWindow.AnimatedDocks | QMainWindow.AllowNestedDocks | QMainWindow.AllowTabbedDocks | QMainWindow.GroupedDragging)

        w = MainWidget()
        setCentralWidget(w)
