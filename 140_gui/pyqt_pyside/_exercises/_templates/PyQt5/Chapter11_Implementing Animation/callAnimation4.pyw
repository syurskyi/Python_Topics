_____ ___

____ PyQt5.?W.. _____ ?D.., ?A..
____ PyQt5.?C.. _____ QRect, QPointF, QPropertyAnimation, pyqtProperty
____ PyQt5.QtGui _____ QPainter, QPainterPath

____ demoAnimation4 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonMoveCurve.clicked.c..(startAnimation)
        path _ QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 80, 180, 180, 170)                
        ui.labelPic.pos _ QPointF(20, 20)
        s..

    ___ paintEvent , e          
        qp _ QPainter()
        qp.begin
        qp.drawPath(path)
        qp.end()  

    ___ startAnimation 
        anim _ QPropertyAnimation(ui.labelPic, b'pos')
        anim.setDuration(4000)        
        anim.setStartValue(QPointF(20, 20))        
        positionValues _ [n/80 for n in range(0, 50)]
        for i in positionValues:
            anim.setKeyValueAt(i, path.pointAtPercent(i))  
        anim.setEndValue(QPointF(160, 150))
        anim.start()
        
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
