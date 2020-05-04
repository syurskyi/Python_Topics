_____ ___
_____ __
____ ?.?C.. _____ _
____ ?.?G.. _____ _

c_ listWidgetClass(?LW..
    ___  -  
        s__(listWidgetClass, self). -
        sWF..(__.WSOTH..)
        sDDM..(?AIV...DO..)

    ___ dropEvent , event
        print 'DROP', ty..(event)  # type event est' QDropEvent i samoe glavnoe shto on delaet on vozvrachaet mimedata
        mimedata _ event.mD..
        print mimedata
        __ ?.hU..(
            print mimedata.u..

    ___ dragEnterEvent , event
        event.a..
        # print 'ENTER', type(event)

    ___ dragMoveEvent , event
        # print 'MOVE', type(event)
        pass

__ _____ __ ______
    app _ ?A..([])
    w _ listWidgetClass
    w.s..
    app.exec_