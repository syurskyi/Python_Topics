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


____ ?.?C.. ______ QPoint, QRect, QSize, __
____ ?.?G.. ______ (QBrush, QConicalGradient, QLinearGradient, QPainter,
        QPainterPath, ?P.., QPen, QPixmap, QPolygon, QRadialGradient)
____ ?.?W.. ______ (?A.., QCheckBox, QComboBox, QGridLayout,
        QLabel, QSpinBox, QWidget)

______ basicdrawing_rc


c_ RenderArea(QWidget):
    points _ QPolygon([
        QPoint(10, 80),
        QPoint(20, 10),
        QPoint(80, 30),
        QPoint(90, 70)
    ])

    Line, Points, Polyline, Polygon, Rect, RoundedRect, Ellipse, Arc, Chord, \
            Pie, Path, Text, Pixmap _ range(13)

    ___ __init__  parent_None):
        super(RenderArea, self).__init__(parent)

        self.pen _ QPen()
        self.brush _ QBrush()
        self.pixmap _ QPixmap()

        self.shape _ RenderArea.Polygon
        self.antialiased _ False
        self.transformed _ False
        self.pixmap.load(':/images/qt-logo.png')

        self.setBackgroundRole(?P...Base)
        self.setAutoFillBackground(True)

    ___ minimumSizeHint(self):
        r_ QSize(100, 100)

    ___ sizeHint(self):
        r_ QSize(400, 200)

    ___ setShape  shape):
        self.shape _ shape
        self.update()

    ___ setPen  pen):
        self.pen _ pen
        self.update()

    ___ setBrush  brush):
        self.brush _ brush
        self.update()

    ___ setAntialiased  antialiased):
        self.antialiased _ antialiased
        self.update()

    ___ setTransformed  transformed):
        self.transformed _ transformed
        self.update()

    ___ paintEvent  event):
        rect _ QRect(10, 20, 80, 60)

        path _ QPainterPath()
        path.moveTo(20, 80)
        path.lineTo(20, 30)
        path.cubicTo(80, 0, 50, 50, 80, 80)

        startAngle _ 30 * 16
        arcLength _ 120 * 16

        painter _ QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        __ self.antialiased:
            painter.setRenderHint(QPainter.Antialiasing)

        for x in range(0, self.width(), 100):
            for y in range(0, self.height(), 100):
                painter.save()
                painter.translate(x, y)
                __ self.transformed:
                    painter.translate(50, 50)
                    painter.rotate(60.0)
                    painter.scale(0.6, 0.9)
                    painter.translate(-50, -50)

                __ self.shape == RenderArea.Line:
                    painter.drawLine(rect.bottomLeft(), rect.topRight())
                ____ self.shape == RenderArea.Points:
                    painter.drawPoints(RenderArea.points)
                ____ self.shape == RenderArea.Polyline:
                    painter.drawPolyline(RenderArea.points)
                ____ self.shape == RenderArea.Polygon:
                    painter.drawPolygon(RenderArea.points)
                ____ self.shape == RenderArea.Rect:
                    painter.drawRect(rect)
                ____ self.shape == RenderArea.RoundedRect:
                    painter.drawRoundedRect(rect, 25, 25, __.RelativeSize)
                ____ self.shape == RenderArea.Ellipse:
                    painter.drawEllipse(rect)
                ____ self.shape == RenderArea.Arc:
                    painter.drawArc(rect, startAngle, arcLength)
                ____ self.shape == RenderArea.Chord:
                    painter.drawChord(rect, startAngle, arcLength)
                ____ self.shape == RenderArea.Pie:
                    painter.drawPie(rect, startAngle, arcLength)
                ____ self.shape == RenderArea.Path:
                    painter.drawPath(path)
                ____ self.shape == RenderArea.Text:
                    painter.drawText(rect, __.AlignCenter,
                            "PyQt by\nRiverbank Computing")
                ____ self.shape == RenderArea.Pixmap:
                    painter.drawPixmap(10, 10, self.pixmap)

                painter.restore()

        painter.setPen(self.palette().dark().color())
        painter.setBrush(__.NoBrush)
        painter.drawRect(QRect(0, 0, self.width() - 1, self.height() - 1))


IdRole _ __.UserRole

c_ Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        self.renderArea _ RenderArea()

        self.shapeComboBox _ QComboBox()
        self.shapeComboBox.addItem("Polygon", RenderArea.Polygon)
        self.shapeComboBox.addItem("Rectangle", RenderArea.Rect)
        self.shapeComboBox.addItem("Rounded Rectangle", RenderArea.RoundedRect)
        self.shapeComboBox.addItem("Ellipse", RenderArea.Ellipse)
        self.shapeComboBox.addItem("Pie", RenderArea.Pie)
        self.shapeComboBox.addItem("Chord", RenderArea.Chord)
        self.shapeComboBox.addItem("Path", RenderArea.Path)
        self.shapeComboBox.addItem("Line", RenderArea.Line)
        self.shapeComboBox.addItem("Polyline", RenderArea.Polyline)
        self.shapeComboBox.addItem("Arc", RenderArea.Arc)
        self.shapeComboBox.addItem("Points", RenderArea.Points)
        self.shapeComboBox.addItem("Text", RenderArea.Text)
        self.shapeComboBox.addItem("Pixmap", RenderArea.Pixmap)

        shapeLabel _ QLabel("&Shape:")
        shapeLabel.setBuddy(self.shapeComboBox)

        self.penWidthSpinBox _ QSpinBox()
        self.penWidthSpinBox.setRange(0, 20)
        self.penWidthSpinBox.setSpecialValueText("0 (cosmetic pen)")

        penWidthLabel _ QLabel("Pen &Width:")
        penWidthLabel.setBuddy(self.penWidthSpinBox)

        self.penStyleComboBox _ QComboBox()
        self.penStyleComboBox.addItem("Solid", __.SolidLine)
        self.penStyleComboBox.addItem("Dash", __.DashLine)
        self.penStyleComboBox.addItem("Dot", __.DotLine)
        self.penStyleComboBox.addItem("Dash Dot", __.DashDotLine)
        self.penStyleComboBox.addItem("Dash Dot Dot", __.DashDotDotLine)
        self.penStyleComboBox.addItem("None", __.NoPen)

        penStyleLabel _ QLabel("&Pen Style:")
        penStyleLabel.setBuddy(self.penStyleComboBox)

        self.penCapComboBox _ QComboBox()
        self.penCapComboBox.addItem("Flat", __.FlatCap)
        self.penCapComboBox.addItem("Square", __.SquareCap)
        self.penCapComboBox.addItem("Round", __.RoundCap)

        penCapLabel _ QLabel("Pen &Cap:")
        penCapLabel.setBuddy(self.penCapComboBox)

        self.penJoinComboBox _ QComboBox()
        self.penJoinComboBox.addItem("Miter", __.MiterJoin)
        self.penJoinComboBox.addItem("Bevel", __.BevelJoin)
        self.penJoinComboBox.addItem("Round", __.RoundJoin)

        penJoinLabel _ QLabel("Pen &Join:")
        penJoinLabel.setBuddy(self.penJoinComboBox)

        self.brushStyleComboBox _ QComboBox()
        self.brushStyleComboBox.addItem("Linear Gradient",
                __.LinearGradientPattern)
        self.brushStyleComboBox.addItem("Radial Gradient",
                __.RadialGradientPattern)
        self.brushStyleComboBox.addItem("Conical Gradient",
                __.ConicalGradientPattern)
        self.brushStyleComboBox.addItem("Texture", __.TexturePattern)
        self.brushStyleComboBox.addItem("Solid", __.SolidPattern)
        self.brushStyleComboBox.addItem("Horizontal", __.HorPattern)
        self.brushStyleComboBox.addItem("Vertical", __.VerPattern)
        self.brushStyleComboBox.addItem("Cross", __.CrossPattern)
        self.brushStyleComboBox.addItem("Backward Diagonal", __.BDiagPattern)
        self.brushStyleComboBox.addItem("Forward Diagonal", __.FDiagPattern)
        self.brushStyleComboBox.addItem("Diagonal Cross", __.DiagCrossPattern)
        self.brushStyleComboBox.addItem("Dense 1", __.Dense1Pattern)
        self.brushStyleComboBox.addItem("Dense 2", __.Dense2Pattern)
        self.brushStyleComboBox.addItem("Dense 3", __.Dense3Pattern)
        self.brushStyleComboBox.addItem("Dense 4", __.Dense4Pattern)
        self.brushStyleComboBox.addItem("Dense 5", __.Dense5Pattern)
        self.brushStyleComboBox.addItem("Dense 6", __.Dense6Pattern)
        self.brushStyleComboBox.addItem("Dense 7", __.Dense7Pattern)
        self.brushStyleComboBox.addItem("None", __.NoBrush)

        brushStyleLabel _ QLabel("&Brush Style:")
        brushStyleLabel.setBuddy(self.brushStyleComboBox)

        otherOptionsLabel _ QLabel("Other Options:")
        self.antialiasingCheckBox _ QCheckBox("&Antialiasing")
        self.transformationsCheckBox _ QCheckBox("&Transformations")

        self.shapeComboBox.activated.c..(self.shapeChanged)
        self.penWidthSpinBox.valueChanged.c..(self.penChanged)
        self.penStyleComboBox.activated.c..(self.penChanged)
        self.penCapComboBox.activated.c..(self.penChanged)
        self.penJoinComboBox.activated.c..(self.penChanged)
        self.brushStyleComboBox.activated.c..(self.brushChanged)
        self.antialiasingCheckBox.toggled.c..(self.renderArea.setAntialiased)
        self.transformationsCheckBox.toggled.c..(self.renderArea.setTransformed)

        mainLayout _ QGridLayout()
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(3, 1)
        mainLayout.addWidget(self.renderArea, 0, 0, 1, 4)
        mainLayout.setRowMinimumHeight(1, 6)
        mainLayout.addWidget(shapeLabel, 2, 1, __.AlignRight)
        mainLayout.addWidget(self.shapeComboBox, 2, 2)
        mainLayout.addWidget(penWidthLabel, 3, 1, __.AlignRight)
        mainLayout.addWidget(self.penWidthSpinBox, 3, 2)
        mainLayout.addWidget(penStyleLabel, 4, 1, __.AlignRight)
        mainLayout.addWidget(self.penStyleComboBox, 4, 2)
        mainLayout.addWidget(penCapLabel, 5, 1, __.AlignRight)
        mainLayout.addWidget(self.penCapComboBox, 5, 2)
        mainLayout.addWidget(penJoinLabel, 6, 1, __.AlignRight)
        mainLayout.addWidget(self.penJoinComboBox, 6, 2)
        mainLayout.addWidget(brushStyleLabel, 7, 1, __.AlignRight)
        mainLayout.addWidget(self.brushStyleComboBox, 7, 2)
        mainLayout.setRowMinimumHeight(8, 6)
        mainLayout.addWidget(otherOptionsLabel, 9, 1, __.AlignRight)
        mainLayout.addWidget(self.antialiasingCheckBox, 9, 2)
        mainLayout.addWidget(self.transformationsCheckBox, 10, 2)
        self.setLayout(mainLayout)

        self.shapeChanged()
        self.penChanged()
        self.brushChanged()
        self.antialiasingCheckBox.setChecked(True)

        self.setWindowTitle("Basic Drawing")

    ___ shapeChanged(self):
        shape _ self.shapeComboBox.itemData(self.shapeComboBox.currentIndex(),
                IdRole)
        self.renderArea.setShape(shape)

    ___ penChanged(self):
        width _ self.penWidthSpinBox.value()
        style _ __.PenStyle(self.penStyleComboBox.itemData(
                self.penStyleComboBox.currentIndex(), IdRole))
        cap _ __.PenCapStyle(self.penCapComboBox.itemData(
                self.penCapComboBox.currentIndex(), IdRole))
        join _ __.PenJoinStyle(self.penJoinComboBox.itemData(
                self.penJoinComboBox.currentIndex(), IdRole))

        self.renderArea.setPen(QPen(__.blue, width, style, cap, join))

    ___ brushChanged(self):
        style _ __.BrushStyle(self.brushStyleComboBox.itemData(
                self.brushStyleComboBox.currentIndex(), IdRole))

        __ style == __.LinearGradientPattern:
            linearGradient _ QLinearGradient(0, 0, 100, 100)
            linearGradient.setColorAt(0.0, __.white)
            linearGradient.setColorAt(0.2, __.green)
            linearGradient.setColorAt(1.0, __.black)
            self.renderArea.setBrush(QBrush(linearGradient))
        ____ style == __.RadialGradientPattern:
            radialGradient _ QRadialGradient(50, 50, 50, 70, 70)
            radialGradient.setColorAt(0.0, __.white)
            radialGradient.setColorAt(0.2, __.green)
            radialGradient.setColorAt(1.0, __.black)
            self.renderArea.setBrush(QBrush(radialGradient))
        ____ style == __.ConicalGradientPattern:
            conicalGradient _ QConicalGradient(50, 50, 150)
            conicalGradient.setColorAt(0.0, __.white)
            conicalGradient.setColorAt(0.2, __.green)
            conicalGradient.setColorAt(1.0, __.black)
            self.renderArea.setBrush(QBrush(conicalGradient))
        ____ style == __.TexturePattern:
            self.renderArea.setBrush(QBrush(QPixmap(':/images/brick.png')))
        ____
            self.renderArea.setBrush(QBrush(__.green, style))


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ Window()
    window.s..
    sys.exit(app.exec_())
