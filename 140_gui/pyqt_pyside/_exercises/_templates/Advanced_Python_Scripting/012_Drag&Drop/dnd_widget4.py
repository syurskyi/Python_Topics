_____ ___
_____ os
____ ?.?C.. _____ _
____ ?.?G.. _____ _


c_ listWidgetClass(?LW..
    ___  -
        s__(listWidgetClass, self). -
        sWF..(__.WSOTH..)
        sDDM..(QAbstractItemView.DO..)

    ___ dropEvent , event
        # print 'DROP', type(event)
        mimedata _ event.mimeData
        __ mimedata.hasUrls(
            ___ f __ mimedata.urls(
                print f.toLocalFile

    ___ dragEnterEvent , event
        mimedata _ event.mimeData
        __ mimedata.hasUrls(
            event.a..
        ____
            event.ignore

    ___ dragMoveEvent , event
        mimedata _ event.mimeData
        __ mimedata.hasUrls(
            event.a..
        ____
            event.ignore

    ___ addFile , path
        pass

__ _____ __ ______
    app _ ?A..([])
    w _ listWidgetClass
    w.s..
    app.exec_