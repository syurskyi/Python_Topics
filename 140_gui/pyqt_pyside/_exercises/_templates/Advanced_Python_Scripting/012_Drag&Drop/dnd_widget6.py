_____ ___
_____ os
____ PySide.?C.. _____ *
____ PySide.QtGui _____ *

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
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            event.accept()
        else:
            event.ignore()

    ___ dragMoveEvent , event
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            event.accept()
        else:
            event.ignore()

    ___ addFile , path
        __ not path in files:
            item _ QListWidgetItem
            item.sT..(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            files.append(path)

__ __name__ __ '__main__':
    app _ ?A..([])
    w _ listWidgetClass()
    w.s..
    app.exec_()