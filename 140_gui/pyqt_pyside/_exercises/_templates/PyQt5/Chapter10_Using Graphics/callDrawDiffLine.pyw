_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.QtGui _____ QPainter, QPen
____ ?.?C.. _____ Qt

____ demoDrawDiffLine _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        lineType="SolidLine"
        pos1 = [0,0]
        pos2 = [0,0]
        s..

    ___ paintEvent , event
        qp = QPainter()
        qp.begin
        pen = QPen(Qt.black, 4)
        lineTypeFormat="Qt."+lineType
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
        qp.end()
        
    ___ mousePressEvent , event
        __ event.buttons() & ?C...Qt.LeftButton:
            pos1[0], pos1[1] = event.pos().x(), event.pos().y()
                        
    ___ mouseReleaseEvent , event
        lineType=ui.listWidgetLineType.currentItem().text()
        pos2[0], pos2[1] = event.pos().x(), event.pos().y()
        update()
                  
__ __name____"__main__":
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
