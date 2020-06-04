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


____ ?.?C.. ______ (QAbstractTransition, QEasingCurve, QEvent,
        QParallelAnimationGroup, ?PA.., qrand, QRect,
        QSequentialAnimationGroup, qsrand, QState, QStateMachine, __, ?T..,
        ?T..)
____ ?.?W.. ______ (?A.., QGraphicsScene, QGraphicsView,
        QGraphicsWidget)


c_ StateSwitchEvent(QEvent):
    StateSwitchType _ QEvent.User + 256

    ___  -   rand_0):
        s__(StateSwitchEvent, self). - (StateSwitchEvent.StateSwitchType)

        m_rand _ rand

    ___ rand 
        r_ m_rand


c_ QGraphicsRectWidget(QGraphicsWidget):
    ___ paint  painter, option, widget):
        painter.fillRect(rect(), __.blue)


c_ StateSwitchTransition(QAbstractTransition):
    ___  -   rand):
        s__(StateSwitchTransition, self). - ()

        m_rand _ rand

    ___ eventTest  event):
        r_ (event.type() __ StateSwitchEvent.StateSwitchType and
                event.rand() __ m_rand)

    ___ onTransition  event):
        p..


c_ StateSwitcher(QState):
    ___  -   machine):
        s__(StateSwitcher, self). - (machine)

        m_stateCount _ 0
        m_lastIndex _ 0

    ___ onEntry  event):
        n _ qrand() % m_stateCount + 1
        w__ n __ m_lastIndex:
            n _ qrand() % m_stateCount + 1

        m_lastIndex _ n
        machine().postEvent(StateSwitchEvent(n))

    ___ onExit  event):
        p..

    ___ addState  state, animation):
        m_stateCount +_ 1
        trans _ StateSwitchTransition(m_stateCount)
        trans.setTargetState(state)
        addTransition(trans)
        trans.addAnimation(animation)


___ createGeometryState(w1, rect1, w2, rect2, w3, rect3, w4, rect4, parent):
    result _ QState(parent)

    result.assignProperty(w1, 'geometry', rect1)
    result.assignProperty(w1, 'geometry', rect1)
    result.assignProperty(w2, 'geometry', rect2)
    result.assignProperty(w3, 'geometry', rect3)
    result.assignProperty(w4, 'geometry', rect4)

    r_ result


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    button1 _ QGraphicsRectWidget()
    button2 _ QGraphicsRectWidget()
    button3 _ QGraphicsRectWidget()
    button4 _ QGraphicsRectWidget()
    button2.setZValue(1)
    button3.setZValue(2)
    button4.setZValue(3)

    scene _ QGraphicsScene(0, 0, 300, 300)
    scene.setBackgroundBrush(__.black)
    scene.aI..(button1)
    scene.aI..(button2)
    scene.aI..(button3)
    scene.aI..(button4)

    window _ QGraphicsView(scene)
    window.setFrameStyle(0)
    window.setAlignment(__.AlignLeft | __.AlignTop)
    window.setHorizontalScrollBarPolicy(__.ScrollBarAlwaysOff)
    window.setVerticalScrollBarPolicy(__.ScrollBarAlwaysOff)

    machine _ QStateMachine()

    group _ QState()
    timer _ ?T..
    timer.sI..(1250)
    timer.setSingleShot( st.
    group.entered.c..(timer.start)

    state1 _ createGeometryState(button1, QRect(100, 0, 50, 50), button2,
            QRect(150, 0, 50, 50), button3, QRect(200, 0, 50, 50), button4,
            QRect(250, 0, 50, 50), group)

    state2 _ createGeometryState(button1, QRect(250, 100, 50, 50), button2,
            QRect(250, 150, 50, 50), button3, QRect(250, 200, 50, 50), button4,
            QRect(250, 250, 50, 50), group)

    state3 _ createGeometryState(button1, QRect(150, 250, 50, 50), button2,
            QRect(100, 250, 50, 50), button3, QRect(50, 250, 50, 50), button4,
            QRect(0, 250, 50, 50), group)

    state4 _ createGeometryState(button1, QRect(0, 150, 50, 50), button2,
            QRect(0, 100, 50, 50), button3, QRect(0, 50, 50, 50), button4,
            QRect(0, 0, 50, 50), group)

    state5 _ createGeometryState(button1, QRect(100, 100, 50, 50), button2,
            QRect(150, 100, 50, 50), button3, QRect(100, 150, 50, 50), button4,
            QRect(150, 150, 50, 50), group)

    state6 _ createGeometryState(button1, QRect(50, 50, 50, 50), button2,
            QRect(200, 50, 50, 50), button3, QRect(50, 200, 50, 50), button4,
            QRect(200, 200, 50, 50), group)

    state7 _ createGeometryState(button1, QRect(0, 0, 50, 50), button2,
            QRect(250, 0, 50, 50), button3, QRect(0, 250, 50, 50), button4,
            QRect(250, 250, 50, 50), group)

    group.setInitialState(state1)

    animationGroup _ ?PAG..
    anim _ ?PA..(button4, b'geometry')
    anim.sD..(1000)
    anim.setEasingCurve(QEasingCurve.OutElastic)
    animationGroup.addAnimation(anim)

    subGroup _ QSequentialAnimationGroup(animationGroup)
    subGroup.addPause(100)
    anim _ ?PA..(button3, b'geometry')
    anim.sD..(1000)
    anim.setEasingCurve(QEasingCurve.OutElastic)
    subGroup.addAnimation(anim)

    subGroup _ QSequentialAnimationGroup(animationGroup)
    subGroup.addPause(150)
    anim _ ?PA..(button2, b'geometry')
    anim.sD..(1000)
    anim.setEasingCurve(QEasingCurve.OutElastic)
    subGroup.addAnimation(anim)

    subGroup _ QSequentialAnimationGroup(animationGroup)
    subGroup.addPause(200)
    anim _ ?PA..(button1, b'geometry')
    anim.sD..(1000)
    anim.setEasingCurve(QEasingCurve.OutElastic)
    subGroup.addAnimation(anim)

    stateSwitcher _ StateSwitcher(machine)
    group.addTransition(timer.timeout, stateSwitcher)
    stateSwitcher.addState(state1, animationGroup)
    stateSwitcher.addState(state2, animationGroup)
    stateSwitcher.addState(state3, animationGroup)
    stateSwitcher.addState(state4, animationGroup)
    stateSwitcher.addState(state5, animationGroup)
    stateSwitcher.addState(state6, animationGroup)
    stateSwitcher.addState(state7, animationGroup)

    machine.addState(group)
    machine.setInitialState(group)
    machine.start()

    window.r..(300, 300)
    window.s..

    qsrand(?T..(0, 0, 0).secsTo(?T...currentTime()))

    ___.e.. ?.e..
