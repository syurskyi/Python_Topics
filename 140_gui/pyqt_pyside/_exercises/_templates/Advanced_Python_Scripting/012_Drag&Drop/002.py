_____ ___
_____ os
____ PySide.?C.. _____ *
____ PySide.QtGui _____ *


c_ listWidgetClass(QListWidget
    ___  -
        super(listWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DropOnly)

    ___ dropEvent , event
        print 'DROP', type(event)
        mimedata = event.mimeData()
        __ mimedata.hasUrls(
            print mimedata.urls()
        elif mimedata.hasColor(
            print mimedata.colorData()
        elif mimedata.hasText(
            print mimedata.text()


    ___ dragEnterEvent , event
        event.accept()
        print 'ENTER', type(event)

    ___ dragMoveEvent , event
        event.accept()
        # print 'MOVE'


__ __name__ __ '__main__':
    _____ ___

    app = None
    try:
        _____ nuke
    except ImportError:
        app = ?A..(___.argv)
    main = listWidgetClass()
    main.s..

    __ app is not None:
        app.exec_()