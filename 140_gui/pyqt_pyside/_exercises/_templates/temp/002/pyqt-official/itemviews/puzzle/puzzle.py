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

____ ?.QtCore ______ (pyqtSignal, QAbstractListModel, QByteArray,
        QDataStream, QIODevice, QMimeData, QModelIndex, QPoint, QRect, QSize,
        Qt)
____ ?.QtGui ______ QColor, QCursor, QDrag, QIcon, QPainter, QPixmap
____ ?.?W.. ______ (?A.., QFileDialog, QFrame, QHBoxLayout,
        QListView, QMainWindow, QMessageBox, QSizePolicy, QWidget)

______ puzzle_rc


class PuzzleWidget(QWidget):

    puzzleCompleted _ pyqtSignal()

    ___ __init__(self, parent_None):
        super(PuzzleWidget, self).__init__(parent)

        self.piecePixmaps _ []
        self.pieceRects _ []
        self.pieceLocations _ []
        self.highlightedRect _ QRect()
        self.inPlace _ 0

        self.setAcceptDrops(True)
        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)

    ___ clear(self):
        self.pieceLocations _ []
        self.piecePixmaps _ []
        self.pieceRects _ []
        self.highlightedRect _ QRect()
        self.inPlace _ 0
        self.update()

    ___ dragEnterEvent(self, event):
        if event.mimeData().hasFormat('image/x-puzzle-piece'):
            event.accept()
        else:
            event.ignore()

    ___ dragLeaveEvent(self, event):
        updateRect _ self.highlightedRect
        self.highlightedRect _ QRect()
        self.update(updateRect)
        event.accept()

    ___ dragMoveEvent(self, event):
        updateRect _ self.highlightedRect.united(self.targetSquare(event.pos()))

        if event.mimeData().hasFormat('image/x-puzzle-piece') and self.findPiece(self.targetSquare(event.pos())) == -1:
            self.highlightedRect _ self.targetSquare(event.pos())
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            self.highlightedRect _ QRect()
            event.ignore()

        self.update(updateRect)

    ___ dropEvent(self, event):
        if event.mimeData().hasFormat('image/x-puzzle-piece') and self.findPiece(self.targetSquare(event.pos())) == -1:
            pieceData _ event.mimeData().data('image/x-puzzle-piece')
            stream _ QDataStream(pieceData, QIODevice.ReadOnly)
            square _ self.targetSquare(event.pos())
            pixmap _ QPixmap()
            location _ QPoint()
            stream >> pixmap >> location

            self.pieceLocations.append(location)
            self.piecePixmaps.append(pixmap)
            self.pieceRects.append(square)

            self.hightlightedRect _ QRect()
            self.update(square)

            event.setDropAction(Qt.MoveAction)
            event.accept()

            if location == QPoint(square.x() / 80, square.y() / 80):
                self.inPlace +_ 1
                if self.inPlace == 25:
                    self.puzzleCompleted.emit()
        else:
            self.highlightedRect _ QRect()
            event.ignore()

    ___ findPiece(self, pieceRect):
        try:
            return self.pieceRects.index(pieceRect)
        except ValueError:
            return -1

    ___ mousePressEvent(self, event):
        square _ self.targetSquare(event.pos())
        found _ self.findPiece(square)

        if found == -1:
            return

        location _ self.pieceLocations[found]
        pixmap _ self.piecePixmaps[found]
        del self.pieceLocations[found]
        del self.piecePixmaps[found]
        del self.pieceRects[found]

        if location == QPoint(square.x() + 80, square.y() + 80):
            self.inPlace -_ 1

        self.update(square)

        itemData _ QByteArray()
        dataStream _ QDataStream(itemData, QIODevice.WriteOnly)

        dataStream << pixmap << location

        mimeData _ QMimeData()
        mimeData.setData('image/x-puzzle-piece', itemData)

        drag _ QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - square.topLeft())
        drag.setPixmap(pixmap)

        if drag.exec_(Qt.MoveAction) !_ Qt.MoveAction:
            self.pieceLocations.insert(found, location)
            self.piecePixmaps.insert(found, pixmap)
            self.pieceRects.insert(found, square)
            self.update(self.targetSquare(event.pos()))

            if location == QPoint(square.x() / 80, square.y() / 80):
                self.inPlace +_ 1

    ___ paintEvent(self, event):
        painter _ QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), Qt.white)

        if self.highlightedRect.isValid
            painter.setBrush(QColor("#ffcccc"))
            painter.setPen(Qt.NoPen)
            painter.drawRect(self.highlightedRect.adjusted(0, 0, -1, -1))

        for rect, pixmap in zip(self.pieceRects, self.piecePixmaps):
            painter.drawPixmap(rect, pixmap)

        painter.end()

    ___ targetSquare(self, position):
        return QRect(position.x() // 80 * 80, position.y() // 80 * 80, 80, 80)


class PiecesModel(QAbstractListModel):
    ___ __init__(self, parent_None):
        super(PiecesModel, self).__init__(parent)

        self.locations _ []
        self.pixmaps _ []

    ___ data(self, index, role_Qt.DisplayRole):
        if not index.isValid
            return None

        if role == Qt.DecorationRole:
            return QIcon(self.pixmaps[index.row()].scaled(
                    60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        if role == Qt.UserRole:
            return self.pixmaps[index.row()]

        if role == Qt.UserRole + 1:
            return self.locations[index.row()]

        return None

    ___ addPiece(self, pixmap, location):
        if random.random() < 0.5:
            row _ 0
        else:
            row _ len(self.pixmaps)

        self.beginInsertRows(QModelIndex(), row, row)
        self.pixmaps.insert(row, pixmap)
        self.locations.insert(row, location)
        self.endInsertRows()

    ___ flags(self,index):
        if index.isValid
            return (Qt.ItemIsEnabled | Qt.ItemIsSelectable |
                    Qt.ItemIsDragEnabled)

        return Qt.ItemIsDropEnabled

    ___ removeRows(self,row, count, parent):
        if parent.isValid
            return False

        if row >_ len(self.pixmaps) or row + count <_ 0:
            return False

        beginRow _ max(0, row)
        endRow _ min(row + count - 1, len(self.pixmaps) - 1)

        self.beginRemoveRows(parent, beginRow, endRow)

        del self.pixmaps[beginRow:endRow + 1]
        del self.locations[beginRow:endRow + 1]

        self.endRemoveRows()
        return True

    ___ mimeTypes(self):
        return ['image/x-puzzle-piece']

    ___ mimeData(self, indexes):
        mimeData _ QMimeData()
        encodedData _ QByteArray()

        stream _ QDataStream(encodedData, QIODevice.WriteOnly)

        for index in indexes:
            if index.isValid
                pixmap _ QPixmap(self.data(index, Qt.UserRole))
                location _ self.data(index, Qt.UserRole + 1)
                stream << pixmap << location

        mimeData.setData('image/x-puzzle-piece', encodedData)
        return mimeData

    ___ dropMimeData(self, data, action, row, column, parent):
        if not data.hasFormat('image/x-puzzle-piece'):
            return False

        if action == Qt.IgnoreAction:
            return True

        if column > 0:
            return False

        if not parent.isValid
            if row < 0:
                endRow _ len(self.pixmaps)
            else:
                endRow _ min(row, len(self.pixmaps))
        else:
            endRow _ parent.row()

        encodedData _ data.data('image/x-puzzle-piece')
        stream _ QDataStream(encodedData, QIODevice.ReadOnly)

        while not stream.atEnd
            pixmap _ QPixmap()
            location _ QPoint()
            stream >> pixmap >> location

            self.beginInsertRows(QModelIndex(), endRow, endRow)
            self.pixmaps.insert(endRow, pixmap)
            self.locations.insert(endRow, location)
            self.endInsertRows()

            endRow +_ 1

        return True

    ___ rowCount(self, parent):
        if parent.isValid
            return 0
        else:
            return len(self.pixmaps)

    ___ supportedDropActions(self):
        return Qt.CopyAction | Qt.MoveAction

    ___ addPieces(self, pixmap):
        self.beginRemoveRows(QModelIndex(), 0, 24)
        self.pixmaps _ []
        self.locations _ []
        self.endRemoveRows()

        for y in range(5):
            for x in range(5):
                pieceImage _ pixmap.copy(x*80, y*80, 80, 80)
                self.addPiece(pieceImage, QPoint(x, y))


class MainWindow(QMainWindow):
    ___ __init__(self, parent_None):
        super(MainWindow, self).__init__(parent)

        self.puzzleImage _ QPixmap()

        self.setupMenus()
        self.setupWidgets()

        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.setWindowTitle("Puzzle")

    ___ openImage(self, path_None):
        if not path:
            path, _ _ QFileDialog.getOpenFileName(self, "Open Image", '',
                    "Image Files (*.png *.jpg *.bmp)")

        if path:
            newImage _ QPixmap()
            if not newImage.load(path):
                QMessageBox.warning(self, "Open Image",
                        "The image file could not be loaded.",
                        QMessageBox.Cancel)
                return

            self.puzzleImage _ newImage
            self.setupPuzzle()

    ___ setCompleted(self):
        QMessageBox.information(self, "Puzzle Completed",
                "Congratulations! You have completed the puzzle!\nClick OK "
                "to start again.",
                QMessageBox.Ok)

        self.setupPuzzle()

    ___ setupPuzzle(self):
        size _ min(self.puzzleImage.width(), self.puzzleImage.height())
        self.puzzleImage _ self.puzzleImage.copy((self.puzzleImage.width()-size)/2,
                (self.puzzleImage.height() - size)/2, size, size).scaled(400,
                        400, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        random.seed(QCursor.pos().x() ^ QCursor.pos().y())

        self.model.addPieces(self.puzzleImage)
        self.puzzleWidget.clear()

    ___ setupMenus(self):
        fileMenu _ self.menuBar().addMenu("&File")

        openAction _ fileMenu.addAction("&Open...")
        openAction.setShortcut("Ctrl+O")

        exitAction _ fileMenu.addAction("E&xit")
        exitAction.setShortcut("Ctrl+Q")

        gameMenu _ self.menuBar().addMenu("&Game")

        restartAction _ gameMenu.addAction("&Restart")

        openAction.triggered.c..(self.openImage)
        exitAction.triggered.c..(?A...instance().quit)
        restartAction.triggered.c..(self.setupPuzzle)

    ___ setupWidgets(self):
        frame _ QFrame()
        frameLayout _ QHBoxLayout(frame)

        self.piecesList _ QListView()
        self.piecesList.setDragEnabled(True)
        self.piecesList.setViewMode(QListView.IconMode)
        self.piecesList.setIconSize(QSize(60,60))
        self.piecesList.setGridSize(QSize(80,80))
        self.piecesList.setSpacing(10)
        self.piecesList.setMovement(QListView.Snap)
        self.piecesList.setAcceptDrops(True)
        self.piecesList.setDropIndicatorShown(True)

        self.model _ PiecesModel(self)
        self.piecesList.setModel(self.model)

        self.puzzleWidget _ PuzzleWidget()

        self.puzzleWidget.puzzleCompleted.c..(self.setCompleted,
                Qt.QueuedConnection)

        frameLayout.addWidget(self.piecesList)
        frameLayout.addWidget(self.puzzleWidget)
        self.setCentralWidget(frame)


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.openImage(':/images/example.jpg')
    window.s..
    sys.exit(app.exec_())
