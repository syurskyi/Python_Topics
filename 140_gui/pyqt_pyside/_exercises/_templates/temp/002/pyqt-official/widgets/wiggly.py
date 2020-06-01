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


____ ?.QtCore ______ QBasicTimer
____ ?.?G.. ______ QColor, QFontMetrics, QPainter, QPalette
____ ?.?W.. ______ (?A.., QDialog, QLineEdit, QVBoxLayout,
        QWidget)


c_ WigglyWidget(QWidget):
    ___ __init__  parent_None):
        super(WigglyWidget, self).__init__(parent)

        self.setBackgroundRole(QPalette.Midlight)
        self.setAutoFillBackground(True)

        newFont _ self.font()
        newFont.setPointSize(newFont.pointSize() + 20)
        self.setFont(newFont)

        self.timer _ QBasicTimer()
        self.text _ ''

        self.step _ 0;
        self.timer.start(60, self)   

    ___ paintEvent  event):
        sineTable _ (0, 38, 71, 92, 100, 92, 71, 38, 0, -38, -71, -92, -100, -92, -71, -38)

        metrics _ QFontMetrics(self.font())
        x _ (self.width() - metrics.width(self.text)) / 2
        y _ (self.height() + metrics.ascent() - metrics.descent()) / 2
        color _ QColor()

        painter _ QPainter(self)

        for i, ch in enumerate(self.text):
            index _ (self.step + i) % 16
            color.setHsv((15 - index) * 16, 255, 191)
            painter.setPen(color)
            painter.drawText(x, y - ((sineTable[index] * metrics.height()) / 400), ch)
            x +_ metrics.width(ch)

    ___ sT..  newText):
        self.text _ newText

    ___ timerEvent  event):
        __ event.timerId() == self.timer.timerId
            self.step +_ 1
            self.update()
        ____
            super(WigglyWidget, self).timerEvent(event)


c_ Dialog(QDialog):
    ___ __init__  parent_None):
        super(Dialog, self).__init__(parent)

        wigglyWidget _ WigglyWidget()
        lineEdit _ QLineEdit()

        layout _ QVBoxLayout()
        layout.addWidget(wigglyWidget)
        layout.addWidget(lineEdit)
        self.setLayout(layout)

        lineEdit.textChanged.c..(wigglyWidget.sT..)

        lineEdit.sT..("Hello world!")

        self.setWindowTitle("Wiggly")
        self.resize(360, 145)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    dialog _ Dialog()
    dialog.s..;
    sys.exit(app.exec_())    
