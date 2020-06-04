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


____ ?.?C.. ______ QRect, QRectF, ?S.., __, ?T..
____ ?.?G.. ______ ?C.., QPainter, ?P.., ?P..
____ ?.?W.. ______ (?A.., QFrame, QGridLayout, ?L..,
        ?SP.., ?W..)


c_ CircleWidget(?W..):
    ___  -   parent_None):
        s__(CircleWidget, self). - (parent)

        floatBased _ F..
        antialiased _ F..
        frameNo _ 0

        setBackgroundRole(?P...Base)
        sSP..(?SP...E.., ?SP...E..)

    ___ setFloatBased  floatBased):
        floatBased _ floatBased
        update()

    ___ setAntialiased  antialiased):
        antialiased _ antialiased
        update()

    ___ minimumSizeHint
        r_ ?S..(50, 50)

    ___ sH..
        r_ ?S..(180, 180)

    ___ nextAnimationFrame
        frameNo +_ 1
        update()

    ___ paintEvent  event):
        painter _ QPainter
        painter.setRenderHint(QPainter.Antialiasing, antialiased)
        painter.translate(width() / 2, height() / 2)

        ___ diameter __ ra..(0, 256, 9):
            delta _ abs((frameNo % 128) - diameter / 2)
            alpha _ 255 - (delta * delta) / 4 - diameter
            __ alpha > 0:
                painter.sP..(?P..(?C..(0, diameter / 2, 127, alpha), 3))

                __ floatBased:
                    painter.drawEllipse(QRectF(-diameter / 2.0,
                            -diameter / 2.0, diameter, diameter))
                ____
                    painter.drawEllipse(QRect(-diameter / 2,
                            -diameter / 2, diameter, diameter))


c_ Window(?W..):
    ___  -
        s__(Window, self). - ()

        aliasedLabel _ createLabel("Aliased")
        antialiasedLabel _ createLabel("Antialiased")
        intLabel _ createLabel("Int")
        floatLabel _ createLabel("Float")

        layout _ QGridLayout()
        layout.aW..(aliasedLabel, 0, 1)
        layout.aW..(antialiasedLabel, 0, 2)
        layout.aW..(intLabel, 1, 0)
        layout.aW..(floatLabel, 2, 0)

        timer _ ?T..

        ___ i __ ra..(2):
            ___ j __ ra..(2):
                w _ CircleWidget()
                w.setAntialiased(j !_ 0)
                w.setFloatBased(i !_ 0)

                timer.timeout.c..(w.nextAnimationFrame)

                layout.aW..(w, i + 1, j + 1)

        timer.start(100)
        sL..(layout)

        sWT..("Concentric Circles")

    ___ createLabel  t__):
        label _ ?L..(t__)
        label.setAlignment(__.AlignCenter)
        label.setMargin(2)
        label.setFrameStyle(QFrame.Box | QFrame.Sunken)
        r_ label


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ Window()
    window.s..
    ___.e.. ?.e..
