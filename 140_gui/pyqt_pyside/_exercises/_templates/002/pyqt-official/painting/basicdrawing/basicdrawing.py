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


____ ?.?C.. ______ QPoint, QRect, ?S.., __
____ ?.?G.. ______ (?B.., QConicalGradient, QLinearGradient, QPainter,
        QPainterPath, ?P.., ?P.., ?P.., QPolygon, QRadialGradient)
____ ?.?W.. ______ (?A.., QCheckBox, ?CB, QGridLayout,
        ?L.., SB.., ?W..)

______ basicdrawing_rc


c_ RenderArea(?W..):
    points _ QPolygon([
        QPoint(10, 80),
        QPoint(20, 10),
        QPoint(80, 30),
        QPoint(90, 70)
    ])

    Line, Points, Polyline, Polygon, Rect, RoundedRect, Ellipse, Arc, Chord, \
            Pie, Path, Text, Pixmap _ ra..(13)

    ___  -   parent_None):
        s__(RenderArea, self). - (parent)

        pen _ ?P..()
        brush _ ?B..()
        pixmap _ ?P..()

        shape _ RenderArea.Polygon
        antialiased _ F..
        transformed _ F..
        pixmap.load(':/images/qt-logo.png')

        setBackgroundRole(?P...Base)
        setAutoFillBackground( st.

    ___ minimumSizeHint
        r_ ?S..(100, 100)

    ___ sH..
        r_ ?S..(400, 200)

    ___ setShape  shape):
        shape _ shape
        update()

    ___ sP..  pen):
        pen _ pen
        update()

    ___ sB..  brush):
        brush _ brush
        update()

    ___ setAntialiased  antialiased):
        antialiased _ antialiased
        update()

    ___ setTransformed  transformed):
        transformed _ transformed
        update()

    ___ paintEvent  event):
        rect _ QRect(10, 20, 80, 60)

        pa__ _ QPainterPath()
        pa__.moveTo(20, 80)
        pa__.lineTo(20, 30)
        pa__.cubicTo(80, 0, 50, 50, 80, 80)

        startAngle _ 30 * 16
        arcLength _ 120 * 16

        painter _ QPainter
        painter.sP..(pen)
        painter.sB..(brush)
        __ antialiased:
            painter.setRenderHint(QPainter.Antialiasing)

        ___ x __ ra..(0, width(), 100):
            ___ y __ ra..(0, height(), 100):
                painter.save()
                painter.translate(x, y)
                __ transformed:
                    painter.translate(50, 50)
                    painter.rotate(60.0)
                    painter.scale(0.6, 0.9)
                    painter.translate(-50, -50)

                __ shape __ RenderArea.Line:
                    painter.drawLine(rect.bottomLeft(), rect.topRight())
                ____ shape __ RenderArea.Points:
                    painter.drawPoints(RenderArea.points)
                ____ shape __ RenderArea.Polyline:
                    painter.drawPolyline(RenderArea.points)
                ____ shape __ RenderArea.Polygon:
                    painter.drawPolygon(RenderArea.points)
                ____ shape __ RenderArea.Rect:
                    painter.drawRect(rect)
                ____ shape __ RenderArea.RoundedRect:
                    painter.dRR..(rect, 25, 25, __.RelativeSize)
                ____ shape __ RenderArea.Ellipse:
                    painter.drawEllipse(rect)
                ____ shape __ RenderArea.Arc:
                    painter.drawArc(rect, startAngle, arcLength)
                ____ shape __ RenderArea.Chord:
                    painter.drawChord(rect, startAngle, arcLength)
                ____ shape __ RenderArea.Pie:
                    painter.drawPie(rect, startAngle, arcLength)
                ____ shape __ RenderArea.Path:
                    painter.drawPath(pa__)
                ____ shape __ RenderArea.Text:
                    painter.drawText(rect, __.AlignCenter,
                            "PyQt by\nRiverbank Computing")
                ____ shape __ RenderArea.Pixmap:
                    painter.drawPixmap(10, 10, pixmap)

                painter.restore()

        painter.sP..(p...dark().color())
        painter.sB..(__.NoBrush)
        painter.drawRect(QRect(0, 0, width() - 1, height() - 1))


IdRole _ __.UserRole

c_ Window(?W..):
    ___  -
        s__(Window, self). - ()

        renderArea _ RenderArea()

        shapeComboBox _ ?CB()
        shapeComboBox.aI..("Polygon", RenderArea.Polygon)
        shapeComboBox.aI..("Rectangle", RenderArea.Rect)
        shapeComboBox.aI..("Rounded Rectangle", RenderArea.RoundedRect)
        shapeComboBox.aI..("Ellipse", RenderArea.Ellipse)
        shapeComboBox.aI..("Pie", RenderArea.Pie)
        shapeComboBox.aI..("Chord", RenderArea.Chord)
        shapeComboBox.aI..("Path", RenderArea.Path)
        shapeComboBox.aI..("Line", RenderArea.Line)
        shapeComboBox.aI..("Polyline", RenderArea.Polyline)
        shapeComboBox.aI..("Arc", RenderArea.Arc)
        shapeComboBox.aI..("Points", RenderArea.Points)
        shapeComboBox.aI..("Text", RenderArea.Text)
        shapeComboBox.aI..("Pixmap", RenderArea.Pixmap)

        shapeLabel _ ?L..("&Shape:")
        shapeLabel.setBuddy(shapeComboBox)

        penWidthSpinBox _ SB..()
        penWidthSpinBox.setRange(0, 20)
        penWidthSpinBox.setSpecialValueText("0 (cosmetic pen)")

        penWidthLabel _ ?L..("Pen &Width:")
        penWidthLabel.setBuddy(penWidthSpinBox)

        penStyleComboBox _ ?CB()
        penStyleComboBox.aI..("Solid", __.SolidLine)
        penStyleComboBox.aI..("Dash", __.DashLine)
        penStyleComboBox.aI..("Dot", __.DotLine)
        penStyleComboBox.aI..("Dash Dot", __.DashDotLine)
        penStyleComboBox.aI..("Dash Dot Dot", __.DashDotDotLine)
        penStyleComboBox.aI..("None", __.NoPen)

        penStyleLabel _ ?L..("&Pen Style:")
        penStyleLabel.setBuddy(penStyleComboBox)

        penCapComboBox _ ?CB()
        penCapComboBox.aI..("Flat", __.FlatCap)
        penCapComboBox.aI..("Square", __.SquareCap)
        penCapComboBox.aI..("Round", __.RoundCap)

        penCapLabel _ ?L..("Pen &Cap:")
        penCapLabel.setBuddy(penCapComboBox)

        penJoinComboBox _ ?CB()
        penJoinComboBox.aI..("Miter", __.MiterJoin)
        penJoinComboBox.aI..("Bevel", __.BevelJoin)
        penJoinComboBox.aI..("Round", __.RoundJoin)

        penJoinLabel _ ?L..("Pen &Join:")
        penJoinLabel.setBuddy(penJoinComboBox)

        brushStyleComboBox _ ?CB()
        brushStyleComboBox.aI..("Linear Gradient",
                __.LinearGradientPattern)
        brushStyleComboBox.aI..("Radial Gradient",
                __.RadialGradientPattern)
        brushStyleComboBox.aI..("Conical Gradient",
                __.ConicalGradientPattern)
        brushStyleComboBox.aI..("Texture", __.TexturePattern)
        brushStyleComboBox.aI..("Solid", __.SolidPattern)
        brushStyleComboBox.aI..("Horizontal", __.HorPattern)
        brushStyleComboBox.aI..("Vertical", __.VerPattern)
        brushStyleComboBox.aI..("Cross", __.CrossPattern)
        brushStyleComboBox.aI..("Backward Diagonal", __.BDiagPattern)
        brushStyleComboBox.aI..("Forward Diagonal", __.FDiagPattern)
        brushStyleComboBox.aI..("Diagonal Cross", __.DiagCrossPattern)
        brushStyleComboBox.aI..("Dense 1", __.Dense1Pattern)
        brushStyleComboBox.aI..("Dense 2", __.Dense2Pattern)
        brushStyleComboBox.aI..("Dense 3", __.Dense3Pattern)
        brushStyleComboBox.aI..("Dense 4", __.Dense4Pattern)
        brushStyleComboBox.aI..("Dense 5", __.Dense5Pattern)
        brushStyleComboBox.aI..("Dense 6", __.Dense6Pattern)
        brushStyleComboBox.aI..("Dense 7", __.Dense7Pattern)
        brushStyleComboBox.aI..("None", __.NoBrush)

        brushStyleLabel _ ?L..("&Brush Style:")
        brushStyleLabel.setBuddy(brushStyleComboBox)

        otherOptionsLabel _ ?L..("Other Options:")
        antialiasingCheckBox _ QCheckBox("&Antialiasing")
        transformationsCheckBox _ QCheckBox("&Transformations")

        shapeComboBox.activated.c..(shapeChanged)
        penWidthSpinBox.valueChanged.c..(penChanged)
        penStyleComboBox.activated.c..(penChanged)
        penCapComboBox.activated.c..(penChanged)
        penJoinComboBox.activated.c..(penChanged)
        brushStyleComboBox.activated.c..(brushChanged)
        antialiasingCheckBox.t__.c..(renderArea.setAntialiased)
        transformationsCheckBox.t__.c..(renderArea.setTransformed)

        mainLayout _ QGridLayout()
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(3, 1)
        mainLayout.aW..(renderArea, 0, 0, 1, 4)
        mainLayout.setRowMinimumHeight(1, 6)
        mainLayout.aW..(shapeLabel, 2, 1, __.AlignRight)
        mainLayout.aW..(shapeComboBox, 2, 2)
        mainLayout.aW..(penWidthLabel, 3, 1, __.AlignRight)
        mainLayout.aW..(penWidthSpinBox, 3, 2)
        mainLayout.aW..(penStyleLabel, 4, 1, __.AlignRight)
        mainLayout.aW..(penStyleComboBox, 4, 2)
        mainLayout.aW..(penCapLabel, 5, 1, __.AlignRight)
        mainLayout.aW..(penCapComboBox, 5, 2)
        mainLayout.aW..(penJoinLabel, 6, 1, __.AlignRight)
        mainLayout.aW..(penJoinComboBox, 6, 2)
        mainLayout.aW..(brushStyleLabel, 7, 1, __.AlignRight)
        mainLayout.aW..(brushStyleComboBox, 7, 2)
        mainLayout.setRowMinimumHeight(8, 6)
        mainLayout.aW..(otherOptionsLabel, 9, 1, __.AlignRight)
        mainLayout.aW..(antialiasingCheckBox, 9, 2)
        mainLayout.aW..(transformationsCheckBox, 10, 2)
        sL..(mainLayout)

        shapeChanged()
        penChanged()
        brushChanged()
        antialiasingCheckBox.sC__( st.

        sWT..("Basic Drawing")

    ___ shapeChanged
        shape _ shapeComboBox.itemData(shapeComboBox.currentIndex(),
                IdRole)
        renderArea.setShape(shape)

    ___ penChanged
        width _ penWidthSpinBox.v..
        style _ __.PenStyle(penStyleComboBox.itemData(
                penStyleComboBox.currentIndex(), IdRole))
        cap _ __.PenCapStyle(penCapComboBox.itemData(
                penCapComboBox.currentIndex(), IdRole))
        join _ __.PenJoinStyle(penJoinComboBox.itemData(
                penJoinComboBox.currentIndex(), IdRole))

        renderArea.sP..(?P..(__.blue, width, style, cap, join))

    ___ brushChanged
        style _ __.BrushStyle(brushStyleComboBox.itemData(
                brushStyleComboBox.currentIndex(), IdRole))

        __ style __ __.LinearGradientPattern:
            linearGradient _ QLinearGradient(0, 0, 100, 100)
            linearGradient.setColorAt(0.0, __.white)
            linearGradient.setColorAt(0.2, __.green)
            linearGradient.setColorAt(1.0, __.black)
            renderArea.sB..(?B..(linearGradient))
        ____ style __ __.RadialGradientPattern:
            radialGradient _ QRadialGradient(50, 50, 50, 70, 70)
            radialGradient.setColorAt(0.0, __.white)
            radialGradient.setColorAt(0.2, __.green)
            radialGradient.setColorAt(1.0, __.black)
            renderArea.sB..(?B..(radialGradient))
        ____ style __ __.ConicalGradientPattern:
            conicalGradient _ QConicalGradient(50, 50, 150)
            conicalGradient.setColorAt(0.0, __.white)
            conicalGradient.setColorAt(0.2, __.green)
            conicalGradient.setColorAt(1.0, __.black)
            renderArea.sB..(?B..(conicalGradient))
        ____ style __ __.TexturePattern:
            renderArea.sB..(?B..(?P..(':/images/brick.png')))
        ____
            renderArea.sB..(?B..(__.green, style))


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ Window()
    window.s..
    ___.e.. ?.e..
