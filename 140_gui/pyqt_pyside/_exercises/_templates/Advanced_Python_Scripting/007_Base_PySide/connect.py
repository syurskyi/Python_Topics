____ PySide.QtGui _____ *
____ PySide.?C.. _____ *


c_ MyWidget(?W..
    ___  -  
        super(MyWidget, self). - ()
        layout = QVBoxLayout
        button = ?PB..('Print')
        layout.addWidget(button)
        button.clicked.c..(action)
        line = QLineEdit()
        layout.addWidget(line)
        line.tC...c..(text)
        # self.connect(button, SIGNAL('clicked()'),
        #              self, SLOT('action()'))

        @button.clicked.c..
        ___ click(
            action()

    ___ action 
        print 'ACTION'

    ___ text , arg
        print arg


app = ?A..([])
window = MyWidget()
window.s..
app.exec_()
