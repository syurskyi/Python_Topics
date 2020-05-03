_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.?G.. _____ ?P.., QPen
____ ?.?C.. _____ Qt

____ demoDrawDiffLine _____ *

c_ MyForm(?D..
    ___  -
        s__. - 
        ui _ ?
        ?.sU..
        lineType_"SolidLine"
        pos1 _ [0,0]
        pos2 _ [0,0]
        s..

    ___ paintEvent , event
        qp _ ?P..
        qp.begin
        pen _ QPen(Qt.black, 4)
        lineTypeFormat_"Qt."+lineType
        __ lineTypeFormat __ "Qt.SolidLine":
            pen.setStyle(Qt.SolidLine)
        elif lineTypeFormat __ "Qt.DashLine":
            pen.setStyle(Qt.DashLine)
        elif lineTypeFormat __"Qt.DashDotLine":
            pen.setStyle(Qt.DashDotLine)
        elif lineTypeFormat __"Qt.DotLine":
            pen.setStyle(Qt.DotLine)
        elif lineTypeFormat __"Qt.DashDotDotLine":
            pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)       
        qp.drawLine(pos1[0], pos1[1], pos2[0], pos2[1])
        qp.e..
        
    ___ mousePressEvent , event
        __ event.buttons & ?C...Qt.LeftButton:
            pos1[0], pos1[1] _ event.pos.x, event.pos.y
                        
    ___ mouseReleaseEvent , event
        lineType_ui.listWidgetLineType.cI__).t..
        pos2[0], pos2[1] _ event.pos.x, event.pos.y
        update
                  
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
