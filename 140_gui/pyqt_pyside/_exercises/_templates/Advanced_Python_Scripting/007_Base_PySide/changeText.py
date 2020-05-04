____ ?.?C.. _____ _
____ ?.?G.. _____ _
# from import PyQt4 import QtCore


c_ SimpleWindowClass(?W..
    ___  -  
        s__(SimpleWindowClass, self). -
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


__ _____ __ ______
    app _ ?A..
    w _ SimpleWindowClass
    w.s..
    app.e..
