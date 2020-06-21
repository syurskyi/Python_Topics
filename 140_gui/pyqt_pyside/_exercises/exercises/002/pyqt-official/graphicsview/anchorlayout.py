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


____ ?.?C.. ______ QSizeF, __
____ ?.?W.. ______ (?A.., QGraphicsAnchorLayout,
        QGraphicsProxyWidget, QGraphicsScene, QGraphicsView, QGraphicsWidget,
        ?PB.., ?SP..)


___ createItem(minimum, preferred, maximum, name):
    w _ QGraphicsProxyWidget()

    w.setWidget(?PB..(name))
    w.sMS..(minimum)
    w.setPreferredSize(preferred)
    w.sMS..(maximum)
    w.sSP..(?SP...Preferred, ?SP...Preferred)

    r_ w


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    scene _ QGraphicsScene()
    scene.setSceneRect(0, 0, 800, 480)

    minSize _ QSizeF(30, 100)
    prefSize _ QSizeF(210, 100)
    maxSize _ QSizeF(300, 100)

    a _ createItem(minSize, prefSize, maxSize, "A")
    b _ createItem(minSize, prefSize, maxSize, "B")
    c _ createItem(minSize, prefSize, maxSize, "C")
    d _ createItem(minSize, prefSize, maxSize, "D")
    e _ createItem(minSize, prefSize, maxSize, "E")
    f _ createItem(QSizeF(30, 50), QSizeF(150, 50), maxSize, "F")
    g _ createItem(QSizeF(30, 50), QSizeF(30, 100), maxSize, "G")

    l _ QGraphicsAnchorLayout()
    l.setSpacing(0)

    w _ QGraphicsWidget(N.., __.Window)
    w.setPos(20, 20)
    w.sL..(l)

    # Vertical.
    l.addAnchor(a, __.AnchorTop, l, __.AnchorTop)
    l.addAnchor(b, __.AnchorTop, l, __.AnchorTop)

    l.addAnchor(c, __.AnchorTop, a, __.AnchorBottom)
    l.addAnchor(c, __.AnchorTop, b, __.AnchorBottom)
    l.addAnchor(c, __.AnchorBottom, d, __.AnchorTop)
    l.addAnchor(c, __.AnchorBottom, e, __.AnchorTop)

    l.addAnchor(d, __.AnchorBottom, l, __.AnchorBottom)
    l.addAnchor(e, __.AnchorBottom, l, __.AnchorBottom)

    l.addAnchor(c, __.AnchorTop, f, __.AnchorTop)
    l.addAnchor(c, __.AnchorVerticalCenter, f, __.AnchorBottom)
    l.addAnchor(f, __.AnchorBottom, g, __.AnchorTop)
    l.addAnchor(c, __.AnchorBottom, g, __.AnchorBottom)

    # Horizontal.
    l.addAnchor(l, __.AnchorLeft, a, __.AnchorLeft)
    l.addAnchor(l, __.AnchorLeft, d, __.AnchorLeft)
    l.addAnchor(a, __.AnchorRight, b, __.AnchorLeft)

    l.addAnchor(a, __.AnchorRight, c, __.AnchorLeft)
    l.addAnchor(c, __.AnchorRight, e, __.AnchorLeft)

    l.addAnchor(b, __.AnchorRight, l, __.AnchorRight)
    l.addAnchor(e, __.AnchorRight, l, __.AnchorRight)
    l.addAnchor(d, __.AnchorRight, e, __.AnchorLeft)

    l.addAnchor(l, __.AnchorLeft, f, __.AnchorLeft)
    l.addAnchor(l, __.AnchorLeft, g, __.AnchorLeft)
    l.addAnchor(f, __.AnchorRight, g, __.AnchorRight)

    scene.aI..(w)
    scene.setBackgroundBrush(__.darkGreen)

    view _ QGraphicsView(scene)
    view.s..

    ___.e.. ?.e..
