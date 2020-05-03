_____ ___
____ ?.?W.. _____ ?M.., ?A..
____ ?.?G.. _____ ?P..

____ demoToolBars _____ _

c_ AppWindow(?M..
    ___  -
        s__. - 
        ui _ Ui_MainWindow
        ?.setupUi
        pos1 _ [0,0]
        pos2 _ [0,0]
        toDraw_""
        ?.actionCircle.t__.c..(drawCircle)
        ?.actionRectangle.t__.c..(drawRectangle)
        ?.actionLine.t__.c..(dL..)
        s..

    ___ paintEvent , event
        qp _ ?P..
        qp.b..
        __ toDraw__"rectangle":
            width _ pos2[0]-pos1[0]
            height _ pos2[1] - pos1[1]
            qp.dR..(pos1[0], pos1[1], width, height)
        __ toDraw__"line":
            qp.dL..(pos1[0], pos1[1], pos2[0], pos2[1])
        __ toDraw__"circle":
            width _ pos2[0]-pos1[0]
            height _ pos2[1] - pos1[1]
            rect _ ?C...?R..(pos1[0], pos1[1], width, height)
            startAngle _ 0
            arcLength _ 360 *16
            qp.drawArc(rect, startAngle, arcLength)      
        qp.e..
        
    ___ mousePressEvent , event
        __ event.buttons & ?C...__.LB..:
            pos1[0], pos1[1] _ event.p...x, event.p...y
                        
    ___ mouseReleaseEvent , event
        pos2[0], pos2[1] _ event.p...x, event.p...y
        update
               
    ___ drawCircle
        toDraw_"circle"

    ___ drawRectangle
        toDraw_"rectangle"

    ___ dL..
        toDraw_"line"

app _ ?A..
w _ AppWindow
w.s..
___.e.. ?.e




