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


____ ?.?C.. ______ QPointF, QSize, __
____ ?.?G.. ______ QBrush, QFont, QFontMetrics, QPainter, QPainterPath
____ ?.?W.. ______ ?A.., QComboBox, QGridLayout, QWidget


NoTransformation, Translate, Rotate, Scale _ range(4)

c_ RenderArea(QWidget):
    ___ __init__  parent_None):
        super(RenderArea, self).__init__(parent)

        newFont _ self.font()
        newFont.setPixelSize(12)
        self.setFont(newFont)

        fontMetrics _ QFontMetrics(newFont)
        self.xBoundingRect _ fontMetrics.boundingRect("x")
        self.yBoundingRect _ fontMetrics.boundingRect("y")
        self.shape _ QPainterPath()
        self.operations _ []

    ___ setOperations  operations):
        self.operations _ operations
        self.update()

    ___ setShape  shape):
        self.shape _ shape
        self.update()

    ___ minimumSizeHint(self):
        r_ QSize(182, 182)

    ___ sizeHint(self):
        r_ QSize(232, 232)

    ___ paintEvent  event):
        painter _ QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(__.white))

        painter.translate(66, 66)

        painter.save()
        self.transformPainter(painter)
        self.drawShape(painter)
        painter.restore()

        self.drawOutline(painter)

        self.transformPainter(painter)
        self.drawCoordinates(painter)

    ___ drawCoordinates  painter):
        painter.setPen(__.red)

        painter.drawLine(0, 0, 50, 0)
        painter.drawLine(48, -2, 50, 0)
        painter.drawLine(48, 2, 50, 0)
        painter.drawText(60 - self.xBoundingRect.width() / 2,
                         0 + self.xBoundingRect.height() / 2, "x")

        painter.drawLine(0, 0, 0, 50)
        painter.drawLine(-2, 48, 0, 50)
        painter.drawLine(2, 48, 0, 50)
        painter.drawText(0 - self.yBoundingRect.width() / 2,
                         60 + self.yBoundingRect.height() / 2, "y")

    ___ drawOutline  painter):
        painter.setPen(__.darkGreen)
        painter.setPen(__.DashLine)
        painter.setBrush(__.NoBrush)
        painter.drawRect(0, 0, 100, 100)

    ___ drawShape  painter):
        painter.fillPath(self.shape, __.blue)

    ___ transformPainter  painter):
        for operation in self.operations:
            __ operation == Translate:
                painter.translate(50, 50)

            ____ operation == Scale:
                painter.scale(0.75, 0.75)

            ____ operation == Rotate:
                painter.rotate(60)


c_ Window(QWidget):

    operationTable _ (NoTransformation, Rotate, Scale, Translate)
    NumTransformedAreas _ 3

    ___ __init__(self):
        super(Window, self).__init__()

        self.originalRenderArea _ RenderArea()

        self.shapeComboBox _ QComboBox()
        self.shapeComboBox.addItem("Clock")
        self.shapeComboBox.addItem("House")
        self.shapeComboBox.addItem("Text")
        self.shapeComboBox.addItem("Truck")

        layout _ QGridLayout()
        layout.aW..(self.originalRenderArea, 0, 0)
        layout.aW..(self.shapeComboBox, 1, 0)

        self.transformedRenderAreas _ list(range(Window.NumTransformedAreas))
        self.operationComboBoxes _ list(range(Window.NumTransformedAreas))

        for i in range(Window.NumTransformedAreas):
            self.transformedRenderAreas[i] _ RenderArea()

            self.operationComboBoxes[i] _ QComboBox()
            self.operationComboBoxes[i].addItem("No transformation")
            self.operationComboBoxes[i].addItem(u"Rotate by 60\N{DEGREE SIGN}")
            self.operationComboBoxes[i].addItem("Scale to 75%")
            self.operationComboBoxes[i].addItem("Translate by (50, 50)")

            self.operationComboBoxes[i].activated.c..(self.operationChanged)

            layout.aW..(self.transformedRenderAreas[i], 0, i + 1)
            layout.aW..(self.operationComboBoxes[i], 1, i + 1)

        self.sL..(layout)
        self.setupShapes()
        self.shapeSelected(0)

        self.setWindowTitle("Transformations")

    ___ setupShapes(self):
        truck _ QPainterPath()
        truck.setFillRule(__.WindingFill)
        truck.moveTo(0.0, 87.0)
        truck.lineTo(0.0, 60.0)
        truck.lineTo(10.0, 60.0)
        truck.lineTo(35.0, 35.0)
        truck.lineTo(100.0, 35.0)
        truck.lineTo(100.0, 87.0)
        truck.lineTo(0.0, 87.0)
        truck.moveTo(17.0, 60.0)
        truck.lineTo(55.0, 60.0)
        truck.lineTo(55.0, 40.0)
        truck.lineTo(37.0, 40.0)
        truck.lineTo(17.0, 60.0)
        truck.addEllipse(17.0, 75.0, 25.0, 25.0)
        truck.addEllipse(63.0, 75.0, 25.0, 25.0)

        clock _ QPainterPath()
        clock.addEllipse(-50.0, -50.0, 100.0, 100.0)
        clock.addEllipse(-48.0, -48.0, 96.0, 96.0)
        clock.moveTo(0.0, 0.0)
        clock.lineTo(-2.0, -2.0)
        clock.lineTo(0.0, -42.0)
        clock.lineTo(2.0, -2.0)
        clock.lineTo(0.0, 0.0)
        clock.moveTo(0.0, 0.0)
        clock.lineTo(2.732, -0.732)
        clock.lineTo(24.495, 14.142)
        clock.lineTo(0.732, 2.732)
        clock.lineTo(0.0, 0.0)

        house _ QPainterPath()
        house.moveTo(-45.0, -20.0)
        house.lineTo(0.0, -45.0)
        house.lineTo(45.0, -20.0)
        house.lineTo(45.0, 45.0)
        house.lineTo(-45.0, 45.0)
        house.lineTo(-45.0, -20.0)
        house.addRect(15.0, 5.0, 20.0, 35.0)
        house.addRect(-35.0, -15.0, 25.0, 25.0)

        t__ _ QPainterPath()
        font _ QFont()
        font.setPixelSize(50)
        fontBoundingRect _ QFontMetrics(font).boundingRect("Qt")
        t__.addText(-QPointF(fontBoundingRect.center()), font, "Qt")

        self.shapes _ (clock, house, t__, truck)

        self.shapeComboBox.activated.c..(self.shapeSelected)

    ___ operationChanged(self):
        operations _ []
        for i in range(Window.NumTransformedAreas):
            index _ self.operationComboBoxes[i].currentIndex()
            operations.append(Window.operationTable[index])
            self.transformedRenderAreas[i].setOperations(operations[:])

    ___ shapeSelected  index):
        shape _ self.shapes[index]
        self.originalRenderArea.setShape(shape)
        for i in range(Window.NumTransformedAreas):
            self.transformedRenderAreas[i].setShape(shape)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ Window()
    window.s..
    sys.exit(app.exec_())
