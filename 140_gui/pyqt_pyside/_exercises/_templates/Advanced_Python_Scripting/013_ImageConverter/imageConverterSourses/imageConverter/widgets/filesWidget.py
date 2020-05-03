____ PySide.?C.. _____ _
____ PySide.?G.. _____ _
_____ os

icon _ os.path.j..(os.path.dirname(__file__), 'drag.png')


c_ listWidgetClass(QListWidget
    ___  -
        super(listWidgetClass, self). - 
        setWindowFlags(__.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DropOnly)
        setSelectionMode(QAbstractItemView.ExtendedSelection)
        files _ []

    ___ dropEvent , event
        mimedata _ event.mimeData
        __ mimedata.hasUrls(
            ___ f __ mimedata.urls(
                addFile(f.toLocalFile())

    ___ dragEnterEvent , event
        __ event.source is self:
            event.ignore
        ____
            mimedata _ event.mimeData
            __ mimedata.hasUrls(
                event.accept
            ____
                event.ignore

    ___ dragMoveEvent , event
        __ event.source is self:
            event.ignore
        ____
            mimedata _ event.mimeData
            __ mimedata.hasUrls(
                event.accept
            ____
                event.ignore

    ___ addFile , path
        __ not path __ files:
            item _ ?LWI..
            item.sT..(os.path.basename(path))
            item.setData(__.UserRole, path)
            files.ap..(path)

    ___ deleteSelected
        ___ s __ selectedItems(
            files.remove(s.data(32))
            tI..(indexFromItem(s).row())


    ___ getAllFiles
        r_ files

    ___ keyPressEvent , event
        __ event.key __ __.Key_Delete:
            deleteSelected
