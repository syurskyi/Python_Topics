_____ ___
_____ os
____ PySide.?C.. _____ *
____ PySide.QtGui _____ *

c_ listWidgetClass(QListWidget
    ___  -  
        super(listWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)          # #okno bydet vsegda poverh drygih okon
        setDragDropMode(QAbstractItemView.DropOnly)      # shto bu dropEvent zarabotal nado vklychit dlja etogo vidgeta setDragDropMode

    ___ dropEvent , event                # to shto proishodit kogda mu sbrasuvaem dannue na vidget
        print 'DROP', type(event)
        mimedata = event.mimeData()            # kogda mu peretaskivaem element, to pomimo togo shto srabatuvaet DropEvent,
                                               # srabatuvaet echjo 2 eventa, dragEnterEvent and dragMoveEvent
                                               # obuchno oni odinakovue i govorjat mozet li nash vidget prinjat' eti dannue kotorue mu peretaskivaem
                                               # i vnytri etogo eventa kak raz proverjaetsja kakogo tipa dannue k nam prishli
                                               # i etot event dolzen skazat' mozet li nash event eti dannue prinjat'
        __ mimedata.hasText(
            print 'text'
        elif mimedata.hasUrls(
            print 'urls'

    ___ dragEnterEvent , event
        event.accept()
        print 'ENTER', type(event)

    ___ dragMoveEvent , event
        event.accept()
        print 'MOVE'

__ __name__ __ '__main__':
    app = ?A..([])
    w = listWidgetClass()
    w.s..
    app.exec_()