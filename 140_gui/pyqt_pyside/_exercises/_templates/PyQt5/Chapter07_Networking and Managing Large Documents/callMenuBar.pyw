_____ ___
____ ?.?W.. _____ QMainWindow, ?A..
____ ?.QtGui _____ QPainter

____ demoMenuBar _____ *

c_ AppWindow(QMainWindow
    ___  -  
        s__. - ()
        ui = Ui_MainWindow()
        ui.setupUi
        pos1 = [0,0]
        pos2 = [0,0]
        toDraw=""
        ui.actionDraw_Circle.triggered.c..(drawCircle)
        ui.actionDraw_Rectangle.triggered.c..(drawRectangle)
        ui.actionDraw_Line.triggered.c..(drawLine)
        ui.actionPage_Setup.triggered.c..(pageSetup)
        ui.actionSet_Password.triggered.c..(setPassword)
        ui.actionCut.triggered.c..(cutMethod)
        ui.actionCopy.triggered.c..(copyMethod)
        ui.actionPaste.triggered.c..(pasteMethod)       
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
        ui.label.sT..("")
        toDraw="circle"

    ___ drawRectangle 
        ui.label.sT..("")
        toDraw="rectangle"

    ___ drawLine 
        ui.label.sT..("")
        toDraw="line"

    ___ pageSetup 
        ui.label.sT..("Page Setup menu item is selected")

    ___ setPassword 
        ui.label.sT..("Set Password menu item is selected")
        
    ___ cutMethod 
        ui.label.sT..("Cut menu item is selected")

    ___ copyMethod 
        ui.label.sT..("Copy menu item is selected")

    ___ pasteMethod 
        ui.label.sT..("Paste menu item is selected")

app = ?A..(___.argv)
w = AppWindow()
w.s..
___.e..(app.exec_())




