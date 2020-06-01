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


______ sys
______ math

____ ?.QtCore ______ QPointF, QRect, QRectF, Qt, QTimer
____ ?.?G.. ______ (QBrush, QColor, QFont, QLinearGradient, QPainter,
        QPen, QSurfaceFormat)
____ ?.?W.. ______ (?A.., QGridLayout, QLabel, QOpenGLWidget,
        QWidget)


c_ Helper(object):
    ___ __init__(self):
        gradient _ QLinearGradient(QPointF(50, -20), QPointF(80, 20))
        gradient.setColorAt(0.0, Qt.white)
        gradient.setColorAt(1.0, QColor(0xa6, 0xce, 0x39))

        self.background _ QBrush(QColor(64, 32, 64))
        self.circleBrush _ QBrush(gradient)
        self.circlePen _ QPen(Qt.black)
        self.circlePen.setWidth(1)
        self.textPen _ QPen(Qt.white)
        self.textFont _ QFont()
        self.textFont.setPixelSize(50)

    ___ paint  painter, event, elapsed):
        painter.fillRect(event.rect(), self.background)
        painter.translate(100, 100)

        painter.save()
        painter.setBrush(self.circleBrush)
        painter.setPen(self.circlePen)
        painter.rotate(elapsed * 0.030)

        r _ elapsed / 1000.0
        n _ 30
        for i in range(n):
            painter.rotate(30)
            radius _ 0 + 120.0*((i+r)/n)
            circleRadius _ 1 + ((i+r)/n)*20
            painter.drawEllipse(QRectF(radius, -circleRadius,
                    circleRadius*2, circleRadius*2))

        painter.restore()

        painter.setPen(self.textPen)
        painter.setFont(self.textFont)
        painter.drawText(QRect(-50, -50, 100, 100), Qt.AlignCenter, "Qt")


c_ Widget(QWidget):
    ___ __init__  helper, parent):
        super(Widget, self).__init__(parent)

        self.helper _ helper
        self.elapsed _ 0
        self.setFixedSize(200, 200)

    ___ animate(self):
        self.elapsed _ (self.elapsed + self.sender().interval()) % 1000
        self.repaint()

    ___ paintEvent  event):
        painter _ QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.helper.paint(painter, event, self.elapsed)
        painter.end()


c_ GLWidget(QOpenGLWidget):
    ___ __init__  helper, parent):
        super(GLWidget, self).__init__(parent)

        self.helper _ helper
        self.elapsed _ 0
        self.setFixedSize(200, 200)
        self.setAutoFillBackground F..

    ___ animate(self):
        self.elapsed _ (self.elapsed + self.sender().interval()) % 1000
        self.update()

    ___ paintEvent  event):
        painter _ QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.helper.paint(painter, event, self.elapsed)
        painter.end()


c_ Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("2D Painting on Native and OpenGL Widgets")

        helper _ Helper()
        native _ Widget(helper, self)
        openGL _ GLWidget(helper, self)
        nativeLabel _ QLabel("Native")
        nativeLabel.setAlignment(Qt.AlignHCenter)
        openGLLabel _ QLabel("OpenGL")
        openGLLabel.setAlignment(Qt.AlignHCenter)

        layout _ QGridLayout()
        layout.addWidget(native, 0, 0)
        layout.addWidget(openGL, 0, 1)
        layout.addWidget(nativeLabel, 1, 0)
        layout.addWidget(openGLLabel, 1, 1)
        self.setLayout(layout)

        timer _ QTimer(self)
        timer.timeout.c..(native.animate)
        timer.timeout.c..(openGL.animate)
        timer.start(50)


__ __name__ == '__main__':

    app _ ?A..(sys.argv)

    fmt _ QSurfaceFormat()
    fmt.setSamples(4)
    QSurfaceFormat.setDefaultFormat(fmt)

    window _ Window()
    window.s..
    sys.exit(app.exec_())
