_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.?G.. _____ ?P..

____ demoDrawCircle _____ *

c_ MyForm(?D..
    ___  -  
        s__. - 
        ui _ ?
        ?.sU..
        pos1 _ [0,0]
        pos2 _ [0,0]
        s..

    ___ paintEvent , event
        width _ pos2[0]-pos1[0]
        height _ pos2[1] - pos1[1]     
        qp _ ?P..
        qp.begin     
        rect _ ?C...QRect(pos1[0], pos1[1], width, height)
        startAngle _ 0
        arcLength _ 360 *16
        qp.drawArc(rect, startAngle, arcLength)         
        qp.end
        
    ___ mousePressEvent , event
        __ event.buttons & ?C...Qt.LeftButton:
            pos1[0], pos1[1] _ event.pos.x, event.pos.y
                        
    ___ mouseReleaseEvent , event
        pos2[0], pos2[1] _ event.pos.x, event.pos.y    
        update
                  
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
