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


____ ?.?C.. ______ (pS.., QMutex, ?ML.., QPoint, ?S.., __,
        ?T.., QWaitCondition)
____ ?.?G.. ______ ?C.., QImage, QPainter, ?P.., qRgb
____ ?.?W.. ______ ?A.., ?W..


DefaultCenterX _ -0.647011
DefaultCenterY _ -0.0395159
DefaultScale _ 0.00403897

ZoomInFactor _ 0.8
ZoomOutFactor _ 1 / ZoomInFactor
ScrollStep _ 20


c_ RenderThread(?T..):
    ColormapSize _ 512

    renderedImage _ pS..(QImage, fl..)

    ___  -   parent_None):
        s__(RenderThread, self). - (parent)

        mutex _ QMutex()
        condition _ QWaitCondition()
        centerX _ 0.0
        centerY _ 0.0
        scaleFactor _ 0.0
        resultSize _ ?S..()
        colormap _   # list

        restart _ F..
        abort _ F..

        ___ i __ ra..(RenderThread.ColormapSize):
            colormap.ap..(rgbFromWaveLength(380.0 + (i * 400.0 / RenderThread.ColormapSize)))

    ___ __del__ 
        mutex.lock()
        abort _ T..
        condition.wakeOne()
        mutex.unlock()

        wait()

    ___ render  centerX, centerY, scaleFactor, resultSize):
        locker _ ?ML..(mutex)

        centerX _ centerX
        centerY _ centerY
        scaleFactor _ scaleFactor
        resultSize _ resultSize

        __ no. isRunning
            start(?T...LowPriority)
        ____
            restart _ T..
            condition.wakeOne()

    ___ run 
        w__ T..
            mutex.lock()
            resultSize _ resultSize
            scaleFactor _ scaleFactor
            centerX _ centerX
            centerY _ centerY
            mutex.unlock()

            halfWidth _ resultSize.width() // 2
            halfHeight _ resultSize.height() // 2
            image _ QImage(resultSize, QImage.Format_RGB32)

            NumPasses _ 8
            curpass _ 0

            w__ curpass < NumPasses:
                MaxIterations _ (1 << (2 * curpass + 6)) + 32
                Limit _ 4
                allBlack _ T..

                ___ y __ ra..(-halfHeight, halfHeight):
                    __ restart:
                        break
                    __ abort:
                        r_

                    ay _ 1j * (centerY + (y * scaleFactor))

                    ___ x __ ra..(-halfWidth, halfWidth):
                        c0 _ centerX + (x * scaleFactor) + ay
                        c _ c0
                        numIterations _ 0

                        w__ numIterations < MaxIterations:
                            numIterations +_ 1
                            c _ c*c + c0
                            __ abs(c) >_ Limit:
                                break
                            numIterations +_ 1
                            c _ c*c + c0
                            __ abs(c) >_ Limit:
                                break
                            numIterations +_ 1
                            c _ c*c + c0
                            __ abs(c) >_ Limit:
                                break
                            numIterations +_ 1
                            c _ c*c + c0
                            __ abs(c) >_ Limit:
                                break

                        __ numIterations < MaxIterations:
                            image.setPixel(x + halfWidth, y + halfHeight,
                                           colormap[numIterations % RenderThread.ColormapSize])
                            allBlack _ F..
                        ____
                            image.setPixel(x + halfWidth, y + halfHeight, qRgb(0, 0, 0))

                __ allBlack and curpass __ 0:
                    curpass _ 4
                ____
                    __ no. restart:
                        renderedImage.e..(image, scaleFactor)
                    curpass +_ 1

            mutex.lock()
            __ no. restart:
                condition.wait(mutex)
            restart _ F..
            mutex.unlock()

    ___ rgbFromWaveLength  wave):
        r _ 0.0
        g _ 0.0
        b _ 0.0

        __ wave >_ 380.0 and wave <_ 440.0:
            r _ -1.0 * (wave - 440.0) / (440.0 - 380.0)
            b _ 1.0
        ____ wave >_ 440.0 and wave <_ 490.0:
            g _ (wave - 440.0) / (490.0 - 440.0)
            b _ 1.0
        ____ wave >_ 490.0 and wave <_ 510.0:
            g _ 1.0
            b _ -1.0 * (wave - 510.0) / (510.0 - 490.0)
        ____ wave >_ 510.0 and wave <_ 580.0:
            r _ (wave - 510.0) / (580.0 - 510.0)
            g _ 1.0
        ____ wave >_ 580.0 and wave <_ 645.0:
            r _ 1.0
            g _ -1.0 * (wave - 645.0) / (645.0 - 580.0)
        ____ wave >_ 645.0 and wave <_ 780.0:
            r _ 1.0

        s _ 1.0
        __ wave > 700.0:
            s _ 0.3 + 0.7 * (780.0 - wave) / (780.0 - 700.0)
        ____ wave < 420.0:
            s _ 0.3 + 0.7 * (wave - 380.0) / (420.0 - 380.0)

        r _ pow(r * s, 0.8)
        g _ pow(g * s, 0.8)
        b _ pow(b * s, 0.8)

        r_ qRgb(r*255, g*255, b*255)


c_ MandelbrotWidget(?W..):
    ___  -   parent_None):
        s__(MandelbrotWidget, self). - (parent)

        thread _ RenderThread()
        pixmap _ ?P..()
        pixmapOffset _ QPoint()
        lastDragPos _ QPoint()

        centerX _ DefaultCenterX
        centerY _ DefaultCenterY
        pixmapScale _ DefaultScale
        curScale _ DefaultScale

        thread.renderedImage.c..(updatePixmap)

        sWT..("Mandelbrot")
        setCursor(__.CrossCursor)
        r..(550, 400)

    ___ paintEvent  event):
        painter _ QPainter
        painter.fillRect(rect(), __.black)

        __ pixmap.isNull
            painter.sP..(__.white)
            painter.drawText(rect(), __.AlignCenter,
                    "Rendering initial image, please wait...")
            r_

        __ curScale __ pixmapScale:
            painter.drawPixmap(pixmapOffset, pixmap)
        ____
            scaleFactor _ pixmapScale / curScale
            newWidth _ in.(pixmap.width() * scaleFactor)
            newHeight _ in.(pixmap.height() * scaleFactor)
            newX _ pixmapOffset.x() + (pixmap.width() - newWidth) / 2
            newY _ pixmapOffset.y() + (pixmap.height() - newHeight) / 2

            painter.save()
            painter.translate(newX, newY)
            painter.scale(scaleFactor, scaleFactor)
            exposed, _ _ painter.matrix().inverted()
            exposed _ exposed.mapRect(rect()).adjusted(-1, -1, 1, 1)
            painter.drawPixmap(exposed, pixmap, exposed)
            painter.restore()

        t__ _ "Use mouse wheel or the '+' and '-' keys to zoom. Press and " \
                "hold left mouse button to scroll."
        metrics _ painter.fontMetrics()
        textWidth _ metrics.width(t__)

        painter.sP..(__.NoPen)
        painter.sB..(?C..(0, 0, 0, 127))
        painter.drawRect((width() - textWidth) / 2 - 5, 0, textWidth + 10,
                metrics.lineSpacing() + 5)
        painter.sP..(__.white)
        painter.drawText((width() - textWidth) / 2,
                metrics.leading() + metrics.ascent(), t__)

    ___ resizeEvent  event):
        thread.render(centerX, centerY, curScale,
                size())

    ___ keyPressEvent  event):
        __ event.key() __ __.Key_Plus:
            zoom(ZoomInFactor)
        ____ event.key() __ __.Key_Minus:
            zoom(ZoomOutFactor)
        ____ event.key() __ __.Key_Left:
            scroll(-ScrollStep, 0)
        ____ event.key() __ __.Key_Right:
            scroll(+ScrollStep, 0)
        ____ event.key() __ __.Key_Down:
            scroll(0, -ScrollStep)
        ____ event.key() __ __.Key_Up:
            scroll(0, +ScrollStep)
        ____
            s__(MandelbrotWidget, self).keyPressEvent(event)

    ___ wheelEvent  event):
        numDegrees _ event.angleDelta().y() / 8
        numSteps _ numDegrees / 15.0
        zoom(pow(ZoomInFactor, numSteps))

    ___ mousePressEvent  event):
        __ event.buttons() __ __.LeftButton:
            lastDragPos _ QPoint(event.pos())

    ___ mouseMoveEvent  event):
        __ event.buttons() & __.LeftButton:
            pixmapOffset +_ event.pos() - lastDragPos
            lastDragPos _ QPoint(event.pos())
            update()

    ___ mouseReleaseEvent  event):
        __ event.button() __ __.LeftButton:
            pixmapOffset +_ event.pos() - lastDragPos
            lastDragPos _ QPoint()

            deltaX _ (width() - pixmap.width()) / 2 - pixmapOffset.x()
            deltaY _ (height() - pixmap.height()) / 2 - pixmapOffset.y()
            scroll(deltaX, deltaY)

    ___ updatePixmap  image, scaleFactor):
        __ no. lastDragPos.isNull
            r_

        pixmap _ ?P...fromImage(image)
        pixmapOffset _ QPoint()
        lastDragPosition _ QPoint()
        pixmapScale _ scaleFactor
        update()

    ___ zoom  zoomFactor):
        curScale *_ zoomFactor
        update()
        thread.render(centerX, centerY, curScale,
                size())

    ___ scroll  deltaX, deltaY):
        centerX +_ deltaX * curScale
        centerY +_ deltaY * curScale
        update()
        thread.render(centerX, centerY, curScale,
                size())


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    widget _ MandelbrotWidget()
    widget.s..
    ___.e.. ?.e..
