______ ___
____ PySide ______ QtGui, ?C..


c_ Communicate(?C...QObject):

    closeApp _ ?C...pyqtSignal


c_ Example(QtGui.QMainWindow):

    ___ -
        s__ ?  .-

        ?


    ___ initUI

        c _ Communicate
        c.closeApp.c..(close)

        sG__(300, 300, 290, 150)
        sWT__('Emit signal')
        show


    ___ mousePressEvent(self, event):

        c.closeApp.emit


__ _____ __ _______
    ______ ___

    app _ N..
    ___
        ______ n..
    ______ I..
        app _ QtGui.?A..(___.argv)
    main _ Example
    main.show

    __ app __ no. N..:
        app.e..