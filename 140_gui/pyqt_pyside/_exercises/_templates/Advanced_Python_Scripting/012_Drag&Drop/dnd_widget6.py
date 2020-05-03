_____ ___
_____ os
____ ?.?C.. _____ _
____ ?.?G.. _____ _

c_ listWidgetClass(?LW..
    ___  -
        s__(listWidgetClass, self). -
        sWF..(__.WSOTH..)
        sDDM..(QAbstractItemView.DragDrop)
        setSelectionMode(QAbstractItemView.ExtendedSelection)
        files _ []

    ___ dropEvent , event
        # print 'DROP', type(event)
        mimedata _ event.mD..
        __ mimedata.hU..(
            ___ f __ mimedata.u..(
                addFile(f.toLocalFile())

    ___ dragEnterEvent , event
        mimedata _ event.mD..
        __ mimedata.hU..(
            event.a..
        ____
            event.ignore

    ___ dragMoveEvent , event
        mimedata _ event.mD..
        __ mimedata.hU..(
            event.a..
        ____
            event.ignore

    ___ addFile , path
        __ no. path __ files:
            item _ ?LWI..
            item.sT..(os.path.basename(path))
            item.setData(__.UserRole, path)
            files.ap..(path)

__ _____ __ ______
    app _ ?A..([])
    w _ listWidgetClass
    w.s..
    app.exec_