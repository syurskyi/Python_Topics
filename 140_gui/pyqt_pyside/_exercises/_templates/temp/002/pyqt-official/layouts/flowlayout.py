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


____ ?.?C.. ______ QPoint, QRect, QSize, __
____ ?.?W.. ______ (?A.., QLayout, ?PB.., QSizePolicy,
        QWidget)


c_ Window(QWidget):
    ___  -
        super(Window, self). - ()

        flowLayout _ FlowLayout()
        flowLayout.aW..(?PB..("Short"))
        flowLayout.aW..(?PB..("Longer"))
        flowLayout.aW..(?PB..("Different text"))
        flowLayout.aW..(?PB..("More text"))
        flowLayout.aW..(?PB..("Even longer button text"))
        sL..(flowLayout)

        setWindowTitle("Flow Layout")


c_ FlowLayout(QLayout):
    ___  -   parent_None, margin_0, spacing_-1):
        super(FlowLayout, self). - (parent)

        __ parent __ no. N..:
            setContentsMargins(margin, margin, margin, margin)

        setSpacing(spacing)

        itemList _   # list

    ___ __del__
        item _ takeAt(0)
        w__ item:
            item _ takeAt(0)

    ___ addItem  item):
        itemList.ap..(item)

    ___ count
        r_ le.(itemList)

    ___ itemAt  index):
        __ index >_ 0 and index < le.(itemList):
            r_ itemList[index]

        r_ N..

    ___ takeAt  index):
        __ index >_ 0 and index < le.(itemList):
            r_ itemList.p.. index)

        r_ N..

    ___ expandingDirections
        r_ __.Orientations(__.Orientation(0))

    ___ hasHeightForWidth
        r_ True

    ___ heightForWidth  width):
        height _ doLayout(QRect(0, 0, width, 0), True)
        r_ height

    ___ setGeometry  rect):
        super(FlowLayout, self).setGeometry(rect)
        doLayout(rect, False)

    ___ sizeHint
        r_ minimumSize()

    ___ minimumSize
        size _ QSize()

        ___ item __ itemList:
            size _ size.expandedTo(item.minimumSize())

        margin, _, _, _ _ getContentsMargins()

        size +_ QSize(2 * margin, 2 * margin)
        r_ size

    ___ doLayout  rect, testOnly):
        x _ rect.x()
        y _ rect.y()
        lineHeight _ 0

        ___ item __ itemList:
            wid _ item.widget()
            spaceX _ spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, __.Horizontal)
            spaceY _ spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, __.Vertical)
            nextX _ x + item.sizeHint().width() + spaceX
            __ nextX - spaceX > rect.right() and lineHeight > 0:
                x _ rect.x()
                y _ y + lineHeight + spaceY
                nextX _ x + item.sizeHint().width() + spaceX
                lineHeight _ 0

            __ no. testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x _ nextX
            lineHeight _ max(lineHeight, item.sizeHint().height())

        r_ y + lineHeight - rect.y()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    mainWin _ Window()
    mainWin.s..
    ___.exit(app.exec_())
