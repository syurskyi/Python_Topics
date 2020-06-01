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


____ ?.?C.. ______ (pyqtSignal, QMutex, QMutexLocker, QPoint, QSize, __,
        QThread, QWaitCondition)
____ ?.?G.. ______ ?C.., QImage, QPainter, QPixmap, qRgb
____ ?.?W.. ______ ?A.., QWidget


DefaultCenterX _ -0.647011
DefaultCenterY _ -0.0395159
DefaultScale _ 0.00403897

ZoomInFactor _ 0.8
ZoomOutFactor _ 1 / ZoomInFactor
ScrollStep _ 20


c_ RenderThread(QThread):
    ColormapSize _ 512

    renderedImage _ pyqtSignal(QImage, float)

    ___ __init__  parent_None):
        super(RenderThread, self).__init__(parent)

        self.mutex _ QMutex()
        self.condition _ QWaitCondition()
        self.centerX _ 0.0
        self.centerY _ 0.0
        self.scaleFactor _ 0.0
        self.resultSize _ QSize()
        self.colormap _ []

        self.restart _ False
        self.abort _ False

        for i in range(RenderThread.ColormapSize):
            self.colormap.append(self.rgbFromWaveLength(380.0 + (i * 400.0 / RenderThread.ColormapSize)))

    ___ __del__(self):
        self.mutex.lock()
        self.abort _ True
        self.condition.wakeOne()
        self.mutex.unlock()

        self.wait()

    ___ render  centerX, centerY, scaleFactor, resultSize):
        locker _ QMutexLocker(self.mutex)

        self.centerX _ centerX
        self.centerY _ centerY
        self.scaleFactor _ scaleFactor
        self.resultSize _ resultSize

        __ no. self.isRunning
            self.start(QThread.LowPriority)
        ____
            self.restart _ True
            self.condition.wakeOne()

    ___ run(self):
        while True:
            self.mutex.lock()
            resultSize _ self.resultSize
            scaleFactor _ self.scaleFactor
            centerX _ self.centerX
            centerY _ self.centerY
            self.mutex.unlock()

            halfWidth _ resultSize.width() // 2
            halfHeight _ resultSize.height() // 2
            image _ QImage(resultSize, QImage.Format_RGB32)

            NumPasses _ 8
            curpass _ 0

            while curpass < NumPasses:
                MaxIterations _ (1 << (2 * curpass + 6)) + 32
                Limit _ 4
                allBlack _ True

                for y in range(-halfHeight, halfHeight):
                    __ self.restart:
                        break
                    __ self.abort:
                        r_

                    ay _ 1j * (centerY + (y * scaleFactor))

                    for x in range(-halfWidth, halfWidth):
                        c0 _ centerX + (x * scaleFactor) + ay
                        c _ c0
                        numIterations _ 0

                        while numIterations < MaxIterations:
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
                                           self.colormap[numIterations % RenderThread.ColormapSize])
                            allBlack _ False
                        ____
                            image.setPixel(x + halfWidth, y + halfHeight, qRgb(0, 0, 0))

                __ allBlack and curpass == 0:
                    curpass _ 4
                ____
                    __ no. self.restart:
                        self.renderedImage.emit(image, scaleFactor)
                    curpass +_ 1

            self.mutex.lock()
            __ no. self.restart:
                self.condition.wait(self.mutex)
            self.restart _ False
            self.mutex.unlock()

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


c_ MandelbrotWidget(QWidget):
    ___ __init__  parent_None):
        super(MandelbrotWidget, self).__init__(parent)

        self.thread _ RenderThread()
        self.pixmap _ QPixmap()
        self.pixmapOffset _ QPoint()
        self.lastDragPos _ QPoint()

        self.centerX _ DefaultCenterX
        self.centerY _ DefaultCenterY
        self.pixmapScale _ DefaultScale
        self.curScale _ DefaultScale

        self.thread.renderedImage.c..(self.updatePixmap)

        self.setWindowTitle("Mandelbrot")
        self.setCursor(__.CrossCursor)
        self.resize(550, 400)

    ___ paintEvent  event):
        painter _ QPainter(self)
        painter.fillRect(self.rect(), __.black)

        __ self.pixmap.isNull
            painter.setPen(__.white)
            painter.drawText(self.rect(), __.AlignCenter,
                    "Rendering initial image, please wait...")
            r_

        __ self.curScale == self.pixmapScale:
            painter.drawPixmap(self.pixmapOffset, self.pixmap)
        ____
            scaleFactor _ self.pixmapScale / self.curScale
            newWidth _ int(self.pixmap.width() * scaleFactor)
            newHeight _ int(self.pixmap.height() * scaleFactor)
            newX _ self.pixmapOffset.x() + (self.pixmap.width() - newWidth) / 2
            newY _ self.pixmapOffset.y() + (self.pixmap.height() - newHeight) / 2

            painter.save()
            painter.translate(newX, newY)
            painter.scale(scaleFactor, scaleFactor)
            exposed, _ _ painter.matrix().inverted()
            exposed _ exposed.mapRect(self.rect()).adjusted(-1, -1, 1, 1)
            painter.drawPixmap(exposed, self.pixmap, exposed)
            painter.restore()

        t__ _ "Use mouse wheel or the '+' and '-' keys to zoom. Press and " \
                "hold left mouse button to scroll."
        metrics _ painter.fontMetrics()
        textWidth _ metrics.width(t__)

        painter.setPen(__.NoPen)
        painter.setBrush(?C..(0, 0, 0, 127))
        painter.drawRect((self.width() - textWidth) / 2 - 5, 0, textWidth + 10,
                metrics.lineSpacing() + 5)
        painter.setPen(__.white)
        painter.drawText((self.width() - textWidth) / 2,
                metrics.leading() + metrics.ascent(), t__)

    ___ resizeEvent  event):
        self.thread.render(self.centerX, self.centerY, self.curScale,
                self.size())

    ___ keyPressEvent  event):
        __ event.key() == __.Key_Plus:
            self.zoom(ZoomInFactor)
        ____ event.key() == __.Key_Minus:
            self.zoom(ZoomOutFactor)
        ____ event.key() == __.Key_Left:
            self.scroll(-ScrollStep, 0)
        ____ event.key() == __.Key_Right:
            self.scroll(+ScrollStep, 0)
        ____ event.key() == __.Key_Down:
            self.scroll(0, -ScrollStep)
        ____ event.key() == __.Key_Up:
            self.scroll(0, +ScrollStep)
        ____
            super(MandelbrotWidget, self).keyPressEvent(event)

    ___ wheelEvent  event):
        numDegrees _ event.angleDelta().y() / 8
        numSteps _ numDegrees / 15.0
        self.zoom(pow(ZoomInFactor, numSteps))

    ___ mousePressEvent  event):
        __ event.buttons() == __.LeftButton:
            self.lastDragPos _ QPoint(event.pos())

    ___ mouseMoveEvent  event):
        __ event.buttons() & __.LeftButton:
            self.pixmapOffset +_ event.pos() - self.lastDragPos
            self.lastDragPos _ QPoint(event.pos())
            self.update()

    ___ mouseReleaseEvent  event):
        __ event.button() == __.LeftButton:
            self.pixmapOffset +_ event.pos() - self.lastDragPos
            self.lastDragPos _ QPoint()

            deltaX _ (self.width() - self.pixmap.width()) / 2 - self.pixmapOffset.x()
            deltaY _ (self.height() - self.pixmap.height()) / 2 - self.pixmapOffset.y()
            self.scroll(deltaX, deltaY)

    ___ updatePixmap  image, scaleFactor):
        __ no. self.lastDragPos.isNull
            r_

        self.pixmap _ QPixmap.fromImage(image)
        self.pixmapOffset _ QPoint()
        self.lastDragPosition _ QPoint()
        self.pixmapScale _ scaleFactor
        self.update()

    ___ zoom  zoomFactor):
        self.curScale *_ zoomFactor
        self.update()
        self.thread.render(self.centerX, self.centerY, self.curScale,
                self.size())

    ___ scroll  deltaX, deltaY):
        self.centerX +_ deltaX * self.curScale
        self.centerY +_ deltaY * self.curScale
        self.update()
        self.thread.render(self.centerX, self.centerY, self.curScale,
                self.size())


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    widget _ MandelbrotWidget()
    widget.s..
    sys.exit(app.exec_())
