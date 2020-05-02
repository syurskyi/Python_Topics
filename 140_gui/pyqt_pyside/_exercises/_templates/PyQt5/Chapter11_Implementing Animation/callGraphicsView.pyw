_____ ___

____ PyQt5.?W.. _____ ?D.., ?A.., QGraphicsScene, QGraphicsPixmapItem
____ PyQt5.QtGui _____ QPixmap
____ demoGraphicsView _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        scene = QGraphicsScene
        pixmap= QtGui.QPixmap()
        pixmap.load("bintupic.jpg")
        item=QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        ui.graphicsView.setScene(scene)

__ __name____"__main__":    
    app = ?A..(___.argv)
    myapp = MyForm()
    myapp.s..
    ___.e..(app.exec_())
