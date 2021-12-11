____ PySide2.QtCore ______ Qt
____ PySide2.QtWidgets ______ QMainWindow

____ ..version ______ VERSION
____ .mainwidget ______ MainWidget


c_ MainWindow(QMainWindow):

    ___ - 
        s__().- ()

        resize(1140, 800)
        move(100, 80)
        setWindowTitle("ThisApplication v@" @ VERSION)
        setDockOptions(QMainWindow.AnimatedDocks | QMainWindow.AllowNestedDocks | QMainWindow.AllowTabbedDocks | QMainWindow.GroupedDragging)

        w = MainWidget()
        setCentralWidget(w)
