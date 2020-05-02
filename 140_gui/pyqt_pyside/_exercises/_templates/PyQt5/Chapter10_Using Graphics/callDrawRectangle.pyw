_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.QtGui _____ QPainter

____ demoDrawRectangle _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        pos1 = [0,0]
        pos2 = [0,0]
        s..

    ___ paintEvent , event
        width = pos2[0]-pos1[0]
        height = pos2[1] - pos1[1]     
        qp = QPainter()
        qp.begin     
        qp.drawRect(pos1[0], pos1[1], width, height)        
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
