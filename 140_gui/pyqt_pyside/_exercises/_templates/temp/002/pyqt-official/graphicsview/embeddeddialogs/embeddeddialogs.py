#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################


____ ?.?C.. ______ QEvent, QRectF, __, QTimeLine
____ ?.?G.. ______ (QBrush, ?C.., QPainter, QPainterPath, QPixmap,
        QTransform)
____ ?.?W.. ______ (?A.., QDialog, QGraphicsItem,
        QGraphicsProxyWidget, QGraphicsScene, QGraphicsView, QStyleFactory,
        ?W..)

______ embeddeddialogs_rc
____ embeddeddialog ______ Ui_embeddedDialog


c_ CustomProxy(QGraphicsProxyWidget):
    ___  -   parent_None, wFlags_0):
        super(CustomProxy, self). - (parent, wFlags)

        popupShown _ False
        currentPopup _ N..

        timeLine _ QTimeLine(250, self)
        timeLine.valueChanged.c..(updateStep)
        timeLine.stateChanged.c..(stateChanged)

    ___ boundingRect
        r_ QGraphicsProxyWidget.boundingRect.adjusted(0, 0, 10, 10)

    ___ paintWindowFrame  painter, option, widget):
        color _ ?C..(0, 0, 0, 64)

        r _ windowFrameRect()
        right _ QRectF(r.right(), r.top()+10, 10, r.height()-10)
        bottom _ QRectF(r.left()+10, r.bottom(), r.width(), 10)
        intersectsRight _ right.intersects(option.exposedRect)
        intersectsBottom _ bottom.intersects(option.exposedRect)
        __ intersectsRight and intersectsBottom:
            path _ QPainterPath()
            path.addRect(right)
            path.addRect(bottom)
            painter.setPen(__.NoPen)
            painter.setBrush(color)
            painter.drawPath(path)
        ____ intersectsBottom:
            painter.fillRect(bottom, color)
        ____ intersectsRight:
            painter.fillRect(right, color)

        super(CustomProxy, self).paintWindowFrame(painter, option, widget)

    ___ hoverEnterEvent  event):
        super(CustomProxy, self).hoverEnterEvent(event)

        scene().setActiveWindow
        __ timeLine.currentValue !_ 1:
            zoomIn()

    ___ hoverLeaveEvent  event):
        super(CustomProxy, self).hoverLeaveEvent(event)

        __ no. popupShown and (timeLine.direction() !_ QTimeLine.Backward or timeLine.currentValue() !_ 0):
            zoomOut()

    ___ sceneEventFilter  watched, event):
        __ watched.isWindow() and (event.type() == QEvent.UngrabMouse or event.type() == QEvent.GrabMouse):
            popupShown _ watched.isVisible()
            __ no. popupShown and no. isUnderMouse
                zoomOut()

        r_ super(CustomProxy, self).sceneEventFilter(watched, event)

    ___ itemChange  change, value):
        __ change == ItemChildAddedChange or change == ItemChildRemovedChange :
            __ change == ItemChildAddedChange:
                currentPopup _ value
                currentPopup.setCacheMode(ItemCoordinateCache)
                __ scene() __ no. N..:
                    currentPopup.installSceneEventFilter
            ____ scene() __ no. N..:
                currentPopup.removeSceneEventFilter
                currentPopup _ N..
        ____ currentPopup __ no. N.. and change == ItemSceneHasChanged:
                currentPopup.installSceneEventFilter

        r_ super(CustomProxy, self).itemChange(change, value)

    ___ updateStep  step):
        r _ boundingRect()
        setTransform(QTransform() \
                            .translate(r.width() / 2, r.height() / 2)\
                            .rotate(step * 30, __.XAxis)\
                            .rotate(step * 10, __.YAxis)\
                            .rotate(step * 5, __.ZAxis)\
                            .scale(1 + 1.5 * step, 1 + 1.5 * step)\
                            .translate(-r.width() / 2, -r.height() / 2))

    ___ stateChanged  state):
        __ state == QTimeLine.Running:
            __ timeLine.direction() == QTimeLine.Forward:
                setCacheMode(NoCache)
        ____ state == QTimeLine.NotRunning:
            __ timeLine.direction() == QTimeLine.Backward:
                setCacheMode(DeviceCoordinateCache)

    ___ zoomIn
        __ timeLine.direction() !_ QTimeLine.Forward:
            timeLine.setDirection(QTimeLine.Forward)
        __ timeLine.state() == QTimeLine.NotRunning:
            timeLine.start()

    ___ zoomOut
        __ timeLine.direction() !_ QTimeLine.Backward:
            timeLine.setDirection(QTimeLine.Backward)
        __ timeLine.state() == QTimeLine.NotRunning:
            timeLine.start()


c_ EmbeddedDialog(QDialog):
    ___  -   parent_None):
        super(EmbeddedDialog, self). - (parent)

        ui _ Ui_embeddedDialog()
        ui.setupUi
        ui.layoutDirection.setCurrentIndex(layoutDirection() !_ __.LeftToRight)

        ___ styleName __ QStyleFactory.keys
            ui.style.aI..(styleName)
            __ style().objectName().lower() == styleName.lower
                ui.style.setCurrentIndex(ui.style.count() -1)

        ui.layoutDirection.activated.c..(layoutDirectionChanged)
        ui.spacing.valueChanged.c..(spacingChanged)
        ui.fontComboBox.currentFontChanged.c..(fontChanged)
        ui.style.activated[str].c..(styleChanged)

    ___ layoutDirectionChanged  index):
        __ index == 0:
            setLayoutDirection(__.LeftToRight)
        ____
            setLayoutDirection(__.RightToLeft)

    ___ spacingChanged  spacing):
        layout().setSpacing(spacing)
        adjustSize()

    ___ fontChanged  font):
        setFont(font)

    ___ setStyleHelper  widget, style):
        widget.setStyle(style)
        widget.sP..(style.standardPalette())
        ___ child __ widget.children
            __ isinstance(child, ?W..):
                setStyleHelper(child, style)
    
    ___ styleChanged  styleName):
        style _ QStyleFactory.create(styleName)
        __ style:
            setStyleHelper  style)

        # Keep a reference to the style.
        _style _ style


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    scene _ QGraphicsScene()
    scene.setStickyFocus(True)

    ___ y __ range(10):
        ___ x __ range(10):
            proxy _ CustomProxy(N.., __.Window)
            proxy.setWidget(EmbeddedDialog())

            rect _ proxy.boundingRect()

            proxy.setPos( x * rect.width()*1.05, y*rect.height()*1.05 )
            proxy.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
            scene.aI..(proxy)

    scene.setSceneRect(scene.itemsBoundingRect())

    view _ QGraphicsView(scene)
    view.scale(0.5, 0.5)
    view.setRenderHints(view.renderHints() | QPainter.Antialiasing  | QPainter.SmoothPixmapTransform)
    view.setBackgroundBrush(QBrush(QPixmap(':/No-Ones-Laughing-3.jpg')))
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    view.s..
    view.sWT..("Embedded Dialogs Demo")

    ___.e..(app.exec_())
