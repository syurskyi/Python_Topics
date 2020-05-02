_____ ___
_____ os
____ PySide.?C.. _____ _
____ PySide.?G.. _____ _

c_ listWidgetClass(QListWidget
    ___  -  
        super(listWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DragDrop)
        setSelectionMode(QAbstractItemView.ExtendedSelection)
        files _ []

    ___ dropEvent , event
        # print 'DROP', type(event)
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            ___ f __ mimedata.urls(
                addFile(f.toLocalFile())

    ___ dragEnterEvent , event
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            event.accept()
        ____
            event.ignore()

    ___ dragMoveEvent , event
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            event.accept()
        ____
            event.ignore()

    ___ addFile , path
        __ not path __ files:
            item _ ?LWI..
            item.sT..(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            files.ap..(path)

__ __name__ __ '__main__':
    _____ ___

    app _ None
    try:
        _____ nuke
    except ImportError:
        app _ ?A..
    main _ listWidgetClass()
    main.s..

    __ app is not None:
        app.exec_()