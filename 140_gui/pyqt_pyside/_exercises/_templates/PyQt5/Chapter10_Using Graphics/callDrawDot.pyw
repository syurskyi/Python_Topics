_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.QtGui _____ QPainter, QPen
____ ?.?C.. _____ Qt
____ demoDrawDot _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        pos1 = [0,0]
        s..

    ___ paintEvent , event
        qp = QPainter()
        qp.begin
        pen = QPen(Qt.black, 5)
        qp.setPen(pen)
        qp.drawPoint(pos1[0], pos1[1])
        qp.end()
        
    ___ mousePressEvent , event
        __ event.buttons() & ?C...Qt.LeftButton:
            pos1[0], pos1[1] = event.pos().x(), event.pos().y()
            update()
                              
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
