_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ demoMouseClicks _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ ?
        ui.sU..
        s..

    ___ mousePressEvent , event
        __ event.buttons() & ?C...Qt.LeftButton:
            x _ event.x()
            y _ event.y()    
            t.. _ "x: {0},  y: {1}".format(x, y)
            ui.labelPress.sT..('Mouse button pressed at '+t..)
            
    ___ mouseReleaseEvent , event
        x _ event.x()
        y _ event.y()    
        t.. _ "x: {0},  y: {1}".format(x, y)
        ui.labelRelease.sT..('Mouse button released at '+t..)
        update()
                  
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e..(app.e
