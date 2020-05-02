_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ demoMouseClicks _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        s..

    ___ mousePressEvent , event
        __ event.buttons() & ?C...Qt.LeftButton:
            x = event.x()
            y = event.y()    
            text = "x: {0},  y: {1}".format(x, y)
            ui.labelPress.sT..('Mouse button pressed at '+text)
            
    ___ mouseReleaseEvent , event
        x = event.x()
        y = event.y()    
        text = "x: {0},  y: {1}".format(x, y)
        ui.labelRelease.sT..('Mouse button released at '+text)
        update()
                  
__ __name____"__main__":
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
