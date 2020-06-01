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


______ math

____ ?.?C.. ______ (qAbs, QLineF, QPointF, QRectF, qrand, qsrand, __,
        QTime, QTimer)
____ ?.?G.. ______ (QBrush, ?C.., QPainter, QPainterPath, QPixmap,
        QPolygonF)
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsScene,
        QGraphicsView, QGraphicsWidget)

______ mice_rc


c_ Mouse(QGraphicsItem):
    Pi _ math.pi
    TwoPi _ 2.0 * Pi

    # Create the bounding rectangle once.
    adjust _ 0.5
    BoundingRect _ QRectF(-20 - adjust, -22 - adjust, 40 + adjust, 83 + adjust)

    ___ __init__(self):
        super(Mouse, self).__init__()

        self.angle _ 0.0
        self.speed _ 0.0
        self.mouseEyeDirection _ 0.0
        self.color _ ?C..(qrand() % 256, qrand() % 256, qrand() % 256)

        self.setRotation(qrand() % (360 * 16))

        # In the C++ version of this example, this class is also derived from
        # QObject in order to receive timer events.  PyQt does not support
        # deriving from more than one wrapped class so we just create an
        # explicit timer instead.
        self.timer _ ?T..
        self.timer.timeout.c..(self.timerEvent)
        self.timer.start(1000 / 33)

    @staticmethod
    ___ normalizeAngle(angle):
        while angle < 0:
            angle +_ Mouse.TwoPi
        while angle > Mouse.TwoPi:
            angle -_ Mouse.TwoPi
        r_ angle

    ___ boundingRect(self):
        r_ Mouse.BoundingRect

    ___ shape(self):
        path _ QPainterPath()
        path.addRect(-10, -20, 20, 40)
        r_ path;

    ___ paint  painter, option, widget):
        # Body.
        painter.setBrush(self.color)
        painter.drawEllipse(-10, -20, 20, 40)

        # Eyes.
        painter.setBrush(__.white)
        painter.drawEllipse(-10, -17, 8, 8)
        painter.drawEllipse(2, -17, 8, 8)

        # Nose.
        painter.setBrush(__.black)
        painter.drawEllipse(QRectF(-2, -22, 4, 4))

        # Pupils.
        painter.drawEllipse(QRectF(-8.0 + self.mouseEyeDirection, -17, 4, 4))
        painter.drawEllipse(QRectF(4.0 + self.mouseEyeDirection, -17, 4, 4))

        # Ears.
        __ self.scene().collidingItems(self):
            painter.setBrush(__.red)
        ____
            painter.setBrush(__.darkYellow)

        painter.drawEllipse(-17, -12, 16, 16)
        painter.drawEllipse(1, -12, 16, 16)

        # Tail.
        path _ QPainterPath(QPointF(0, 20))
        path.cubicTo(-5, 22, -5, 22, 0, 25)
        path.cubicTo(5, 27, 5, 32, 0, 30)
        path.cubicTo(-5, 32, -5, 42, 0, 35)
        painter.setBrush(__.NoBrush)
        painter.drawPath(path)

    ___ timerEvent(self):
        # Don't move too far away.
        lineToCenter _ QLineF(QPointF(0, 0), self.mapFromScene(0, 0))
        __ lineToCenter.length() > 150:
            angleToCenter _ math.acos(lineToCenter.dx() / lineToCenter.length())
            __ lineToCenter.dy() < 0:
                angleToCenter _ Mouse.TwoPi - angleToCenter;
            angleToCenter _ Mouse.normalizeAngle((Mouse.Pi - angleToCenter) + Mouse.Pi / 2)

            __ angleToCenter < Mouse.Pi and angleToCenter > Mouse.Pi / 4:
                # Rotate left.
                self.angle +_ [-0.25, 0.25][self.angle < -Mouse.Pi / 2]
            ____ angleToCenter >_ Mouse.Pi and angleToCenter < (Mouse.Pi + Mouse.Pi / 2 + Mouse.Pi / 4):
                # Rotate right.
                self.angle +_ [-0.25, 0.25][self.angle < Mouse.Pi / 2]
        ____ math.sin(self.angle) < 0:
            self.angle +_ 0.25
        ____ math.sin(self.angle) > 0:
            self.angle -_ 0.25

        # Try not to crash with any other mice.
        dangerMice _ self.scene().items(QPolygonF([self.mapToScene(0, 0),
                                                         self.mapToScene(-30, -50),
                                                         self.mapToScene(30, -50)]))

        for item in dangerMice:
            __ item __ self:
                continue
        
            lineToMouse _ QLineF(QPointF(0, 0), self.mapFromItem(item, 0, 0))
            angleToMouse _ math.acos(lineToMouse.dx() / lineToMouse.length())
            __ lineToMouse.dy() < 0:
                angleToMouse _ Mouse.TwoPi - angleToMouse
            angleToMouse _ Mouse.normalizeAngle((Mouse.Pi - angleToMouse) + Mouse.Pi / 2)

            __ angleToMouse >_ 0 and angleToMouse < Mouse.Pi / 2:
                # Rotate right.
                self.angle +_ 0.5
            ____ angleToMouse <_ Mouse.TwoPi and angleToMouse > (Mouse.TwoPi - Mouse.Pi / 2):
                # Rotate left.
                self.angle -_ 0.5

        # Add some random movement.
        __ len(dangerMice) > 1 and (qrand() % 10) == 0:
            __ qrand() % 1:
                self.angle +_ (qrand() % 100) / 500.0
            ____
                self.angle -_ (qrand() % 100) / 500.0

        self.speed +_ (-50 + qrand() % 100) / 100.0

        dx _ math.sin(self.angle) * 10
        self.mouseEyeDirection _ 0.0 __ qAbs(dx / 5) < 1 else dx / 5

        self.setRotation(self.rotation() + dx)
        self.setPos(self.mapToParent(0, -(3 + math.sin(self.speed) * 3)))


__ __name__ == '__main__':

    ______ sys

    MouseCount _ 7

    app _ ?A..(sys.argv)
    qsrand(QTime(0,0,0).secsTo(QTime.currentTime()))

    scene _ QGraphicsScene()
    scene.setSceneRect(-300, -300, 600, 600)
    scene.setItemIndexMethod(QGraphicsScene.NoIndex)

    for i in range(MouseCount):
        mouse _ Mouse()
        mouse.setPos(math.sin((i * 6.28) / MouseCount) * 200,
                     math.cos((i * 6.28) / MouseCount) * 200)
        scene.addItem(mouse)

    view _ QGraphicsView(scene)
    view.setRenderHint(QPainter.Antialiasing)
    view.setBackgroundBrush(QBrush(QPixmap(':/images/cheese.jpg')))
    view.setCacheMode(QGraphicsView.CacheBackground)
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    view.setDragMode(QGraphicsView.ScrollHandDrag)
    view.setWindowTitle("Colliding Mice")
    view.resize(400, 300)
    view.s..

    sys.exit(app.exec_())
