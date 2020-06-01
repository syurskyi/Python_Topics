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

____ ?.?C.. ______ QEvent, QPoint, QPointF, QSize, __
____ ?.?G.. ______ ?C.., QIcon, QPainter, QPainterPath, ?P..
____ ?.?W.. ______ (?A.., QStyle, QToolButton, QToolTip,
        QWidget)

______ tooltips_rc


c_ ShapeItem(object):
    ___ __init__(self):    
        self.myPath _ QPainterPath()
        self.myPosition _ QPoint()
        self.myColor  _ ?C..()
        self.myToolTip _ ''

    ___ path(self):
        r_ self.myPath

    ___ position(self):
        r_ self.myPosition

    ___ color(self):
        r_ self.myColor

    ___ toolTip(self):
        r_ self.myToolTip

    ___ setPath  path):
        self.myPath _ path

    ___ setToolTip  toolTip):
        self.myToolTip _ toolTip

    ___ setPosition  position):
        self.myPosition _ position

    ___ sC..  color):
        self.myColor _ color


c_ SortingBox(QWidget):
    circle_count _ square_count _ triangle_count _ 1

    ___ __init__(self):
        super(SortingBox, self).__init__()

        self.circlePath _ QPainterPath()
        self.squarePath _ QPainterPath()
        self.trianglePath _ QPainterPath()
        self.shapeItems _ []

        self.previousPosition _ QPoint()

        self.setMouseTracking(True)
        self.setBackgroundRole(?P...Base)

        self.itemInMotion _ N..

        self.newCircleButton _ self.createToolButton("New Circle",
                QIcon(':/images/circle.png'), self.createNewCircle)
        self.newSquareButton _ self.createToolButton("New Square",
                QIcon(':/images/square.png'), self.createNewSquare)
        self.newTriangleButton _ self.createToolButton("New Triangle",
                QIcon(':/images/triangle.png'), self.createNewTriangle)

        self.circlePath.addEllipse(0, 0, 100, 100)
        self.squarePath.addRect(0, 0, 100, 100)

        x _ self.trianglePath.currentPosition().x()
        y _ self.trianglePath.currentPosition().y()
        self.trianglePath.moveTo(x + 120 / 2, y)
        self.trianglePath.lineTo(0, 100)
        self.trianglePath.lineTo(120, 100)
        self.trianglePath.lineTo(x + 120 / 2, y)

        self.setWindowTitle("Tooltips")
        self.resize(500, 300)

        self.createShapeItem(self.circlePath, "Circle",
                self.initialItemPosition(self.circlePath),
                self.initialItemColor())
        self.createShapeItem(self.squarePath, "Square",
                self.initialItemPosition(self.squarePath),
                self.initialItemColor())
        self.createShapeItem(self.trianglePath, "Triangle",
                self.initialItemPosition(self.trianglePath),
                self.initialItemColor())

    ___ event  event):
        __ event.type() == QEvent.ToolTip:
            helpEvent _ event
            index _ self.itemAt(helpEvent.pos())
            __ index !_ -1:
                QToolTip.showText(helpEvent.globalPos(),
                        self.shapeItems[index].toolTip())
            ____
                QToolTip.hideText()
                event.ignore()

            r_ True

        r_ super(SortingBox, self).event(event)

    ___ resizeEvent  event):
        margin _ self.style().pixelMetric(QStyle.PM_DefaultTopLevelMargin)
        x _ self.width() - margin
        y _ self.height() - margin

        y _ self.updateButtonGeometry(self.newCircleButton, x, y)
        y _ self.updateButtonGeometry(self.newSquareButton, x, y)
        self.updateButtonGeometry(self.newTriangleButton, x, y)

    ___ paintEvent  event):
        painter _ QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for shapeItem in self.shapeItems:
            painter.translate(shapeItem.position())
            painter.setBrush(shapeItem.color())
            painter.drawPath(shapeItem.path())
            painter.translate(-shapeItem.position())

    ___ mousePressEvent  event):
        __ event.button() == __.LeftButton:
            index _ self.itemAt(event.pos())
            __ index !_ -1:
                self.itemInMotion _ self.shapeItems[index]
                self.previousPosition _ event.pos()

                value _ self.shapeItems[index]
                del self.shapeItems[index]
                self.shapeItems.insert(len(self.shapeItems) - 1, value)

                self.update()

    ___ mouseMoveEvent  event):
        __ (event.buttons() & __.LeftButton) and self.itemInMotion:
            self.moveItemTo(event.pos())

    ___ mouseReleaseEvent  event):
        __ (event.button() == __.LeftButton) and self.itemInMotion:
            self.moveItemTo(event.pos())
            self.itemInMotion _ N..

    ___ createNewCircle(self):
        SortingBox.circle_count +_ 1
        self.createShapeItem(self.circlePath,
                "Circle <%d>" % SortingBox.circle_count,
                self.randomItemPosition(), self.randomItemColor())

    ___ createNewSquare(self):
        SortingBox.square_count +_ 1
        self.createShapeItem(self.squarePath,
                "Square <%d>" % SortingBox.square_count,
                self.randomItemPosition(), self.randomItemColor())

    ___ createNewTriangle(self):
        SortingBox.triangle_count +_ 1
        self.createShapeItem(self.trianglePath,
                "Triangle <%d>" % SortingBox.triangle_count,
                self.randomItemPosition(), self.randomItemColor())

    ___ itemAt  pos):
        for i in range(len(self.shapeItems) - 1, -1, -1):
            item _ self.shapeItems[i]
            __ item.path().contains(QPointF(pos - item.position())):
                r_ i

        r_ -1

    ___ moveItemTo  pos):
        offset _ pos - self.previousPosition
        self.itemInMotion.setPosition(self.itemInMotion.position() + offset)
        self.previousPosition _ QPoint(pos)
        self.update()

    ___ updateButtonGeometry  button, x, y):
        size _ button.sizeHint()
        button.setGeometry(x - size.width(), y - size.height(),
                size.width(), size.height())

        r_ y - size.height() - self.style().pixelMetric(QStyle.PM_DefaultLayoutSpacing)

    ___ createShapeItem  path, toolTip, pos, color):
        shapeItem _ ShapeItem()
        shapeItem.setPath(path)
        shapeItem.setToolTip(toolTip)
        shapeItem.setPosition(pos)
        shapeItem.sC..(color)
        self.shapeItems.append(shapeItem)
        self.update()

    ___ createToolButton  toolTip, icon, member):
        button _ QToolButton(self)
        button.setToolTip(toolTip)
        button.setIcon(icon)
        button.setIconSize(QSize(32, 32))
        button.c__.c..(member)

        r_ button

    ___ initialItemPosition  path):
        y _ (self.height() - path.controlPointRect().height()) / 2

        __ len(self.shapeItems) == 0:
            x _ ((3 * self.width()) / 2 - path.controlPointRect().width()) / 2
        ____
            x _ (self.width() / len(self.shapeItems) - path.controlPointRect().width()) / 2

        r_ QPoint(x, y)

    ___ randomItemPosition(self):
        x _ random.randint(0, self.width() - 120)
        y _ random.randint(0, self.height() - 120)

        r_ QPoint(x, y)

    ___ initialItemColor(self):
        hue _ ((len(self.shapeItems) + 1) * 85) % 256
        r_ ?C...fromHsv(hue, 255, 190)

    ___ randomItemColor(self):
        r_ ?C...fromHsv(random.randint(0, 256), 255, 190)


__ __name__ == "__main__":

    ______ sys

    app _ ?A..(sys.argv)
    sortingBox _ SortingBox()
    sortingBox.s..
    sys.exit(app.exec_())
