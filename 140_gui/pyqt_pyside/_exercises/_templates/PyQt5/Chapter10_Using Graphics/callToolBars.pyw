_____ ___
____ ?.?W.. _____ QMainWindow, ?A..
____ ?.QtGui _____ QPainter

____ demoToolBars _____ *

c_ AppWindow(QMainWindow
    ___  -
        s__. - ()
        ui = Ui_MainWindow()
        ui.setupUi
        pos1 = [0,0]
        pos2 = [0,0]
        toDraw=""
        ui.actionCircle.triggered.c..(drawCircle)
        ui.actionRectangle.triggered.c..(drawRectangle)
        ui.actionLine.triggered.c..(drawLine)
        s..

    ___ paintEvent , event
        qp = QPainter()
        qp.begin
        __ toDraw__"rectangle":
            width = pos2[0]-pos1[0]
            height = pos2[1] - pos1[1]
            qp.drawRect(pos1[0], pos1[1], width, height)
        __ toDraw__"line":
            qp.drawLine(pos1[0], pos1[1], pos2[0], pos2[1])
        __ toDraw__"circle":
            width = pos2[0]-pos1[0]
            height = pos2[1] - pos1[1]
            rect = ?C...QRect(pos1[0], pos1[1], width, height)
            startAngle = 0
            arcLength = 360 *16
            qp.drawArc(rect, startAngle, arcLength)      
        qp.end()
        
    ___ mousePressEvent , event
        __ event.buttons() & ?C...Qt.LeftButton:
            pos1[0], pos1[1] = event.pos().x(), event.pos().y()
                        
    ___ mouseReleaseEvent , event
        pos2[0], pos2[1] = event.pos().x(), event.pos().y()
        update()
               
    ___ drawCircle
        toDraw="circle"

    ___ drawRectangle
        toDraw="rectangle"

    ___ drawLine
        toDraw="line"

app = ?A..(___.argv)
w = AppWindow()
w.s..
___.e..(app.exec_())




