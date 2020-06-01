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

____ ?.?C.. ______ pyqtSignal, QBasicTimer, QSize, __
____ ?.?G.. ______ ?C.., QPainter, QPixmap
____ ?.?W.. ______ (?A.., QFrame, QGridLayout, QLabel,
        QLCDNumber, ?PB.., QWidget)


NoShape, ZShape, SShape, LineShape, TShape, SquareShape, LShape, MirroredLShape _ range(8)


c_ TetrixWindow(QWidget):
    ___ __init__(self):
        super(TetrixWindow, self).__init__()

        self.board _ TetrixBoard()

        nextPieceLabel _ QLabel()
        nextPieceLabel.setFrameStyle(QFrame.Box | QFrame.Raised)
        nextPieceLabel.setAlignment(__.AlignCenter)
        self.board.setNextPieceLabel(nextPieceLabel)

        scoreLcd _ QLCDNumber(5)
        scoreLcd.setSegmentStyle(QLCDNumber.Filled)
        levelLcd _ QLCDNumber(2)
        levelLcd.setSegmentStyle(QLCDNumber.Filled)
        linesLcd _ QLCDNumber(5)
        linesLcd.setSegmentStyle(QLCDNumber.Filled)

        startButton _ ?PB..("&Start")
        startButton.setFocusPolicy(__.NoFocus)
        quitButton _ ?PB..("&Quit")
        quitButton.setFocusPolicy(__.NoFocus)
        pauseButton _ ?PB..("&Pause")
        pauseButton.setFocusPolicy(__.NoFocus)

        startButton.c__.c..(self.board.start)
        pauseButton.c__.c..(self.board.pause)
        quitButton.c__.c..(?A...instance().quit)
        self.board.scoreChanged.c..(scoreLcd.display)
        self.board.levelChanged.c..(levelLcd.display)
        self.board.linesRemovedChanged.c..(linesLcd.display)

        layout _ QGridLayout()
        layout.addWidget(self.createLabel("NEXT"), 0, 0)
        layout.addWidget(nextPieceLabel, 1, 0)
        layout.addWidget(self.createLabel("LEVEL"), 2, 0)
        layout.addWidget(levelLcd, 3, 0)
        layout.addWidget(startButton, 4, 0)
        layout.addWidget(self.board, 0, 1, 6, 1)
        layout.addWidget(self.createLabel("SCORE"), 0, 2)
        layout.addWidget(scoreLcd, 1, 2)
        layout.addWidget(self.createLabel("LINES REMOVED"), 2, 2)
        layout.addWidget(linesLcd, 3, 2)
        layout.addWidget(quitButton, 4, 2)
        layout.addWidget(pauseButton, 5, 2)
        self.setLayout(layout)

        self.setWindowTitle("Tetrix")
        self.resize(550, 370)

    ___ createLabel  text):
        lbl _ QLabel(text)
        lbl.setAlignment(__.AlignHCenter | __.AlignBottom)
        r_ lbl


c_ TetrixBoard(QFrame):
    BoardWidth _ 10
    BoardHeight _ 22

    scoreChanged _ pyqtSignal(int)

    levelChanged _ pyqtSignal(int)

    linesRemovedChanged _ pyqtSignal(int)

    ___ __init__  parent_None):
        super(TetrixBoard, self).__init__(parent)

        self.timer _ QBasicTimer()
        self.nextPieceLabel _ N..
        self.isWaitingAfterLine _ False
        self.curPiece _ TetrixPiece()
        self.nextPiece _ TetrixPiece()
        self.curX _ 0
        self.curY _ 0
        self.numLinesRemoved _ 0
        self.numPiecesDropped _ 0
        self.score _ 0
        self.level _ 0
        self.board _ N..

        self.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.setFocusPolicy(__.StrongFocus)
        self.isStarted _ False
        self.isPaused _ False
        self.clearBoard()

        self.nextPiece.setRandomShape()

    ___ shapeAt  x, y):
        r_ self.board[(y * TetrixBoard.BoardWidth) + x]

    ___ setShapeAt  x, y, shape):
        self.board[(y * TetrixBoard.BoardWidth) + x] _ shape   

    ___ timeoutTime(self):
        r_ 1000 / (1 + self.level)

    ___ squareWidth(self):
        r_ self.contentsRect().width() / TetrixBoard.BoardWidth

    ___ squareHeight(self):
        r_ self.contentsRect().height() / TetrixBoard.BoardHeight

    ___ setNextPieceLabel  label):
        self.nextPieceLabel _ label

    ___ sizeHint(self):
        r_ QSize(TetrixBoard.BoardWidth * 15 + self.frameWidth() * 2,
                TetrixBoard.BoardHeight * 15 + self.frameWidth() * 2)

    ___ minimumSizeHint(self):
        r_ QSize(TetrixBoard.BoardWidth * 5 + self.frameWidth() * 2,
                TetrixBoard.BoardHeight * 5 + self.frameWidth() * 2)

    ___ start(self):
        __ self.isPaused:
            r_

        self.isStarted _ True
        self.isWaitingAfterLine _ False
        self.numLinesRemoved _ 0
        self.numPiecesDropped _ 0
        self.score _ 0
        self.level _ 1
        self.clearBoard()

        self.linesRemovedChanged.emit(self.numLinesRemoved)
        self.scoreChanged.emit(self.score)
        self.levelChanged.emit(self.level)

        self.newPiece()
        self.timer.start(self.timeoutTime(), self)

    ___ pause(self):
        __ no. self.isStarted:
            r_

        self.isPaused _ no. self.isPaused
        __ self.isPaused:
            self.timer.stop()
        ____
            self.timer.start(self.timeoutTime(), self)

        self.update()

    ___ paintEvent  event):
        super(TetrixBoard, self).paintEvent(event)

        painter _ QPainter(self)
        rect _ self.contentsRect()

        __ self.isPaused:
            painter.drawText(rect, __.AlignCenter, "Pause")
            r_

        boardTop _ rect.bottom() - TetrixBoard.BoardHeight * self.squareHeight()

        for i in range(TetrixBoard.BoardHeight):
            for j in range(TetrixBoard.BoardWidth):
                shape _ self.shapeAt(j, TetrixBoard.BoardHeight - i - 1)
                __ shape !_ NoShape:
                    self.drawSquare(painter,
                            rect.left() + j * self.squareWidth(),
                            boardTop + i * self.squareHeight(), shape)

        __ self.curPiece.shape() !_ NoShape:
            for i in range(4):
                x _ self.curX + self.curPiece.x(i)
                y _ self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                        boardTop + (TetrixBoard.BoardHeight - y - 1) * self.squareHeight(),
                        self.curPiece.shape())

    ___ keyPressEvent  event):
        __ no. self.isStarted or self.isPaused or self.curPiece.shape() == NoShape:
            super(TetrixBoard, self).keyPressEvent(event)
            r_

        key _ event.key()
        __ key == __.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
        ____ key == __.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
        ____ key == __.Key_Down:
            self.tryMove(self.curPiece.rotatedRight(), self.curX, self.curY)
        ____ key == __.Key_Up:
            self.tryMove(self.curPiece.rotatedLeft(), self.curX, self.curY)
        ____ key == __.Key_Space:
            self.dropDown()
        ____ key == __.Key_D:
            self.oneLineDown()
        ____
            super(TetrixBoard, self).keyPressEvent(event)

    ___ timerEvent  event):
        __ event.timerId() == self.timer.timerId
            __ self.isWaitingAfterLine:
                self.isWaitingAfterLine _ False
                self.newPiece()
                self.timer.start(self.timeoutTime(), self)
            ____
                self.oneLineDown()
        ____
            super(TetrixBoard, self).timerEvent(event)

    ___ clearBoard(self):
        self.board _ [NoShape for i in range(TetrixBoard.BoardHeight * TetrixBoard.BoardWidth)]

    ___ dropDown(self):
        dropHeight _ 0
        newY _ self.curY
        while newY > 0:
            __ no. self.tryMove(self.curPiece, self.curX, newY - 1):
                break
            newY -_ 1
            dropHeight +_ 1

        self.pieceDropped(dropHeight)

    ___ oneLineDown(self):
        __ no. self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped(0)

    ___ pieceDropped  dropHeight):
        for i in range(4):
            x _ self.curX + self.curPiece.x(i)
            y _ self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.numPiecesDropped +_ 1
        __ self.numPiecesDropped % 25 == 0:
            self.level +_ 1
            self.timer.start(self.timeoutTime(), self)
            self.levelChanged.emit(self.level)

        self.score +_ dropHeight + 7
        self.scoreChanged.emit(self.score)
        self.removeFullLines()

        __ no. self.isWaitingAfterLine:
            self.newPiece()

    ___ removeFullLines(self):
        numFullLines _ 0

        for i in range(TetrixBoard.BoardHeight - 1, -1, -1):
            lineIsFull _ True

            for j in range(TetrixBoard.BoardWidth):
                __ self.shapeAt(j, i) == NoShape:
                    lineIsFull _ False
                    break

            __ lineIsFull:
                numFullLines +_ 1
                for k in range(TetrixBoard.BoardHeight - 1):
                    for j in range(TetrixBoard.BoardWidth):
                        self.setShapeAt(j, k, self.shapeAt(j, k + 1))

                for j in range(TetrixBoard.BoardWidth):
                    self.setShapeAt(j, TetrixBoard.BoardHeight - 1, NoShape)

        __ numFullLines > 0:
            self.numLinesRemoved +_ numFullLines
            self.score +_ 10 * numFullLines
            self.linesRemovedChanged.emit(self.numLinesRemoved)
            self.scoreChanged.emit(self.score)

            self.timer.start(500, self)
            self.isWaitingAfterLine _ True
            self.curPiece.setShape(NoShape)
            self.update()

    ___ newPiece(self):
        self.curPiece _ copy.deepcopy(self.nextPiece)
        self.nextPiece.setRandomShape()
        self.showNextPiece()
        self.curX _ TetrixBoard.BoardWidth // 2 + 1
        self.curY _ TetrixBoard.BoardHeight - 1 + self.curPiece.minY()

        __ no. self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(NoShape)
            self.timer.stop()
            self.isStarted _ False

    ___ showNextPiece(self):
        __ self.nextPieceLabel __ N..:
            r_

        dx _ self.nextPiece.maxX() - self.nextPiece.minX() + 1
        dy _ self.nextPiece.maxY() - self.nextPiece.minY() + 1

        pixmap _ QPixmap(dx * self.squareWidth(), dy * self.squareHeight())
        painter _ QPainter(pixmap)
        painter.fillRect(pixmap.rect(), self.nextPieceLabel.palette().window())

        for i in range(4):
            x _ self.nextPiece.x(i) - self.nextPiece.minX()
            y _ self.nextPiece.y(i) - self.nextPiece.minY()
            self.drawSquare(painter, x * self.squareWidth(),
                    y * self.squareHeight(), self.nextPiece.shape())

        painter.end()

        self.nextPieceLabel.setPixmap(pixmap)

    ___ tryMove  newPiece, newX, newY):
        for i in range(4):
            x _ newX + newPiece.x(i)
            y _ newY - newPiece.y(i)
            __ x < 0 or x >_ TetrixBoard.BoardWidth or y < 0 or y >_ TetrixBoard.BoardHeight:
                r_ False
            __ self.shapeAt(x, y) !_ NoShape:
                r_ False

        self.curPiece _ newPiece
        self.curX _ newX
        self.curY _ newY
        self.update()
        r_ True

    ___ drawSquare  painter, x, y, shape):
        colorTable _ [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color _ ?C..(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


c_ TetrixPiece(object):
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

    ___ __init__(self):
        self.coords _ [[0, 0] for _ in range(4)]
        self.pieceShape _ NoShape

        self.setShape(NoShape)

    ___ shape(self):
        r_ self.pieceShape

    ___ setShape  shape):
        table _ TetrixPiece.coordsTable[shape]
        for i in range(4):
            for j in range(2):
                self.coords[i][j] _ table[i][j]

        self.pieceShape _ shape

    ___ setRandomShape(self):
        self.setShape(random.randint(1, 7))

    ___ x  index):
        r_ self.coords[index][0]

    ___ y  index):
        r_ self.coords[index][1]

    ___ setX  index, x):
        self.coords[index][0] _ x

    ___ setY  index, y):
        self.coords[index][1] _ y

    ___ minX(self):
        m _ self.coords[0][0]
        for i in range(4):
            m _ min(m, self.coords[i][0])

        r_ m

    ___ maxX(self):
        m _ self.coords[0][0]
        for i in range(4):
            m _ max(m, self.coords[i][0])

        r_ m

    ___ minY(self):
        m _ self.coords[0][1]
        for i in range(4):
            m _ min(m, self.coords[i][1])

        r_ m

    ___ maxY(self):
        m _ self.coords[0][1]
        for i in range(4):
            m _ max(m, self.coords[i][1])

        r_ m

    ___ rotatedLeft(self):
        __ self.pieceShape == SquareShape:
            r_ self

        result _ TetrixPiece()
        result.pieceShape _ self.pieceShape
        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        r_ result

    ___ rotatedRight(self):
        __ self.pieceShape == SquareShape:
            r_ self

        result _ TetrixPiece()
        result.pieceShape _ self.pieceShape
        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        r_ result


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ TetrixWindow()
    window.s..
    random.seed(N..)
    sys.exit(app.exec_())
