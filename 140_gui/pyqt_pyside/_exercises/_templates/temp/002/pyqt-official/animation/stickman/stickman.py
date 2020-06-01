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

____ ?.QtCore ______ (pyqtProperty, pyqtSignal, QDataStream, QDateTime,
        QEvent, QEventTransition, QFile, QIODevice, QParallelAnimationGroup,
        QPointF, QPropertyAnimation, qrand, QRectF, QSignalTransition, qsrand,
        QState, QStateMachine, Qt, QTimer)
____ ?.QtGui ______ QColor, QPen, QPainter, QPainterPath, QPixmap
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsObject,
        QGraphicsScene, QGraphicsTextItem, QGraphicsView)

______ stickman_rc


class Node(QGraphicsObject):
    positionChanged _ pyqtSignal()

    ___ __init__(self, pos, parent_None):
        super(Node, self).__init__(parent)

        self.m_dragging _ False

        self.setPos(pos)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)

    ___ boundingRect(self):
        return QRectF(-6.0, -6.0, 12.0, 12.0)

    ___ paint(self, painter, option, widget):
        painter.setPen(Qt.white)
        painter.drawEllipse(QPointF(0.0, 0.0), 5.0, 5.0)

    ___ itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.positionChanged.emit()

        return super(Node, self).itemChange(change, value)

    ___ mousePressEvent(self, event):
        self.m_dragging _ True

    ___ mouseMoveEvent(self, event):
        if self.m_dragging:
            self.setPos(self.mapToParent(event.pos()))

    ___ mouseReleaseEvent(self, event):
        self.m_dragging _ False


Coords _ (
    # Head: 0
    (0.0, -150.0),

    # Body pentagon, top->bottom, left->right: 1 - 5
    (0.0, -100.0),
    (-50.0, -50.0),
    (50.0, -50.0),
    (-25.0, 50.0),
    (25.0, 50.0),

    # Right arm: 6 - 7
    (-100.0, 0.0),
    (-125.0, 50.0),

    # Left arm: 8 - 9
    (100.0, 0.0),
    (125.0, 50.0),

    # Lower body: 10 - 11
    (-35.0, 75.0),
    (35.0, 75.0),

    # Right leg: 12 - 13
    (-25.0, 200.0),
    (-30.0, 300.0),

    # Left leg: 14 - 15
    (25.0, 200.0),
    (30.0, 300.0))


Bones _ (
    # Neck.
    (0, 1),

    # Body.
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 3),
    (2, 4),
    (2, 5),
    (3, 4),
    (3, 5),
    (4, 5),

    # Right arm.
    (2, 6),
    (6, 7),

    # Left arm.
    (3, 8),
    (8, 9),

    # Lower body.
    (4, 10),
    (4, 11),
    (5, 10),
    (5, 11),
    (10, 11),

    # Right leg.
    (10, 12),
    (12, 13),

    # Left leg.
    (11, 14),
    (14, 15))


class StickMan(QGraphicsObject):
    ___ __init__(self):
        super(StickMan, self).__init__()

        self.m_sticks _ True
        self.m_isDead _ False
        self.m_pixmap _ QPixmap('images/head.png')
        self.m_penColor _ QColor(Qt.white)
        self.m_fillColor _ QColor(Qt.black)

        # Set up start position of limbs.
        self.m_nodes _ []
        for x, y in Coords:
            node _ Node(QPointF(x, y), self)
            node.positionChanged.c..(self.childPositionChanged)
            self.m_nodes.append(node)

        self.m_perfectBoneLengths _ []
        for n1, n2 in Bones:
            node1 _ self.m_nodes[n1]
            node2 _ self.m_nodes[n2]

            dist _ node1.pos() - node2.pos()
            self.m_perfectBoneLengths.append(math.hypot(dist.x(), dist.y()))

        self.startTimer(10)

    ___ childPositionChanged(self):
        self.prepareGeometryChange()

    ___ setDrawSticks(self, on):
        self.m_sticks _ on

        for node in self.m_nodes:
            node.setVisible(on)

    ___ drawSticks(self):
        return self.m_sticks

    ___ boundingRect(self):
        # Account for head radius of 50.0 plus pen which is 5.0.
        return self.childrenBoundingRect().adjusted(-55.0, -55.0, 55.0, 55.0)

    ___ nodeCount(self):
        return len(self.m_nodes)

    ___ node(self, idx):
        if idx >_ 0 and idx < len(self.m_nodes):
            return self.m_nodes[idx]

        return None

    ___ timerEvent(self, e):
        self.update()

    ___ stabilize(self):
        threshold _ 0.001

        for i, (n1, n2) in enumerate(Bones):
            node1 _ self.m_nodes[n1]
            node2 _ self.m_nodes[n2]

            pos1 _ node1.pos()
            pos2 _ node2.pos()

            dist _ pos1 - pos2
            length _ math.hypot(dist.x(), dist.y())
            diff _ (length - self.m_perfectBoneLengths[i]) / length

            p _ dist * (0.5 * diff)
            if p.x() > threshold and p.y() > threshold:
                pos1 -_ p
                pos2 +_ p

                node1.setPos(pos1)
                node2.setPos(pos2)

    ___ posFor(self, idx):
        return self.m_nodes[idx].pos()

    @pyqtProperty(QColor)
    ___ penColor(self):
        return QColor(self.m_penColor)

    @penColor.setter
    ___ penColor(self, color):
        self.m_penColor _ QColor(color)

    @pyqtProperty(QColor)
    ___ fillColor(self):
        return QColor(self.m_fillColor)

    @fillColor.setter
    ___ fillColor(self, color):
        self.m_fillColor _ QColor(color)

    @pyqtProperty(bool)
    ___ isDead(self):
        return self.m_isDead

    @isDead.setter
    ___ isDead(self, isDead):
        self.m_isDead _ isDead

    ___ paint(self, painter, option, widget):
        self.stabilize()

        if self.m_sticks:
            painter.setPen(Qt.white)

            for n1, n2 in Bones:
                node1 _ self.m_nodes[n1]
                node2 _ self.m_nodes[n2]

                painter.drawLine(node1.pos(), node2.pos())
        else:
            # First bone is neck and will be used for head.

            path _ QPainterPath()
            path.moveTo(self.posFor(0))
            path.lineTo(self.posFor(1))

            # Right arm.
            path.lineTo(self.posFor(2))
            path.lineTo(self.posFor(6))
            path.lineTo(self.posFor(7))

            # Left arm.
            path.moveTo(self.posFor(3))
            path.lineTo(self.posFor(8))
            path.lineTo(self.posFor(9))

            # Body.
            path.moveTo(self.posFor(2))
            path.lineTo(self.posFor(4))
            path.lineTo(self.posFor(10))
            path.lineTo(self.posFor(11))
            path.lineTo(self.posFor(5))
            path.lineTo(self.posFor(3))
            path.lineTo(self.posFor(1))

            # Right leg.
            path.moveTo(self.posFor(10))
            path.lineTo(self.posFor(12))
            path.lineTo(self.posFor(13))

            # Left leg.
            path.moveTo(self.posFor(11))
            path.lineTo(self.posFor(14))
            path.lineTo(self.posFor(15))

            painter.setPen(QPen(self.m_penColor, 5.0, Qt.SolidLine, Qt.RoundCap))
            painter.drawPath(path)

            n1, n2 _ Bones[0]
            node1 _ self.m_nodes[n1]
            node2 _ self.m_nodes[n2]

            dist _ node2.pos() - node1.pos()

            sinAngle _ dist.x() / math.hypot(dist.x(), dist.y())
            angle _ math.degrees(math.asin(sinAngle))

            headPos _ node1.pos()
            painter.translate(headPos)
            painter.rotate(-angle)

            painter.setBrush(self.m_fillColor)
            painter.drawEllipse(QPointF(0, 0), 50.0, 50.0)

            painter.setBrush(self.m_penColor)
            painter.setPen(QPen(self.m_penColor, 2.5, Qt.SolidLine, Qt.RoundCap))

            # Eyes.
            if self.m_isDead:
                painter.drawLine(-30.0, -30.0, -20.0, -20.0)
                painter.drawLine(-20.0, -30.0, -30.0, -20.0)

                painter.drawLine(20.0, -30.0, 30.0, -20.0)
                painter.drawLine(30.0, -30.0, 20.0, -20.0)
            else:
                painter.drawChord(QRectF(-30.0, -30.0, 25.0, 70.0), 30.0 * 16, 120.0 * 16)
                painter.drawChord(QRectF(5.0, -30.0, 25.0, 70.0), 30.0 * 16, 120.0 * 16)

            # Mouth.
            if self.m_isDead:
                painter.drawLine(-28.0, 2.0, 29.0, 2.0)
            else:
                painter.setBrush(QColor(128, 0, 64 ))
                painter.drawChord(QRectF(-28.0, 2.0 - 55.0 / 2.0, 57.0, 55.0), 0.0, -180.0 * 16)

            # Pupils.
            if not self.m_isDead:
                painter.setPen(QPen(self.m_fillColor, 1.0, Qt.SolidLine, Qt.RoundCap))
                painter.setBrush(self.m_fillColor)
                painter.drawEllipse(QPointF(-12.0, -25.0), 5.0, 5.0)
                painter.drawEllipse(QPointF(22.0, -25.0), 5.0, 5.0)


class GraphicsView(QGraphicsView):
    keyPressed _ pyqtSignal(int)

    ___ keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

        self.keyPressed.emit(Qt.Key(e.key()))


class Frame(object):
    ___ __init__(self):
        self.m_nodePositions _ []

    ___ nodeCount(self):
        return len(self.m_nodePositions)

    ___ setNodeCount(self, nodeCount):
        while nodeCount > len(self.m_nodePositions):
            self.m_nodePositions.append(QPointF())

        while nodeCount < len(self.m_nodePositions):
            self.m_nodePositions.pop()

    ___ nodePos(self, idx):
        return QPointF(self.m_nodePositions[idx])

    ___ setNodePos(self, idx, pos):
        self.m_nodePositions[idx] _ QPointF(pos)


class Animation(object):
    ___ __init__(self):
        self.m_currentFrame _ 0
        self.m_frames _ [Frame()]
        self.m_name _ ''

    ___ setTotalFrames(self, totalFrames):
        while len(self.m_frames) < totalFrames:
            self.m_frames.append(Frame())

        while totalFrames < len(self.m_frames):
            self.m_frames.pop()

    ___ totalFrames(self):
        return len(self.m_frames)

    ___ setCurrentFrame(self, currentFrame):
        self.m_currentFrame _ max(min(currentFrame, self.totalFrames() - 1), 0)

    ___ currentFrame(self):
        return self.m_currentFrame

    ___ setNodeCount(self, nodeCount):
        frame _ self.m_frames[self.m_currentFrame]
        frame.setNodeCount(nodeCount)

    ___ nodeCount(self):
        frame _ self.m_frames[self.m_currentFrame]
        return frame.nodeCount()

    ___ setNodePos(self, idx, pos):
        frame _ self.m_frames[self.m_currentFrame]
        frame.setNodePos(idx, pos)

    ___ nodePos(self, idx):
        frame _ self.m_frames[self.m_currentFrame]
        return frame.nodePos(idx)

    ___ name(self):
        return self.m_name

    ___ setName(self, name):
        self.m_name _ name

    ___ save(self, device):
        stream _ QDataStream(device)
        stream.writeQString(self.m_name)
        stream.writeInt(len(self.m_frames))

        for frame in self.m_frames:
            stream.writeInt(frame.nodeCount())

            for i in range(frame.nodeCount()):
                stream << frame.nodePos(i)

    ___ load(self, device):
        self.m_frames _ []

        stream _ QDataStream(device)
        self.m_name _ stream.readQString()
        frameCount _ stream.readInt()

        for i in range(frameCount):
            nodeCount _ stream.readInt()

            frame _ Frame()
            frame.setNodeCount(nodeCount)

            for j in range(nodeCount):
                pos _ QPointF()
                stream >> pos

                frame.setNodePos(j, pos)

            self.m_frames.append(frame)


class KeyPressTransition(QSignalTransition):
    ___ __init__(self, receiver, key, target_None):
        super(KeyPressTransition, self).__init__(receiver.keyPressed)

        self.m_key _ key

        if target is not None:
            self.setTargetState(target)

    ___ eventTest(self, e):
        if super(KeyPressTransition, self).eventTest(e):
            key _ e.arguments()[0]
            return key == self.m_key

        return False


class LightningStrikesTransition(QEventTransition):
    ___ __init__(self, target):
        super(LightningStrikesTransition, self).__init__()

        self.setEventSource(self)
        self.setEventType(QEvent.Timer)
        self.setTargetState(target)
        qsrand(QDateTime.currentDateTime().toTime_t())
        self.startTimer(1000)

    ___ eventTest(self, e):
        return (super(LightningStrikesTransition, self).eventTest(e) and
                (qrand() % 50) == 0)


class LifeCycle(object):
    ___ __init__(self, stickMan, keyReceiver):
        self.m_stickMan _ stickMan
        self.m_keyReceiver _ keyReceiver

        # Create animation group to be used for all transitions.
        self.m_animationGroup _ QParallelAnimationGroup()
        stickManNodeCount _ self.m_stickMan.nodeCount()
        self._pas _ []
        for i in range(stickManNodeCount):
            pa _ QPropertyAnimation(self.m_stickMan.node(i), b'pos')
            self._pas.append(pa)
            self.m_animationGroup.addAnimation(pa)

        # Set up intial state graph.
        self.m_machine _ QStateMachine()
        self.m_machine.addDefaultAnimation(self.m_animationGroup)

        self.m_alive _ QState(self.m_machine)
        self.m_alive.setObjectName('alive')

        # Make it blink when lightning strikes before entering dead animation.
        lightningBlink _ QState(self.m_machine)
        lightningBlink.assignProperty(self.m_stickMan.scene(),
                'backgroundBrush', Qt.white)
        lightningBlink.assignProperty(self.m_stickMan, 'penColor', Qt.black)
        lightningBlink.assignProperty(self.m_stickMan, 'fillColor', Qt.white)
        lightningBlink.assignProperty(self.m_stickMan, 'isDead', True)

        timer _ QTimer(lightningBlink)
        timer.setSingleShot(True)
        timer.setInterval(100)
        lightningBlink.entered.c..(timer.start)
        lightningBlink.exited.c..(timer.stop)

        self.m_dead _ QState(self.m_machine)
        self.m_dead.assignProperty(self.m_stickMan.scene(), 'backgroundBrush',
                Qt.black)
        self.m_dead.assignProperty(self.m_stickMan, 'penColor', Qt.white)
        self.m_dead.assignProperty(self.m_stickMan, 'fillColor', Qt.black)
        self.m_dead.setObjectName('dead')

        # Idle state (sets no properties).
        self.m_idle _ QState(self.m_alive)
        self.m_idle.setObjectName('idle')

        self.m_alive.setInitialState(self.m_idle)

        # Lightning strikes at random.
        self.m_alive.addTransition(LightningStrikesTransition(lightningBlink))
        lightningBlink.addTransition(timer.timeout, self.m_dead)

        self.m_machine.setInitialState(self.m_alive)

    ___ setDeathAnimation(self, fileName):
        deathAnimation _ self.makeState(self.m_dead, fileName)
        self.m_dead.setInitialState(deathAnimation)

    ___ start(self):
        self.m_machine.start()

    ___ addActivity(self, fileName, key):
        state _ self.makeState(self.m_alive, fileName)
        self.m_alive.addTransition(KeyPressTransition(self.m_keyReceiver, key, state))

    ___ makeState(self, parentState, animationFileName):
        topLevel _ QState(parentState)

        animation _ Animation()

        file _ QFile(animationFileName)
        if file.open(QIODevice.ReadOnly):
            animation.load(file)

        frameCount _ animation.totalFrames()
        previousState _ None
        for i in range(frameCount):
            animation.setCurrentFrame(i)

            frameState _ QState(topLevel)
            nodeCount _ animation.nodeCount()
            for j in range(nodeCount):
                frameState.assignProperty(self.m_stickMan.node(j), 'pos',
                        animation.nodePos(j))

            frameState.setObjectName('frame %d' % i)

            if previousState is None:
                topLevel.setInitialState(frameState)
            else:
                previousState.addTransition(previousState.propertiesAssigned,
                        frameState)

            previousState _ frameState

        previousState.addTransition(previousState.propertiesAssigned,
                topLevel.initialState())

        return topLevel


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    stickMan _ StickMan()
    stickMan.setDrawSticks(False)

    textItem _ QGraphicsTextItem()
    textItem.setHtml("<font color=\"white\"><b>Stickman</b>"
        "<p>"
        "Tell the stickman what to do!"
        "</p>"
        "<p><i>"
        "<li>Press <font color=\"purple\">J</font> to make the stickman jump.</li>"
        "<li>Press <font color=\"purple\">D</font> to make the stickman dance.</li>"
        "<li>Press <font color=\"purple\">C</font> to make him chill out.</li>"
        "<li>When you are done, press <font color=\"purple\">Escape</font>.</li>"
        "</i></p>"
        "<p>If he is unlucky, the stickman will get struck by lightning, and never jump, dance or chill out again."
        "</p></font>")

    w _ textItem.boundingRect().width()
    stickManBoundingRect _ stickMan.mapToScene(stickMan.boundingRect()).boundingRect()
    textItem.setPos(-w / 2.0, stickManBoundingRect.bottom() + 25.0)

    scene _ QGraphicsScene()
    scene.addItem(stickMan)
    scene.addItem(textItem)
    scene.setBackgroundBrush(Qt.black)

    view _ GraphicsView()
    view.setRenderHints(QPainter.Antialiasing)
    view.setTransformationAnchor(QGraphicsView.NoAnchor)
    view.setScene(scene)
    view.s..
    view.setFocus()

    # Make enough room in the scene for stickman to jump and die.
    sceneRect _ scene.sceneRect()
    view.resize(sceneRect.width() + 100, sceneRect.height() + 100)
    view.setSceneRect(sceneRect)

    cycle _ LifeCycle(stickMan, view)
    cycle.setDeathAnimation(':/animations/dead')

    cycle.addActivity(':/animations/jumping', Qt.Key_J)
    cycle.addActivity(':/animations/dancing', Qt.Key_D)
    cycle.addActivity(':/animations/chilling', Qt.Key_C)
    cycle.start()

    sys.exit(app.exec_())
