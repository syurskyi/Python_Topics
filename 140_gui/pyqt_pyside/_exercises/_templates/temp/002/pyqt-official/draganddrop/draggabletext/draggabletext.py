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


____ ?.?C.. ______ QFile, QIODevice, QMimeData, QPoint, __, QTextStream
____ ?.?G.. ______ QDrag, ?P.., ?P..
____ ?.?W.. ______ ?A.., QFrame, ?L.., ?W..

______ draggabletext_rc


c_ DragLabel(?L..):
    ___  -   t__, parent):
        s__(DragLabel, self). - (t__, parent)

        setAutoFillBackground( st.
        setFrameShape(QFrame.Panel)
        setFrameShadow(QFrame.Raised)

    ___ mousePressEvent  event):
        hotSpot _ event.pos()

        mimeData _ QMimeData()
        mimeData.sT..(t__())
        mimeData.setData('application/x-hotspot',
                '%d %d' % (hotSpot.x(), hotSpot.y()))

        pixmap _ ?P..(size())
        render(pixmap)

        drag _ QDrag
        drag.setMimeData(mimeData)
        drag.sP..(pixmap)
        drag.setHotSpot(hotSpot)

        dropAction _ drag.e..(__.CopyAction | __.MoveAction, __.CopyAction)

        __ dropAction __ __.MoveAction:
            c..
            update()


c_ DragWidget(?W..):
    ___  -   parent_None):
        s__(DragWidget, self). - (parent)

        dictionaryFile _ QFile(':/dictionary/words.txt')
        dictionaryFile.o..(QIODevice.ReadOnly)

        x _ 5
        y _ 5

        ___ word __ QTextStream(dictionaryFile).rA...sp..
            wordLabel _ DragLabel(word, self)
            wordLabel.move(x, y)
            wordLabel.s..
            x +_ wordLabel.width() + 2
            __ x >_ 195:
                x _ 5
                y +_ wordLabel.height() + 2

        newPalette _ p..
        newPalette.sC..(?P...Window, __.white)
        sP..(newPalette)

        setAcceptDrops( st.
        sMS..(400, max(200, y))
        sWT..("Draggable Text")

    ___ dragEnterEvent  event):
        __ event.mimeData().hasText
            __ event.source() __ children
                event.setDropAction(__.MoveAction)
                event.accept()
            ____
                event.acceptProposedAction()
        ____
            event.ignore()

    ___ dropEvent  event):
        __ event.mimeData().hasText
            mime _ event.mimeData()
            pieces _ mime.t__().sp..()
            position _ event.pos()
            hotSpot _ QPoint()

            hotSpotPos _ mime.data('application/x-hotspot').sp..(' ')
            __ le.(hotSpotPos) __ 2:
               hotSpot.setX(hotSpotPos[0].toInt()[0])
               hotSpot.setY(hotSpotPos[1].toInt()[0])

            ___ piece __ pieces:
                newLabel _ DragLabel(piece, self)
                newLabel.move(position - hotSpot)
                newLabel.s..

                position +_ QPoint(newLabel.width(), 0)

            __ event.source() __ children
                event.setDropAction(__.MoveAction)
                event.accept()
            ____
                event.acceptProposedAction()
        ____
            event.ignore()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ DragWidget()
    window.s..
    ___.e.. ?.e..
