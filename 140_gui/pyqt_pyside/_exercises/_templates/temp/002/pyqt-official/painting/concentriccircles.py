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


____ ?.?C.. ______ QRect, QRectF, QSize, __, QTimer
____ ?.?G.. ______ ?C.., QPainter, ?P.., QPen
____ ?.?W.. ______ (?A.., QFrame, QGridLayout, QLabel,
        QSizePolicy, QWidget)


c_ CircleWidget(QWidget):
    ___ __init__  parent_None):
        super(CircleWidget, self).__init__(parent)

        self.floatBased _ False
        self.antialiased _ False
        self.frameNo _ 0

        self.setBackgroundRole(?P...Base)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    ___ setFloatBased  floatBased):
        self.floatBased _ floatBased
        self.update()

    ___ setAntialiased  antialiased):
        self.antialiased _ antialiased
        self.update()

    ___ minimumSizeHint(self):
        r_ QSize(50, 50)

    ___ sizeHint(self):
        r_ QSize(180, 180)

    ___ nextAnimationFrame(self):
        self.frameNo +_ 1
        self.update()

    ___ paintEvent  event):
        painter _ QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, self.antialiased)
        painter.translate(self.width() / 2, self.height() / 2)

        for diameter in range(0, 256, 9):
            delta _ abs((self.frameNo % 128) - diameter / 2)
            alpha _ 255 - (delta * delta) / 4 - diameter
            __ alpha > 0:
                painter.setPen(QPen(?C..(0, diameter / 2, 127, alpha), 3))

                __ self.floatBased:
                    painter.drawEllipse(QRectF(-diameter / 2.0,
                            -diameter / 2.0, diameter, diameter))
                ____
                    painter.drawEllipse(QRect(-diameter / 2,
                            -diameter / 2, diameter, diameter))


c_ Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        aliasedLabel _ self.createLabel("Aliased")
        antialiasedLabel _ self.createLabel("Antialiased")
        intLabel _ self.createLabel("Int")
        floatLabel _ self.createLabel("Float")

        layout _ QGridLayout()
        layout.aW..(aliasedLabel, 0, 1)
        layout.aW..(antialiasedLabel, 0, 2)
        layout.aW..(intLabel, 1, 0)
        layout.aW..(floatLabel, 2, 0)

        timer _ QTimer(self)

        for i in range(2):
            for j in range(2):
                w _ CircleWidget()
                w.setAntialiased(j !_ 0)
                w.setFloatBased(i !_ 0)

                timer.timeout.c..(w.nextAnimationFrame)

                layout.aW..(w, i + 1, j + 1)

        timer.start(100)
        self.sL..(layout)

        self.setWindowTitle("Concentric Circles")

    ___ createLabel  t__):
        label _ QLabel(t__)
        label.setAlignment(__.AlignCenter)
        label.setMargin(2)
        label.setFrameStyle(QFrame.Box | QFrame.Sunken)
        r_ label


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    window _ Window()
    window.s..
    ___.exit(app.exec_())
