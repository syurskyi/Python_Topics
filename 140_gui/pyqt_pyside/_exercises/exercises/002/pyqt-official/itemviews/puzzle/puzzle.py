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

____ ?.?C.. ______ (pS.., QAbstractListModel, QByteArray,
        ?DS.., QIODevice, QMimeData, QModelIndex, QPoint, QRect, ?S..,
        __)
____ ?.?G.. ______ ?C.., ?C.., QDrag, ?I.., QPainter, ?P..
____ ?.?W.. ______ (?A.., ?FD.., QFrame, ?HBL..,
        ?LV.., ?MW.., ?MB.., ?SP.., ?W..)

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
            stream _ ?DS..(pieceData, QIODevice.ReadOnly)
            square _ targetSquare(event.pos())
            pixmap _ ?P..()
            location _ QPoint()
            stream >> pixmap >> location

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

        __ location __ QPoint(square.x() + 80, square.y() + 80):
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


c_ PiecesModel(QAbstractListModel):
    ___  -   parent_None):
        s__(PiecesModel, self). - (parent)

        locations _   # list
        pixmaps _   # list

    ___ data  index, role_Qt.DR..):
        __ no. index.isValid
            r_ N..

        __ role __ __.DecorationRole:
            r_ ?I..(pixmaps[index.row()].scaled(
                    60, 60, __.KeepAspectRatio, __.SmoothTransformation))

        __ role __ __.UserRole:
            r_ pixmaps[index.row()]

        __ role __ __.UserRole + 1:
            r_ locations[index.row()]

        r_ N..

    ___ addPiece  pixmap, location):
        __ random.random() < 0.5:
            row _ 0
        ____
            row _ le.(pixmaps)

        beginInsertRows(QModelIndex(), row, row)
        pixmaps.insert(row, pixmap)
        locations.insert(row, location)
        endInsertRows()

    ___ flags index):
        __ index.isValid
            r_ (__.ItemIsEnabled | __.ItemIsSelectable |
                    __.ItemIsDragEnabled)

        r_ __.ItemIsDropEnabled

    ___ removeRows row, count, parent):
        __ parent.isValid
            r_ F..

        __ row >_ le.(pixmaps) or row + count <_ 0:
            r_ F..

        beginRow _ max(0, row)
        endRow _ min(row + count - 1, le.(pixmaps) - 1)

        beginRemoveRows(parent, beginRow, endRow)

        del pixmaps[beginRow:endRow + 1]
        del locations[beginRow:endRow + 1]

        endRemoveRows()
        r_ T..

    ___ mimeTypes 
        r_ ['image/x-puzzle-piece']

    ___ mimeData  indexes):
        mimeData _ QMimeData()
        encodedData _ QByteArray()

        stream _ ?DS..(encodedData, QIODevice.WriteOnly)

        ___ index __ indexes:
            __ index.isValid
                pixmap _ ?P..(data(index, __.UserRole))
                location _ data(index, __.UserRole + 1)
                stream << pixmap << location

        mimeData.setData('image/x-puzzle-piece', encodedData)
        r_ mimeData

    ___ dropMimeData  data, action, row, column, parent):
        __ no. data.hasFormat('image/x-puzzle-piece'):
            r_ F..

        __ action __ __.IgnoreAction:
            r_ T..

        __ column > 0:
            r_ F..

        __ no. parent.isValid
            __ row < 0:
                endRow _ le.(pixmaps)
            ____
                endRow _ min(row, le.(pixmaps))
        ____
            endRow _ parent.row()

        encodedData _ data.data('image/x-puzzle-piece')
        stream _ ?DS..(encodedData, QIODevice.ReadOnly)

        w__ no. stream.atEnd
            pixmap _ ?P..()
            location _ QPoint()
            stream >> pixmap >> location

            beginInsertRows(QModelIndex(), endRow, endRow)
            pixmaps.insert(endRow, pixmap)
            locations.insert(endRow, location)
            endInsertRows()

            endRow +_ 1

        r_ T..

    ___ rowCount  parent):
        __ parent.isValid
            r_ 0
        ____
            r_ le.(pixmaps)

    ___ supportedDropActions 
        r_ __.CopyAction | __.MoveAction

    ___ addPieces  pixmap):
        beginRemoveRows(QModelIndex(), 0, 24)
        pixmaps _   # list
        locations _   # list
        endRemoveRows()

        ___ y __ ra..(5):
            ___ x __ ra..(5):
                pieceImage _ pixmap.copy(x*80, y*80, 80, 80)
                addPiece(pieceImage, QPoint(x, y))


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
        puzzleImage _ puzzleImage.copy((puzzleImage.width()-size)/2,
                (puzzleImage.height() - size)/2, size, size).scaled(400,
                        400, __.IgnoreAspectRatio, __.SmoothTransformation)

        random.seed(?C...pos().x() ^ ?C...pos().y())

        model.addPieces(puzzleImage)
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

        piecesList _ ?LV..
        piecesList.setDragEnabled( st.
        piecesList.setViewMode(?LV...IconMode)
        piecesList.setIconSize(?S..(60,60))
        piecesList.setGridSize(?S..(80,80))
        piecesList.setSpacing(10)
        piecesList.setMovement(?LV...Snap)
        piecesList.setAcceptDrops( st.
        piecesList.setDropIndicatorShown( st.

        model _ PiecesModel
        piecesList.sM..(model)

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
