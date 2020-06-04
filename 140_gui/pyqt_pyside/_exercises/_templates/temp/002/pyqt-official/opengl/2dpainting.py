#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2015 Riverbank Computing Limited.
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


______ ___
______ m__

____ ?.?C.. ______ QPointF, QRect, QRectF, __, ?T..
____ ?.?G.. ______ (?B.., ?C.., ?F.., QLinearGradient, QPainter,
        ?P.., QSurfaceFormat)
____ ?.?W.. ______ (?A.., QGridLayout, ?L.., QOpenGLWidget,
        ?W..)


c_ Helper o..
    ___  -
        gradient _ QLinearGradient(QPointF(50, -20), QPointF(80, 20))
        gradient.setColorAt(0.0, __.white)
        gradient.setColorAt(1.0, ?C..(0xa6, 0xce, 0x39))

        background _ ?B..(?C..(64, 32, 64))
        circleBrush _ ?B..(gradient)
        circlePen _ ?P..(__.black)
        circlePen.sW..(1)
        textPen _ ?P..(__.white)
        textFont _ ?F..()
        textFont.setPixelSize(50)

    ___ paint  painter, event, elapsed):
        painter.fillRect(event.rect(), background)
        painter.translate(100, 100)

        painter.save()
        painter.sB..(circleBrush)
        painter.sP..(circlePen)
        painter.rotate(elapsed * 0.030)

        r _ elapsed / 1000.0
        n _ 30
        ___ i __ ra..(n):
            painter.rotate(30)
            radius _ 0 + 120.0*((i+r)/n)
            circleRadius _ 1 + ((i+r)/n)*20
            painter.drawEllipse(QRectF(radius, -circleRadius,
                    circleRadius*2, circleRadius*2))

        painter.restore()

        painter.sP..(textPen)
        painter.sF..(textFont)
        painter.drawText(QRect(-50, -50, 100, 100), __.AlignCenter, "Qt")


c_ Widget(?W..):
    ___  -   helper, parent):
        s__(Widget, self). - (parent)

        helper _ helper
        elapsed _ 0
        sFS..(200, 200)

    ___ animate 
        elapsed _ (elapsed + sender().interval()) % 1000
        repaint()

    ___ paintEvent  event):
        painter _ QPainter()
        painter.begin
        painter.setRenderHint(QPainter.Antialiasing)
        helper.paint(painter, event, elapsed)
        painter.end()


c_ GLWidget(QOpenGLWidget):
    ___  -   helper, parent):
        s__(GLWidget, self). - (parent)

        helper _ helper
        elapsed _ 0
        sFS..(200, 200)
        setAutoFillBackground F..

    ___ animate 
        elapsed _ (elapsed + sender().interval()) % 1000
        update()

    ___ paintEvent  event):
        painter _ QPainter()
        painter.begin
        painter.setRenderHint(QPainter.Antialiasing)
        helper.paint(painter, event, elapsed)
        painter.end()


c_ Window(?W..):
    ___  -
        s__(Window, self). - ()

        sWT..("2D Painting on Native and OpenGL Widgets")

        helper _ Helper()
        native _ Widget(helper, self)
        openGL _ GLWidget(helper, self)
        nativeLabel _ ?L..("Native")
        nativeLabel.setAlignment(__.AlignHCenter)
        openGLLabel _ ?L..("OpenGL")
        openGLLabel.setAlignment(__.AlignHCenter)

        layout _ QGridLayout()
        layout.aW..(native, 0, 0)
        layout.aW..(openGL, 0, 1)
        layout.aW..(nativeLabel, 1, 0)
        layout.aW..(openGLLabel, 1, 1)
        sL..(layout)

        timer _ ?T..
        timer.timeout.c..(native.animate)
        timer.timeout.c..(openGL.animate)
        timer.start(50)


__ ______ __ ______

    app _ ?A..(___.a..

    fmt _ QSurfaceFormat()
    fmt.setSamples(4)
    QSurfaceFormat.setDefaultFormat(fmt)

    window _ Window()
    window.s..
    ___.e.. ?.e..
