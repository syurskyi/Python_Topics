____ PySide.?C.. _____ *
____ PySide.QtGui _____ *

c_ dialogClass(?D..
    ___  -
        super(dialogClass, self). - ()
        ly _ QVBoxLayout
        label _ QLineEdit()
        ly.addWidget(label)

        ok_btn _ ?PB..('OK')
        ly.addWidget(ok_btn)

        cancel_btn _ ?PB..('Cancel')
        ly.addWidget(cancel_btn)

        ok_btn.c___.c..(accept)
        cancel_btn.c___.c..(reject)

    ___ getData
        return dict(text_label.t..())