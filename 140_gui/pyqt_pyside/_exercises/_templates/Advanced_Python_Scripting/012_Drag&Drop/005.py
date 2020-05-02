_____ ___
_____ os
____ PySide.?C.. _____ *
____ PySide.QtGui _____ *

icon _ os.path.join(os.path.dirname(__file__), 'drag.png')

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
            for f in mimedata.urls(
                addFile(f.toLocalFile())

    ___ dragEnterEvent , event
        __ event.source() is self:
            event.ignore()
        ____
            mimedata _ event.mimeData()
            __ mimedata.hasUrls(
                event.accept()
            ____
                event.ignore()

    ___ dragMoveEvent , event
        __ event.source() is self:
            event.ignore()
        ____
            mimedata _ event.mimeData()
            __ mimedata.hasUrls(
                event.accept()
            ____
                event.ignore()

    ___ startDrag , dropAction
        drag _ QDrag
        mimedata _ QMimeData()
        url _ []
        for i in selectedItems(
            url.append(i.data(Qt.UserRole))
        mimedata.setUrls([QUrl.fromLocalFile(x) for x in url])
        drag.setMimeData(mimedata)
        pix _ QPixmap(icon)
        drag.setPixmap(pix)
        r _ drag.exec_()
        __ r __ Qt.DropAction.MoveAction:
            deleteSelected()

    ___ addFile , path
        __ not path in files:
            item _ QListWidgetItem
            item.sT..(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            files.append(path)

    ___ deleteSelected
        for s in selectedItems(
            files.remove(s.data(32))
            takeItem(indexFromItem(s).row())

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