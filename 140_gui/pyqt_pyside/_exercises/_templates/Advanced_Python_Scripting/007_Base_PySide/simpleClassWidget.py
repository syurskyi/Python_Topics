____ PySide.QtGui _____ *

c_ myWidget(?W..
    ___  -
        super(myWidget, self). - ()
        l = QVBoxLayout()
        setLayout(l)
        label = QLabel('Text')
        l.addWidget(label)
        b = ?PB..('OK')
        l.addWidget(b)

app = ?A..([])
w = myWidget()
w.s..
app.exec_()