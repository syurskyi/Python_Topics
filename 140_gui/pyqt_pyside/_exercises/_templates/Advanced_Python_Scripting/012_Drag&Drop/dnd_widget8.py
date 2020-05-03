_____ ___
_____ os
____ PySide.?C.. _____ _
____ PySide.?G.. _____ _

icon _ os.path.j..(os.path.dirname(__file__), 'drag.png')

c_ listWidgetClass(QListWidget
    ___  -
        super(listWidgetClass, self). -
        setWindowFlags(__.WindowStaysOnTopHint)
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
            url.ap..(i.data(__.UserRole))
        mimedata.setUrls([?U__.fromLocalFile(x) ___ x __ url])
        drag.setMimeData(mimedata)
        pix _ QPixmap(icon)
        drag.setPixmap(pix)
        r _ drag.exec_
        __ r __ __.DropAction.MoveAction:
            deleteSelected

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

    ___ mousePressEvent , event
        __ event.button __ __.MouseButton.RightButton:
            pass
        ____ event.button __ __.MouseButton.LB..:
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