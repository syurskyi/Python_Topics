_____ ___
_____ os
____ ?.?C.. _____ _
____ ?.?G.. _____ _

icon _ os.path.j..(os.path.dirname(__file__), 'drag.png')

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
        __ event.source __ self:
            event.ignore
        ____
            mimedata _ event.mimeData
            __ mimedata.hasUrls(
                event.a..
            ____
                event.ignore

    ___ dragMoveEvent , event
        __ event.source __ self:
            event.ignore
        ____
            mimedata _ event.mimeData
            __ mimedata.hasUrls(
                event.a..
            ____
                event.ignore

    ___ startDrag , dropAction
        drag _ QDrag
        mimedata _ QMimeData
        url _ []
        ___ i __ selectedItems(
            url.ap..(i.data(__.UserRole))
        mimedata.setUrls([?U__.fromLocalFile(x) ___ x __ url])
        drag.setMimeData(mimedata)
        pix _ QPixmap(icon)
        drag.setPixmap(pix)
        r _ drag.exec_
        __ r __ __.DropAction.MoveAction:
            deleteSelected

    ___ addFile , path
        __ no. path __ files:
            item _ ?LWI..
            item.sT..(os.path.basename(path))
            item.setData(__.UserRole, path)
            files.ap..(path)

    ___ deleteSelected
        ___ s __ selectedItems(
            files.remove(s.data(32))
            tI..(indexFromItem(s).row())

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