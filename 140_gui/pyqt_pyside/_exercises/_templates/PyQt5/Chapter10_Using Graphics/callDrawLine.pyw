_____ ___

____ PyQt5.?W.. _____ ?D.., ?A..
____ PyQt5.?G.. _____ QPainter

____ demoDrawLine _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        pos1 _ [0,0]
        pos2 _ [0,0]
        s..

    ___ paintEvent , event   
        qp _ QPainter()
        qp.begin     
        qp.drawLine(pos1[0], pos1[1], pos2[0], pos2[1])        
        qp.end()
        
    ___ mousePressEvent , event
        __ event.buttons() & ?C...Qt.LeftButton:
            pos1[0], pos1[1] _ event.pos().x(), event.pos().y()
                        
    ___ mouseReleaseEvent , event
        pos2[0], pos2[1] _ event.pos().x(), event.pos().y()    
        update()
                  
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ ?
    w.s..
    ___.e..(app.e
