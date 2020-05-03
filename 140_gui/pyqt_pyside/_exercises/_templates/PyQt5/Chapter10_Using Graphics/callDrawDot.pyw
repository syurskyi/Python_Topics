_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.?G.. _____ ?P.., ?P..
____ ?.?C.. _____ __
____ demoDrawDot _____ _

c_ MyForm(?D..
    ___  -
        s__. - 
        ui _ ?
        ?.sU..
        pos1 _ [0,0]
        s..

    ___ paintEvent , event
        qp _ ?P..
        qp.begin
        pen _ ?P..(__.b.., 5)
        qp.setPen(pen)
        qp.drawPoint(pos1[0], pos1[1])
        qp.e..
        
    ___ mousePressEvent , event
        __ event.buttons & ?C...__.LeftButton:
            pos1[0], pos1[1] _ event.pos.x, event.pos.y
            update
                              
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
