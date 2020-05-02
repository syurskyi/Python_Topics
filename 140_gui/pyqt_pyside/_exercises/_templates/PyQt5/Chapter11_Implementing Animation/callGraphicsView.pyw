_____ ___

____ PyQt5.?W.. _____ ?D.., ?A.., QGraphicsScene, QGraphicsPixmapItem
____ PyQt5.QtGui _____ QPixmap
____ demoGraphicsView _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        scene _ QGraphicsScene
        pixmap_ QtGui.QPixmap()
        pixmap.load("bintupic.jpg")
        item_QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        ui.graphicsView.setScene(scene)

__ _ ____ __ _____
    app _ ?A..(___.argv)
    myapp _ MyForm()
    myapp.s..
    ___.e..(app.exec_())
