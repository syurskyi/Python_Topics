_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.?G.. _____ ?P..

____ demoDrawLine _____ _

c_ MyForm(?D..
    ___  -  
        s__. - 
        ui _ ?
        ?.sU..
        pos1 _ [0,0]
        pos2 _ [0,0]
        s..

    ___ paintEvent , event   
        qp _ ?P..
        qp.b..
        qp.drawLine(pos1[0], pos1[1], pos2[0], pos2[1])        
        qp.e..
        
    ___ mousePressEvent , event
        __ event.buttons & ?C...__.LB..:
            pos1[0], pos1[1] _ event.p...x, event.p...y
                        
    ___ mouseReleaseEvent , event
        pos2[0], pos2[1] _ event.p...x, event.p...y
        update
                  
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
