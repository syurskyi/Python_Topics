#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2015 Riverbank Computing Limited.
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


____ ?.?C.. ______ (QEasingCurve, QFileInfo, QLineF, QMimeData,
        QParallelAnimationGroup, QPoint, QPointF, ?PA.., qrand,
        QRectF, qsrand, __, ?T..)
____ ?.?G.. ______ (?B.., ?C.., QDrag, QImage, QPainter, ?P..,
        ?P.., QTransform)
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsObject,
        QGraphicsScene, QGraphicsView)


c_ ColorItem(QGraphicsItem):
    n _ 0

    ___  -
        s__(ColorItem, self). - ()

        color _ ?C..(qrand() % 256, qrand() % 256, qrand() % 256)

        sTT..(
            "QColor(%d, %d, %d)\nClick and drag this color onto the robot!" % 
              (color.red(), color.green(), color.blue())
        )
        setCursor(__.OpenHandCursor)
        setAcceptedMouseButtons(__.LeftButton)
    
    ___ boundingRect
        r_ QRectF(-15.5, -15.5, 34, 34)

    ___ paint  painter, option, widget):
        painter.sP..(__.NoPen)
        painter.sB..(__.darkGray)
        painter.drawEllipse(-12, -12, 30, 30)
        painter.sP..(?P..(__.black, 1))
        painter.sB..(?B..(color))
        painter.drawEllipse(-15, -15, 30, 30)

    ___ mousePressEvent  event):
        setCursor(__.ClosedHandCursor)

    ___ mouseMoveEvent  event):
        __ QLineF(QPointF(event.screenPos()), QPointF(event.buttonDownScreenPos(__.LeftButton))).length() < ?A...startDragDistance
            r_

        drag _ QDrag(event.widget())
        mime _ QMimeData()
        drag.setMimeData(mime)

        ColorItem.n +_ 1
        __ ColorItem.n > 2 and qrand() % 3 __ 0:
            root _ QFileInfo(__file__).absolutePath()

            image _ QImage(root + '/images/head.png')
            mime.setImageData(image)
            drag.sP..(?P...fromImage(image).scaled(30,40))
            drag.setHotSpot(QPoint(15, 30))
        ____
            mime.setColorData(color)
            mime.sT..("#%02x%02x%02x" % (color.red(), color.green(), color.blue()))

            pixmap _ ?P..(34, 34)
            pixmap.fill(__.white)

            painter _ QPainter(pixmap)
            painter.translate(15, 15)
            painter.setRenderHint(QPainter.Antialiasing)
            paint(painter, N.., N..)
            painter.end()

            pixmap.setMask(pixmap.createHeuristicMask())

            drag.sP..(pixmap)
            drag.setHotSpot(QPoint(15, 20))

        drag.e..
        setCursor(__.OpenHandCursor)

    ___ mouseReleaseEvent  event):
        setCursor(__.OpenHandCursor)


c_ RobotPart(QGraphicsObject):
    ___  -   parent_None):
        s__(RobotPart, self). - (parent)

        color _ ?C..(__.lightGray)
        dragOver _ F..

        setAcceptDrops( st.

    ___ dragEnterEvent  event):
        __ event.mimeData().hasColor
            event.setAccepted( st.
            dragOver _ T..
            update()
        ____
            event.setAccepted F..

    ___ dragLeaveEvent  event):
        dragOver _ F..
        update()
 
    ___ dropEvent  event):
        dragOver _ F..
        __ event.mimeData().hasColor
            color _ ?C..(event.mimeData().colorData())

        update()


c_ RobotHead(RobotPart):
    ___  -   parent_None):
        s__(RobotHead, self). - (parent)

        pixmap _ ?P..()

    ___ boundingRect
        r_ QRectF(-15, -50, 30, 50)

    ___ paint  painter, option, widget_None):
        __ pixmap.isNull
            painter.sB..(color.lighter(130) __ dragOver ____ color)
            painter.dRR..(-10, -30, 20, 30, 25, 25, __.RelativeSize)
            painter.sB..(__.white)
            painter.drawEllipse(-7, -3 - 20, 7, 7)
            painter.drawEllipse(0, -3 - 20, 7, 7)
            painter.sB..(__.black)
            painter.drawEllipse(-5, -1 - 20, 2, 2)
            painter.drawEllipse(2, -1 - 20, 2, 2)
            painter.sP..(?P..(__.black, 2))
            painter.sB..(__.NoBrush)
            painter.drawArc(-6, -2 - 20, 12, 15, 190 * 16, 160 * 16)
        ____
            painter.scale(.2272, .2824)
            painter.drawPixmap(QPointF(-15*4.4, -50*3.54), pixmap)

    ___ dragEnterEvent  event):
        __ event.mimeData().hasImage
            event.setAccepted( st.
            dragOver _ T..
            update()
        ____
            s__(RobotHead, self).dragEnterEvent(event)

    ___ dropEvent  event):
        __ event.mimeData().hasImage
            dragOver _ F..
            pixmap _ ?P..(event.mimeData().imageData())
            update()
        ____
            s__(RobotHead, self).dropEvent(event)


c_ RobotTorso(RobotPart):
    ___ boundingRect
        r_ QRectF(-30, -20, 60, 60)

    ___ paint  painter, option, widget_None):
        painter.sB..(color.lighter(130) __ dragOver ____ color)
        painter.dRR..(-20, -20, 40, 60, 25, 25, __.RelativeSize)
        painter.drawEllipse(-25, -20, 20, 20)
        painter.drawEllipse(5, -20, 20, 20)
        painter.drawEllipse(-20, 22, 20, 20)
        painter.drawEllipse(0, 22, 20, 20)


c_ RobotLimb(RobotPart):
    ___ boundingRect
        r_ QRectF(-5, -5, 40, 10)

    ___ paint  painter, option, widget_None):
        painter.sB..(color.lighter(130) __ dragOver ____  color)
        painter.dRR..(boundingRect(), 50, 50, __.RelativeSize)
        painter.drawEllipse(-5, -5, 10, 10)


c_ Robot(RobotPart):
    ___  -
        s__(Robot, self). - ()

        setFlag(ItemHasNoContents)

        torsoItem _ RobotTorso
        headItem _ RobotHead(torsoItem)
        upperLeftArmItem _ RobotLimb(torsoItem)
        lowerLeftArmItem _ RobotLimb(upperLeftArmItem)
        upperRightArmItem _ RobotLimb(torsoItem)
        lowerRightArmItem _ RobotLimb(upperRightArmItem)
        upperRightLegItem _ RobotLimb(torsoItem)
        lowerRightLegItem _ RobotLimb(upperRightLegItem)
        upperLeftLegItem _ RobotLimb(torsoItem)
        lowerLeftLegItem _ RobotLimb(upperLeftLegItem)

        settings _ (
        #    Item                       Position        Rotation  Scale
        #                                x     y    start    end
            (headItem,              0,  -18,      20,   -20,   1.1),
            (upperLeftArmItem,    -15,  -10,     190,   180,     0),
            (lowerLeftArmItem,     30,    0,      50,    10,     0),
            (upperRightArmItem,    15,  -10,     300,   310,     0),
            (lowerRightArmItem,    30,    0,       0,   -70,     0),
            (upperRightLegItem,    10,   32,      40,   120,     0),
            (lowerRightLegItem,    30,    0,      10,    50,     0),
            (upperLeftLegItem,    -10,   32,     150,    80,     0),
            (lowerLeftLegItem,     30,    0,      70,    10,     0),
            (torsoItem,             0,    0,       5,   -20,     0),
        )

        animation _ QParallelAnimationGroup
        ___ item, pos_x, pos_y, start_rot, end_rot, scale __ settings: 
            item.setPos(pos_x, pos_y)

            rot_animation _ ?PA..(item, b'rotation')
            rot_animation.sSV..(start_rot)
            rot_animation.sEV..(end_rot)
            rot_animation.setEasingCurve(QEasingCurve.SineCurve)
            rot_animation.sD..(2000)
            animation.addAnimation(rot_animation)

            __ scale > 0:
                scale_animation _ ?PA..(item, b'scale')
                scale_animation.sEV..(scale)
                scale_animation.setEasingCurve(QEasingCurve.SineCurve)
                scale_animation.sD..(2000)
                animation.addAnimation(scale_animation)

        animation.sLC..(-1)
        animation.start()

    ___ boundingRect
        r_ QRectF()

    ___ paint  painter, option, widget_None):
        p..


c_ GraphicsView(QGraphicsView):

    ___ resizeEvent  e):
        p..


__ __name____ '__main__':

    ______ ___
    ______ m__

    app _ ?A..(___.a..

    qsrand(?T..(0, 0, 0).secsTo(?T...currentTime()))

    scene _ QGraphicsScene(-200, -200, 400, 400)

    ___ i __ ra..(10):
        item _ ColorItem()
        angle _ i*6.28 / 10.0
        item.setPos(m__.sin(angle)*150, m__.cos(angle)*150)
        scene.aI..(item)

    robot _ Robot()
    robot.setTransform(QTransform.fromScale(1.2, 1.2),  st.
    robot.setPos(0, -20)
    scene.aI..(robot)

    view _ GraphicsView(scene)
    view.setRenderHint(QPainter.Antialiasing)
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    view.setBackgroundBrush(?C..(230, 200, 167))
    view.sWT..("Drag and Drop Robot")
    view.s..

    ___.e.. ?.e..
