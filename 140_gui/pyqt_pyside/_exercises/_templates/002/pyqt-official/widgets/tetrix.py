#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2014 Riverbank Computing Limited.
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


______ copy
______ random

____ ?.?C.. ______ pS.., QBasicTimer, ?S.., __
____ ?.?G.. ______ ?C.., QPainter, ?P..
____ ?.?W.. ______ (?A.., QFrame, QGridLayout, ?L..,
        QLCDNumber, ?PB.., ?W..)


NoShape, ZShape, SShape, LineShape, TShape, SquareShape, LShape, MirroredLShape _ ra..(8)


c_ TetrixWindow(?W..):
    ___  -
        s__(TetrixWindow, self). - ()

        board _ TetrixBoard()

        nextPieceLabel _ ?L..
        nextPieceLabel.setFrameStyle(QFrame.Box | QFrame.Raised)
        nextPieceLabel.setAlignment(__.AlignCenter)
        board.setNextPieceLabel(nextPieceLabel)

        scoreLcd _ QLCDNumber(5)
        scoreLcd.setSegmentStyle(QLCDNumber.Filled)
        levelLcd _ QLCDNumber(2)
        levelLcd.setSegmentStyle(QLCDNumber.Filled)
        linesLcd _ QLCDNumber(5)
        linesLcd.setSegmentStyle(QLCDNumber.Filled)

        startButton _ ?PB..("&Start")
        startButton.sFP..(__.NF..)
        quitButton _ ?PB..("&Quit")
        quitButton.sFP..(__.NF..)
        pauseButton _ ?PB..("&Pause")
        pauseButton.sFP..(__.NF..)

        startButton.c__.c..(board.start)
        pauseButton.c__.c..(board.pause)
        quitButton.c__.c..(?A...i.. .quit)
        board.scoreChanged.c..(scoreLcd.display)
        board.levelChanged.c..(levelLcd.display)
        board.linesRemovedChanged.c..(linesLcd.display)

        layout _ QGridLayout()
        layout.aW..(createLabel("NEXT"), 0, 0)
        layout.aW..(nextPieceLabel, 1, 0)
        layout.aW..(createLabel("LEVEL"), 2, 0)
        layout.aW..(levelLcd, 3, 0)
        layout.aW..(startButton, 4, 0)
        layout.aW..(board, 0, 1, 6, 1)
        layout.aW..(createLabel("SCORE"), 0, 2)
        layout.aW..(scoreLcd, 1, 2)
        layout.aW..(createLabel("LINES REMOVED"), 2, 2)
        layout.aW..(linesLcd, 3, 2)
        layout.aW..(quitButton, 4, 2)
        layout.aW..(pauseButton, 5, 2)
        sL..(layout)

        sWT..("Tetrix")
        r..(550, 370)

    ___ createLabel  t__):
        lbl _ ?L..(t__)
        lbl.setAlignment(__.AlignHCenter | __.AlignBottom)
        r_ lbl


c_ TetrixBoard(QFrame):
    BoardWidth _ 10
    BoardHeight _ 22

    scoreChanged _ pS..(in.)

    levelChanged _ pS..(in.)

    linesRemovedChanged _ pS..(in.)

    ___  -   parent_None):
        s__(TetrixBoard, self). - (parent)

        timer _ QBasicTimer()
        nextPieceLabel _ N..
        isWaitingAfterLine _ F..
        curPiece _ TetrixPiece()
        nextPiece _ TetrixPiece()
        curX _ 0
        curY _ 0
        numLinesRemoved _ 0
        numPiecesDropped _ 0
        score _ 0
        level _ 0
        board _ N..

        setFrameStyle(QFrame.Panel | QFrame.Sunken)
        sFP..(__.StrongFocus)
        isStarted _ F..
        isPaused _ F..
        clearBoard()

        nextPiece.setRandomShape()

    ___ shapeAt  x, y):
        r_ board[(y * TetrixBoard.BoardWidth) + x]

    ___ setShapeAt  x, y, shape):
        board[(y * TetrixBoard.BoardWidth) + x] _ shape

    ___ timeoutTime 
        r_ 1000 / (1 + level)

    ___ squareWidth 
        r_ contentsRect().width() / TetrixBoard.BoardWidth

    ___ squareHeight 
        r_ contentsRect().height() / TetrixBoard.BoardHeight

    ___ setNextPieceLabel  label):
        nextPieceLabel _ label

    ___ sH..
        r_ ?S..(TetrixBoard.BoardWidth * 15 + frameWidth() * 2,
                TetrixBoard.BoardHeight * 15 + frameWidth() * 2)

    ___ minimumSizeHint 
        r_ ?S..(TetrixBoard.BoardWidth * 5 + frameWidth() * 2,
                TetrixBoard.BoardHeight * 5 + frameWidth() * 2)

    ___ start 
        __ isPaused:
            r_

        isStarted _ T..
        isWaitingAfterLine _ F..
        numLinesRemoved _ 0
        numPiecesDropped _ 0
        score _ 0
        level _ 1
        clearBoard()

        linesRemovedChanged.e..(numLinesRemoved)
        scoreChanged.e..(score)
        levelChanged.e..(level)

        newPiece()
        timer.start(timeoutTime(), self)

    ___ pause 
        __ no. isStarted:
            r_

        isPaused _ no. isPaused
        __ isPaused:
            timer.s..
        ____
            timer.start(timeoutTime(), self)

        update()

    ___ paintEvent  event):
        s__(TetrixBoard, self).paintEvent(event)

        painter _ QPainter
        rect _ contentsRect()

        __ isPaused:
            painter.drawText(rect, __.AlignCenter, "Pause")
            r_

        boardTop _ rect.bottom() - TetrixBoard.BoardHeight * squareHeight()

        ___ i __ ra..(TetrixBoard.BoardHeight):
            ___ j __ ra..(TetrixBoard.BoardWidth):
                shape _ shapeAt(j, TetrixBoard.BoardHeight - i - 1)
                __ shape !_ NoShape:
                    drawSquare(painter,
                            rect.left() + j * squareWidth(),
                            boardTop + i * squareHeight(), shape)

        __ curPiece.shape() !_ NoShape:
            ___ i __ ra..(4):
                x _ curX + curPiece.x(i)
                y _ curY - curPiece.y(i)
                drawSquare(painter, rect.left() + x * squareWidth(),
                        boardTop + (TetrixBoard.BoardHeight - y - 1) * squareHeight(),
                        curPiece.shape())

    ___ keyPressEvent  event):
        __ no. isStarted or isPaused or curPiece.shape() __ NoShape:
            s__(TetrixBoard, self).keyPressEvent(event)
            r_

        key _ event.key()
        __ key __ __.Key_Left:
            tryMove(curPiece, curX - 1, curY)
        ____ key __ __.Key_Right:
            tryMove(curPiece, curX + 1, curY)
        ____ key __ __.Key_Down:
            tryMove(curPiece.rotatedRight(), curX, curY)
        ____ key __ __.Key_Up:
            tryMove(curPiece.rotatedLeft(), curX, curY)
        ____ key __ __.Key_Space:
            dropDown()
        ____ key __ __.Key_D:
            oneLineDown()
        ____
            s__(TetrixBoard, self).keyPressEvent(event)

    ___ timerEvent  event):
        __ event.timerId() __ timer.timerId
            __ isWaitingAfterLine:
                isWaitingAfterLine _ F..
                newPiece()
                timer.start(timeoutTime(), self)
            ____
                oneLineDown()
        ____
            s__(TetrixBoard, self).timerEvent(event)

    ___ clearBoard 
        board _ [NoShape ___ i __ ra..(TetrixBoard.BoardHeight * TetrixBoard.BoardWidth)]

    ___ dropDown 
        dropHeight _ 0
        newY _ curY
        w__ newY > 0:
            __ no. tryMove(curPiece, curX, newY - 1):
                break
            newY -_ 1
            dropHeight +_ 1

        pieceDropped(dropHeight)

    ___ oneLineDown 
        __ no. tryMove(curPiece, curX, curY - 1):
            pieceDropped(0)

    ___ pieceDropped  dropHeight):
        ___ i __ ra..(4):
            x _ curX + curPiece.x(i)
            y _ curY - curPiece.y(i)
            setShapeAt(x, y, curPiece.shape())

        numPiecesDropped +_ 1
        __ numPiecesDropped % 25 __ 0:
            level +_ 1
            timer.start(timeoutTime(), self)
            levelChanged.e..(level)

        score +_ dropHeight + 7
        scoreChanged.e..(score)
        removeFullLines()

        __ no. isWaitingAfterLine:
            newPiece()

    ___ removeFullLines 
        numFullLines _ 0

        ___ i __ ra..(TetrixBoard.BoardHeight - 1, -1, -1):
            lineIsFull _ T..

            ___ j __ ra..(TetrixBoard.BoardWidth):
                __ shapeAt(j, i) __ NoShape:
                    lineIsFull _ F..
                    break

            __ lineIsFull:
                numFullLines +_ 1
                ___ k __ ra..(TetrixBoard.BoardHeight - 1):
                    ___ j __ ra..(TetrixBoard.BoardWidth):
                        setShapeAt(j, k, shapeAt(j, k + 1))

                ___ j __ ra..(TetrixBoard.BoardWidth):
                    setShapeAt(j, TetrixBoard.BoardHeight - 1, NoShape)

        __ numFullLines > 0:
            numLinesRemoved +_ numFullLines
            score +_ 10 * numFullLines
            linesRemovedChanged.e..(numLinesRemoved)
            scoreChanged.e..(score)

            timer.start(500, self)
            isWaitingAfterLine _ T..
            curPiece.setShape(NoShape)
            update()

    ___ newPiece 
        curPiece _ copy.deepcopy(nextPiece)
        nextPiece.setRandomShape()
        showNextPiece()
        curX _ TetrixBoard.BoardWidth // 2 + 1
        curY _ TetrixBoard.BoardHeight - 1 + curPiece.minY()

        __ no. tryMove(curPiece, curX, curY):
            curPiece.setShape(NoShape)
            timer.s..
            isStarted _ F..

    ___ showNextPiece 
        __ nextPieceLabel __ N..:
            r_

        dx _ nextPiece.maxX() - nextPiece.minX() + 1
        dy _ nextPiece.maxY() - nextPiece.minY() + 1

        pixmap _ ?P..(dx * squareWidth(), dy * squareHeight())
        painter _ QPainter(pixmap)
        painter.fillRect(pixmap.rect(), nextPieceLabel.p...window())

        ___ i __ ra..(4):
            x _ nextPiece.x(i) - nextPiece.minX()
            y _ nextPiece.y(i) - nextPiece.minY()
            drawSquare(painter, x * squareWidth(),
                    y * squareHeight(), nextPiece.shape())

        painter.end()

        nextPieceLabel.sP..(pixmap)

    ___ tryMove  newPiece, newX, newY):
        ___ i __ ra..(4):
            x _ newX + newPiece.x(i)
            y _ newY - newPiece.y(i)
            __ x < 0 or x >_ TetrixBoard.BoardWidth or y < 0 or y >_ TetrixBoard.BoardHeight:
                r_ F..
            __ shapeAt(x, y) !_ NoShape:
                r_ F..

        curPiece _ newPiece
        curX _ newX
        curY _ newY
        update()
        r_ T..

    ___ drawSquare  painter, x, y, shape):
        colorTable _ [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color _ ?C..(colorTable[shape])
        painter.fillRect(x + 1, y + 1, squareWidth() - 2,
                squareHeight() - 2, color)

        painter.sP..(color.lighter())
        painter.drawLine(x, y + squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + squareWidth() - 1, y)

        painter.sP..(color.darker())
        painter.drawLine(x + 1, y + squareHeight() - 1,
                x + squareWidth() - 1, y + squareHeight() - 1)
        painter.drawLine(x + squareWidth() - 1,
                y + squareHeight() - 1, x + squareWidth() - 1, y + 1)


c_ TetrixPiece o..
    coordsTable _ (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    ___  -
        coords _ [[0, 0] ___ _ __ ra..(4)]
        pieceShape _ NoShape

        setShape(NoShape)

    ___ shape 
        r_ pieceShape

    ___ setShape  shape):
        table _ TetrixPiece.coordsTable[shape]
        ___ i __ ra..(4):
            ___ j __ ra..(2):
                coords[i][j] _ table[i][j]

        pieceShape _ shape

    ___ setRandomShape 
        setShape(random.randint(1, 7))

    ___ x  index):
        r_ coords[index][0]

    ___ y  index):
        r_ coords[index][1]

    ___ setX  index, x):
        coords[index][0] _ x

    ___ setY  index, y):
        coords[index][1] _ y

    ___ minX 
        m _ coords[0][0]
        ___ i __ ra..(4):
            m _ min(m, coords[i][0])

        r_ m

    ___ maxX 
        m _ coords[0][0]
        ___ i __ ra..(4):
            m _ max(m, coords[i][0])

        r_ m

    ___ minY 
        m _ coords[0][1]
        ___ i __ ra..(4):
            m _ min(m, coords[i][1])

        r_ m

    ___ maxY 
        m _ coords[0][1]
        ___ i __ ra..(4):
            m _ max(m, coords[i][1])

        r_ m

    ___ rotatedLeft 
        __ pieceShape __ SquareShape:
            r_ self

        result _ TetrixPiece()
        result.pieceShape _ pieceShape
        ___ i __ ra..(4):
            result.setX(i, y(i))
            result.setY(i, -x(i))

        r_ result

    ___ rotatedRight 
        __ pieceShape __ SquareShape:
            r_ self

        result _ TetrixPiece()
        result.pieceShape _ pieceShape
        ___ i __ ra..(4):
            result.setX(i, -y(i))
            result.setY(i, x(i))

        r_ result


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ TetrixWindow()
    window.s..
    random.seed(N..)
    ___.e.. ?.e..
