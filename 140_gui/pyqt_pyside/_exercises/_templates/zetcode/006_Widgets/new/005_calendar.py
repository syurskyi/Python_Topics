#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ (W.., QCalendarWidget,
                             ?L.., ?A.., ?VB..)
____ ?.?C.. ______ QDate
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        vbox _ ?VB..(

        cal _ QCalendarWidget(
        cal.setGridVisible(T..)
        cal.c__[QDate].c..(showDate)

        vbox.aW..(cal)

        lbl _ ?L..(
        date _ cal.selectedDate
        lbl.sT..(date.toString())

        vbox.aW..(lbl)

        sL..(vbox)

        sG__(300, 300, 350, 300)
        sWT__('Calendar')
        show

    ___ showDate(self, date):
        lbl.sT..(date.toString())


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())