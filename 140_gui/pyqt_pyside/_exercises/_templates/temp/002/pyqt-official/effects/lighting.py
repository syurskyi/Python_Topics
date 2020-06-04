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


______ m__

____ ?.?C.. ______ QPointF, __, ?T..
____ ?.?G.. ______ (?B.., ?C.., QLinearGradient, ?P.., QPainter,
        ?P.., QRadialGradient)
____ ?.?W.. ______ (?A.., QFrame, QGraphicsDropShadowEffect,
        QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView)


c_ Lighting(QGraphicsView):
    ___  -   parent_None):
        s__(Lighting, self). - (parent)

        angle _ 0.0
        m_scene _ QGraphicsScene()
        m_lightSource _ N..
        m_items _   # list

        setScene(m_scene)

        setupScene()

        timer _ ?T..
        timer.timeout.c..(animate)
        timer.sI..(30)
        timer.start()

        setRenderHint(QPainter.Antialiasing)
        setFrameStyle(QFrame.NoFrame)

    ___ setupScene 
        m_scene.setSceneRect(-300, -200, 600, 460)

        linearGrad _ QLinearGradient(QPointF(-100, -100), QPointF(100, 100))
        linearGrad.setColorAt(0, ?C..(255, 255, 255))
        linearGrad.setColorAt(1, ?C..(192, 192, 255))
        setBackgroundBrush(linearGrad)

        radialGrad _ QRadialGradient(30, 30, 30)
        radialGrad.setColorAt(0, __.yellow)
        radialGrad.setColorAt(0.2, __.yellow)
        radialGrad.setColorAt(1, __.transparent)

        pixmap _ ?P..(60, 60)
        pixmap.fill(__.transparent)

        painter _ QPainter(pixmap)
        painter.sP..(__.NoPen)
        painter.sB..(radialGrad)
        painter.drawEllipse(0, 0, 60, 60)
        painter.end()

        m_lightSource _ m_scene.aP..(pixmap)
        m_lightSource.setZValue(2)

        ___ i __ ra..(-2, 3):
            ___ j __ ra..(-2, 3):
                __ (i + j) & 1:
                    item _ QGraphicsEllipseItem(0, 0, 50, 50)
                ____
                    item _ QGraphicsRectItem(0, 0, 50, 50)

                item.sP..(?P..(__.black, 1))
                item.sB..(?B..(__.white))

                effect _ QGraphicsDropShadowEffect
                effect.setBlurRadius(8)
                item.setGraphicsEffect(effect)
                item.setZValue(1)
                item.setPos(i * 80, j * 80)
                m_scene.aI..(item)
                m_items.ap..(item)

    ___ animate 
        angle +_ (m__.pi / 30)
        xs _ 200 * m__.sin(angle) - 40 + 25
        ys _ 200 * m__.cos(angle) - 40 + 25
        m_lightSource.setPos(xs, ys)

        ___ item __ m_items:
            effect _ item.graphicsEffect()

            delta _ QPointF(item.x() - xs, item.y() - ys)
            effect.setOffset(QPointF(delta.toPoint() / 30))

            dd _ m__.hypot(delta.x(), delta.y())
            color _ effect.color()
            color.setAlphaF(max(0.4, min(1 - dd / 200.0, 0.7)))
            effect.sC..(color)

        m_scene.update()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    lighting _ Lighting()
    lighting.sWT..("Lighting and Shadows")
    lighting.r..(640, 480)
    lighting.s..

    ___.e.. ?.e..
