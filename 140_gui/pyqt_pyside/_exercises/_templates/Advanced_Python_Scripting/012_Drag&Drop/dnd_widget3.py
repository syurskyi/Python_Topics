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
        mimedata _ event.mD..
        __ mimedata.hU..(
            ___ f __ mimedata.u..(
                print f.toLocalFile

    ___ dragEnterEvent , event
        event.a..
        # print 'ENTER', type(event)

    ___ dragMoveEvent , event
        # print 'MOVE'
        pass

__ _____ __ ______
    app _ ?A..([])
    w _ listWidgetClass
    w.s..
    app.exec_