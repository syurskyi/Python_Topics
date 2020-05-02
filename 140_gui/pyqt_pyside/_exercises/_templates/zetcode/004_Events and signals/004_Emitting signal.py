______ ___
____ PySide ______ QtGui, QtCore


c_ Communicate(QtCore.QObject):

    closeApp _ QtCore.pyqtSignal


c_ Example(QtGui.QMainWindow):

    ___ -
        s__ ?  .-

        ?


    ___ initUI

        c _ Communicate
        c.closeApp.connect(close)

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
        app _ QtGui.QApplication(___.argv)
    main _ Example
    main.show

    __ app __ no. N..:
        app.e..