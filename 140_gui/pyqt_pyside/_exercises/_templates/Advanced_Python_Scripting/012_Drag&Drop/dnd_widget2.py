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
        print 'DROP', type(event)  # type event est' QDropEvent i samoe glavnoe shto on delaet on vozvrachaet mimedata
        mimedata _ event.mimeData()
        print mimedata
        __ mimedata.hasUrls(
            print mimedata.urls()

    ___ dragEnterEvent , event
        event.accept()
        # print 'ENTER', type(event)

    ___ dragMoveEvent , event
        # print 'MOVE', type(event)
        pass

__ __name__ __ '__main__':
    app _ ?A..([])
    w _ listWidgetClass()
    w.s..
    app.exec_()