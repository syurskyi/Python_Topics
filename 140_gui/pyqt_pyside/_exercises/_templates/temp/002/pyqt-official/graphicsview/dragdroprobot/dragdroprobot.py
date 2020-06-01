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


____ ?.QtCore ______ (QEasingCurve, QFileInfo, QLineF, QMimeData,
        QParallelAnimationGroup, QPoint, QPointF, QPropertyAnimation, qrand,
        QRectF, qsrand, Qt, QTime)
____ ?.QtGui ______ (QBrush, QColor, QDrag, QImage, QPainter, QPen,
        QPixmap, QTransform)
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsObject,
        QGraphicsScene, QGraphicsView)


class ColorItem(QGraphicsItem):
    n _ 0

    ___ __init__(self):
        super(ColorItem, self).__init__()

        self.color _ QColor(qrand() % 256, qrand() % 256, qrand() % 256)

        self.setToolTip(
            "QColor(%d, %d, %d)\nClick and drag this color onto the robot!" % 
              (self.color.red(), self.color.green(), self.color.blue())
        )
        self.setCursor(Qt.OpenHandCursor)
        self.setAcceptedMouseButtons(Qt.LeftButton)
    
    ___ boundingRect(self):
        return QRectF(-15.5, -15.5, 34, 34)

    ___ paint(self, painter, option, widget):
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGray)
        painter.drawEllipse(-12, -12, 30, 30)
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(self.color))
        painter.drawEllipse(-15, -15, 30, 30)

    ___ mousePressEvent(self, event):
        self.setCursor(Qt.ClosedHandCursor)

    ___ mouseMoveEvent(self, event):
        if QLineF(QPointF(event.screenPos()), QPointF(event.buttonDownScreenPos(Qt.LeftButton))).length() < ?A...startDragDistance
            return

        drag _ QDrag(event.widget())
        mime _ QMimeData()
        drag.setMimeData(mime)

        ColorItem.n +_ 1
        if ColorItem.n > 2 and qrand() % 3 == 0:
            root _ QFileInfo(__file__).absolutePath()

            image _ QImage(root + '/images/head.png')
            mime.setImageData(image)
            drag.setPixmap(QPixmap.fromImage(image).scaled(30,40))
            drag.setHotSpot(QPoint(15, 30))
        else:
            mime.setColorData(self.color)
            mime.sT..("#%02x%02x%02x" % (self.color.red(), self.color.green(), self.color.blue()))

            pixmap _ QPixmap(34, 34)
            pixmap.fill(Qt.white)

            painter _ QPainter(pixmap)
            painter.translate(15, 15)
            painter.setRenderHint(QPainter.Antialiasing)
            self.paint(painter, None, None)
            painter.end()

            pixmap.setMask(pixmap.createHeuristicMask())

            drag.setPixmap(pixmap)
            drag.setHotSpot(QPoint(15, 20))

        drag.e..
        self.setCursor(Qt.OpenHandCursor)

    ___ mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)


class RobotPart(QGraphicsObject):
    ___ __init__(self, parent_None):
        super(RobotPart, self).__init__(parent)

        self.color _ QColor(Qt.lightGray)
        self.dragOver _ False

        self.setAcceptDrops(True)

    ___ dragEnterEvent(self, event):
        if event.mimeData().hasColor
            event.setAccepted(True)
            self.dragOver _ True
            self.update()
        else:
            event.setAccepted(False)

    ___ dragLeaveEvent(self, event):
        self.dragOver _ False
        self.update()
 
    ___ dropEvent(self, event):
        self.dragOver _ False
        if event.mimeData().hasColor
            self.color _ QColor(event.mimeData().colorData())

        self.update()


class RobotHead(RobotPart):
    ___ __init__(self, parent_None):
        super(RobotHead, self).__init__(parent)

        self.pixmap _ QPixmap()

    ___ boundingRect(self):
        return QRectF(-15, -50, 30, 50)

    ___ paint(self, painter, option, widget_None):
        if self.pixmap.isNull
            painter.setBrush(self.color.lighter(130) if self.dragOver else self.color)
            painter.drawRoundedRect(-10, -30, 20, 30, 25, 25, Qt.RelativeSize)
            painter.setBrush(Qt.white)
            painter.drawEllipse(-7, -3 - 20, 7, 7)
            painter.drawEllipse(0, -3 - 20, 7, 7)
            painter.setBrush(Qt.black)
            painter.drawEllipse(-5, -1 - 20, 2, 2)
            painter.drawEllipse(2, -1 - 20, 2, 2)
            painter.setPen(QPen(Qt.black, 2))
            painter.setBrush(Qt.NoBrush)
            painter.drawArc(-6, -2 - 20, 12, 15, 190 * 16, 160 * 16)
        else:
            painter.scale(.2272, .2824)
            painter.drawPixmap(QPointF(-15*4.4, -50*3.54), self.pixmap)

    ___ dragEnterEvent(self, event):
        if event.mimeData().hasImage
            event.setAccepted(True)
            self.dragOver _ True
            self.update()
        else:
            super(RobotHead, self).dragEnterEvent(event)

    ___ dropEvent(self, event):
        if event.mimeData().hasImage
            self.dragOver _ False
            self.pixmap _ QPixmap(event.mimeData().imageData())
            self.update()
        else:
            super(RobotHead, self).dropEvent(event)


class RobotTorso(RobotPart):
    ___ boundingRect(self):
        return QRectF(-30, -20, 60, 60)

    ___ paint(self, painter, option, widget_None):
        painter.setBrush(self.color.lighter(130) if self.dragOver else self.color)
        painter.drawRoundedRect(-20, -20, 40, 60, 25, 25, Qt.RelativeSize)
        painter.drawEllipse(-25, -20, 20, 20)
        painter.drawEllipse(5, -20, 20, 20)
        painter.drawEllipse(-20, 22, 20, 20)
        painter.drawEllipse(0, 22, 20, 20)


class RobotLimb(RobotPart):
    ___ boundingRect(self):
        return QRectF(-5, -5, 40, 10)

    ___ paint(self, painter, option, widget_None):
        painter.setBrush(self.color.lighter(130) if self.dragOver else  self.color)
        painter.drawRoundedRect(self.boundingRect(), 50, 50, Qt.RelativeSize)
        painter.drawEllipse(-5, -5, 10, 10)


class Robot(RobotPart):
    ___ __init__(self):
        super(Robot, self).__init__()

        self.setFlag(self.ItemHasNoContents)

        self.torsoItem _ RobotTorso(self)
        self.headItem _ RobotHead(self.torsoItem)
        self.upperLeftArmItem _ RobotLimb(self.torsoItem)
        self.lowerLeftArmItem _ RobotLimb(self.upperLeftArmItem)
        self.upperRightArmItem _ RobotLimb(self.torsoItem)
        self.lowerRightArmItem _ RobotLimb(self.upperRightArmItem)
        self.upperRightLegItem _ RobotLimb(self.torsoItem)
        self.lowerRightLegItem _ RobotLimb(self.upperRightLegItem)
        self.upperLeftLegItem _ RobotLimb(self.torsoItem)
        self.lowerLeftLegItem _ RobotLimb(self.upperLeftLegItem)

        settings _ (
        #    Item                       Position        Rotation  Scale
        #                                x     y    start    end
            (self.headItem,              0,  -18,      20,   -20,   1.1),
            (self.upperLeftArmItem,    -15,  -10,     190,   180,     0),
            (self.lowerLeftArmItem,     30,    0,      50,    10,     0),
            (self.upperRightArmItem,    15,  -10,     300,   310,     0),
            (self.lowerRightArmItem,    30,    0,       0,   -70,     0),
            (self.upperRightLegItem,    10,   32,      40,   120,     0),
            (self.lowerRightLegItem,    30,    0,      10,    50,     0),
            (self.upperLeftLegItem,    -10,   32,     150,    80,     0),
            (self.lowerLeftLegItem,     30,    0,      70,    10,     0),
            (self.torsoItem,             0,    0,       5,   -20,     0),
        )

        animation _ QParallelAnimationGroup(self)
        for item, pos_x, pos_y, start_rot, end_rot, scale in settings: 
            item.setPos(pos_x, pos_y)

            rot_animation _ QPropertyAnimation(item, b'rotation')
            rot_animation.setStartValue(start_rot)
            rot_animation.setEndValue(end_rot)
            rot_animation.setEasingCurve(QEasingCurve.SineCurve)
            rot_animation.setDuration(2000)
            animation.addAnimation(rot_animation)

            if scale > 0:
                scale_animation _ QPropertyAnimation(item, b'scale')
                scale_animation.setEndValue(scale)
                scale_animation.setEasingCurve(QEasingCurve.SineCurve)
                scale_animation.setDuration(2000)
                animation.addAnimation(scale_animation)

        animation.setLoopCount(-1)
        animation.start()

    ___ boundingRect(self):
        return QRectF()

    ___ paint(self, painter, option, widget_None):
        pass


class GraphicsView(QGraphicsView):

    ___ resizeEvent(self, e):
        pass


if __name__== '__main__':

    ______ sys
    ______ math

    app _ ?A..(sys.argv)

    qsrand(QTime(0, 0, 0).secsTo(QTime.currentTime()))

    scene _ QGraphicsScene(-200, -200, 400, 400)

    for i in range(10):
        item _ ColorItem()
        angle _ i*6.28 / 10.0
        item.setPos(math.sin(angle)*150, math.cos(angle)*150)
        scene.addItem(item)

    robot _ Robot()
    robot.setTransform(QTransform.fromScale(1.2, 1.2), True)
    robot.setPos(0, -20)
    scene.addItem(robot)

    view _ GraphicsView(scene)
    view.setRenderHint(QPainter.Antialiasing)
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    view.setBackgroundBrush(QColor(230, 200, 167))
    view.setWindowTitle("Drag and Drop Robot")
    view.s..

    sys.exit(app.exec_())
