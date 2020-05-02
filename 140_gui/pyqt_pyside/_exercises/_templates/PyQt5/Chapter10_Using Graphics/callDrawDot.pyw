_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.QtGui _____ QPainter, QPen
____ ?.?C.. _____ Qt
____ demoDrawDot _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        pos1 _ [0,0]
        s..

    ___ paintEvent , event
        qp _ QPainter()
        qp.begin
        pen _ QPen(Qt.black, 5)
        qp.setPen(pen)
        qp.drawPoint(pos1[0], pos1[1])
        qp.end()
        
    ___ mousePressEvent , event
        __ event.buttons() & ?C...Qt.LeftButton:
            pos1[0], pos1[1] _ event.pos().x(), event.pos().y()
            update()
                              
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
