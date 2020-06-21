#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


____ ?.?C.. ______ (pP.., pS.., pyqtSlot, QPoint, ?S..,
        __, ?T.., ?T..)
____ ?.?G.. ______ ?B.., ?C.., QPainter, ?P.., QPolygon
____ ?.?W.. ______ ?A.., ?W..


c_ PyAnalogClock(?W..):
    """PyAnalogClock(QWidget)

    Provides an analog clock custom widget with signals, slots and properties.
    The implementation is based on the Analog Clock example provided with both
    Qt and PyQt.
    """

    # Emitted when the clock's time changes.
    timeChanged _ pS..(?T..)

    # Emitted when the clock's time zone changes.
    timeZoneChanged _ pS..(in.)

    ___  -   parent_None):

        s__(PyAnalogClock, self). - (parent)

        timeZoneOffset _ 0

        timer _ ?T..
        timer.timeout.c..(update)
        timer.timeout.c..(updateTime)
        timer.start(1000)

        sWT..("Analog Clock")
        r..(200, 200)

        hourHand _ QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -40)
        ])
        minuteHand _ QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -70)
        ])

        hourColor _ ?C..(0, 127, 0)
        minuteColor _ ?C..(0, 127, 127, 191)

    ___ paintEvent  event):

        side _ min(width(), height())
        t__ _ ?T...currentTime()
        t__ _ t__.addSecs(timeZoneOffset * 3600)

        painter _ QPainter()
        painter.begin
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(width() / 2, height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.sP..(__.NoPen)
        painter.sB..(?B..(hourColor))

        painter.save()
        painter.rotate(30.0 * ((t__.hour() + t__.minute() / 60.0)))
        painter.drawConvexPolygon(hourHand)
        painter.restore()

        painter.sP..(hourColor)

        ___ i __ ra..(0, 12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.sP..(__.NoPen)
        painter.sB..(?B..(minuteColor))

        painter.save()
        painter.rotate(6.0 * (t__.minute() + t__.second() / 60.0))
        painter.drawConvexPolygon(minuteHand)
        painter.restore()

        painter.sP..(?P..(minuteColor))

        ___ j __ ra..(0, 60):
            __ (j % 5) !_ 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)

        painter.end()

    ___ minimumSizeHint

        r_ ?S..(50, 50)

    ___ sH..

        r_ ?S..(100, 100)

    ___ updateTime

        timeChanged.e..(?T...currentTime())

    # The timeZone property is implemented using the getTimeZone() getter
    # method, the setTimeZone() setter method, and the resetTimeZone() method.

    # The getter just returns the internal time zone value.
    ___ getTimeZone

        r_ timeZoneOffset

    # The setTimeZone() method is also defined to be a slot. The @pyqtSlot
    # decorator is used to tell PyQt which argument type the method expects,
    # and is especially useful when you want to define slots with the same
    # name that accept different argument types.

    @pyqtSlot(in.)
    ___ setTimeZone  value):

        timeZoneOffset _ value
        timeZoneChanged.e..(value)
        update()

    # Qt's property system supports properties that can be reset to their
    # original values. This method enables the timeZone property to be reset.
    ___ resetTimeZone

        timeZoneOffset _ 0
        timeZoneChanged.e..(0)
        update()

    # Qt-style properties are defined differently to Python's properties.
    # To declare a property, we call pyqtProperty() to specify the type and,
    # in this case, getter, setter and resetter methods.
    timeZone _ pP..(in., getTimeZone, setTimeZone, resetTimeZone)


__ __name__ __ "__main__":

    ______ ___

    app _ ?A..(___.a..
    clock _ PyAnalogClock()
    clock.s..
    ___.e.. ?.e..
