_____ ___
____ ?.?W.. _____ QMainWindow, ?A..
____ ?.?G.. _____ QPainter

____ demoMenuBar _____ _

c_ AppWindow(QMainWindow
    ___  -  
        s__. - 
        ui _ Ui_MainWindow
        ?.sU..
        pos1 _ [0,0]
        pos2 _ [0,0]
        toDraw_""
        ?.actionDraw_Circle.t__.c..(drawCircle)
        ?.actionDraw_Rectangle.t__.c..(drawRectangle)
        ?.actionDraw_Line.t__.c..(drawLine)
        ?.actionPage_Setup.t__.c..(pageSetup)
        ?.actionSet_Password.t__.c..(setPassword)
        ?.actionCut.t__.c..(cutMethod)
        ?.actionCopy.t__.c..(copyMethod)
        ?.actionPaste.t__.c..(pasteMethod)
        s..

    ___ paintEvent , event
        qp _ QPainter
        qp.begin
        __ toDraw__"rectangle":
            width _ pos2[0]-pos1[0]
            height _ pos2[1] - pos1[1]     
            qp.drawRect(pos1[0], pos1[1], width, height)
        __ toDraw__"line":
            qp.drawLine(pos1[0], pos1[1], pos2[0], pos2[1])
        __ toDraw__"circle":
            width _ pos2[0]-pos1[0]
            height _ pos2[1] - pos1[1]           
            rect _ ?C...QRect(pos1[0], pos1[1], width, height)
            startAngle _ 0
            arcLength _ 360 *16
            qp.drawArc(rect, startAngle, arcLength)      
        qp.end
        
    ___ mousePressEvent , event
        __ event.buttons & ?C...Qt.LeftButton:
            pos1[0], pos1[1] _ event.pos.x, event.pos.y
                        
    ___ mouseReleaseEvent , event
        pos2[0], pos2[1] _ event.pos.x, event.pos.y    
        update
               
    ___ drawCircle 
        ?.label.sT..("")
        toDraw_"circle"

    ___ drawRectangle 
        ?.label.sT..("")
        toDraw_"rectangle"

    ___ drawLine 
        ?.label.sT..("")
        toDraw_"line"

    ___ pageSetup 
        ?.label.sT..("Page Setup menu item is selected")

    ___ setPassword 
        ?.label.sT..("Set Password menu item is selected")
        
    ___ cutMethod 
        ?.label.sT..("Cut menu item is selected")

    ___ copyMethod 
        ?.label.sT..("Copy menu item is selected")

    ___ pasteMethod 
        ?.label.sT..("Paste menu item is selected")

app _ ?A..
w _ AppWindow
w.s..
___.e.. ?.e




