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


____ ?.QtCore ______ (pyqtSignal, QPointF, QPropertyAnimation, QRect,
        QRectF, QState, QStateMachine, Qt)
____ ?.QtGui ______ QPixmap
____ ?.?W.. ______ (QApplication, QGraphicsScene, QGraphicsView,
        QGraphicsWidget)

______ appchooser_rc


class Pixmap(QGraphicsWidget):
    c__ _ pyqtSignal()

    ___ __init__(self, pix, parent_None):
        super(Pixmap, self).__init__(parent)

        self.orig _ QPixmap(pix)
        self.p _ QPixmap(pix)

    ___ paint(self, painter, option, widget):
        painter.drawPixmap(QPointF(), self.p)

    ___ mousePressEvent(self, ev):
        self.c__.emit()

    ___ setGeometry(self, rect):
        super(Pixmap, self).setGeometry(rect)

        if rect.size().width() > self.orig.size().width
            self.p _ self.orig.scaled(rect.size().toSize())
        else:
            self.p _ QPixmap(self.orig)


___ createStates(objects, selectedRect, parent):
    for obj in objects:
        state _ QState(parent)
        state.assignProperty(obj, 'geometry', selectedRect)
        parent.addTransition(obj.c__, state)


___ createAnimations(objects, machine):
    for obj in objects:
        animation _ QPropertyAnimation(obj, b'geometry', obj)
        machine.addDefaultAnimation(animation)


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)

    p1 _ Pixmap(QPixmap(':/digikam.png'))
    p2 _ Pixmap(QPixmap(':/akregator.png'))
    p3 _ Pixmap(QPixmap(':/accessories-dictionary.png'))
    p4 _ Pixmap(QPixmap(':/k3b.png'))

    p1.setGeometry(QRectF(0.0, 0.0, 64.0, 64.0))
    p2.setGeometry(QRectF(236.0, 0.0, 64.0, 64.0))
    p3.setGeometry(QRectF(236.0, 236.0, 64.0, 64.0))
    p4.setGeometry(QRectF(0.0, 236.0, 64.0, 64.0))

    scene _ QGraphicsScene(0, 0, 300, 300)
    scene.setBackgroundBrush(Qt.white)
    scene.addItem(p1)
    scene.addItem(p2)
    scene.addItem(p3)
    scene.addItem(p4)

    window _ QGraphicsView(scene)
    window.setFrameStyle(0)
    window.setAlignment(Qt.AlignLeft | Qt.AlignTop)
    window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

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

    window.resize(300, 300)
    window.s..

    sys.exit(app.exec_())
