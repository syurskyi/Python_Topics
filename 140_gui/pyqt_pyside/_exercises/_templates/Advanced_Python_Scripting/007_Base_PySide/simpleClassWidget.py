____ PySide.QtGui _____ *

c_ myWidget(?W..
    ___  -
        super(myWidget, self). - ()
        l _ QVBoxLayout()
        setLayout(l)
        label _ QLabel('Text')
        l.addWidget(label)
        b _ ?PB..('OK')
        l.addWidget(b)

app _ ?A..([])
w _ myWidget()
w.s..
app.exec_()