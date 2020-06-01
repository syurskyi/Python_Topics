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
        QWidget)

______ embeddeddialogs_rc
____ embeddeddialog ______ Ui_embeddedDialog


c_ CustomProxy(QGraphicsProxyWidget):
    ___ __init__  parent_None, wFlags_0):
        super(CustomProxy, self).__init__(parent, wFlags)

        self.popupShown _ False
        self.currentPopup _ N..

        self.timeLine _ QTimeLine(250, self)
        self.timeLine.valueChanged.c..(self.updateStep)
        self.timeLine.stateChanged.c..(self.stateChanged)

    ___ boundingRect(self):
        r_ QGraphicsProxyWidget.boundingRect(self).adjusted(0, 0, 10, 10)

    ___ paintWindowFrame  painter, option, widget):
        color _ ?C..(0, 0, 0, 64)

        r _ self.windowFrameRect()
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

        self.scene().setActiveWindow(self)
        __ self.timeLine.currentValue !_ 1:
            self.zoomIn()

    ___ hoverLeaveEvent  event):
        super(CustomProxy, self).hoverLeaveEvent(event)

        __ no. self.popupShown and (self.timeLine.direction() !_ QTimeLine.Backward or self.timeLine.currentValue() !_ 0):
            self.zoomOut()

    ___ sceneEventFilter  watched, event):
        __ watched.isWindow() and (event.type() == QEvent.UngrabMouse or event.type() == QEvent.GrabMouse):
            self.popupShown _ watched.isVisible()
            __ no. self.popupShown and no. self.isUnderMouse
                self.zoomOut()

        r_ super(CustomProxy, self).sceneEventFilter(watched, event)

    ___ itemChange  change, value):
        __ change == self.ItemChildAddedChange or change == self.ItemChildRemovedChange :
            __ change == self.ItemChildAddedChange:
                self.currentPopup _ value
                self.currentPopup.setCacheMode(self.ItemCoordinateCache)
                __ self.scene() __ no. N..:
                    self.currentPopup.installSceneEventFilter(self)
            ____ self.scene() __ no. N..:
                self.currentPopup.removeSceneEventFilter(self)
                self.currentPopup _ N..
        ____ self.currentPopup __ no. N.. and change == self.ItemSceneHasChanged:
                self.currentPopup.installSceneEventFilter(self)

        r_ super(CustomProxy, self).itemChange(change, value)

    ___ updateStep  step):
        r _ self.boundingRect()
        self.setTransform(QTransform() \
                            .translate(r.width() / 2, r.height() / 2)\
                            .rotate(step * 30, __.XAxis)\
                            .rotate(step * 10, __.YAxis)\
                            .rotate(step * 5, __.ZAxis)\
                            .scale(1 + 1.5 * step, 1 + 1.5 * step)\
                            .translate(-r.width() / 2, -r.height() / 2))

    ___ stateChanged  state):
        __ state == QTimeLine.Running:
            __ self.timeLine.direction() == QTimeLine.Forward:
                self.setCacheMode(self.NoCache)
        ____ state == QTimeLine.NotRunning:
            __ self.timeLine.direction() == QTimeLine.Backward:
                self.setCacheMode(self.DeviceCoordinateCache)

    ___ zoomIn(self):
        __ self.timeLine.direction() !_ QTimeLine.Forward:
            self.timeLine.setDirection(QTimeLine.Forward)
        __ self.timeLine.state() == QTimeLine.NotRunning:
            self.timeLine.start()

    ___ zoomOut(self):
        __ self.timeLine.direction() !_ QTimeLine.Backward:
            self.timeLine.setDirection(QTimeLine.Backward)
        __ self.timeLine.state() == QTimeLine.NotRunning:
            self.timeLine.start()


c_ EmbeddedDialog(QDialog):
    ___ __init__  parent_None):
        super(EmbeddedDialog, self).__init__(parent)

        self.ui _ Ui_embeddedDialog()
        self.ui.setupUi(self)
        self.ui.layoutDirection.setCurrentIndex(self.layoutDirection() !_ __.LeftToRight)

        for styleName in QStyleFactory.keys
            self.ui.style.addItem(styleName)
            __ self.style().objectName().lower() == styleName.lower
                self.ui.style.setCurrentIndex(self.ui.style.count() -1)

        self.ui.layoutDirection.activated.c..(self.layoutDirectionChanged)
        self.ui.spacing.valueChanged.c..(self.spacingChanged)
        self.ui.fontComboBox.currentFontChanged.c..(self.fontChanged)
        self.ui.style.activated[str].c..(self.styleChanged)

    ___ layoutDirectionChanged  index):
        __ index == 0:
            self.setLayoutDirection(__.LeftToRight)
        ____
            self.setLayoutDirection(__.RightToLeft)

    ___ spacingChanged  spacing):
        self.layout().setSpacing(spacing)
        self.adjustSize()

    ___ fontChanged  font):
        self.setFont(font)

    ___ setStyleHelper  widget, style):
        widget.setStyle(style)
        widget.sP..(style.standardPalette())
        for child in widget.children
            __ isinstance(child, QWidget):
                self.setStyleHelper(child, style)
    
    ___ styleChanged  styleName):
        style _ QStyleFactory.create(styleName)
        __ style:
            self.setStyleHelper  style)

        # Keep a reference to the style.
        self._style _ style


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)

    scene _ QGraphicsScene()
    scene.setStickyFocus(True)

    for y in range(10):
        for x in range(10):
            proxy _ CustomProxy(N.., __.Window)
            proxy.setWidget(EmbeddedDialog())

            rect _ proxy.boundingRect()

            proxy.setPos( x * rect.width()*1.05, y*rect.height()*1.05 )
            proxy.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
            scene.addItem(proxy)

    scene.setSceneRect(scene.itemsBoundingRect())

    view _ QGraphicsView(scene)
    view.scale(0.5, 0.5)
    view.setRenderHints(view.renderHints() | QPainter.Antialiasing  | QPainter.SmoothPixmapTransform)
    view.setBackgroundBrush(QBrush(QPixmap(':/No-Ones-Laughing-3.jpg')))
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    view.s..
    view.setWindowTitle("Embedded Dialogs Demo")

    ___.exit(app.exec_())
