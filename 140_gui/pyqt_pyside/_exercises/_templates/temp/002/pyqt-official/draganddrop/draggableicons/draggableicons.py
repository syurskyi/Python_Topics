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


____ ?.QtCore ______ (QByteArray, QDataStream, QIODevice, QMimeData,
        QPoint, Qt)
____ ?.QtGui ______ QColor, QDrag, QPainter, QPixmap
____ ?.?W.. ______ ?A.., QFrame, QHBoxLayout, QLabel, QWidget

______ draggableicons_rc


class DragWidget(QFrame):
    ___ __init__(self, parent_None):
        super(DragWidget, self).__init__(parent)

        self.setMinimumSize(200, 200)
        self.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.setAcceptDrops(True)

        boatIcon _ QLabel(self)
        boatIcon.setPixmap(QPixmap(':/images/boat.png'))
        boatIcon.move(20, 20)
        boatIcon.s..
        boatIcon.setAttribute(Qt.WA_DeleteOnClose)

        carIcon _ QLabel(self)
        carIcon.setPixmap(QPixmap(':/images/car.png'))
        carIcon.move(120, 20)
        carIcon.s..
        carIcon.setAttribute(Qt.WA_DeleteOnClose)

        houseIcon _ QLabel(self)
        houseIcon.setPixmap(QPixmap(':/images/house.png'))
        houseIcon.move(20, 120)
        houseIcon.s..
        houseIcon.setAttribute(Qt.WA_DeleteOnClose)

    ___ dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-dnditemdata'):
            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    dragMoveEvent _ dragEnterEvent

    ___ dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-dnditemdata'):
            itemData _ event.mimeData().data('application/x-dnditemdata')
            dataStream _ QDataStream(itemData, QIODevice.ReadOnly)

            pixmap _ QPixmap()
            offset _ QPoint()
            dataStream >> pixmap >> offset

            newIcon _ QLabel(self)
            newIcon.setPixmap(pixmap)
            newIcon.move(event.pos() - offset)
            newIcon.s..
            newIcon.setAttribute(Qt.WA_DeleteOnClose)

            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    ___ mousePressEvent(self, event):
        child _ self.childAt(event.pos())
        if not child:
            return

        pixmap _ QPixmap(child.pixmap())

        itemData _ QByteArray()
        dataStream _ QDataStream(itemData, QIODevice.WriteOnly)
        dataStream << pixmap << QPoint(event.pos() - child.pos())

        mimeData _ QMimeData()
        mimeData.setData('application/x-dnditemdata', itemData)

        drag _ QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos() - child.pos())

        tempPixmap _ QPixmap(pixmap)
        painter _ QPainter()
        painter.begin(tempPixmap)
        painter.fillRect(pixmap.rect(), QColor(127, 127, 127, 127))
        painter.end()

        child.setPixmap(tempPixmap)

        if drag.exec_(Qt.CopyAction | Qt.MoveAction, Qt.CopyAction) == Qt.MoveAction:
            child.close()
        else:
            child.s..
            child.setPixmap(pixmap)


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    mainWidget _ QWidget()
    horizontalLayout _ QHBoxLayout()
    horizontalLayout.addWidget(DragWidget())
    horizontalLayout.addWidget(DragWidget())

    mainWidget.setLayout(horizontalLayout)
    mainWidget.setWindowTitle("Draggable Icons")
    mainWidget.s..

    sys.exit(app.exec_())
