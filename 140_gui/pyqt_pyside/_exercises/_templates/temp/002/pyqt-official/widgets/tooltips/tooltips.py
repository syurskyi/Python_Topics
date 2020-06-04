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


______ random

____ ?.?C.. ______ QEvent, QPoint, QPointF, ?S.., __
____ ?.?G.. ______ ?C.., ?I.., QPainter, QPainterPath, ?P..
____ ?.?W.. ______ (?A.., ?S.., QToolButton, QToolTip,
        ?W..)

______ tooltips_rc


c_ ShapeItem o..
    ___  -
        myPath _ QPainterPath()
        myPosition _ QPoint()
        myColor  _ ?C..()
        myToolTip _ ''

    ___ pa__
        r_ myPath

    ___ position 
        r_ myPosition

    ___ color 
        r_ myColor

    ___ toolTip 
        r_ myToolTip

    ___ setPath  pa__):
        myPath _ pa__

    ___ sTT..  toolTip):
        myToolTip _ toolTip

    ___ setPosition  position):
        myPosition _ position

    ___ sC..  color):
        myColor _ color


c_ SortingBox(?W..):
    circle_count _ square_count _ triangle_count _ 1

    ___  -
        s__(SortingBox, self). - ()

        circlePath _ QPainterPath()
        squarePath _ QPainterPath()
        trianglePath _ QPainterPath()
        shapeItems _   # list

        previousPosition _ QPoint()

        setMouseTracking( st.
        setBackgroundRole(?P...Base)

        itemInMotion _ N..

        newCircleButton _ createToolButton("New Circle",
                ?I..(':/images/circle.png'), createNewCircle)
        newSquareButton _ createToolButton("New Square",
                ?I..(':/images/square.png'), createNewSquare)
        newTriangleButton _ createToolButton("New Triangle",
                ?I..(':/images/triangle.png'), createNewTriangle)

        circlePath.addEllipse(0, 0, 100, 100)
        squarePath.addRect(0, 0, 100, 100)

        x _ trianglePath.currentPosition().x()
        y _ trianglePath.currentPosition().y()
        trianglePath.moveTo(x + 120 / 2, y)
        trianglePath.lineTo(0, 100)
        trianglePath.lineTo(120, 100)
        trianglePath.lineTo(x + 120 / 2, y)

        sWT..("Tooltips")
        r..(500, 300)

        createShapeItem(circlePath, "Circle",
                initialItemPosition(circlePath),
                initialItemColor())
        createShapeItem(squarePath, "Square",
                initialItemPosition(squarePath),
                initialItemColor())
        createShapeItem(trianglePath, "Triangle",
                initialItemPosition(trianglePath),
                initialItemColor())

    ___ event  event):
        __ event.type() __ QEvent.ToolTip:
            helpEvent _ event
            index _ itemAt(helpEvent.pos())
            __ index !_ -1:
                QToolTip.showText(helpEvent.globalPos(),
                        shapeItems[index].toolTip())
            ____
                QToolTip.hideText()
                event.ignore()

            r_ T..

        r_ s__(SortingBox, self).event(event)

    ___ resizeEvent  event):
        margin _ style().pixelMetric(?S...PM_DefaultTopLevelMargin)
        x _ width() - margin
        y _ height() - margin

        y _ updateButtonGeometry(newCircleButton, x, y)
        y _ updateButtonGeometry(newSquareButton, x, y)
        updateButtonGeometry(newTriangleButton, x, y)

    ___ paintEvent  event):
        painter _ QPainter
        painter.setRenderHint(QPainter.Antialiasing)
        ___ shapeItem __ shapeItems:
            painter.translate(shapeItem.position())
            painter.sB..(shapeItem.color())
            painter.drawPath(shapeItem.pa__())
            painter.translate(-shapeItem.position())

    ___ mousePressEvent  event):
        __ event.button() __ __.LeftButton:
            index _ itemAt(event.pos())
            __ index !_ -1:
                itemInMotion _ shapeItems[index]
                previousPosition _ event.pos()

                value _ shapeItems[index]
                del shapeItems[index]
                shapeItems.insert(le.(shapeItems) - 1, value)

                update()

    ___ mouseMoveEvent  event):
        __ (event.buttons() & __.LeftButton) and itemInMotion:
            moveItemTo(event.pos())

    ___ mouseReleaseEvent  event):
        __ (event.button() __ __.LeftButton) and itemInMotion:
            moveItemTo(event.pos())
            itemInMotion _ N..

    ___ createNewCircle 
        SortingBox.circle_count +_ 1
        createShapeItem(circlePath,
                "Circle <%d>" % SortingBox.circle_count,
                randomItemPosition(), randomItemColor())

    ___ createNewSquare 
        SortingBox.square_count +_ 1
        createShapeItem(squarePath,
                "Square <%d>" % SortingBox.square_count,
                randomItemPosition(), randomItemColor())

    ___ createNewTriangle 
        SortingBox.triangle_count +_ 1
        createShapeItem(trianglePath,
                "Triangle <%d>" % SortingBox.triangle_count,
                randomItemPosition(), randomItemColor())

    ___ itemAt  pos):
        ___ i __ ra..(le.(shapeItems) - 1, -1, -1):
            item _ shapeItems[i]
            __ item.pa__().contains(QPointF(pos - item.position())):
                r_ i

        r_ -1

    ___ moveItemTo  pos):
        offset _ pos - previousPosition
        itemInMotion.setPosition(itemInMotion.position() + offset)
        previousPosition _ QPoint(pos)
        update()

    ___ updateButtonGeometry  button, x, y):
        size _ button.sH..()
        button.setGeometry(x - size.width(), y - size.height(),
                size.width(), size.height())

        r_ y - size.height() - style().pixelMetric(?S...PM_DefaultLayoutSpacing)

    ___ createShapeItem  pa__, toolTip, pos, color):
        shapeItem _ ShapeItem()
        shapeItem.setPath(pa__)
        shapeItem.sTT..(toolTip)
        shapeItem.setPosition(pos)
        shapeItem.sC..(color)
        shapeItems.ap..(shapeItem)
        update()

    ___ createToolButton  toolTip, icon, member):
        button _ QToolButton
        button.sTT..(toolTip)
        button.sI..(icon)
        button.setIconSize(?S..(32, 32))
        button.c__.c..(member)

        r_ button

    ___ initialItemPosition  pa__):
        y _ (height() - pa__.controlPointRect().height()) / 2

        __ le.(shapeItems) __ 0:
            x _ ((3 * width()) / 2 - pa__.controlPointRect().width()) / 2
        ____
            x _ (width() / le.(shapeItems) - pa__.controlPointRect().width()) / 2

        r_ QPoint(x, y)

    ___ randomItemPosition 
        x _ random.randint(0, width() - 120)
        y _ random.randint(0, height() - 120)

        r_ QPoint(x, y)

    ___ initialItemColor 
        hue _ ((le.(shapeItems) + 1) * 85) % 256
        r_ ?C...fromHsv(hue, 255, 190)

    ___ randomItemColor 
        r_ ?C...fromHsv(random.randint(0, 256), 255, 190)


__ __name__ __ "__main__":

    ______ ___

    app _ ?A..(___.a..
    sortingBox _ SortingBox()
    sortingBox.s..
    ___.e.. ?.e..
