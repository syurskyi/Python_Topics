_____ ___
_____ os
____ PySide.?C.. _____ _
____ PySide.?G.. _____ _

icon _ os.path.join(os.path.dirname(__file__), 'drag.png')

c_ listWidgetClass(QListWidget
    ___  -
        super(listWidgetClass, self). -
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DragDrop)
        setSelectionMode(QAbstractItemView.ExtendedSelection)
        files _ []

    ___ dropEvent , event
        # print 'DROP', type(event)
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

    ___ startDrag , dropAction
        drag _ QDrag
        mimedata _ QMimeData
        url _ []
        ___ i __ selectedItems(
            url.ap..(i.data(Qt.UserRole))
        mimedata.setUrls([QUrl.fromLocalFile(x) ___ x __ url])
        drag.setMimeData(mimedata)
        pix _ QPixmap(icon)
        drag.setPixmap(pix)
        r _ drag.exec_
        __ r __ Qt.DropAction.MoveAction:
            deleteSelected

    ___ addFile , path
        __ not path __ files:
            item _ ?LWI..
            item.sT..(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            files.ap..(path)

    ___ deleteSelected
        ___ s __ selectedItems(
            files.remove(s.data(32))
            tI..(indexFromItem(s).row())

    ___ mousePressEvent , event
        __ event.button __ Qt.MouseButton.RightButton:
            pass
        elif event.button __ Qt.MouseButton.LeftButton:
            setDragDropMode(QAbstractItemView.NoDragDrop)
            super(listWidgetClass, self).mousePressEvent(event)
        ____
            setDragDropMode(QAbstractItemView.DragDrop)
            super(listWidgetClass, self).mousePressEvent(event)

    ___ mouseReleaseEvent , event
        setDragDropMode(QAbstractItemView.DragDrop)
        super(listWidgetClass, self).mouseReleaseEvent(event)

__ __name__ __ '__main__':
    app _ ?A..([])
    w _ listWidgetClass
    w.s..
    app.exec_