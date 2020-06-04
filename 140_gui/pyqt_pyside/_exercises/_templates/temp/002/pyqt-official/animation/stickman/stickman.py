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


______ m__

____ ?.?C.. ______ (pP.., pS.., ?DS.., ?DT__,
        QEvent, QEventTransition, QFile, QIODevice, QParallelAnimationGroup,
        QPointF, ?PA.., qrand, QRectF, QSignalTransition, qsrand,
        QState, QStateMachine, __, ?T..)
____ ?.?G.. ______ ?C.., ?P.., QPainter, QPainterPath, ?P..
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsObject,
        QGraphicsScene, QGraphicsTextItem, QGraphicsView)

______ stickman_rc


c_ Node(QGraphicsObject):
    pC.. _ pS..()

    ___  -   pos, parent_None):
        s__(Node, self). - (parent)

        m_dragging _ F..

        setPos(pos)
        setFlag(QGraphicsItem.ItemSendsGeometryChanges)

    ___ boundingRect
        r_ QRectF(-6.0, -6.0, 12.0, 12.0)

    ___ paint  painter, option, widget):
        painter.sP..(__.white)
        painter.drawEllipse(QPointF(0.0, 0.0), 5.0, 5.0)

    ___ itemChange  change, value):
        __ change __ QGraphicsItem.ItemPositionChange:
            pC...e..()

        r_ s__(Node, self).itemChange(change, value)

    ___ mousePressEvent  event):
        m_dragging _ T..

    ___ mouseMoveEvent  event):
        __ m_dragging:
            setPos(mapToParent(event.pos()))

    ___ mouseReleaseEvent  event):
        m_dragging _ F..


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
    ___  -
        s__(StickMan, self). - ()

        m_sticks _ T..
        m_isDead _ F..
        m_pixmap _ ?P..('images/head.png')
        m_penColor _ ?C..(__.white)
        m_fillColor _ ?C..(__.black)

        # Set up start position of limbs.
        m_nodes _   # list
        ___ x, y __ Coords:
            node _ Node(QPointF(x, y), self)
            node.pC...c..(childPositionChanged)
            m_nodes.ap..(node)

        m_perfectBoneLengths _   # list
        ___ n1, n2 __ Bones:
            node1 _ m_nodes[n1]
            node2 _ m_nodes[n2]

            dist _ node1.pos() - node2.pos()
            m_perfectBoneLengths.ap..(m__.hypot(dist.x(), dist.y()))

        startTimer(10)

    ___ childPositionChanged
        prepareGeometryChange()

    ___ setDrawSticks  on):
        m_sticks _ on

        ___ node __ m_nodes:
            node.setVisible(on)

    ___ drawSticks
        r_ m_sticks

    ___ boundingRect
        # Account for head radius of 50.0 plus pen which is 5.0.
        r_ childrenBoundingRect().adjusted(-55.0, -55.0, 55.0, 55.0)

    ___ nodeCount
        r_ le.(m_nodes)

    ___ node  idx):
        __ idx >_ 0 and idx < le.(m_nodes):
            r_ m_nodes[idx]

        r_ N..

    ___ timerEvent  e):
        update()

    ___ stabilize
        threshold _ 0.001

        ___ i, (n1, n2) __ en..(Bones):
            node1 _ m_nodes[n1]
            node2 _ m_nodes[n2]

            pos1 _ node1.pos()
            pos2 _ node2.pos()

            dist _ pos1 - pos2
            length _ m__.hypot(dist.x(), dist.y())
            diff _ (length - m_perfectBoneLengths[i]) / length

            p _ dist * (0.5 * diff)
            __ p.x() > threshold and p.y() > threshold:
                pos1 -_ p
                pos2 +_ p

                node1.setPos(pos1)
                node2.setPos(pos2)

    ___ posFor  idx):
        r_ m_nodes[idx].pos()

    @pP..(?C..)
    ___ penColor
        r_ ?C..(m_penColor)

    @penColor.setter
    ___ penColor  color):
        m_penColor _ ?C..(color)

    @pP..(?C..)
    ___ fillColor
        r_ ?C..(m_fillColor)

    @fillColor.setter
    ___ fillColor  color):
        m_fillColor _ ?C..(color)

    @pP..(bool)
    ___ isDead
        r_ m_isDead

    @isDead.setter
    ___ isDead  isDead):
        m_isDead _ isDead

    ___ paint  painter, option, widget):
        stabilize()

        __ m_sticks:
            painter.sP..(__.white)

            ___ n1, n2 __ Bones:
                node1 _ m_nodes[n1]
                node2 _ m_nodes[n2]

                painter.drawLine(node1.pos(), node2.pos())
        ____
            # First bone is neck and will be used for head.

            pa__ _ QPainterPath()
            pa__.moveTo(posFor(0))
            pa__.lineTo(posFor(1))

            # Right arm.
            pa__.lineTo(posFor(2))
            pa__.lineTo(posFor(6))
            pa__.lineTo(posFor(7))

            # Left arm.
            pa__.moveTo(posFor(3))
            pa__.lineTo(posFor(8))
            pa__.lineTo(posFor(9))

            # Body.
            pa__.moveTo(posFor(2))
            pa__.lineTo(posFor(4))
            pa__.lineTo(posFor(10))
            pa__.lineTo(posFor(11))
            pa__.lineTo(posFor(5))
            pa__.lineTo(posFor(3))
            pa__.lineTo(posFor(1))

            # Right leg.
            pa__.moveTo(posFor(10))
            pa__.lineTo(posFor(12))
            pa__.lineTo(posFor(13))

            # Left leg.
            pa__.moveTo(posFor(11))
            pa__.lineTo(posFor(14))
            pa__.lineTo(posFor(15))

            painter.sP..(?P..(m_penColor, 5.0, __.SolidLine, __.RoundCap))
            painter.drawPath(pa__)

            n1, n2 _ Bones[0]
            node1 _ m_nodes[n1]
            node2 _ m_nodes[n2]

            dist _ node2.pos() - node1.pos()

            sinAngle _ dist.x() / m__.hypot(dist.x(), dist.y())
            angle _ m__.degrees(m__.asin(sinAngle))

            headPos _ node1.pos()
            painter.translate(headPos)
            painter.rotate(-angle)

            painter.sB..(m_fillColor)
            painter.drawEllipse(QPointF(0, 0), 50.0, 50.0)

            painter.sB..(m_penColor)
            painter.sP..(?P..(m_penColor, 2.5, __.SolidLine, __.RoundCap))

            # Eyes.
            __ m_isDead:
                painter.drawLine(-30.0, -30.0, -20.0, -20.0)
                painter.drawLine(-20.0, -30.0, -30.0, -20.0)

                painter.drawLine(20.0, -30.0, 30.0, -20.0)
                painter.drawLine(30.0, -30.0, 20.0, -20.0)
            ____
                painter.drawChord(QRectF(-30.0, -30.0, 25.0, 70.0), 30.0 * 16, 120.0 * 16)
                painter.drawChord(QRectF(5.0, -30.0, 25.0, 70.0), 30.0 * 16, 120.0 * 16)

            # Mouth.
            __ m_isDead:
                painter.drawLine(-28.0, 2.0, 29.0, 2.0)
            ____
                painter.sB..(?C..(128, 0, 64 ))
                painter.drawChord(QRectF(-28.0, 2.0 - 55.0 / 2.0, 57.0, 55.0), 0.0, -180.0 * 16)

            # Pupils.
            __ no. m_isDead:
                painter.sP..(?P..(m_fillColor, 1.0, __.SolidLine, __.RoundCap))
                painter.sB..(m_fillColor)
                painter.drawEllipse(QPointF(-12.0, -25.0), 5.0, 5.0)
                painter.drawEllipse(QPointF(22.0, -25.0), 5.0, 5.0)


c_ GraphicsView(QGraphicsView):
    keyPressed _ pS..(in.)

    ___ keyPressEvent  e):
        __ e.key() __ __.Key_Escape:
            c..

        keyPressed.e..(__.Key(e.key()))


c_ Frame o..
    ___  -
        m_nodePositions _   # list

    ___ nodeCount
        r_ le.(m_nodePositions)

    ___ setNodeCount  nodeCount):
        w__ nodeCount > le.(m_nodePositions):
            m_nodePositions.ap..(QPointF())

        w__ nodeCount < le.(m_nodePositions):
            m_nodePositions.p.. )

    ___ nodePos  idx):
        r_ QPointF(m_nodePositions[idx])

    ___ setNodePos  idx, pos):
        m_nodePositions[idx] _ QPointF(pos)


c_ Animation o..
    ___  -
        m_currentFrame _ 0
        m_frames _ [Frame()]
        m_name _ ''

    ___ setTotalFrames  totalFrames):
        w__ le.(m_frames) < totalFrames:
            m_frames.ap..(Frame())

        w__ totalFrames < le.(m_frames):
            m_frames.p.. )

    ___ totalFrames
        r_ le.(m_frames)

    ___ setCurrentFrame  currentFrame):
        m_currentFrame _ max(min(currentFrame, totalFrames() - 1), 0)

    ___ currentFrame
        r_ m_currentFrame

    ___ setNodeCount  nodeCount):
        frame _ m_frames[m_currentFrame]
        frame.setNodeCount(nodeCount)

    ___ nodeCount
        frame _ m_frames[m_currentFrame]
        r_ frame.nodeCount()

    ___ setNodePos  idx, pos):
        frame _ m_frames[m_currentFrame]
        frame.setNodePos(idx, pos)

    ___ nodePos  idx):
        frame _ m_frames[m_currentFrame]
        r_ frame.nodePos(idx)

    ___ name
        r_ m_name

    ___ setName  name):
        m_name _ name

    ___ save  device):
        stream _ ?DS..(device)
        stream.writeQString(m_name)
        stream.writeInt(le.(m_frames))

        ___ frame __ m_frames:
            stream.writeInt(frame.nodeCount())

            ___ i __ ra..(frame.nodeCount()):
                stream << frame.nodePos(i)

    ___ load  device):
        m_frames _   # list

        stream _ ?DS..(device)
        m_name _ stream.rQS..
        frameCount _ stream.readInt()

        ___ i __ ra..(frameCount):
            nodeCount _ stream.readInt()

            frame _ Frame()
            frame.setNodeCount(nodeCount)

            ___ j __ ra..(nodeCount):
                pos _ QPointF()
                stream >> pos

                frame.setNodePos(j, pos)

            m_frames.ap..(frame)


c_ KeyPressTransition(QSignalTransition):
    ___  -   receiver, key, target_None):
        s__(KeyPressTransition, self). - (receiver.keyPressed)

        m_key _ key

        __ target __ no. N..:
            setTargetState(target)

    ___ eventTest  e):
        __ s__(KeyPressTransition, self).eventTest(e):
            key _ e.arguments()[0]
            r_ key __ m_key

        r_ F..


c_ LightningStrikesTransition(QEventTransition):
    ___  -   target):
        s__(LightningStrikesTransition, self). - ()

        setEventSource
        setEventType(QEvent.Timer)
        setTargetState(target)
        qsrand(?DT__.cDT.. .toTime_t())
        startTimer(1000)

    ___ eventTest  e):
        r_ (s__(LightningStrikesTransition, self).eventTest(e) and
                (qrand() % 50) __ 0)


c_ LifeCycle o..
    ___  -   stickMan, keyReceiver):
        m_stickMan _ stickMan
        m_keyReceiver _ keyReceiver

        # Create animation group to be used for all transitions.
        m_animationGroup _ ?PAG..
        stickManNodeCount _ m_stickMan.nodeCount()
        _pas _   # list
        ___ i __ ra..(stickManNodeCount):
            pa _ ?PA..(m_stickMan.node(i), b'pos')
            _pas.ap..(pa)
            m_animationGroup.addAnimation(pa)

        # Set up intial state graph.
        m_machine _ QStateMachine()
        m_machine.addDefaultAnimation(m_animationGroup)

        m_alive _ QState(m_machine)
        m_alive.setObjectName('alive')

        # Make it blink when lightning strikes before entering dead animation.
        lightningBlink _ QState(m_machine)
        lightningBlink.assignProperty(m_stickMan.scene(),
                'backgroundBrush', __.white)
        lightningBlink.assignProperty(m_stickMan, 'penColor', __.black)
        lightningBlink.assignProperty(m_stickMan, 'fillColor', __.white)
        lightningBlink.assignProperty(m_stickMan, 'isDead',  st.

        timer _ ?T..(lightningBlink)
        timer.setSingleShot( st.
        timer.sI..(100)
        lightningBlink.entered.c..(timer.start)
        lightningBlink.exited.c..(timer.stop)

        m_dead _ QState(m_machine)
        m_dead.assignProperty(m_stickMan.scene(), 'backgroundBrush',
                __.black)
        m_dead.assignProperty(m_stickMan, 'penColor', __.white)
        m_dead.assignProperty(m_stickMan, 'fillColor', __.black)
        m_dead.setObjectName('dead')

        # Idle state (sets no properties).
        m_idle _ QState(m_alive)
        m_idle.setObjectName('idle')

        m_alive.setInitialState(m_idle)

        # Lightning strikes at random.
        m_alive.addTransition(LightningStrikesTransition(lightningBlink))
        lightningBlink.addTransition(timer.timeout, m_dead)

        m_machine.setInitialState(m_alive)

    ___ setDeathAnimation  fileName):
        deathAnimation _ makeState(m_dead, fileName)
        m_dead.setInitialState(deathAnimation)

    ___ start
        m_machine.start()

    ___ addActivity  fileName, key):
        state _ makeState(m_alive, fileName)
        m_alive.addTransition(KeyPressTransition(m_keyReceiver, key, state))

    ___ makeState  parentState, animationFileName):
        topLevel _ QState(parentState)

        animation _ Animation()

        file _ QFile(animationFileName)
        __ file.o..(QIODevice.ReadOnly):
            animation.load(file)

        frameCount _ animation.totalFrames()
        previousState _ N..
        ___ i __ ra..(frameCount):
            animation.setCurrentFrame(i)

            frameState _ QState(topLevel)
            nodeCount _ animation.nodeCount()
            ___ j __ ra..(nodeCount):
                frameState.assignProperty(m_stickMan.node(j), 'pos',
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


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

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
    scene.aI..(stickMan)
    scene.aI..(textItem)
    scene.setBackgroundBrush(__.black)

    view _ GraphicsView()
    view.setRenderHints(QPainter.Antialiasing)
    view.setTransformationAnchor(QGraphicsView.NoAnchor)
    view.setScene(scene)
    view.s..
    view.setFocus()

    # Make enough room in the scene for stickman to jump and die.
    sceneRect _ scene.sceneRect()
    view.r..(sceneRect.width() + 100, sceneRect.height() + 100)
    view.setSceneRect(sceneRect)

    cycle _ LifeCycle(stickMan, view)
    cycle.setDeathAnimation(':/animations/dead')

    cycle.addActivity(':/animations/jumping', __.Key_J)
    cycle.addActivity(':/animations/dancing', __.Key_D)
    cycle.addActivity(':/animations/chilling', __.Key_C)
    cycle.start()

    ___.e.. ?.e..
