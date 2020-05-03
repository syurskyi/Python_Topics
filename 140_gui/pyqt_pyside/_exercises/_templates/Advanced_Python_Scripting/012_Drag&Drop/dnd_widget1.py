_____ ___
_____ os
____ ?.?C.. _____ _
____ ?.?G.. _____ _

c_ listWidgetClass(?LW..
    ___  -  
        s__(listWidgetClass, self). -
        sWF..(__.WSOTH..)          # #okno bydet vsegda poverh drygih okon
        sDDM..(QAbstractItemView.DO..)      # shto bu dropEvent zarabotal nado vklychit dlja etogo vidgeta setDragDropMode

    ___ dropEvent , event                # to shto proishodit kogda mu sbrasuvaem dannue na vidget
        print 'DROP', ty..(event)
        mimedata _ event.mD..            # kogda mu peretaskivaem element, to pomimo togo shto srabatuvaet DropEvent,
                                               # srabatuvaet echjo 2 eventa, dragEnterEvent and dragMoveEvent
                                               # obuchno oni odinakovue i govorjat mozet li nash vidget prinjat' eti dannue kotorue mu peretaskivaem
                                               # i vnytri etogo eventa kak raz proverjaetsja kakogo tipa dannue k nam prishli
                                               # i etot event dolzen skazat' mozet li nash event eti dannue prinjat'
        __ mimedata.hasText(
            print 'text'
        ____ mimedata.hU..(
            print 'urls'

    ___ dragEnterEvent , event
        event.a..
        print 'ENTER', ty..(event)

    ___ dragMoveEvent , event
        event.a..
        print 'MOVE'

__ _____ __ ______
    app _ ?A..([])
    w _ listWidgetClass
    w.s..
    app.exec_