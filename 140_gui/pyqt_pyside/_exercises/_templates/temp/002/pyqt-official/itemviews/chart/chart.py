#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2017 Riverbank Computing Limited.
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


______ math

____ ?.?C.. ______ (QByteArray, QFile, QItemSelection,
        QItemSelectionModel, QModelIndex, QPoint, QRect, QSize, __,
        QTextStream)
____ ?.?G.. ______ (QBrush, ?C.., QFontMetrics, QPainter, QPainterPath,
        ?P.., QPen, QRegion, QStandardItemModel)
____ ?.?W.. ______ (QAbstractItemView, ?A.., ?FD..,
        QMainWindow, QMenu, QRubberBand, QSplitter, QStyle, QTableView)

______ chart_rc


c_ PieView(QAbstractItemView):
    ___ __init__  parent_None):
        super(PieView, self).__init__(parent)

        self.horizontalScrollBar().setRange(0, 0)
        self.verticalScrollBar().setRange(0, 0)

        self.margin _ 8
        self.totalSize _ 300
        self.pieSize _ self.totalSize - 2*self.margin
        self.validItems _ 0
        self.totalValue _ 0.0
        self.origin _ QPoint()
        self.rubberBand _ N..

    ___ dataChanged  topLeft, bottomRight, roles):
        super(PieView, self).dataChanged(topLeft, bottomRight, roles)

        self.validItems _ 0
        self.totalValue _ 0.0

        for row in range(self.model().rowCount(self.rootIndex())):

            index _ self.model().index(row, 1, self.rootIndex())
            value _ self.model().data(index)

            __ value __ no. N.. and value > 0.0:
                self.totalValue +_ value
                self.validItems +_ 1

        self.viewport().update()

    ___ edit  index, trigger, event):
        __ index.column() == 0:
            r_ super(PieView, self).edit(index, trigger, event)
        ____
            r_ False

    ___ indexAt  point):
        __ self.validItems == 0:
            r_ QModelIndex()

        # Transform the view coordinates into contents widget coordinates.
        wx _ point.x() + self.horizontalScrollBar().value()
        wy _ point.y() + self.verticalScrollBar().value()

        __ wx < self.totalSize:
            cx _ wx - self.totalSize/2
            cy _ self.totalSize/2 - wy; # positive cy for items above the center

            # Determine the distance from the center point of the pie chart.
            d _ (cx**2 + cy**2)**0.5

            __ d == 0 or d > self.pieSize/2:
                r_ QModelIndex()

            # Determine the angle of the point.
            angle _ (180 / math.pi) * math.acos(cx/d)
            __ cy < 0:
                angle _ 360 - angle

            # Find the relevant slice of the pie.
            startAngle _ 0.0

            for row in range(self.model().rowCount(self.rootIndex())):

                index _ self.model().index(row, 1, self.rootIndex())
                value _ self.model().data(index)

                __ value > 0.0:
                    sliceAngle _ 360*value/self.totalValue

                    __ angle >_ startAngle and angle < (startAngle + sliceAngle):
                        r_ self.model().index(row, 1, self.rootIndex())

                    startAngle +_ sliceAngle

        ____
            itemHeight _ QFontMetrics(self.viewOptions().font).height()
            listItem _ int((wy - self.margin) / itemHeight)
            validRow _ 0

            for row in range(self.model().rowCount(self.rootIndex())):

                index _ self.model().index(row, 1, self.rootIndex())
                __ self.model().data(index) > 0.0:

                    __ listItem == validRow:
                        r_ self.model().index(row, 0, self.rootIndex())

                    # Update the list index that corresponds to the next valid
                    # row.
                    validRow +_ 1

        r_ QModelIndex()

    ___ isIndexHidden  index):
        r_ False

    ___ itemRect  index):
        __ no. index.isValid
            r_ QRect()

        # Check whether the index's row is in the list of rows represented
        # by slices.

        __ index.column() !_ 1:
            valueIndex _ self.model().index(index.row(), 1, self.rootIndex())
        ____
            valueIndex _ index

        value _ self.model().data(valueIndex)
        __ value __ no. N.. and value > 0.0:

            listItem _ 0
            for row in range(index.row()-1, -1, -1):
                __ self.model().data(self.model().index(row, 1, self.rootIndex())) > 0.0:
                    listItem +_ 1

            __ index.column() == 0:
            
                itemHeight _ QFontMetrics(self.viewOptions().font).height()
                r_ QRect(self.totalSize,
                             int(self.margin + listItem*itemHeight),
                             self.totalSize - self.margin, int(itemHeight))
            ____ index.column() == 1:
                r_ self.viewport().rect()

        r_ QRect()

    ___ itemRegion  index):
        __ no. index.isValid
            r_ QRegion()

        __ index.column() !_ 1:
            r_ QRegion(self.itemRect(index))

        __ self.model().data(index) <_ 0.0:
            r_ QRegion()

        startAngle _ 0.0
        for row in range(self.model().rowCount(self.rootIndex())):

            sliceIndex _ self.model().index(row, 1, self.rootIndex())
            value _ self.model().data(sliceIndex)

            __ value > 0.0:
                angle _ 360*value/self.totalValue

                __ sliceIndex == index:
                    slicePath _ QPainterPath()
                    slicePath.moveTo(self.totalSize/2, self.totalSize/2)
                    slicePath.arcTo(self.margin, self.margin,
                            self.margin+self.pieSize, self.margin+self.pieSize,
                            startAngle, angle)
                    slicePath.closeSubpath()

                    r_ QRegion(slicePath.toFillPolygon().toPolygon())

                startAngle +_ angle

        r_ QRegion()

    ___ horizontalOffset(self):
        r_ self.horizontalScrollBar().value()

    ___ mousePressEvent  event):
        super(PieView, self).mousePressEvent(event)

        self.origin _ event.pos()
        __ no. self.rubberBand:
            self.rubberBand _ QRubberBand(QRubberBand.Rectangle, self)
        self.rubberBand.setGeometry(QRect(self.origin, QSize()))
        self.rubberBand.s..

    ___ mouseMoveEvent  event):
        __ self.rubberBand:
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

        super(PieView, self).mouseMoveEvent(event)

    ___ mouseReleaseEvent  event):
        super(PieView, self).mouseReleaseEvent(event)

        __ self.rubberBand:
            self.rubberBand.hide()

        self.viewport().update()

    ___ moveCursor  cursorAction, modifiers):
        current _ self.currentIndex()

        __ cursorAction in (QAbstractItemView.MoveLeft, QAbstractItemView.MoveUp):

            __ current.row() > 0:
                current _ self.model().index(current.row() - 1,
                        current.column(), self.rootIndex())
            ____
                current _ self.model().index(0, current.column(),
                        self.rootIndex())

        ____ cursorAction in (QAbstractItemView.MoveRight, QAbstractItemView.MoveDown):

            __ current.row() < self.rows(current) - 1:
                current _ self.model().index(current.row() + 1,
                        current.column(), self.rootIndex())
            ____
                current _ self.model().index(self.rows(current) - 1,
                        current.column(), self.rootIndex())

        self.viewport().update()
        r_ current

    ___ paintEvent  event):
        selections _ self.selectionModel()
        option _ self.viewOptions()
        state _ option.state

        background _ option.palette.base()
        foreground _ QPen(option.palette.color(?P...WindowText))
        textPen _ QPen(option.palette.color(?P...Text))
        highlightedPen _ QPen(option.palette.color(?P...HighlightedText))

        painter _ QPainter(self.viewport())
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(event.rect(), background)
        painter.setPen(foreground)

        # Viewport rectangles
        pieRect _ QRect(self.margin, self.margin, self.pieSize,
                self.pieSize)
        keyPoint _ QPoint(self.totalSize - self.horizontalScrollBar().value(),
                self.margin - self.verticalScrollBar().value())

        __ self.validItems > 0:
            painter.save()
            painter.translate(pieRect.x() - self.horizontalScrollBar().value(),
                    pieRect.y() - self.verticalScrollBar().value())
            painter.drawEllipse(0, 0, self.pieSize, self.pieSize)
            startAngle _ 0.0

            for row in range(self.model().rowCount(self.rootIndex())):

                index _ self.model().index(row, 1, self.rootIndex())
                value _ self.model().data(index)

                __ value > 0.0:
                    angle _ 360*value/self.totalValue

                    colorIndex _ self.model().index(row, 0, self.rootIndex())
                    color _ self.model().data(colorIndex, __.DecorationRole)

                    __ self.currentIndex() == index:
                        painter.setBrush(QBrush(color, __.Dense4Pattern))
                    ____ selections.isSelected(index):
                        painter.setBrush(QBrush(color, __.Dense3Pattern))
                    ____
                        painter.setBrush(QBrush(color))

                    painter.drawPie(0, 0, self.pieSize, self.pieSize,
                            int(startAngle*16), int(angle*16))

                    startAngle +_ angle

            painter.restore()

            keyNumber _ 0

            for row in range(self.model().rowCount(self.rootIndex())):
                index _ self.model().index(row, 1, self.rootIndex())
                value _ self.model().data(index)

                __ value > 0.0:
                    labelIndex _ self.model().index(row, 0, self.rootIndex())

                    option _ self.viewOptions()
                    option.rect _ self.visualRect(labelIndex)
                    __ selections.isSelected(labelIndex):
                        option.state |_ QStyle.State_Selected
                    __ self.currentIndex() == labelIndex:
                        option.state |_ QStyle.State_HasFocus
                    self.itemDelegate().paint(painter, option, labelIndex)

                    keyNumber +_ 1

    ___ resizeEvent  event):
        self.updateGeometries()

    ___ rows  index):
        r_ self.model().rowCount(self.model().parent(index))

    ___ rowsInserted  parent, start, end):
        for row in range(start, end + 1):
            index _ self.model().index(row, 1, self.rootIndex())
            value _ self.model().data(index)

            __ value __ no. N.. and value > 0.0:
                self.totalValue +_ value
                self.validItems +_ 1

        super(PieView, self).rowsInserted(parent, start, end)

    ___ rowsAboutToBeRemoved  parent, start, end):
        for row in range(start, end + 1):
            index _ self.model().index(row, 1, self.rootIndex())
            value _ self.model().data(index)

            __ value __ no. N.. and value > 0.0:
                self.totalValue -_ value
                self.validItems -_ 1

        super(PieView, self).rowsAboutToBeRemoved(parent, start, end)

    ___ scrollContentsBy  dx, dy):
        self.viewport().scroll(dx, dy)

    ___ scrollTo  index, ScrollHint):
        area _ self.viewport().rect()
        rect _ self.visualRect(index)

        __ rect.left() < area.left
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() + rect.left() - area.left())
        ____ rect.right() > area.right
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() + min(
                    rect.right() - area.right(), rect.left() - area.left()))

        __ rect.top() < area.top
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() + rect.top() - area.top())
        ____ rect.bottom() > area.bottom
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() + min(
                    rect.bottom() - area.bottom(), rect.top() - area.top()))

    ___ setSelection  rect, command):
        # Use content widget coordinates because we will use the itemRegion()
        # function to check for intersections.

        contentsRect _ rect.translated(self.horizontalScrollBar().value(),
                self.verticalScrollBar().value()).normalized()

        rows _ self.model().rowCount(self.rootIndex())
        columns _ self.model().columnCount(self.rootIndex())
        indexes _ []

        for row in range(rows):
            for column in range(columns):
                index _ self.model().index(row, column, self.rootIndex())
                region _ self.itemRegion(index)
                __ region.intersects(QRegion(contentsRect)):
                    indexes.append(index)

        __ len(indexes) > 0:
            firstRow _ indexes[0].row()
            lastRow _ indexes[0].row()
            firstColumn _ indexes[0].column()
            lastColumn _ indexes[0].column()

            for i in range(1, len(indexes)):
                firstRow _ min(firstRow, indexes[i].row())
                lastRow _ max(lastRow, indexes[i].row())
                firstColumn _ min(firstColumn, indexes[i].column())
                lastColumn _ max(lastColumn, indexes[i].column())

            selection _ QItemSelection(
                self.model().index(firstRow, firstColumn, self.rootIndex()),
                self.model().index(lastRow, lastColumn, self.rootIndex()))
            self.selectionModel().select(selection, command)
        ____
            noIndex _ QModelIndex()
            selection _ QItemSelection(noIndex, noIndex)
            self.selectionModel().select(selection, command)

        self.update()

    ___ updateGeometries(self):
        self.horizontalScrollBar().setPageStep(self.viewport().width())
        self.horizontalScrollBar().setRange(0, max(0, 2*self.totalSize - self.viewport().width()))
        self.verticalScrollBar().setPageStep(self.viewport().height())
        self.verticalScrollBar().setRange(0, max(0, self.totalSize - self.viewport().height()))

    ___ verticalOffset(self):
        r_ self.verticalScrollBar().value()

    ___ visualRect  index):
        rect _ self.itemRect(index)
        __ rect.isValid
            r_ QRect(rect.left() - self.horizontalScrollBar().value(),
                         rect.top() - self.verticalScrollBar().value(),
                         rect.width(), rect.height())
        ____
            r_ rect

    ___ visualRegionForSelection  selection):
        region _ QRegion()

        for span in selection:
            for row in range(span.top(), span.bottom() + 1):
                for col in range(span.left(), span.right() + 1):
                    index _ self.model().index(row, col, self.rootIndex())
                    region +_ self.visualRect(index)

        r_ region


c_ MainWindow ?MW..
    ___ __init__(self):
        super(MainWindow, self).__init__()

        fileMenu _ QMenu("&File", self)
        openAction _ fileMenu.aA..("&Open...")
        openAction.sS..("Ctrl+O")
        saveAction _ fileMenu.aA..("&Save As...")
        saveAction.sS..("Ctrl+S")
        quitAction _ fileMenu.aA..("E&xit")
        quitAction.sS..("Ctrl+Q")

        self.setupModel()
        self.setupViews()

        openAction.t__.c..(self.openFile)
        saveAction.t__.c..(self.saveFile)
        quitAction.t__.c..(?A...instance().quit)

        self.mB.. .aM..(fileMenu)
        self.statusBar()

        self.openFile(':/Charts/qtdata.cht')

        self.setWindowTitle("Chart")
        self.resize(870, 550)

    ___ setupModel(self):
        self.model _ QStandardItemModel(8, 2, self)
        self.model.setHeaderData(0, __.Horizontal, "Label")
        self.model.setHeaderData(1, __.Horizontal, "Quantity")

    ___ setupViews(self):
        splitter _ QSplitter()
        table _ QTableView()
        self.pieChart _ PieView()
        splitter.aW..(table)
        splitter.aW..(self.pieChart)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)

        table.setModel(self.model)
        self.pieChart.setModel(self.model)

        self.selectionModel _ QItemSelectionModel(self.model)
        table.setSelectionModel(self.selectionModel)
        self.pieChart.setSelectionModel(self.selectionModel)

        table.horizontalHeader().setStretchLastSection(True)

        self.sCW..(splitter)

    ___ openFile  path_None):
        __ no. path:
            path, _ _ ?FD...gOFN..  "Choose a data file",
                    '', '*.cht')

        __ path:
            f _ QFile(path)

            __ f.o..(QFile.ReadOnly | QFile.Text):
                stream _ QTextStream(f)

                self.model.removeRows(0, self.model.rowCount(QModelIndex()),
                        QModelIndex())

                row _ 0
                line _ stream.readLine()
                while line:
                    self.model.insertRows(row, 1, QModelIndex())

                    pieces _ line.split(',')
                    self.model.setData(self.model.index(row, 0, QModelIndex()),
                                pieces[0])
                    self.model.setData(self.model.index(row, 1, QModelIndex()),
                                float(pieces[1]))
                    self.model.setData(self.model.index(row, 0, QModelIndex()),
                                ?C..(pieces[2]), __.DecorationRole)

                    row +_ 1
                    line _ stream.readLine()

                f.close()
                self.statusBar().showMessage("Loaded %s" % path, 2000)

    ___ saveFile(self):
        fileName, _ _ ?FD...getSaveFileName  "Save file as", '',
                '*.cht')

        __ fileName:
            f _ QFile(fileName)

            __ f.o..(QFile.WriteOnly | QFile.Text):
                for row in range(self.model.rowCount(QModelIndex())):
                    pieces _ []

                    pieces.append(
                            self.model.data(
                                    self.model.index(row, 0, QModelIndex()),
                                    __.DisplayRole))
                    pieces.append(
                            '%g' % self.model.data(
                                    self.model.index(row, 1, QModelIndex()),
                                    __.DisplayRole))
                    pieces.append(
                            self.model.data(
                                    self.model.index(row, 0, QModelIndex()),
                                    __.DecorationRole).name())

                    f.w..(b','.join([p.encode('utf-8') for p in pieces]))
                    f.w..(b'\n')

            f.close()
            self.statusBar().showMessage("Saved %s" % fileName, 2000)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())
