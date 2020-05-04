____ ?.?G.. _____ _
# from PyQt4.QtGui import *

c_ simpleWindow(?W..
    ___  -  
        s__(simpleWindow, self). -
        ly _ QVBoxLayout
        btn  _ ?PB..('Open')
        ly.addWidget(btn)
        r..(300,200)
        btn.c___.c..(showMessage)

    ___ showMessage 
        _filter _ 'Python File(*.py);; All(*.*)'
        d _ ?FD__.gOFN.. , 'Set folder', 'c:/tmp', _filter)
        print d

__ _____ __ ______
    app _ ?A..
    w _ simpleWindow
    w.s..
    app.e..