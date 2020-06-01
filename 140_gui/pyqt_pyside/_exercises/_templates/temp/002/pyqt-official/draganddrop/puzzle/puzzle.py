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

____ ?.?C.. ______ (pyqtSignal, QByteArray, QDataStream, QIODevice,
        QMimeData, QPoint, QRect, QSize, __)
____ ?.?G.. ______ QDrag, ?C.., QCursor, QIcon, QPainter, QPixmap
____ ?.?W.. ______ (?A.., ?FD.., QFrame, QHBoxLayout,
        QListView, QListWidget, QListWidgetItem, QMainWindow, ?MB..,
        QSizePolicy, QWidget)

______ puzzle_rc


c_ PuzzleWidget(QWidget):

    puzzleCompleted _ pyqtSignal()

    ___  -   parent_None):
        super(PuzzleWidget, self). - (parent)

        piecePixmaps _   # list
        pieceRects _   # list
        pieceLocations _   # list
        highlightedRect _ QRect()
        inPlace _ 0

        setAcceptDrops(True)
        setMinimumSize(400, 400)
        setMaximumSize(400, 400)

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

        __ event.mimeData().hasFormat('image/x-puzzle-piece') and findPiece(targetSquare(event.pos())) == -1:
            highlightedRect _ targetSquare(event.pos())
            event.setDropAction(__.MoveAction)
            event.accept()
        ____
            highlightedRect _ QRect()
            event.ignore()

        update(updateRect)

    ___ dropEvent  event):
        __ event.mimeData().hasFormat('image/x-puzzle-piece') and findPiece(targetSquare(event.pos())) == -1:
            pieceData _ event.mimeData().data('image/x-puzzle-piece')
            dataStream _ QDataStream(pieceData, QIODevice.ReadOnly)
            square _ targetSquare(event.pos())
            pixmap _ QPixmap()
            location _ QPoint()
            dataStream >> pixmap >> location

            pieceLocations.ap..(location)
            piecePixmaps.ap..(pixmap)
            pieceRects.ap..(square)

            hightlightedRect _ QRect()
            update(square)

            event.setDropAction(__.MoveAction)
            event.accept()

            __ location == QPoint(square.x() / 80, square.y() / 80):
                inPlace +_ 1
                __ inPlace == 25:
                    puzzleCompleted.emit()
        ____
            highlightedRect _ QRect()
            event.ignore()

    ___ findPiece  pieceRect):
        try:
            r_ pieceRects.index(pieceRect)
        except ValueError:
            r_ -1

    ___ mousePressEvent  event):
        square _ targetSquare(event.pos())
        found _ findPiece(square)

        __ found == -1:
            r_

        location _ pieceLocations[found]
        pixmap _ piecePixmaps[found]
        del pieceLocations[found]
        del piecePixmaps[found]
        del pieceRects[found]

        __ location == QPoint(square.x() / 80, square.y() / 80):
            inPlace -_ 1

        update(square)

        itemData _ QByteArray()
        dataStream _ QDataStream(itemData, QIODevice.WriteOnly)

        dataStream << pixmap << location

        mimeData _ QMimeData()
        mimeData.setData('image/x-puzzle-piece', itemData)

        drag _ QDrag
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - square.topLeft())
        drag.setPixmap(pixmap)

        __ drag.exec_(__.MoveAction) !_ __.MoveAction:
            pieceLocations.insert(found, location)
            piecePixmaps.insert(found, pixmap)
            pieceRects.insert(found, square)
            update(targetSquare(event.pos()))

            __ location == QPoint(square.x() / 80, square.y() / 80):
                inPlace +_ 1

    ___ paintEvent  event):
        painter _ QPainter()
        painter.begin
        painter.fillRect(event.rect(), __.white)

        __ highlightedRect.isValid
            painter.setBrush(?C..("#ffcccc"))
            painter.setPen(__.NoPen)
            painter.drawRect(highlightedRect.adjusted(0, 0, -1, -1))

        ___ rect, pixmap __ zip(pieceRects, piecePixmaps):
            painter.drawPixmap(rect, pixmap)

        painter.end()

    ___ targetSquare  position):
        r_ QRect(position.x() // 80 * 80, position.y() // 80 * 80, 80, 80)


c_ PiecesList(QListWidget):
    ___  -   parent_None):
        super(PiecesList, self). - (parent)

        setDragEnabled(True)
        setViewMode(QListView.IconMode)
        setIconSize(QSize(60, 60))
        setSpacing(10)
        setAcceptDrops(True)
        setDropIndicatorShown(True)

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
            dataStream _ QDataStream(pieceData, QIODevice.ReadOnly)
            pixmap _ QPixmap()
            location _ QPoint()
            dataStream >> pixmap >> location

            addPiece(pixmap, location)

            event.setDropAction(__.MoveAction)
            event.accept()
        ____
            event.ignore()

    ___ addPiece  pixmap, location):
        pieceItem _ QListWidgetItem
        pieceItem.setIcon(QIcon(pixmap))
        pieceItem.setData(__.UserRole, pixmap)
        pieceItem.setData(__.UserRole+1, location)
        pieceItem.setFlags(__.ItemIsEnabled | __.ItemIsSelectable | __.ItemIsDragEnabled)

    ___ startDrag  supportedActions):
        item _ currentItem()

        itemData _ QByteArray()
        dataStream _ QDataStream(itemData, QIODevice.WriteOnly)
        pixmap _ QPixmap(item.data(__.UserRole))
        location _ item.data(__.UserRole+1)

        dataStream << pixmap << location

        mimeData _ QMimeData()
        mimeData.setData('image/x-puzzle-piece', itemData)

        drag _ QDrag
        drag.setMimeData(mimeData)
        drag.setHotSpot(QPoint(pixmap.width()/2, pixmap.height()/2))
        drag.setPixmap(pixmap)

        __ drag.exec_(__.MoveAction) == __.MoveAction:
            __ currentItem() __ no. N..:
                takeItem(row(item))


c_ MainWindow ?MW..
    ___  -   parent_None):
        super(MainWindow, self). - (parent)

        puzzleImage _ QPixmap()

        setupMenus()
        setupWidgets()

        sSP..(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        sWT..("Puzzle")

    ___ openImage  path_None):
        __ no. path:
            path, _ _ ?FD...gOFN..  "Open Image", '',
                    "Image Files (*.png *.jpg *.bmp)")

        __ path:
            newImage _ QPixmap()
            __ no. newImage.load(path):
                ?MB...warning  "Open Image",
                        "The image file could not be loaded.",
                        ?MB...Cancel)
                r_

            puzzleImage _ newImage
            setupPuzzle()

    ___ setCompleted
        ?MB...information  "Puzzle Completed",
                "Congratulations! You have completed the puzzle!\nClick OK "
                "to start again.",
                ?MB...Ok)

        setupPuzzle()

    ___ setupPuzzle
        size _ min(puzzleImage.width(), puzzleImage.height())
        puzzleImage _ puzzleImage.copy(
                (puzzleImage.width() - size)/2,
                (puzzleImage.height() - size)/2, size, size).scaled(400, 400, __.IgnoreAspectRatio, __.SmoothTransformation)

        piecesList.clear()

        ___ y __ range(5):
            ___ x __ range(5):
                pieceImage _ puzzleImage.copy(x*80, y*80, 80, 80)
                piecesList.addPiece(pieceImage, QPoint(x,y))

        random.seed(QCursor.pos().x() ^ QCursor.pos().y())

        ___ i __ range(piecesList.count()):
            __ random.random() < 0.5:
                item _ piecesList.takeItem(i)
                piecesList.insertItem(0, item)

        puzzleWidget.clear()

    ___ setupMenus
        fileMenu _ mB.. .aM..("&File")

        openAction _ fileMenu.aA..("&Open...")
        openAction.sS..("Ctrl+O")

        exitAction _ fileMenu.aA..("E&xit")
        exitAction.sS..("Ctrl+Q")

        gameMenu _ mB.. .aM..("&Game")

        restartAction _ gameMenu.aA..("&Restart")

        openAction.t__.c..(openImage)
        exitAction.t__.c..(?A...instance().quit)
        restartAction.t__.c..(setupPuzzle)

    ___ setupWidgets
        frame _ QFrame()
        frameLayout _ QHBoxLayout(frame)

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
    ___.e..(app.exec_())
