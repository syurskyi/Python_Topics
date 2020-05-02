____ PySide.?C.. _____ *
____ PySide.QtGui _____ *

c_ dialogClass(?D..
    ___  -
        super(dialogClass, self). - ()
        ly = QVBoxLayout
        label = QLineEdit()
        ly.addWidget(label)

        ok_btn = ?PB..('OK')
        ly.addWidget(ok_btn)

        cancel_btn = ?PB..('Cancel')
        ly.addWidget(cancel_btn)

        ok_btn.clicked.c..(accept)
        cancel_btn.clicked.c..(reject)

    ___ getData
        return dict(text=label.text())