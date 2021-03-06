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


____ ?.?C.. ______ QPoint, __, ?T.., ?T..
____ ?.?G.. ______ ?C.., QPainter, QPolygon
____ ?.?W.. ______ ?A.., ?W..


c_ AnalogClock(?W..):
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

    hourColor _ ?C..(127, 0, 127)
    minuteColor _ ?C..(0, 127, 127, 191)

    ___  -   parent_None):
        s__(AnalogClock, self). - (parent)

        timer _ ?T..
        timer.timeout.c..(update)
        timer.start(1000)

        sWT..("Analog Clock")
        r..(200, 200)

    ___ paintEvent  event):
        side _ min(width(), height())
        t__ _ ?T...currentTime()

        painter _ QPainter
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(width() / 2, height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.sP..(__.NoPen)
        painter.sB..(AnalogClock.hourColor)

        painter.save()
        painter.rotate(30.0 * ((t__.hour() + t__.minute() / 60.0)))
        painter.drawConvexPolygon(AnalogClock.hourHand)
        painter.restore()

        painter.sP..(AnalogClock.hourColor)

        ___ i __ ra..(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.sP..(__.NoPen)
        painter.sB..(AnalogClock.minuteColor)

        painter.save()
        painter.rotate(6.0 * (t__.minute() + t__.second() / 60.0))
        painter.drawConvexPolygon(AnalogClock.minuteHand)
        painter.restore()

        painter.sP..(AnalogClock.minuteColor)

        ___ j __ ra..(60):
            __ (j % 5) !_ 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    clock _ AnalogClock()
    clock.s..
    ___.e.. ?.e..
