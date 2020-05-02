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
        # print 'DROP', type(event)
        mimedata = event.mimeData()
        __ mimedata.hasUrls(
            for f in mimedata.urls(
                print f.toLocalFile()

    ___ dragEnterEvent , event
        mimedata = event.mimeData()
        __ mimedata.hasUrls(
            event.accept()
        else:
            event.ignore()

    ___ dragMoveEvent , event
        mimedata = event.mimeData()
        __ mimedata.hasUrls(
            event.accept()
        else:
            event.ignore()

    ___ addFile , path
        pass

__ __name__ __ '__main__':
    app = ?A..([])
    w = listWidgetClass()
    w.s..
    app.exec_()