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


____ ?.?C.. ______ (pS.., QPointF, ?PA.., QRect,
        QRectF, QState, QStateMachine, __)
____ ?.?G.. ______ ?P..
____ ?.?W.. ______ (?A.., QGraphicsScene, QGraphicsView,
        QGraphicsWidget)

______ appchooser_rc


c_ Pixmap(QGraphicsWidget):
    c__ _ pS..()

    ___  -   pix, parent_None):
        s__(Pixmap, self). - (parent)

        orig _ ?P..(pix)
        p _ ?P..(pix)

    ___ paint  painter, option, widget):
        painter.drawPixmap(QPointF(), p)

    ___ mousePressEvent  ev):
        c__.e..()

    ___ setGeometry  rect):
        s__(Pixmap, self).setGeometry(rect)

        __ rect.size().width() > orig.size().width
            p _ orig.scaled(rect.size().toSize())
        ____
            p _ ?P..(orig)


___ createStates(objects, selectedRect, parent):
    ___ obj __ objects:
        state _ QState(parent)
        state.assignProperty(obj, 'geometry', selectedRect)
        parent.addTransition(obj.c__, state)


___ createAnimations(objects, machine):
    ___ obj __ objects:
        animation _ ?PA..(obj, b'geometry', obj)
        machine.addDefaultAnimation(animation)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    p1 _ Pixmap(?P..(':/digikam.png'))
    p2 _ Pixmap(?P..(':/akregator.png'))
    p3 _ Pixmap(?P..(':/accessories-dictionary.png'))
    p4 _ Pixmap(?P..(':/k3b.png'))

    p1.setGeometry(QRectF(0.0, 0.0, 64.0, 64.0))
    p2.setGeometry(QRectF(236.0, 0.0, 64.0, 64.0))
    p3.setGeometry(QRectF(236.0, 236.0, 64.0, 64.0))
    p4.setGeometry(QRectF(0.0, 236.0, 64.0, 64.0))

    scene _ QGraphicsScene(0, 0, 300, 300)
    scene.setBackgroundBrush(__.white)
    scene.aI..(p1)
    scene.aI..(p2)
    scene.aI..(p3)
    scene.aI..(p4)

    window _ QGraphicsView(scene)
    window.setFrameStyle(0)
    window.setAlignment(__.AlignLeft | __.AlignTop)
    window.setHorizontalScrollBarPolicy(__.ScrollBarAlwaysOff)
    window.setVerticalScrollBarPolicy(__.ScrollBarAlwaysOff)

    machine _ QStateMachine()
    machine.setGlobalRestorePolicy(QStateMachine.RestoreProperties)

    group _ QState(machine)
    selectedRect _ QRect(86, 86, 128, 128)

    idleState _ QState(group)
    group.setInitialState(idleState)

    objects _ [p1, p2, p3, p4]
    createStates(objects, selectedRect, group)
    createAnimations(objects, machine)

    machine.setInitialState(group)
    machine.start()

    window.r..(300, 300)
    window.s..

    ___.e.. ?.e..
