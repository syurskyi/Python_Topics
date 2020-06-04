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


____ ?.?C.. ______ QBasicTimer
____ ?.?G.. ______ ?C.., QFontMetrics, QPainter, ?P..
____ ?.?W.. ______ (?A.., ?D.., QLineEdit, ?VBL..,
        ?W..)


c_ WigglyWidget(?W..):
    ___  -   parent_None):
        s__(WigglyWidget, self). - (parent)

        setBackgroundRole(?P...Midlight)
        setAutoFillBackground( st.

        newFont _ font()
        newFont.sPS..(newFont.pointSize() + 20)
        sF..(newFont)

        timer _ QBasicTimer()
        t__ _ ''

        step _ 0;
        timer.start(60, self)

    ___ paintEvent  event):
        sineTable _ (0, 38, 71, 92, 100, 92, 71, 38, 0, -38, -71, -92, -100, -92, -71, -38)

        metrics _ QFontMetrics(font())
        x _ (width() - metrics.width(t__)) / 2
        y _ (height() + metrics.ascent() - metrics.descent()) / 2
        color _ ?C..()

        painter _ QPainter

        ___ i, ch __ en..(t__):
            index _ (step + i) % 16
            color.setHsv((15 - index) * 16, 255, 191)
            painter.sP..(color)
            painter.drawText(x, y - ((sineTable[index] * metrics.height()) / 400), ch)
            x +_ metrics.width(ch)

    ___ sT..  newText):
        t__ _ newText

    ___ timerEvent  event):
        __ event.timerId() __ timer.timerId
            step +_ 1
            update()
        ____
            s__(WigglyWidget, self).timerEvent(event)


c_ Dialog(?D..):
    ___  -   parent_None):
        s__(Dialog, self). - (parent)

        wigglyWidget _ WigglyWidget()
        lineEdit _ ?LE..

        layout _ ?VBL..
        layout.aW..(wigglyWidget)
        layout.aW..(lineEdit)
        sL..(layout)

        lineEdit.tC...c..(wigglyWidget.sT..)

        lineEdit.sT..("Hello world!")

        sWT..("Wiggly")
        r..(360, 145)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    dialog _ Dialog()
    dialog.s..;
    ___.e.. ?.e..
