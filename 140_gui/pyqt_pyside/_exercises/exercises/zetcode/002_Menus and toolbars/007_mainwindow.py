import sys
from PySide2.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PySide2.QtGui import QIcon


c_ Example ?M..

    ___ -
        s__. -

        ?

    ___ initUI
        textEdit _ ?TE..
        sCW.. ?

        exitAct _ ?A.. ?I.. *exit24.png *Exit ?
        ?.sS.. *Ctrl+Q
        ?.sST.. *Exit application
        ?.t___.c.. cl..

        sB..

        menubar _ mB..
        fileMenu _ ?.aM.. *&File
        ?.aA.. eA..

        toolbar _ aTB.. *Exi
        ?.aA.. eA..

        sG.. 300, 300, 350, 250
        sWT.. *Main window
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