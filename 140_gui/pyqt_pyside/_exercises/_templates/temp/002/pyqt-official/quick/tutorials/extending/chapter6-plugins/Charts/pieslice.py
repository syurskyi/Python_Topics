#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
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
##   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
##     of its contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
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


____ ?.QtCore ______ pyqtProperty, QRectF
____ ?.?G.. ______ QColor, QPainter, QPen
____ ?.QtQuick ______ QQuickPaintedItem


c_ PieSlice(QQuickPaintedItem):

    @pyqtProperty(QColor)
    ___ color(self):
        r_ self._color

    @color.setter
    ___ color  color):
        self._color _ QColor(color)

    @pyqtProperty(int)
    ___ fromAngle(self):
        r_ self._fromAngle

    @fromAngle.setter
    ___ fromAngle  fromAngle):
        self._fromAngle _ fromAngle

    @pyqtProperty(int)
    ___ angleSpan(self):
        r_ self._angleSpan

    @angleSpan.setter
    ___ angleSpan  angleSpan):
        self._angleSpan _ angleSpan

    ___ __init__  parent_None):
        super(PieSlice, self).__init__(parent)

        self._color _ QColor()
        self._fromAngle _ 0
        self._angleSpan _ 0

    ___ paint  painter):
        painter.setPen(QPen(self._color, 2))
        painter.setRenderHints(QPainter.Antialiasing, True)

        rect _ QRectF(0, 0, self.width(), self.height()).adjusted(1, 1, -1, -1)
        painter.drawPie(rect, self._fromAngle * 16, self._angleSpan * 16)
