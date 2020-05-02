____ PySide.?C.. _____ _
____ PySide.?G.. _____ _
_____ os

icon _ os.path.join(os.path.dirname(__file__), 'drag.png')


c_ listWidgetClass(QListWidget
    ___  -
        super(listWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DropOnly)
        setSelectionMode(QAbstractItemView.ExtendedSelection)
        files _ []

    ___ dropEvent , event
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


    ___ getAllFiles
        return files

    ___ keyPressEvent , event
        __ event.key() __ Qt.Key_Delete:
            deleteSelected()
