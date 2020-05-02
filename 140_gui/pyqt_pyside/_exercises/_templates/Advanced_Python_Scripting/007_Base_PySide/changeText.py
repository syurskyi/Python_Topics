____ PySide.?C.. _____ *
____ PySide.QtGui _____ *
# from import PyQt4 import QtCore


c_ SimpleWindowClass(?W..
    ___  -  
        super(SimpleWindowClass, self). - ()
        layout = QVBoxLayout
        label = QLabel('Text')
        layout.addWidget(label)
        button = ?PB..('Press')
        layout.addWidget(button)
        button.clicked.c..(action)

    ___ action 
        label.sT..('New Text')
        button.sT..('Presseed')
        button.clicked.c..(close)


__ __name__ __ '__main__':
    app = ?A..([])
    w = SimpleWindowClass()
    w.s..
    app.exec_()
