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


____ ?.?C.. ______ (pP.., QEasingCurve, ?O.., QPoint, QPointF,
        ?PA.., QRect, QRectF, ?S.., __)
____ ?.?G.. ______ (?B.., ?C.., ?I.., QLinearGradient, QPainter,
        QPainterPath, ?P..)
____ ?.?W.. ______ (?A.., QGraphicsPixmapItem, QGraphicsScene,
        QListWidgetItem, ?W..)

______ easing_rc
____ ui_form ______ Ui_Form


c_ Animation(?PA..):
    LinearPath, CirclePath _ ra..(2)

    ___  -   target, prop):
        s__(Animation, self). - (target, prop)

        setPathType(Animation.LinearPath)

    ___ setPathType  pathType):
        m_pathType _ pathType
        m_path _ QPainterPath()

    ___ updateCurrentTime  currentTime):
        __ m_pathType __ Animation.CirclePath:
            __ m_path.isEmpty
                end _ endValue()
                start _ startValue()
                m_path.moveTo(start)
                m_path.addEllipse(QRectF(start, end))

            dura _ duration()
            __ dura __ 0:
                progress _ 1.0
            ____
                progress _ (((currentTime - 1) % dura) + 1) / fl..(dura)

            easedProgress _ easingCurve().valueForProgress(progress)
            __ easedProgress > 1.0:
                easedProgress -_ 1.0
            ____ easedProgress < 0:
                easedProgress +_ 1.0

            pt _ m_path.pointAtPercent(easedProgress)
            updateCurrentValue(pt)
            valueChanged.e..(pt)
        ____
            s__(Animation, self).updateCurrentTime(currentTime)


# PyQt doesn't support deriving from more than one wrapped class so we use
# composition and delegate the property.
c_ PixmapItem(?O..):
    ___  -   pix):
        s__(PixmapItem, self). - ()

        pixmap_item _ QGraphicsPixmapItem(pix)

    ___ _set_pos  pos):
        pixmap_item.setPos(pos)

    pos _ pP..(QPointF, fset__set_pos)


c_ Window(?W..):
    ___  -   parent_None):
        s__(?W.., self). - (parent)

        m_iconSize _ ?S..(64, 64)
        m_scene _ QGraphicsScene()
        m_ui _ Ui_Form()

        m_ui.setupUi
        m_ui.easingCurvePicker.setIconSize(m_iconSize)
        m_ui.easingCurvePicker.setMinimumHeight(m_iconSize.height() + 50)
        m_ui.buttonGroup.setId(m_ui.lineRadio, 0)
        m_ui.buttonGroup.setId(m_ui.circleRadio, 1)

        dummy _ QEasingCurve()
        m_ui.periodSpinBox.sV..(dummy.period())
        m_ui.amplitudeSpinBox.sV..(dummy.amplitude())
        m_ui.overshootSpinBox.sV..(dummy.overshoot())

        m_ui.easingCurvePicker.currentRowChanged.c..(curveChanged)
        m_ui.buttonGroup.buttonClicked[in.].c..(pathChanged)
        m_ui.periodSpinBox.valueChanged.c..(periodChanged)
        m_ui.amplitudeSpinBox.valueChanged.c..(amplitudeChanged)
        m_ui.overshootSpinBox.valueChanged.c..(overshootChanged)
        createCurveIcons()

        pix _ ?P..(':/images/qt-logo.png')
        m_item _ PixmapItem(pix)
        m_scene.aI..(m_item.pixmap_item)
        m_ui.graphicsView.setScene(m_scene)

        m_anim _ Animation(m_item, b'pos')
        m_anim.setEasingCurve(QEasingCurve.OutBounce)
        m_ui.easingCurvePicker.setCurrentRow(in.(QEasingCurve.OutBounce))

        startAnimation()

    ___ createCurveIcons
        pix _ ?P..(m_iconSize)
        painter _ QPainter()

        gradient _ QLinearGradient(0, 0, 0, m_iconSize.height())
        gradient.setColorAt(0.0, ?C..(240, 240, 240))
        gradient.setColorAt(1.0, ?C..(224, 224, 224))

        brush _ ?B..(gradient)

        # The original C++ code uses undocumented calls to get the names of the
        # different curve types.  We do the Python equivalant (but without
        # cheating).
        curve_types _ [(n, c) ___ n, c __ QEasingCurve.__dict__.i..()
                __ isinstance(c, QEasingCurve.Type) and c !_ QEasingCurve.Custom]
        curve_types.s..(key_lambda ct: ct[1])

        painter.begin(pix)

        ___ curve_name, curve_type __ curve_types:
            painter.fillRect(QRect(QPoint(0, 0), m_iconSize), brush)

            curve _ QEasingCurve(curve_type)

            __ curve_type __ QEasingCurve.BezierSpline:
                curve.addCubicBezierSegment(QPointF(0.4, 0.1),
                        QPointF(0.6, 0.9), QPointF(1.0, 1.0))
            ____ curve_type __ QEasingCurve.TCBSpline:
                curve.addTCBSegment(QPointF(0.0, 0.0), 0, 0, 0)
                curve.addTCBSegment(QPointF(0.3, 0.4), 0.2, 1, -0.2)
                curve.addTCBSegment(QPointF(0.7, 0.6), -0.2, 1, 0.2)
                curve.addTCBSegment(QPointF(1.0, 1.0), 0, 0, 0)

            painter.sP..(?C..(0, 0, 255, 64))
            xAxis _ m_iconSize.height() / 1.5
            yAxis _ m_iconSize.width() / 3.0
            painter.drawLine(0, xAxis, m_iconSize.width(),  xAxis)
            painter.drawLine(yAxis, 0, yAxis, m_iconSize.height())

            curveScale _ m_iconSize.height() / 2.0;

            painter.sP..(__.NoPen)

            # Start point.
            painter.sB..(__.red)
            start _ QPoint(yAxis,
                    xAxis - curveScale * curve.valueForProgress(0))
            painter.drawRect(start.x() - 1, start.y() - 1, 3, 3)

            # End point.
            painter.sB..(__.blue)
            end _ QPoint(yAxis + curveScale,
                    xAxis - curveScale * curve.valueForProgress(1))
            painter.drawRect(end.x() - 1, end.y() - 1, 3, 3)

            curvePath _ QPainterPath()
            curvePath.moveTo(QPointF(start))
            t _ 0.0
            w__ t <_ 1.0:
                to _ QPointF(yAxis + curveScale * t,
                        xAxis - curveScale * curve.valueForProgress(t))
                curvePath.lineTo(to)
                t +_ 1.0 / curveScale

            painter.setRenderHint(QPainter.Antialiasing,  st.
            painter.strokePath(curvePath, ?C..(32, 32, 32))
            painter.setRenderHint(QPainter.Antialiasing, F..)

            item _ QListWidgetItem()
            item.sI..(?I..(pix))
            item.sT..(curve_name)
            m_ui.easingCurvePicker.aI..(item)

        painter.end()

    ___ startAnimation
        m_anim.sSV..(QPointF(0, 0))
        m_anim.sEV..(QPointF(100, 100))
        m_anim.sD..(2000)
        m_anim.sLC..(-1)
        m_anim.start()

    ___ curveChanged  row):
        curveType _ QEasingCurve.Type(row)
        m_anim.setEasingCurve(curveType)
        m_anim.setCurrentTime(0)

        isElastic _ (curveType >_ QEasingCurve.InElastic and curveType <_ QEasingCurve.OutInElastic)
        isBounce _ (curveType >_ QEasingCurve.InBounce and curveType <_ QEasingCurve.OutInBounce)

        m_ui.periodSpinBox.sE..(isElastic)
        m_ui.amplitudeSpinBox.sE..(isElastic or isBounce)
        m_ui.overshootSpinBox.sE..(curveType >_ QEasingCurve.InBack and curveType <_ QEasingCurve.OutInBack)

    ___ pathChanged  index):
        m_anim.setPathType(index)

    ___ periodChanged  value):
        curve _ m_anim.easingCurve()
        curve.setPeriod(value)
        m_anim.setEasingCurve(curve)

    ___ amplitudeChanged  value):
        curve _ m_anim.easingCurve()
        curve.setAmplitude(value)
        m_anim.setEasingCurve(curve)

    ___ overshootChanged  value):
        curve _ m_anim.easingCurve()
        curve.setOvershoot(value)
        m_anim.setEasingCurve(curve)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    w _ Window()
    w.r..(400, 400)
    w.s..
    ___.e.. ?.e..
