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


______ random

____ ?.?C.. ______ (pS.., QByteArray, ?DS.., QIODevice,
        QMimeData, QPoint, QRect, ?S.., __)
____ ?.?G.. ______ QDrag, ?C.., ?C.., ?I.., QPainter, ?P..
____ ?.?W.. ______ (?A.., ?FD.., QFrame, ?HBL..,
        ?LV.., QListWidget, QListWidgetItem, ?MW.., ?MB..,
        ?SP.., ?W..)

______ puzzle_rc


c_ PuzzleWidget(?W..):

    puzzleCompleted _ pS..()

    ___  -   parent_None):
        s__(PuzzleWidget, self). - (parent)

        piecePixmaps _   # list
        pieceRects _   # list
        pieceLocations _   # list
        highlightedRect _ QRect()
        inPlace _ 0

        setAcceptDrops( st.
        sMS..(400, 400)
        sMS..(400, 400)

    ___ clear
        pieceLocations _   # list
        piecePixmaps _   # list
        pieceRects _   # list
        highlightedRect _ QRect()
        inPlace _ 0
        update()

    ___ dragEnterEvent  event):
        __ event.mimeData().hasFormat('image/x-puzzle-piece'):
            event.accept()
        ____
            event.ignore()

    ___ dragLeaveEvent  event):
        updateRect _ highlightedRect
        highlightedRect _ QRect()
        update(updateRect)
        event.accept()

    ___ dragMoveEvent  event):
        updateRect _ highlightedRect.united(targetSquare(event.pos()))

        __ event.mimeData().hasFormat('image/x-puzzle-piece') and findPiece(targetSquare(event.pos())) __ -1:
            highlightedRect _ targetSquare(event.pos())
            event.setDropAction(__.MoveAction)
            event.accept()
        ____
            highlightedRect _ QRect()
            event.ignore()

        update(updateRect)

    ___ dropEvent  event):
        __ event.mimeData().hasFormat('image/x-puzzle-piece') and findPiece(targetSquare(event.pos())) __ -1:
            pieceData _ event.mimeData().data('image/x-puzzle-piece')
            dataStream _ ?DS..(pieceData, QIODevice.ReadOnly)
            square _ targetSquare(event.pos())
            pixmap _ ?P..()
            location _ QPoint()
            dataStream >> pixmap >> location

            pieceLocations.ap..(location)
            piecePixmaps.ap..(pixmap)
            pieceRects.ap..(square)

            hightlightedRect _ QRect()
            update(square)

            event.setDropAction(__.MoveAction)
            event.accept()

            __ location __ QPoint(square.x() / 80, square.y() / 80):
                inPlace +_ 1
                __ inPlace __ 25:
                    puzzleCompleted.e..()
        ____
            highlightedRect _ QRect()
            event.ignore()

    ___ findPiece  pieceRect):
        ___
            r_ pieceRects.index(pieceRect)
        _____ V..:
            r_ -1

    ___ mousePressEvent  event):
        square _ targetSquare(event.pos())
        found _ findPiece(square)

        __ found __ -1:
            r_

        location _ pieceLocations[found]
        pixmap _ piecePixmaps[found]
        del pieceLocations[found]
        del piecePixmaps[found]
        del pieceRects[found]

        __ location __ QPoint(square.x() / 80, square.y() / 80):
            inPlace -_ 1

        update(square)

        itemData _ QByteArray()
        dataStream _ ?DS..(itemData, QIODevice.WriteOnly)

        dataStream << pixmap << location

        mimeData _ QMimeData()
        mimeData.setData('image/x-puzzle-piece', itemData)

        drag _ QDrag
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - square.topLeft())
        drag.sP..(pixmap)

        __ drag.e..(__.MoveAction) !_ __.MoveAction:
            pieceLocations.insert(found, location)
            piecePixmaps.insert(found, pixmap)
            pieceRects.insert(found, square)
            update(targetSquare(event.pos()))

            __ location __ QPoint(square.x() / 80, square.y() / 80):
                inPlace +_ 1

    ___ paintEvent  event):
        painter _ QPainter()
        painter.begin
        painter.fillRect(event.rect(), __.white)

        __ highlightedRect.isValid
            painter.sB..(?C..("#ffcccc"))
            painter.sP..(__.NoPen)
            painter.drawRect(highlightedRect.adjusted(0, 0, -1, -1))

        ___ rect, pixmap __ zip(pieceRects, piecePixmaps):
            painter.drawPixmap(rect, pixmap)

        painter.end()

    ___ targetSquare  position):
        r_ QRect(position.x() // 80 * 80, position.y() // 80 * 80, 80, 80)


c_ PiecesList(QListWidget):
    ___  -   parent_None):
        s__(PiecesList, self). - (parent)

        setDragEnabled( st.
        setViewMode(?LV...IconMode)
        setIconSize(?S..(60, 60))
        setSpacing(10)
        setAcceptDrops( st.
        setDropIndicatorShown( st.

    ___ dragEnterEvent  event):
        __ event.mimeData().hasFormat('image/x-puzzle-piece'):
            event.accept()
        ____
            event.ignore()

    ___ dragMoveEvent  event):
        __ event.mimeData().hasFormat('image/x-puzzle-piece'):
            event.setDropAction(__.MoveAction)
            event.accept()
        ____
            event.ignore()

    ___ dropEvent  event):
        __ event.mimeData().hasFormat('image/x-puzzle-piece'):
            pieceData _ event.mimeData().data('image/x-puzzle-piece')
            dataStream _ ?DS..(pieceData, QIODevice.ReadOnly)
            pixmap _ ?P..()
            location _ QPoint()
            dataStream >> pixmap >> location

            addPiece(pixmap, location)

            event.setDropAction(__.MoveAction)
            event.accept()
        ____
            event.ignore()

    ___ addPiece  pixmap, location):
        pieceItem _ QListWidgetItem
        pieceItem.sI..(?I..(pixmap))
        pieceItem.setData(__.UserRole, pixmap)
        pieceItem.setData(__.UserRole+1, location)
        pieceItem.setFlags(__.ItemIsEnabled | __.ItemIsSelectable | __.ItemIsDragEnabled)

    ___ startDrag  supportedActions):
        item _ currentItem()

        itemData _ QByteArray()
        dataStream _ ?DS..(itemData, QIODevice.WriteOnly)
        pixmap _ ?P..(item.data(__.UserRole))
        location _ item.data(__.UserRole+1)

        dataStream << pixmap << location

        mimeData _ QMimeData()
        mimeData.setData('image/x-puzzle-piece', itemData)

        drag _ QDrag
        drag.setMimeData(mimeData)
        drag.setHotSpot(QPoint(pixmap.width()/2, pixmap.height()/2))
        drag.sP..(pixmap)

        __ drag.e..(__.MoveAction) __ __.MoveAction:
            __ currentItem() __ no. N..:
                takeItem(row(item))


c_ MainWindow ?MW..
    ___  -   parent_None):
        s__(MainWindow, self). - (parent)

        puzzleImage _ ?P..()

        setupMenus()
        setupWidgets()

        sSP..(?SP..(?SP...Fixed, ?SP...Fixed))
        sWT..("Puzzle")

    ___ openImage  path_None):
        __ no. pa__:
            pa__, _ _ ?FD...gOFN..  "Open Image", '',
                    "Image Files (*.png *.jpg *.bmp)")

        __ pa__:
            newImage _ ?P..()
            __ no. newImage.load(pa__):
                ?MB...w..  "Open Image",
                        "The image file could not be loaded.",
                        ?MB...Cancel)
                r_

            puzzleImage _ newImage
            setupPuzzle()

    ___ setCompleted
        ?MB...i..  "Puzzle Completed",
                "Congratulations! You have completed the puzzle!\nClick OK "
                "to start again.",
                ?MB...Ok)

        setupPuzzle()

    ___ setupPuzzle
        size _ min(puzzleImage.width(), puzzleImage.height())
        puzzleImage _ puzzleImage.copy(
                (puzzleImage.width() - size)/2,
                (puzzleImage.height() - size)/2, size, size).scaled(400, 400, __.IgnoreAspectRatio, __.SmoothTransformation)

        piecesList.c..

        ___ y __ ra..(5):
            ___ x __ ra..(5):
                pieceImage _ puzzleImage.copy(x*80, y*80, 80, 80)
                piecesList.addPiece(pieceImage, QPoint(x,y))

        random.seed(?C...pos().x() ^ ?C...pos().y())

        ___ i __ ra..(piecesList.count()):
            __ random.random() < 0.5:
                item _ piecesList.takeItem(i)
                piecesList.iI..(0, item)

        puzzleWidget.c..

    ___ setupMenus
        fileMenu _ mB.. .aM..("&File")

        openAction _ fileMenu.aA..("&Open...")
        openAction.sS..("Ctrl+O")

        exitAction _ fileMenu.aA..("E&xit")
        exitAction.sS..("Ctrl+Q")

        gameMenu _ mB.. .aM..("&Game")

        restartAction _ gameMenu.aA..("&Restart")

        openAction.t__.c..(openImage)
        exitAction.t__.c..(?A...i.. .quit)
        restartAction.t__.c..(setupPuzzle)

    ___ setupWidgets
        frame _ QFrame()
        frameLayout _ ?HBL..(frame)

        piecesList _ PiecesList()

        puzzleWidget _ PuzzleWidget()

        puzzleWidget.puzzleCompleted.c..(setCompleted,
                __.QueuedConnection)

        frameLayout.aW..(piecesList)
        frameLayout.aW..(puzzleWidget)
        sCW..(frame)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.openImage(':/images/example.jpg')
    window.s..
    ___.e.. ?.e..
