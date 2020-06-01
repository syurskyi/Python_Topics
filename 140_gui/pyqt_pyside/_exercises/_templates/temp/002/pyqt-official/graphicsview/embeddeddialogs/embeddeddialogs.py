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


____ ?.QtCore ______ QEvent, QRectF, Qt, QTimeLine
____ ?.QtGui ______ (QBrush, QColor, QPainter, QPainterPath, QPixmap,
        QTransform)
____ ?.?W.. ______ (QApplication, QDialog, QGraphicsItem,
        QGraphicsProxyWidget, QGraphicsScene, QGraphicsView, QStyleFactory,
        QWidget)

______ embeddeddialogs_rc
____ embeddeddialog ______ Ui_embeddedDialog


class CustomProxy(QGraphicsProxyWidget):
    ___ __init__(self, parent_None, wFlags_0):
        super(CustomProxy, self).__init__(parent, wFlags)

        self.popupShown _ False
        self.currentPopup _ None

        self.timeLine _ QTimeLine(250, self)
        self.timeLine.valueChanged.c..(self.updateStep)
        self.timeLine.stateChanged.c..(self.stateChanged)

    ___ boundingRect(self):
        return QGraphicsProxyWidget.boundingRect(self).adjusted(0, 0, 10, 10)

    ___ paintWindowFrame(self, painter, option, widget):
        color _ QColor(0, 0, 0, 64)

        r _ self.windowFrameRect()
        right _ QRectF(r.right(), r.top()+10, 10, r.height()-10)
        bottom _ QRectF(r.left()+10, r.bottom(), r.width(), 10)
        intersectsRight _ right.intersects(option.exposedRect)
        intersectsBottom _ bottom.intersects(option.exposedRect)
        if intersectsRight and intersectsBottom:
            path _ QPainterPath()
            path.addRect(right)
            path.addRect(bottom)
            painter.setPen(Qt.NoPen)
            painter.setBrush(color)
            painter.drawPath(path)
        elif intersectsBottom:
            painter.fillRect(bottom, color)
        elif intersectsRight:
            painter.fillRect(right, color)

        super(CustomProxy, self).paintWindowFrame(painter, option, widget)

    ___ hoverEnterEvent(self, event):
        super(CustomProxy, self).hoverEnterEvent(event)

        self.scene().setActiveWindow(self)
        if self.timeLine.currentValue !_ 1:
            self.zoomIn()

    ___ hoverLeaveEvent(self, event):
        super(CustomProxy, self).hoverLeaveEvent(event)

        if not self.popupShown and (self.timeLine.direction() !_ QTimeLine.Backward or self.timeLine.currentValue() !_ 0):
            self.zoomOut()

    ___ sceneEventFilter(self, watched, event):
        if watched.isWindow() and (event.type() == QEvent.UngrabMouse or event.type() == QEvent.GrabMouse):
            self.popupShown _ watched.isVisible()
            if not self.popupShown and not self.isUnderMouse
                self.zoomOut()

        return super(CustomProxy, self).sceneEventFilter(watched, event)

    ___ itemChange(self, change, value):
        if change == self.ItemChildAddedChange or change == self.ItemChildRemovedChange :
            if change == self.ItemChildAddedChange:
                self.currentPopup _ value
                self.currentPopup.setCacheMode(self.ItemCoordinateCache)
                if self.scene() is not None:
                    self.currentPopup.installSceneEventFilter(self)
            elif self.scene() is not None:
                self.currentPopup.removeSceneEventFilter(self)
                self.currentPopup _ None
        elif self.currentPopup is not None and change == self.ItemSceneHasChanged:
                self.currentPopup.installSceneEventFilter(self)

        return super(CustomProxy, self).itemChange(change, value)

    ___ updateStep(self, step):
        r _ self.boundingRect()
        self.setTransform(QTransform() \
                            .translate(r.width() / 2, r.height() / 2)\
                            .rotate(step * 30, Qt.XAxis)\
                            .rotate(step * 10, Qt.YAxis)\
                            .rotate(step * 5, Qt.ZAxis)\
                            .scale(1 + 1.5 * step, 1 + 1.5 * step)\
                            .translate(-r.width() / 2, -r.height() / 2))

    ___ stateChanged(self, state):
        if state == QTimeLine.Running:
            if self.timeLine.direction() == QTimeLine.Forward:
                self.setCacheMode(self.NoCache)
        elif state == QTimeLine.NotRunning:
            if self.timeLine.direction() == QTimeLine.Backward:
                self.setCacheMode(self.DeviceCoordinateCache)

    ___ zoomIn(self):
        if self.timeLine.direction() !_ QTimeLine.Forward:
            self.timeLine.setDirection(QTimeLine.Forward)
        if self.timeLine.state() == QTimeLine.NotRunning:
            self.timeLine.start()

    ___ zoomOut(self):
        if self.timeLine.direction() !_ QTimeLine.Backward:
            self.timeLine.setDirection(QTimeLine.Backward)
        if self.timeLine.state() == QTimeLine.NotRunning:
            self.timeLine.start()


class EmbeddedDialog(QDialog):
    ___ __init__(self, parent_None):
        super(EmbeddedDialog, self).__init__(parent)

        self.ui _ Ui_embeddedDialog()
        self.ui.setupUi(self)
        self.ui.layoutDirection.setCurrentIndex(self.layoutDirection() !_ Qt.LeftToRight)

        for styleName in QStyleFactory.keys
            self.ui.style.addItem(styleName)
            if self.style().objectName().lower() == styleName.lower
                self.ui.style.setCurrentIndex(self.ui.style.count() -1)

        self.ui.layoutDirection.activated.c..(self.layoutDirectionChanged)
        self.ui.spacing.valueChanged.c..(self.spacingChanged)
        self.ui.fontComboBox.currentFontChanged.c..(self.fontChanged)
        self.ui.style.activated[str].c..(self.styleChanged)

    ___ layoutDirectionChanged(self, index):
        if index == 0:
            self.setLayoutDirection(Qt.LeftToRight)
        else:
            self.setLayoutDirection(Qt.RightToLeft)

    ___ spacingChanged(self, spacing):
        self.layout().setSpacing(spacing)
        self.adjustSize()

    ___ fontChanged(self, font):
        self.setFont(font)

    ___ setStyleHelper(self, widget, style):
        widget.setStyle(style)
        widget.setPalette(style.standardPalette())
        for child in widget.children
            if isinstance(child, QWidget):
                self.setStyleHelper(child, style)
    
    ___ styleChanged(self, styleName):
        style _ QStyleFactory.create(styleName)
        if style:
            self.setStyleHelper(self, style)

        # Keep a reference to the style.
        self._style _ style


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)

    scene _ QGraphicsScene()
    scene.setStickyFocus(True)

    for y in range(10):
        for x in range(10):
            proxy _ CustomProxy(None, Qt.Window)
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

    sys.exit(app.exec_())
