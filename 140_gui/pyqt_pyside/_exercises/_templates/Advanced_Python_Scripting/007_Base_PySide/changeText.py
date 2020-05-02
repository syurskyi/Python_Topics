____ PySide.?C.. _____ _
____ PySide.?G.. _____ _
# from import PyQt4 import QtCore


c_ SimpleWindowClass(?W..
    ___  -  
        super(SimpleWindowClass, self). - ()
        layout _ QVBoxLayout
        label _ QLabel('Text')
        layout.addWidget(label)
        button _ ?PB..('Press')
        layout.addWidget(button)
        button.c___.c..(action)

    ___ action 
        label.sT..('New Text')
        button.sT..('Presseed')
        button.c___.c..(close)


__ __name__ __ '__main__':
    app _ ?A..([])
    w _ SimpleWindowClass()
    w.s..
    app.exec_()
