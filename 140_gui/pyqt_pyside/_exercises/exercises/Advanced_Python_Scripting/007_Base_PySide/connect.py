____ ?.?G.. _____ _
____ ?.?C.. _____ _


c_ MyWidget(?W..
    ___  -  
        s__(MyWidget, self). -
        layout _ QVBoxLayout
        button _ ?PB..('Print')
        layout.addWidget(button)
        button.c___.c..(action)
        line _ QLineEdit
        layout.addWidget(line)
        line.tC...c..(t..)
        # self.connect(button, SIGNAL('clicked()'),
        #              self, SLOT('action()'))

        @button.c___.c..
        ___ click(
            action

    ___ action 
        print 'ACTION'

    ___ t.. , arg
        print arg


app _ ?A..
window _ MyWidget
window.s..
app.e..
