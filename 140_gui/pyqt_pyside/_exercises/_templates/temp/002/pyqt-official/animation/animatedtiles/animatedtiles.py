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


____ ?.?C.. ______ (pyqtProperty, pyqtSignal, QEasingCurve, QObject,
        QParallelAnimationGroup, QPointF, QPropertyAnimation, qrand, QRectF,
        QState, QStateMachine, __, QTimer)
____ ?.?G.. ______ (QBrush, QLinearGradient, QPainter, QPainterPath,
        QPixmap)
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsPixmapItem,
        QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsWidget,
        QStyle)

______ animatedtiles_rc


# PyQt doesn't support deriving from more than one wrapped class so we use
# composition and delegate the property.
c_ Pixmap(QObject):
    ___  -   pix):
        super(Pixmap, self). - ()

        pixmap_item _ QGraphicsPixmapItem(pix)
        pixmap_item.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

    ___ _set_pos  pos):
        pixmap_item.setPos(pos)

    pos _ pyqtProperty(QPointF, fset__set_pos)


c_ Button(QGraphicsWidget):
    pressed _ pyqtSignal()

    ___  -   pixmap, parent_None):
        super(Button, self). - (parent)

        _pix _ pixmap

        setAcceptHoverEvents(True)
        setCacheMode(QGraphicsItem.DeviceCoordinateCache)

    ___ boundingRect
        r_ QRectF(-65, -65, 130, 130)

    ___ shape
        path _ QPainterPath()
        path.addEllipse(boundingRect())

        r_ path

    ___ paint  painter, option, widget):
        down _ option.state & QStyle.State_Sunken
        r _ boundingRect()

        grad _ QLinearGradient(r.topLeft(), r.bottomRight())
        __ option.state & QStyle.State_MouseOver:
            color_0 _ __.white
        ____
            color_0 _ __.lightGray

        color_1 _ __.darkGray

        __ down:
            color_0, color_1 _ color_1, color_0

        grad.setColorAt(0, color_0)
        grad.setColorAt(1, color_1)

        painter.setPen(__.darkGray)
        painter.setBrush(grad)
        painter.drawEllipse(r)

        color_0 _ __.darkGray
        color_1 _ __.lightGray

        __ down:
            color_0, color_1 _ color_1, color_0

        grad.setColorAt(0, color_0)
        grad.setColorAt(1, color_1)

        painter.setPen(__.NoPen)
        painter.setBrush(grad)

        __ down:
            painter.translate(2, 2)

        painter.drawEllipse(r.adjusted(5, 5, -5, -5))
        painter.drawPixmap(-_pix.width() / 2, -_pix.height() / 2,
                _pix)

    ___ mousePressEvent  ev):
        pressed.emit()
        update()

    ___ mouseReleaseEvent  ev):
        update()


c_ View(QGraphicsView):
    ___ resizeEvent  event):
        super(View, self).resizeEvent(event)
        fitInView(sceneRect(), __.KeepAspectRatio)


__ ______ __ ______

    ______ ___
    ______ math

    app _ ?A..(___.a..

    kineticPix _ QPixmap(':/images/kinetic.png')
    bgPix _ QPixmap(':/images/Time-For-Lunch-2.jpg')

    scene _ QGraphicsScene(-350, -350, 700, 700)

    items _   # list
    ___ i __ range(64):
        item _ Pixmap(kineticPix)
        item.pixmap_item.setOffset(-kineticPix.width() / 2,
                -kineticPix.height() / 2)
        item.pixmap_item.setZValue(i)
        items.ap..(item)
        scene.addItem(item.pixmap_item)

    # Buttons.
    buttonParent _ QGraphicsRectItem()
    ellipseButton _ Button(QPixmap(':/images/ellipse.png'), buttonParent)
    figure8Button _ Button(QPixmap(':/images/figure8.png'), buttonParent)
    randomButton _ Button(QPixmap(':/images/random.png'), buttonParent)
    tiledButton _ Button(QPixmap(':/images/tile.png'), buttonParent)
    centeredButton _ Button(QPixmap(':/images/centered.png'), buttonParent)

    ellipseButton.setPos(-100, -100)
    figure8Button.setPos(100, -100)
    randomButton.setPos(0, 0)
    tiledButton.setPos(-100, 100)
    centeredButton.setPos(100, 100)

    scene.addItem(buttonParent)
    buttonParent.setScale(0.75)
    buttonParent.setPos(200, 200)
    buttonParent.setZValue(65)

    # States.
    rootState _ QState()
    ellipseState _ QState(rootState)
    figure8State _ QState(rootState)
    randomState _ QState(rootState)
    tiledState _ QState(rootState)
    centeredState _ QState(rootState)

    # Values.
    ___ i, item __ en..(items):
        # Ellipse.
        ellipseState.assignProperty(item, 'pos',
                QPointF(math.cos((i / 63.0) * 6.28) * 250,
                        math.sin((i / 63.0) * 6.28) * 250))

        # Figure 8.
        figure8State.assignProperty(item, 'pos',
                QPointF(math.sin((i / 63.0) * 6.28) * 250,
                        math.sin(((i * 2)/63.0) * 6.28) * 250))

        # Random.
        randomState.assignProperty(item, 'pos',
                QPointF(-250 + qrand() % 500, -250 + qrand() % 500))

        # Tiled.
        tiledState.assignProperty(item, 'pos',
                QPointF(((i % 8) - 4) * kineticPix.width() + kineticPix.width() / 2,
                        ((i // 8) - 4) * kineticPix.height() + kineticPix.height() / 2))

        # Centered.
        centeredState.assignProperty(item, 'pos', QPointF())

    # Ui.
    view _ View(scene)
    view.setWindowTitle("Animated Tiles")
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    view.setBackgroundBrush(QBrush(bgPix))
    view.setCacheMode(QGraphicsView.CacheBackground)
    view.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    view.s..

    states _ QStateMachine()
    states.addState(rootState)
    states.setInitialState(rootState)
    rootState.setInitialState(centeredState)

    group _ QParallelAnimationGroup()
    ___ i, item __ en..(items):
        anim _ QPropertyAnimation(item, b'pos')
        anim.setDuration(750 + i * 25)
        anim.setEasingCurve(QEasingCurve.InOutBack)
        group.addAnimation(anim)

    trans _ rootState.addTransition(ellipseButton.pressed, ellipseState)
    trans.addAnimation(group)

    trans _ rootState.addTransition(figure8Button.pressed, figure8State)
    trans.addAnimation(group)

    trans _ rootState.addTransition(randomButton.pressed, randomState)
    trans.addAnimation(group)

    trans _ rootState.addTransition(tiledButton.pressed, tiledState)
    trans.addAnimation(group)

    trans _ rootState.addTransition(centeredButton.pressed, centeredState)
    trans.addAnimation(group)

    timer _ ?T..
    timer.start(125)
    timer.setSingleShot(True)
    trans _ rootState.addTransition(timer.timeout, ellipseState)
    trans.addAnimation(group)

    states.start()

    ___.exit(app.exec_())
