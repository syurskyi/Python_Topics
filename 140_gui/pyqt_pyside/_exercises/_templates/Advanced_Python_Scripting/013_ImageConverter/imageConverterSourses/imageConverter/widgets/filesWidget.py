____ ?.?C.. _____ _
____ ?.?G.. _____ _
_____ os

icon _ os.path.j..(os.path.dirname(__file__), 'drag.png')


c_ listWidgetClass(?LW..
    ___  -
        s__(listWidgetClass, self). -
        sWF..(__.WSOTH..)
        sDDM..(QAbstractItemView.DO..)
        setSelectionMode(QAbstractItemView.ExtendedSelection)
        files _ []

    ___ dropEvent , event
        mimedata _ event.mD..
        __ mimedata.hU..(
            ___ f __ mimedata.u..(
                addFile(f.toLocalFile())

    ___ dragEnterEvent , event
        __ event.source __ self:
            event.ignore
        ____
            mimedata _ event.mD..
            __ mimedata.hU..(
                event.a..
            ____
                event.ignore

    ___ dragMoveEvent , event
        __ event.source __ self:
            event.ignore
        ____
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

    ___ deleteSelected
        ___ s __ selectedItems(
            files.remove(s.data(32))
            tI..(indexFromItem(s).row())


    ___ getAllFiles
        r_ files

    ___ keyPressEvent , event
        __ event.key __ __.Key_Delete:
            deleteSelected
