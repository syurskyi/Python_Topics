#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ (W.., QCalendarWidget,
                             ?L.., QApplication, ?VB..)
____ ?.QtCore ______ QDate
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        vbox _ ?VB..(

        cal _ QCalendarWidget(
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(showDate)

        vbox.aW..(cal)

        lbl _ ?L..(
        date _ cal.selectedDate
        lbl.setText(date.toString())

        vbox.aW..(lbl)

        sL..(vbox)

        sG__(300, 300, 350, 300)
        sWT__('Calendar')
        show

    ___ showDate(self, date):
        lbl.setText(date.toString())


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())