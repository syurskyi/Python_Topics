#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2018 Riverbank Computing Limited.
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


____ ?.?C.. ______ pP.., pS.., pyqtSlot, QRectF, __, ?U..
____ ?.?G.. ______ ?C.., QGuiApplication, QPainter, ?P..
____ ?.QtQml ______ qmlRegisterType
____ ?.QtQuick ______ QQuickPaintedItem, QQuickView


c_ PieChart(QQuickPaintedItem):

    @pP.. st.
    ___ name
        r_ _name

    @name.setter
    ___ name  name):
        _name _ name

    colorChanged _ pS..()

    @pP..(?C.., notify_colorChanged)
    ___ color
        r_ _color

    @color.setter
    ___ color  color):
        __ _color !_ color:
            _color _ ?C..(color)
            update()
            colorChanged.e..()

    ___  -   parent_None):
        s__(PieChart, self). - (parent)

        _name _ ''
        _color _ ?C..()

    ___ paint  painter):
        painter.sP..(?P..(_color, 2))
        painter.setRenderHints(QPainter.Antialiasing,  st.

        rect _ QRectF(0, 0, width(), height()).adjusted(1, 1, -1, -1)
        painter.drawPie(rect, 90 * 16, 290 * 16)

    @pyqtSlot()
    ___ clearChart
        color _ ?C..(__.transparent)
        update()


__ ______ __ ______
    ______ __
    ______ ___

    app _ QGuiApplication(___.a..

    qmlRegisterType(PieChart, "Charts", 1, 0, "PieChart")

    view _ QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(
            ?U...fLF..(
                    __.p__ .join(__.p__ .dirname(__.p__ .abspath(__file__)),
                            'app.qml')))
    view.s..

    ___.e.. ?.e..
