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
        mimedata _ event.mimeData
        __ mimedata.hasUrls(
            ___ f __ mimedata.urls(
                addFile(f.toLocalFile())

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
        __ no. path __ files:
            item _ ?LWI..
            item.sT..(os.path.basename(path))
            item.setData(__.UserRole, path)
            files.ap..(path)

__ _____ __ ______
    _____ ___

    app _ N..
    ___
        _____ nuke
    _____ I..
        app _ ?A..
    main _ listWidgetClass
    main.s..

    __ app __ no. N..:
        app.exec_