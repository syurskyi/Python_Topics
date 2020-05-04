____ ?.?C.. _____ _
____ ?.?G.. _____ _
_____ __

icon _ __.path.j..(__.path.d_n..(__file__), 'drag.png')


c_ listWidgetClass(?LW..
    ___  -
        s__(listWidgetClass, self). -
        sWF..(__.WSOTH..)
        sDDM..(?AIV...DO..)
        sSM..(?AIV...ES..)
        files _ []

    ___ dropEvent , event
        mimedata _ event.mD..
        __ ?.hU..(
            ___ f __ ?.u..(
                aF..(f.tLF..())

    ___ dragEnterEvent , event
        __ event.source __ self:
            event.i..
        ____
            mimedata _ event.mD..
            __ ?.hU..(
                event.a..
            ____
                event.i..

    ___ dragMoveEvent , event
        __ event.source __ self:
            event.i..
        ____
            mimedata _ event.mD..
            __ ?.hU..(
                event.a..
            ____
                event.i..

    ___ aF.. , path
        __ no. path __ files:
            item _ ?LWI..
            item.sT..(__.path.b..(path))
            item.sD..(__.UR.., path)
            files.ap..(path)

    ___ deleteSelected
        ___ s __ sI..(
            files.r..(s.data(32))
            tI..(iFI..(s).r..())


    ___ getAllFiles
        r_ files

    ___ keyPressEvent , event
        __ event.key __ __.Key_Delete:
            deleteSelected
