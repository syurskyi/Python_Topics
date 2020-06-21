____ ? _______ ?C.., ?G.., ?W..
____ ?.?C.. _______ Qt


c_ _Bar(?W...QWidget):
    pass

c_ PowerBar(?W...QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    ___  - (self, steps=5, *args, **kwargs):
        print('running __init__')
        s__(PowerBar, self). - (*args, **kwargs)

        layout = ?W...QVBoxLayout()
        _bar = _Bar()
        layout.aW..(_bar)

        _dial = ?W...QDial()
        layout.aW..(_dial)

        sL..(layout)
    ___ paintEvent(self, e):
        print('running paintEvent')
        painter = ?G...QPainter(self)
        brush = ?G...QBrush()
        brush.setColor(?G...QColor('black'))
        brush.setStyle(Qt.SolidPattern)
        rect = ?C...QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)
