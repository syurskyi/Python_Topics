_____ ___
_____ os
____ PySide.?C.. _____ _
____ PySide.?G.. _____ _


c_ listWidgetClass(QListWidget
    ___  -  
        super(listWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DropOnly)

    ___ dropEvent , event
        print 'DROP', type(event)
    #     mimedata = event.mimeData()
    #     if mimedata.hasText():
    #         print 'text'
    #         # print mimedata.hasText()
    #     elif mimedata.hasUrls():
    #         print 'urls'
    #         # print mimedata.urls()
    #
    ___ dragEnterEvent , event
        event.accept()
        print 'ENTER', type(event)

    ___ dragMoveEvent , event
        event.accept()
        # print 'MOVE'


__ __name__ __ '__main__':
    _____ ___

    app _ None
    ___
        _____ nuke
    _____ ImportError:
        app _ ?A..
    main _ listWidgetClass()
    main.s..

    __ app is not None:
        app.exec_()