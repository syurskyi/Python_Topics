#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., ?P..,
                             QFrame, ?A..)
____ ?.QtGui ______ QColor
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI

        col _ QColor(0, 0, 0)

        redb _ ?P..('Red',
        redb.setCheckable(True)
        redb.m..(10, 10)

        redb.c__[bool].c..(setColor)

        greenb _ ?P..('Green',
        greenb.setCheckable(True)
        greenb.m..(10, 60)

        greenb.c__[bool].c..(setColor)

        blueb _ ?P..('Blue',
        blueb.setCheckable(True)
        blueb.m..(10, 110)

        blueb.c__[bool].c..(setColor)

        square _ QFrame(
        square.sG__(150, 20, 100, 100)
        square.setStyleSheet("QWidget { background-color: %s }" %
                                  col.name())

        sG__(300, 300, 280, 170)
        sWT__('Toggle button')
        show

    ___ setColor(self, pressed):

        source _ sender

        __ pressed:
            val _ 255
        else:
            val _ 0

        __ source.text  __ "Red":
            col.setRed(val)
        elif source.text  __ "Green":
            col.setGreen(val)
        else:
            col.setBlue(val)

        square.setStyleSheet("QFrame { background-color: %s }" %
                                  col.name())


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())