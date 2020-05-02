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
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            for f in mimedata.urls(
                print f.userName()
                print f.toLocalFile()
        elif mimedata.hasText(
            print mimedata.t..()


    ___ dragEnterEvent , event
        event.accept()
        print 'ENTER', type(event)

    ___ dragMoveEvent , event
        event.accept()
        # print 'MOVE'


__ __name__ __ '__main__':
    _____ ___

    app _ None
    try:
        _____ nuke
    except ImportError:
        app _ ?A..(___.argv)
    main _ listWidgetClass()
    main.s..

    __ app is not None:
        app.exec_()