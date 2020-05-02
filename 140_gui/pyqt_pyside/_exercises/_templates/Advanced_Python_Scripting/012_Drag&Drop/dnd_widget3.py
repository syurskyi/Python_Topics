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
        # print 'DROP', type(event)
        mimedata _ event.mimeData()
        __ mimedata.hasUrls(
            ___ f __ mimedata.urls(
                print f.toLocalFile()

    ___ dragEnterEvent , event
        event.accept()
        # print 'ENTER', type(event)

    ___ dragMoveEvent , event
        # print 'MOVE'
        pass

__ __name__ __ '__main__':
    app _ ?A..([])
    w _ listWidgetClass()
    w.s..
    app.exec_()