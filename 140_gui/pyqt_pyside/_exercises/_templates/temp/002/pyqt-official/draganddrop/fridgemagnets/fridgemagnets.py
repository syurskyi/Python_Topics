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


____ ?.?C.. ______ (QByteArray, QDataStream, QFile, QIODevice, QMimeData,
        QPoint, QRect, QRectF, __, QTextStream)
____ ?.?G.. ______ (QDrag, QFont, QFontMetrics, QImage, QPainter,
        ?P.., QPixmap, qRgba)
____ ?.?W.. ______ ?A.., QLabel, QWidget

______ fridgemagnets_rc


c_ DragLabel(QLabel):
    ___  -   t__, parent):
        super(DragLabel, self). - (parent)

        metric _ QFontMetrics(font())
        size _ metric.size(__.TextSingleLine, t__)

        image _ QImage(size.width() + 12, size.height() + 12,
                QImage.Format_ARGB32_Premultiplied)
        image.fill(qRgba(0, 0, 0, 0))

        font _ QFont()
        font.setStyleStrategy(QFont.ForceOutline)

        painter _ QPainter()
        painter.begin(image)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(__.white)
        painter.drawRoundedRect(
                QRectF(0.5, 0.5, image.width()-1, image.height()-1),
                25, 25, __.RelativeSize)

        painter.setFont(font)
        painter.setBrush(__.black)
        painter.drawText(QRect(QPoint(6, 6), size), __.AlignCenter, t__)
        painter.end()

        setPixmap(QPixmap.fromImage(image))
        labelText _ t__

    ___ mousePressEvent  event):
        itemData _ QByteArray()
        dataStream _ QDataStream(itemData, QIODevice.WriteOnly)
        dataStream << QByteArray(labelText) << QPoint(event.pos() - rect().topLeft())

        mimeData _ QMimeData()
        mimeData.setData('application/x-fridgemagnet', itemData)
        mimeData.sT..(labelText)

        drag _ QDrag
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - rect().topLeft())
        drag.setPixmap(pixmap())

        hide()

        __ drag.exec_(__.MoveAction | __.CopyAction, __.CopyAction) == __.MoveAction:
            close()
        ____
            s..


c_ DragWidget(QWidget):
    ___  -   parent_None):
        super(DragWidget, self). - (parent)

        dictionaryFile _ QFile(':/dictionary/words.txt')
        dictionaryFile.o..(QFile.ReadOnly)

        x _ 5
        y _ 5

        ___ word __ QTextStream(dictionaryFile).readAll().split
            wordLabel _ DragLabel(word, self)
            wordLabel.move(x, y)
            wordLabel.s..
            x +_ wordLabel.width() + 2
            __ x >_ 245:
                x _ 5
                y +_ wordLabel.height() + 2

        newPalette _ palette()
        newPalette.sC..(?P...Window, __.white)
        sP..(newPalette)

        setMinimumSize(400, max(200, y))
        sWT..("Fridge Magnets")
        setAcceptDrops(True)

    ___ dragEnterEvent  event):
        __ event.mimeData().hasFormat('application/x-fridgemagnet'):
            __ event.source() __ children
                event.setDropAction(__.MoveAction)
                event.accept()
            ____
                event.acceptProposedAction()
        ____ event.mimeData().hasText
            event.acceptProposedAction()
        ____
            event.ignore()

    dragMoveEvent _ dragEnterEvent

    ___ dropEvent  event):
        __ event.mimeData().hasFormat('application/x-fridgemagnet'):
            mime _ event.mimeData()
            itemData _ mime.data('application/x-fridgemagnet')
            dataStream _ QDataStream(itemData, QIODevice.ReadOnly)

            t__ _ QByteArray()
            offset _ QPoint()
            dataStream >> t__ >> offset

            try:
                # Python v3.
                t__ _ str(t__, encoding_'latin1')
            except TypeError:
                # Python v2.
                t__ _ str(t__)

            newLabel _ DragLabel(t__, self)
            newLabel.move(event.pos() - offset)
            newLabel.s..

            __ event.source() __ children
                event.setDropAction(__.MoveAction)
                event.accept()
            ____
                event.acceptProposedAction()
        ____ event.mimeData().hasText
            pieces _ event.mimeData().t__().split()
            position _ event.pos()

            ___ piece __ pieces:
                newLabel _ DragLabel(piece, self)
                newLabel.move(position)
                newLabel.s..

                position +_ QPoint(newLabel.width(), 0)

            event.acceptProposedAction()
        ____
            event.ignore()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ DragWidget()
    window.s..
    ___.e..(app.exec_())
