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


____ ?.?C.. ______ (QByteArray, ?DS.., QIODevice, QMimeData,
        QPoint, __)
____ ?.?G.. ______ ?C.., QDrag, QPainter, ?P..
____ ?.?W.. ______ ?A.., QFrame, ?HBL.., ?L.., ?W..

______ draggableicons_rc


c_ DragWidget(QFrame):
    ___  -   parent_None):
        s__(DragWidget, self). - (parent)

        sMS..(200, 200)
        setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        setAcceptDrops( st.

        boatIcon _ ?L..
        boatIcon.sP..(?P..(':/images/boat.png'))
        boatIcon.move(20, 20)
        boatIcon.s..
        boatIcon.setAttribute(__.WA_DeleteOnClose)

        carIcon _ ?L..
        carIcon.sP..(?P..(':/images/car.png'))
        carIcon.move(120, 20)
        carIcon.s..
        carIcon.setAttribute(__.WA_DeleteOnClose)

        houseIcon _ ?L..
        houseIcon.sP..(?P..(':/images/house.png'))
        houseIcon.move(20, 120)
        houseIcon.s..
        houseIcon.setAttribute(__.WA_DeleteOnClose)

    ___ dragEnterEvent  event):
        __ event.mimeData().hasFormat('application/x-dnditemdata'):
            __ event.source() __ self:
                event.setDropAction(__.MoveAction)
                event.accept()
            ____
                event.acceptProposedAction()
        ____
            event.ignore()

    dragMoveEvent _ dragEnterEvent

    ___ dropEvent  event):
        __ event.mimeData().hasFormat('application/x-dnditemdata'):
            itemData _ event.mimeData().data('application/x-dnditemdata')
            dataStream _ ?DS..(itemData, QIODevice.ReadOnly)

            pixmap _ ?P..()
            offset _ QPoint()
            dataStream >> pixmap >> offset

            newIcon _ ?L..
            newIcon.sP..(pixmap)
            newIcon.move(event.pos() - offset)
            newIcon.s..
            newIcon.setAttribute(__.WA_DeleteOnClose)

            __ event.source() __ self:
                event.setDropAction(__.MoveAction)
                event.accept()
            ____
                event.acceptProposedAction()
        ____
            event.ignore()

    ___ mousePressEvent  event):
        child _ childAt(event.pos())
        __ no. child:
            r_

        pixmap _ ?P..(child.pixmap())

        itemData _ QByteArray()
        dataStream _ ?DS..(itemData, QIODevice.WriteOnly)
        dataStream << pixmap << QPoint(event.pos() - child.pos())

        mimeData _ QMimeData()
        mimeData.setData('application/x-dnditemdata', itemData)

        drag _ QDrag
        drag.setMimeData(mimeData)
        drag.sP..(pixmap)
        drag.setHotSpot(event.pos() - child.pos())

        tempPixmap _ ?P..(pixmap)
        painter _ QPainter()
        painter.begin(tempPixmap)
        painter.fillRect(pixmap.rect(), ?C..(127, 127, 127, 127))
        painter.end()

        child.sP..(tempPixmap)

        __ drag.e..(__.CopyAction | __.MoveAction, __.CopyAction) __ __.MoveAction:
            child.c..
        ____
            child.s..
            child.sP..(pixmap)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    mainWidget _ ?W..
    horizontalLayout _ ?HBL..
    horizontalLayout.aW..(DragWidget())
    horizontalLayout.aW..(DragWidget())

    mainWidget.sL..(horizontalLayout)
    mainWidget.sWT..("Draggable Icons")
    mainWidget.s..

    ___.e.. ?.e..
