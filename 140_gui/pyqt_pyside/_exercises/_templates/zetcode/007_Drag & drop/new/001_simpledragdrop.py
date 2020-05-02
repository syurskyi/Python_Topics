#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (?P.., W..,
                             ?L.., ?A..)
______ ___


c_ Button(?P..):

    ___ - (self, title, parent):
        s__ .- (title, parent)

        setAcceptDrops(T..)

    ___ dragEnterEvent(self, e):

        __ e.mimeData .hasFormat('text/plain'):
            e.accept
        ____
            e.ignore

    ___ dropEvent(self, e):

        sT..(e.mimeData .text())


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        edit _ ?L..('',
        edit.setDragEnabled(T..)
        edit.m..(30, 65)

        button _ Button("Button",
        button.m..(190, 65)

        sWT__('Simple drag and drop')
        sG__(300, 300, 300, 150)


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ex.show
    app.e..