import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QAction
from PyQt5.QtGui import QIcon


class Example ?M..

    ___ -
        s__. -

        ?

    ___ initUI
        exitAct _ ?A.. ?I.. *exit24.png *Exit ?
        ?.sS.. *Ctrl+Q
        ?.t__.c.. qA__.q..

        toolbar _ aTB.. *Exit
        ?.aA.. eA..

        sG.. 300, 300, 300, 200
        sWT.. *Toolbar
        ?


if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QApplication(sys.argv)
    main =Example()
    main.show()

    if app is not None:
        app.exec_()