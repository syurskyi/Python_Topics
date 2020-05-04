import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

c_ Example ?M..

    ___ -
        s__. -

        ?

    ___ initUI(
        sG.. 300, 300, 300, 200
        sWT.. *Context menu
        ?

    ___ contextMenuEvent event
        cmenu _ ?M.. ?

        newAct _ ?.aA.. *New
        opnAct _ ?.aA.. *Open
        quitAct _ ?.aA.. *Quit
        action _ ?.e.._ mTG.. ?.p..

        __ ? __ qA..
            qA__.q..

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