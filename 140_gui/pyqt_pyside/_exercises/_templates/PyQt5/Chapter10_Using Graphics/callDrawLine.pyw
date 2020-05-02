_____ ___

____ PyQt5.?W.. _____ ?D.., ?A..
____ PyQt5.QtGui _____ QPainter

____ demoDrawLine _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        pos1 = [0,0]
        pos2 = [0,0]
        s..

    ___ paintEvent , event   
        qp = QPainter()
        qp.begin     
        qp.drawLine(pos1[0], pos1[1], pos2[0], pos2[1])        
        qp.end()
        
    ___ mousePressEvent , event
        __ event.buttons() & ?C...Qt.LeftButton:
            pos1[0], pos1[1] = event.pos().x(), event.pos().y()
                        
    ___ mouseReleaseEvent , event
        pos2[0], pos2[1] = event.pos().x(), event.pos().y()    
        update()
                  
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
