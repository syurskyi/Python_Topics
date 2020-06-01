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


____ ?.QtCore ______ (pyqtProperty, QEasingCurve, QObject, QPoint, QPointF,
        QPropertyAnimation, QRect, QRectF, QSize, Qt)
____ ?.QtGui ______ (QBrush, QColor, QIcon, QLinearGradient, QPainter,
        QPainterPath, QPixmap)
____ ?.?W.. ______ (QApplication, QGraphicsPixmapItem, QGraphicsScene,
        QListWidgetItem, QWidget)

______ easing_rc
____ ui_form ______ Ui_Form


class Animation(QPropertyAnimation):
    LinearPath, CirclePath _ range(2)

    ___ __init__(self, target, prop):
        super(Animation, self).__init__(target, prop)

        self.setPathType(Animation.LinearPath)

    ___ setPathType(self, pathType):
        self.m_pathType _ pathType
        self.m_path _ QPainterPath()

    ___ updateCurrentTime(self, currentTime):
        if self.m_pathType == Animation.CirclePath:
            if self.m_path.isEmpty
                end _ self.endValue()
                start _ self.startValue()
                self.m_path.moveTo(start)
                self.m_path.addEllipse(QRectF(start, end))

            dura _ self.duration()
            if dura == 0:
                progress _ 1.0
            else:
                progress _ (((currentTime - 1) % dura) + 1) / float(dura)

            easedProgress _ self.easingCurve().valueForProgress(progress)
            if easedProgress > 1.0:
                easedProgress -_ 1.0
            elif easedProgress < 0:
                easedProgress +_ 1.0

            pt _ self.m_path.pointAtPercent(easedProgress)
            self.updateCurrentValue(pt)
            self.valueChanged.emit(pt)
        else:
            super(Animation, self).updateCurrentTime(currentTime)


# PyQt doesn't support deriving from more than one wrapped class so we use
# composition and delegate the property.
class PixmapItem(QObject):
    ___ __init__(self, pix):
        super(PixmapItem, self).__init__()

        self.pixmap_item _ QGraphicsPixmapItem(pix)

    ___ _set_pos(self, pos):
        self.pixmap_item.setPos(pos)

    pos _ pyqtProperty(QPointF, fset__set_pos)


class Window(QWidget):
    ___ __init__(self, parent_None):
        super(QWidget, self).__init__(parent)

        self.m_iconSize _ QSize(64, 64)
        self.m_scene _ QGraphicsScene()
        self.m_ui _ Ui_Form()

        self.m_ui.setupUi(self)
        self.m_ui.easingCurvePicker.setIconSize(self.m_iconSize)
        self.m_ui.easingCurvePicker.setMinimumHeight(self.m_iconSize.height() + 50)
        self.m_ui.buttonGroup.setId(self.m_ui.lineRadio, 0)
        self.m_ui.buttonGroup.setId(self.m_ui.circleRadio, 1)

        dummy _ QEasingCurve()
        self.m_ui.periodSpinBox.setValue(dummy.period())
        self.m_ui.amplitudeSpinBox.setValue(dummy.amplitude())
        self.m_ui.overshootSpinBox.setValue(dummy.overshoot())

        self.m_ui.easingCurvePicker.currentRowChanged.c..(self.curveChanged)
        self.m_ui.buttonGroup.buttonClicked[int].c..(self.pathChanged)
        self.m_ui.periodSpinBox.valueChanged.c..(self.periodChanged)
        self.m_ui.amplitudeSpinBox.valueChanged.c..(self.amplitudeChanged)
        self.m_ui.overshootSpinBox.valueChanged.c..(self.overshootChanged)
        self.createCurveIcons()

        pix _ QPixmap(':/images/qt-logo.png')
        self.m_item _ PixmapItem(pix)
        self.m_scene.addItem(self.m_item.pixmap_item)
        self.m_ui.graphicsView.setScene(self.m_scene)

        self.m_anim _ Animation(self.m_item, b'pos')
        self.m_anim.setEasingCurve(QEasingCurve.OutBounce)
        self.m_ui.easingCurvePicker.setCurrentRow(int(QEasingCurve.OutBounce))

        self.startAnimation()

    ___ createCurveIcons(self):
        pix _ QPixmap(self.m_iconSize)
        painter _ QPainter()

        gradient _ QLinearGradient(0, 0, 0, self.m_iconSize.height())
        gradient.setColorAt(0.0, QColor(240, 240, 240))
        gradient.setColorAt(1.0, QColor(224, 224, 224))

        brush _ QBrush(gradient)

        # The original C++ code uses undocumented calls to get the names of the
        # different curve types.  We do the Python equivalant (but without
        # cheating).
        curve_types _ [(n, c) for n, c in QEasingCurve.__dict__.items()
                if isinstance(c, QEasingCurve.Type) and c !_ QEasingCurve.Custom]
        curve_types.sort(key_lambda ct: ct[1])

        painter.begin(pix)

        for curve_name, curve_type in curve_types:
            painter.fillRect(QRect(QPoint(0, 0), self.m_iconSize), brush)

            curve _ QEasingCurve(curve_type)

            if curve_type == QEasingCurve.BezierSpline:
                curve.addCubicBezierSegment(QPointF(0.4, 0.1),
                        QPointF(0.6, 0.9), QPointF(1.0, 1.0))
            elif curve_type == QEasingCurve.TCBSpline:
                curve.addTCBSegment(QPointF(0.0, 0.0), 0, 0, 0)
                curve.addTCBSegment(QPointF(0.3, 0.4), 0.2, 1, -0.2)
                curve.addTCBSegment(QPointF(0.7, 0.6), -0.2, 1, 0.2)
                curve.addTCBSegment(QPointF(1.0, 1.0), 0, 0, 0)

            painter.setPen(QColor(0, 0, 255, 64))
            xAxis _ self.m_iconSize.height() / 1.5
            yAxis _ self.m_iconSize.width() / 3.0
            painter.drawLine(0, xAxis, self.m_iconSize.width(),  xAxis)
            painter.drawLine(yAxis, 0, yAxis, self.m_iconSize.height())

            curveScale _ self.m_iconSize.height() / 2.0;

            painter.setPen(Qt.NoPen)

            # Start point.
            painter.setBrush(Qt.red)
            start _ QPoint(yAxis,
                    xAxis - curveScale * curve.valueForProgress(0))
            painter.drawRect(start.x() - 1, start.y() - 1, 3, 3)

            # End point.
            painter.setBrush(Qt.blue)
            end _ QPoint(yAxis + curveScale,
                    xAxis - curveScale * curve.valueForProgress(1))
            painter.drawRect(end.x() - 1, end.y() - 1, 3, 3)

            curvePath _ QPainterPath()
            curvePath.moveTo(QPointF(start))
            t _ 0.0
            while t <_ 1.0:
                to _ QPointF(yAxis + curveScale * t,
                        xAxis - curveScale * curve.valueForProgress(t))
                curvePath.lineTo(to)
                t +_ 1.0 / curveScale

            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.strokePath(curvePath, QColor(32, 32, 32))
            painter.setRenderHint(QPainter.Antialiasing, False)

            item _ QListWidgetItem()
            item.setIcon(QIcon(pix))
            item.sT..(curve_name)
            self.m_ui.easingCurvePicker.addItem(item)

        painter.end()

    ___ startAnimation(self):
        self.m_anim.setStartValue(QPointF(0, 0))
        self.m_anim.setEndValue(QPointF(100, 100))
        self.m_anim.setDuration(2000)
        self.m_anim.setLoopCount(-1)
        self.m_anim.start()

    ___ curveChanged(self, row):
        curveType _ QEasingCurve.Type(row)
        self.m_anim.setEasingCurve(curveType)
        self.m_anim.setCurrentTime(0)

        isElastic _ (curveType >_ QEasingCurve.InElastic and curveType <_ QEasingCurve.OutInElastic)
        isBounce _ (curveType >_ QEasingCurve.InBounce and curveType <_ QEasingCurve.OutInBounce)

        self.m_ui.periodSpinBox.setEnabled(isElastic)
        self.m_ui.amplitudeSpinBox.setEnabled(isElastic or isBounce)
        self.m_ui.overshootSpinBox.setEnabled(curveType >_ QEasingCurve.InBack and curveType <_ QEasingCurve.OutInBack)

    ___ pathChanged(self, index):
        self.m_anim.setPathType(index)

    ___ periodChanged(self, value):
        curve _ self.m_anim.easingCurve()
        curve.setPeriod(value)
        self.m_anim.setEasingCurve(curve)

    ___ amplitudeChanged(self, value):
        curve _ self.m_anim.easingCurve()
        curve.setAmplitude(value)
        self.m_anim.setEasingCurve(curve)

    ___ overshootChanged(self, value):
        curve _ self.m_anim.easingCurve()
        curve.setOvershoot(value)
        self.m_anim.setEasingCurve(curve)


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    w _ Window()
    w.resize(400, 400)
    w.s..
    sys.exit(app.exec_())
