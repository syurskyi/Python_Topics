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

____ ?.?C.. ______ (pyqtProperty, pyqtSignal, QDataStream, QDateTime,
        QEvent, QEventTransition, QFile, QIODevice, QParallelAnimationGroup,
        QPointF, QPropertyAnimation, qrand, QRectF, QSignalTransition, qsrand,
        QState, QStateMachine, __, QTimer)
____ ?.?G.. ______ ?C.., QPen, QPainter, QPainterPath, QPixmap
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsObject,
        QGraphicsScene, QGraphicsTextItem, QGraphicsView)

______ stickman_rc


c_ Node(QGraphicsObject):
    positionChanged _ pyqtSignal()

    ___ __init__  pos, parent_None):
        super(Node, self).__init__(parent)

        self.m_dragging _ False

        self.setPos(pos)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)

    ___ boundingRect(self):
        r_ QRectF(-6.0, -6.0, 12.0, 12.0)

    ___ paint  painter, option, widget):
        painter.setPen(__.white)
        painter.drawEllipse(QPointF(0.0, 0.0), 5.0, 5.0)

    ___ itemChange  change, value):
        __ change == QGraphicsItem.ItemPositionChange:
            self.positionChanged.emit()

        r_ super(Node, self).itemChange(change, value)

    ___ mousePressEvent  event):
        self.m_dragging _ True

    ___ mouseMoveEvent  event):
        __ self.m_dragging:
            self.setPos(self.mapToParent(event.pos()))

    ___ mouseReleaseEvent  event):
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


c_ StickMan(QGraphicsObject):
    ___ __init__(self):
        super(StickMan, self).__init__()

        self.m_sticks _ True
        self.m_isDead _ False
        self.m_pixmap _ QPixmap('images/head.png')
        self.m_penColor _ ?C..(__.white)
        self.m_fillColor _ ?C..(__.black)

        # Set up start position of limbs.
        self.m_nodes _   # list
        for x, y in Coords:
            node _ Node(QPointF(x, y), self)
            node.positionChanged.c..(self.childPositionChanged)
            self.m_nodes.ap..(node)

        self.m_perfectBoneLengths _   # list
        for n1, n2 in Bones:
            node1 _ self.m_nodes[n1]
            node2 _ self.m_nodes[n2]

            dist _ node1.pos() - node2.pos()
            self.m_perfectBoneLengths.ap..(math.hypot(dist.x(), dist.y()))

        self.startTimer(10)

    ___ childPositionChanged(self):
        self.prepareGeometryChange()

    ___ setDrawSticks  on):
        self.m_sticks _ on

        for node in self.m_nodes:
            node.setVisible(on)

    ___ drawSticks(self):
        r_ self.m_sticks

    ___ boundingRect(self):
        # Account for head radius of 50.0 plus pen which is 5.0.
        r_ self.childrenBoundingRect().adjusted(-55.0, -55.0, 55.0, 55.0)

    ___ nodeCount(self):
        r_ le.(self.m_nodes)

    ___ node  idx):
        __ idx >_ 0 and idx < le.(self.m_nodes):
            r_ self.m_nodes[idx]

        r_ N..

    ___ timerEvent  e):
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
            __ p.x() > threshold and p.y() > threshold:
                pos1 -_ p
                pos2 +_ p

                node1.setPos(pos1)
                node2.setPos(pos2)

    ___ posFor  idx):
        r_ self.m_nodes[idx].pos()

    @pyqtProperty(?C..)
    ___ penColor(self):
        r_ ?C..(self.m_penColor)

    @penColor.setter
    ___ penColor  color):
        self.m_penColor _ ?C..(color)

    @pyqtProperty(?C..)
    ___ fillColor(self):
        r_ ?C..(self.m_fillColor)

    @fillColor.setter
    ___ fillColor  color):
        self.m_fillColor _ ?C..(color)

    @pyqtProperty(bool)
    ___ isDead(self):
        r_ self.m_isDead

    @isDead.setter
    ___ isDead  isDead):
        self.m_isDead _ isDead

    ___ paint  painter, option, widget):
        self.stabilize()

        __ self.m_sticks:
            painter.setPen(__.white)

            for n1, n2 in Bones:
                node1 _ self.m_nodes[n1]
                node2 _ self.m_nodes[n2]

                painter.drawLine(node1.pos(), node2.pos())
        ____
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

            painter.setPen(QPen(self.m_penColor, 5.0, __.SolidLine, __.RoundCap))
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
            painter.setPen(QPen(self.m_penColor, 2.5, __.SolidLine, __.RoundCap))

            # Eyes.
            __ self.m_isDead:
                painter.drawLine(-30.0, -30.0, -20.0, -20.0)
                painter.drawLine(-20.0, -30.0, -30.0, -20.0)

                painter.drawLine(20.0, -30.0, 30.0, -20.0)
                painter.drawLine(30.0, -30.0, 20.0, -20.0)
            ____
                painter.drawChord(QRectF(-30.0, -30.0, 25.0, 70.0), 30.0 * 16, 120.0 * 16)
                painter.drawChord(QRectF(5.0, -30.0, 25.0, 70.0), 30.0 * 16, 120.0 * 16)

            # Mouth.
            __ self.m_isDead:
                painter.drawLine(-28.0, 2.0, 29.0, 2.0)
            ____
                painter.setBrush(?C..(128, 0, 64 ))
                painter.drawChord(QRectF(-28.0, 2.0 - 55.0 / 2.0, 57.0, 55.0), 0.0, -180.0 * 16)

            # Pupils.
            __ no. self.m_isDead:
                painter.setPen(QPen(self.m_fillColor, 1.0, __.SolidLine, __.RoundCap))
                painter.setBrush(self.m_fillColor)
                painter.drawEllipse(QPointF(-12.0, -25.0), 5.0, 5.0)
                painter.drawEllipse(QPointF(22.0, -25.0), 5.0, 5.0)


c_ GraphicsView(QGraphicsView):
    keyPressed _ pyqtSignal(int)

    ___ keyPressEvent  e):
        __ e.key() == __.Key_Escape:
            self.close()

        self.keyPressed.emit(__.Key(e.key()))


c_ Frame(object):
    ___ __init__(self):
        self.m_nodePositions _   # list

    ___ nodeCount(self):
        r_ le.(self.m_nodePositions)

    ___ setNodeCount  nodeCount):
        w__ nodeCount > le.(self.m_nodePositions):
            self.m_nodePositions.ap..(QPointF())

        w__ nodeCount < le.(self.m_nodePositions):
            self.m_nodePositions.p.. )

    ___ nodePos  idx):
        r_ QPointF(self.m_nodePositions[idx])

    ___ setNodePos  idx, pos):
        self.m_nodePositions[idx] _ QPointF(pos)


c_ Animation(object):
    ___ __init__(self):
        self.m_currentFrame _ 0
        self.m_frames _ [Frame()]
        self.m_name _ ''

    ___ setTotalFrames  totalFrames):
        w__ le.(self.m_frames) < totalFrames:
            self.m_frames.ap..(Frame())

        w__ totalFrames < le.(self.m_frames):
            self.m_frames.p.. )

    ___ totalFrames(self):
        r_ le.(self.m_frames)

    ___ setCurrentFrame  currentFrame):
        self.m_currentFrame _ max(min(currentFrame, self.totalFrames() - 1), 0)

    ___ currentFrame(self):
        r_ self.m_currentFrame

    ___ setNodeCount  nodeCount):
        frame _ self.m_frames[self.m_currentFrame]
        frame.setNodeCount(nodeCount)

    ___ nodeCount(self):
        frame _ self.m_frames[self.m_currentFrame]
        r_ frame.nodeCount()

    ___ setNodePos  idx, pos):
        frame _ self.m_frames[self.m_currentFrame]
        frame.setNodePos(idx, pos)

    ___ nodePos  idx):
        frame _ self.m_frames[self.m_currentFrame]
        r_ frame.nodePos(idx)

    ___ name(self):
        r_ self.m_name

    ___ setName  name):
        self.m_name _ name

    ___ save  device):
        stream _ QDataStream(device)
        stream.writeQString(self.m_name)
        stream.writeInt(le.(self.m_frames))

        for frame in self.m_frames:
            stream.writeInt(frame.nodeCount())

            for i in range(frame.nodeCount()):
                stream << frame.nodePos(i)

    ___ load  device):
        self.m_frames _   # list

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

            self.m_frames.ap..(frame)


c_ KeyPressTransition(QSignalTransition):
    ___ __init__  receiver, key, target_None):
        super(KeyPressTransition, self).__init__(receiver.keyPressed)

        self.m_key _ key

        __ target __ no. N..:
            self.setTargetState(target)

    ___ eventTest  e):
        __ super(KeyPressTransition, self).eventTest(e):
            key _ e.arguments()[0]
            r_ key == self.m_key

        r_ False


c_ LightningStrikesTransition(QEventTransition):
    ___ __init__  target):
        super(LightningStrikesTransition, self).__init__()

        self.setEventSource(self)
        self.setEventType(QEvent.Timer)
        self.setTargetState(target)
        qsrand(QDateTime.currentDateTime().toTime_t())
        self.startTimer(1000)

    ___ eventTest  e):
        r_ (super(LightningStrikesTransition, self).eventTest(e) and
                (qrand() % 50) == 0)


c_ LifeCycle(object):
    ___ __init__  stickMan, keyReceiver):
        self.m_stickMan _ stickMan
        self.m_keyReceiver _ keyReceiver

        # Create animation group to be used for all transitions.
        self.m_animationGroup _ QParallelAnimationGroup()
        stickManNodeCount _ self.m_stickMan.nodeCount()
        self._pas _   # list
        for i in range(stickManNodeCount):
            pa _ QPropertyAnimation(self.m_stickMan.node(i), b'pos')
            self._pas.ap..(pa)
            self.m_animationGroup.addAnimation(pa)

        # Set up intial state graph.
        self.m_machine _ QStateMachine()
        self.m_machine.addDefaultAnimation(self.m_animationGroup)

        self.m_alive _ QState(self.m_machine)
        self.m_alive.setObjectName('alive')

        # Make it blink when lightning strikes before entering dead animation.
        lightningBlink _ QState(self.m_machine)
        lightningBlink.assignProperty(self.m_stickMan.scene(),
                'backgroundBrush', __.white)
        lightningBlink.assignProperty(self.m_stickMan, 'penColor', __.black)
        lightningBlink.assignProperty(self.m_stickMan, 'fillColor', __.white)
        lightningBlink.assignProperty(self.m_stickMan, 'isDead', True)

        timer _ QTimer(lightningBlink)
        timer.setSingleShot(True)
        timer.setInterval(100)
        lightningBlink.entered.c..(timer.start)
        lightningBlink.exited.c..(timer.stop)

        self.m_dead _ QState(self.m_machine)
        self.m_dead.assignProperty(self.m_stickMan.scene(), 'backgroundBrush',
                __.black)
        self.m_dead.assignProperty(self.m_stickMan, 'penColor', __.white)
        self.m_dead.assignProperty(self.m_stickMan, 'fillColor', __.black)
        self.m_dead.setObjectName('dead')

        # Idle state (sets no properties).
        self.m_idle _ QState(self.m_alive)
        self.m_idle.setObjectName('idle')

        self.m_alive.setInitialState(self.m_idle)

        # Lightning strikes at random.
        self.m_alive.addTransition(LightningStrikesTransition(lightningBlink))
        lightningBlink.addTransition(timer.timeout, self.m_dead)

        self.m_machine.setInitialState(self.m_alive)

    ___ setDeathAnimation  fileName):
        deathAnimation _ self.makeState(self.m_dead, fileName)
        self.m_dead.setInitialState(deathAnimation)

    ___ start(self):
        self.m_machine.start()

    ___ addActivity  fileName, key):
        state _ self.makeState(self.m_alive, fileName)
        self.m_alive.addTransition(KeyPressTransition(self.m_keyReceiver, key, state))

    ___ makeState  parentState, animationFileName):
        topLevel _ QState(parentState)

        animation _ Animation()

        file _ QFile(animationFileName)
        __ file.o..(QIODevice.ReadOnly):
            animation.load(file)

        frameCount _ animation.totalFrames()
        previousState _ N..
        for i in range(frameCount):
            animation.setCurrentFrame(i)

            frameState _ QState(topLevel)
            nodeCount _ animation.nodeCount()
            for j in range(nodeCount):
                frameState.assignProperty(self.m_stickMan.node(j), 'pos',
                        animation.nodePos(j))

            frameState.setObjectName('frame %d' % i)

            __ previousState __ N..:
                topLevel.setInitialState(frameState)
            ____
                previousState.addTransition(previousState.propertiesAssigned,
                        frameState)

            previousState _ frameState

        previousState.addTransition(previousState.propertiesAssigned,
                topLevel.initialState())

        r_ topLevel


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)

    stickMan _ StickMan()
    stickMan.setDrawSticks F..

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
    scene.setBackgroundBrush(__.black)

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

    cycle.addActivity(':/animations/jumping', __.Key_J)
    cycle.addActivity(':/animations/dancing', __.Key_D)
    cycle.addActivity(':/animations/chilling', __.Key_C)
    cycle.start()

    ___.exit(app.exec_())
