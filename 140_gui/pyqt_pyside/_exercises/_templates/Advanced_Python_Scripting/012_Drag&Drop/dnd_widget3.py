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
        event.accept()
        # print 'ENTER', type(event)

    ___ dragMoveEvent , event
        # print 'MOVE'
        pass

__ __name__ __ '__main__':
    app = ?A..([])
    w = listWidgetClass()
    w.s..
    app.exec_()