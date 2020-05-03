_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.?C.. _____ ?R.., QPointF, ?PA.., pyqtProperty
____ ?.?G.. _____ ?P.., QPainterPath

____ demoAnimation4 _____ _

c_ MyForm(?D..
    ___  -  
        s__. - 
        ui _ ?
        ?.sU..
        ?.pushButtonMoveCurve.c___.c..(startAnimation)
        path _ QPainterPath
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 80, 180, 180, 170)                
        ?.labelPic.p.. _ QPointF(20, 20)
        s..

    ___ paintEvent , e          
        qp _ ?P..
        qp.b..
        qp.drawPath(path)
        qp.e..

    ___ startAnimation 
        anim _ ?PA..(?.labelPic, b'pos')
        anim.sD.(4000)
        anim.sSV..(QPointF(20, 20))
        positionValues _ [n/80 ___ n in range(0, 50)]
        ___ i in positionValues:
            anim.setKeyValueAt(i, path.pointAtPercent(i))  
        anim.sEV..(QPointF(160, 150))
        anim.s..
        
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
