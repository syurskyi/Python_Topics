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


____ ?.?C.. ______ (QPointF, ?PA.., QRect, QRectF,
        QSequentialAnimationGroup, QSizeF, QState, QStateMachine, __)
____ ?.?G.. ______ ?P..
____ ?.?W.. ______ (?A.., QGraphicsLinearLayout,
        QGraphicsObject, QGraphicsProxyWidget, QGraphicsScene, QGraphicsView,
        QGraphicsWidget, ?GB.., ?PB.., QRadioButton, ?TE..,
        ?VBL..)

______ states_rc


c_ Pixmap(QGraphicsObject):
    ___  -   pix):
        s__(Pixmap, self). - ()

        p _ ?P..(pix)

    ___ paint  painter, option, widget):
        painter.drawPixmap(QPointF(), p)

    ___ boundingRect
        r_ QRectF(QPointF(0, 0), QSizeF(p.size()))


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    # Text edit and button.
    edit _ ?TE..()
    edit.sT..("asdf lkjha yuoiqwe asd iuaysd u iasyd uiy "
                 "asdf lkjha yuoiqwe asd iuaysd u iasyd uiy "
                 "asdf lkjha yuoiqwe asd iuaysd u iasyd uiy "
                 "asdf lkjha yuoiqwe asd iuaysd u iasyd uiy!")

    button _ ?PB..()
    buttonProxy _ QGraphicsProxyWidget()
    buttonProxy.setWidget(button)
    editProxy _ QGraphicsProxyWidget()
    editProxy.setWidget(edit)

    box _ ?GB..()
    box.setFlat( st.
    box.setTitle("Options")

    layout2 _ ?VBL..
    box.sL..(layout2)
    layout2.aW..(QRadioButton("Herring"))
    layout2.aW..(QRadioButton("Blue Parrot"))
    layout2.aW..(QRadioButton("Petunias"))
    layout2.addStretch()

    boxProxy _ QGraphicsProxyWidget()
    boxProxy.setWidget(box)

    # Parent widget.
    widget _ QGraphicsWidget()
    layout _ QGraphicsLinearLayout(__.Vertical, widget)
    layout.aI..(editProxy)
    layout.aI..(buttonProxy)
    widget.sL..(layout)

    p1 _ Pixmap(?P..(':/digikam.png'))
    p2 _ Pixmap(?P..(':/akregator.png'))
    p3 _ Pixmap(?P..(':/accessories-dictionary.png'))
    p4 _ Pixmap(?P..(':/k3b.png'))
    p5 _ Pixmap(?P..(':/help-browser.png'))
    p6 _ Pixmap(?P..(':/kchart.png'))

    scene _ QGraphicsScene(0, 0, 400, 300)
    scene.setBackgroundBrush(scene.p...window())
    scene.aI..(widget)
    scene.aI..(boxProxy)
    scene.aI..(p1)
    scene.aI..(p2)
    scene.aI..(p3)
    scene.aI..(p4)
    scene.aI..(p5)
    scene.aI..(p6)

    machine _ QStateMachine()
    state1 _ QState(machine)
    state2 _ QState(machine)
    state3 _ QState(machine)
    machine.setInitialState(state1)

    # State 1.
    state1.assignProperty(button, 'text', "Switch to state 2")
    state1.assignProperty(widget, 'geometry', QRectF(0, 0, 400, 150))
    state1.assignProperty(box, 'geometry', QRect(-200, 150, 200, 150))
    state1.assignProperty(p1, 'pos', QPointF(68, 185))
    state1.assignProperty(p2, 'pos', QPointF(168, 185))
    state1.assignProperty(p3, 'pos', QPointF(268, 185))
    state1.assignProperty(p4, 'pos', QPointF(68 - 150, 48 - 150))
    state1.assignProperty(p5, 'pos', QPointF(168, 48 - 150))
    state1.assignProperty(p6, 'pos', QPointF(268 + 150, 48 - 150))
    state1.assignProperty(p1, 'rotation', 0.0)
    state1.assignProperty(p2, 'rotation', 0.0)
    state1.assignProperty(p3, 'rotation', 0.0)
    state1.assignProperty(p4, 'rotation', -270.0)
    state1.assignProperty(p5, 'rotation', -90.0)
    state1.assignProperty(p6, 'rotation', 270.0)
    state1.assignProperty(boxProxy, 'opacity', 0.0)
    state1.assignProperty(p1, 'opacity', 1.0)
    state1.assignProperty(p2, 'opacity', 1.0)
    state1.assignProperty(p3, 'opacity', 1.0)
    state1.assignProperty(p4, 'opacity', 0.0)
    state1.assignProperty(p5, 'opacity', 0.0)
    state1.assignProperty(p6, 'opacity', 0.0)

    # State 2.
    state2.assignProperty(button, 'text', "Switch to state 3")
    state2.assignProperty(widget, 'geometry', QRectF(200, 150, 200, 150))
    state2.assignProperty(box, 'geometry', QRect(9, 150, 190, 150))
    state2.assignProperty(p1, 'pos', QPointF(68 - 150, 185 + 150))
    state2.assignProperty(p2, 'pos', QPointF(168, 185 + 150))
    state2.assignProperty(p3, 'pos', QPointF(268 + 150, 185 + 150))
    state2.assignProperty(p4, 'pos', QPointF(64, 48))
    state2.assignProperty(p5, 'pos', QPointF(168, 48))
    state2.assignProperty(p6, 'pos', QPointF(268, 48))
    state2.assignProperty(p1, 'rotation', -270.0)
    state2.assignProperty(p2, 'rotation', 90.0)
    state2.assignProperty(p3, 'rotation', 270.0)
    state2.assignProperty(p4, 'rotation', 0.0)
    state2.assignProperty(p5, 'rotation', 0.0)
    state2.assignProperty(p6, 'rotation', 0.0)
    state2.assignProperty(boxProxy, 'opacity', 1.0)
    state2.assignProperty(p1, 'opacity', 0.0)
    state2.assignProperty(p2, 'opacity', 0.0)
    state2.assignProperty(p3, 'opacity', 0.0)
    state2.assignProperty(p4, 'opacity', 1.0)
    state2.assignProperty(p5, 'opacity', 1.0)
    state2.assignProperty(p6, 'opacity', 1.0)

    # State 3.
    state3.assignProperty(button, 'text', "Switch to state 1")
    state3.assignProperty(p1, 'pos', QPointF(0, 5))
    state3.assignProperty(p2, 'pos', QPointF(0, 5 + 64 + 5))
    state3.assignProperty(p3, 'pos', QPointF(5, 5 + (64 + 5) + 64))
    state3.assignProperty(p4, 'pos', QPointF(5 + 64 + 5, 5))
    state3.assignProperty(p5, 'pos', QPointF(5 + 64 + 5, 5 + 64 + 5))
    state3.assignProperty(p6, 'pos', QPointF(5 + 64 + 5, 5 + (64 + 5) + 64))
    state3.assignProperty(widget, 'geometry', QRectF(138, 5, 400 - 138, 200))
    state3.assignProperty(box, 'geometry', QRect(5, 205, 400, 90))
    state3.assignProperty(p1, 'opacity', 1.0)
    state3.assignProperty(p2, 'opacity', 1.0)
    state3.assignProperty(p3, 'opacity', 1.0)
    state3.assignProperty(p4, 'opacity', 1.0)
    state3.assignProperty(p5, 'opacity', 1.0)
    state3.assignProperty(p6, 'opacity', 1.0)

    t1 _ state1.addTransition(button.c__, state2)
    animation1SubGroup _ QSequentialAnimationGroup()
    animation1SubGroup.addPause(250)
    animation1SubGroup.addAnimation(?PA..(box, b'geometry', state1))
    t1.addAnimation(animation1SubGroup)
    t1.addAnimation(?PA..(widget, b'geometry', state1))
    t1.addAnimation(?PA..(p1, b'pos', state1))
    t1.addAnimation(?PA..(p2, b'pos', state1))
    t1.addAnimation(?PA..(p3, b'pos', state1))
    t1.addAnimation(?PA..(p4, b'pos', state1))
    t1.addAnimation(?PA..(p5, b'pos', state1))
    t1.addAnimation(?PA..(p6, b'pos', state1))
    t1.addAnimation(?PA..(p1, b'rotation', state1))
    t1.addAnimation(?PA..(p2, b'rotation', state1))
    t1.addAnimation(?PA..(p3, b'rotation', state1))
    t1.addAnimation(?PA..(p4, b'rotation', state1))
    t1.addAnimation(?PA..(p5, b'rotation', state1))
    t1.addAnimation(?PA..(p6, b'rotation', state1))
    t1.addAnimation(?PA..(p1, b'opacity', state1))
    t1.addAnimation(?PA..(p2, b'opacity', state1))
    t1.addAnimation(?PA..(p3, b'opacity', state1))
    t1.addAnimation(?PA..(p4, b'opacity', state1))
    t1.addAnimation(?PA..(p5, b'opacity', state1))
    t1.addAnimation(?PA..(p6, b'opacity', state1))

    t2 _ state2.addTransition(button.c__, state3)
    t2.addAnimation(?PA..(box, b'geometry', state2))
    t2.addAnimation(?PA..(widget, b'geometry', state2))
    t2.addAnimation(?PA..(p1, b'pos', state2))
    t2.addAnimation(?PA..(p2, b'pos', state2))
    t2.addAnimation(?PA..(p3, b'pos', state2))
    t2.addAnimation(?PA..(p4, b'pos', state2))
    t2.addAnimation(?PA..(p5, b'pos', state2))
    t2.addAnimation(?PA..(p6, b'pos', state2))
    t2.addAnimation(?PA..(p1, b'rotation', state2))
    t2.addAnimation(?PA..(p2, b'rotation', state2))
    t2.addAnimation(?PA..(p3, b'rotation', state2))
    t2.addAnimation(?PA..(p4, b'rotation', state2))
    t2.addAnimation(?PA..(p5, b'rotation', state2))
    t2.addAnimation(?PA..(p6, b'rotation', state2))
    t2.addAnimation(?PA..(p1, b'opacity', state2))
    t2.addAnimation(?PA..(p2, b'opacity', state2))
    t2.addAnimation(?PA..(p3, b'opacity', state2))
    t2.addAnimation(?PA..(p4, b'opacity', state2))
    t2.addAnimation(?PA..(p5, b'opacity', state2))
    t2.addAnimation(?PA..(p6, b'opacity', state2))

    t3 _ state3.addTransition(button.c__, state1)
    t3.addAnimation(?PA..(box, b'geometry', state3))
    t3.addAnimation(?PA..(widget, b'geometry', state3))
    t3.addAnimation(?PA..(p1, b'pos', state3))
    t3.addAnimation(?PA..(p2, b'pos', state3))
    t3.addAnimation(?PA..(p3, b'pos', state3))
    t3.addAnimation(?PA..(p4, b'pos', state3))
    t3.addAnimation(?PA..(p5, b'pos', state3))
    t3.addAnimation(?PA..(p6, b'pos', state3))
    t3.addAnimation(?PA..(p1, b'rotation', state3))
    t3.addAnimation(?PA..(p2, b'rotation', state3))
    t3.addAnimation(?PA..(p3, b'rotation', state3))
    t3.addAnimation(?PA..(p4, b'rotation', state3))
    t3.addAnimation(?PA..(p5, b'rotation', state3))
    t3.addAnimation(?PA..(p6, b'rotation', state3))
    t3.addAnimation(?PA..(p1, b'opacity', state3))
    t3.addAnimation(?PA..(p2, b'opacity', state3))
    t3.addAnimation(?PA..(p3, b'opacity', state3))
    t3.addAnimation(?PA..(p4, b'opacity', state3))
    t3.addAnimation(?PA..(p5, b'opacity', state3))
    t3.addAnimation(?PA..(p6, b'opacity', state3))

    machine.start()

    view _ QGraphicsView(scene)
    view.s..

    ___.e.. ?.e..
