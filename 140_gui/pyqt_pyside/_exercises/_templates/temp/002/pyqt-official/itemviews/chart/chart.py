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

____ ?.QtCore ______ (QByteArray, QFile, QItemSelection,
        QItemSelectionModel, QModelIndex, QPoint, QRect, QSize, Qt,
        QTextStream)
____ ?.QtGui ______ (QBrush, QColor, QFontMetrics, QPainter, QPainterPath,
        QPalette, QPen, QRegion, QStandardItemModel)
____ ?.?W.. ______ (QAbstractItemView, QApplication, QFileDialog,
        QMainWindow, QMenu, QRubberBand, QSplitter, QStyle, QTableView)

______ chart_rc


class PieView(QAbstractItemView):
    ___ __init__(self, parent_None):
        super(PieView, self).__init__(parent)

        self.horizontalScrollBar().setRange(0, 0)
        self.verticalScrollBar().setRange(0, 0)

        self.margin _ 8
        self.totalSize _ 300
        self.pieSize _ self.totalSize - 2*self.margin
        self.validItems _ 0
        self.totalValue _ 0.0
        self.origin _ QPoint()
        self.rubberBand _ None

    ___ dataChanged(self, topLeft, bottomRight, roles):
        super(PieView, self).dataChanged(topLeft, bottomRight, roles)

        self.validItems _ 0
        self.totalValue _ 0.0

        for row in range(self.model().rowCount(self.rootIndex())):

            index _ self.model().index(row, 1, self.rootIndex())
            value _ self.model().data(index)

            if value is not None and value > 0.0:
                self.totalValue +_ value
                self.validItems +_ 1

        self.viewport().update()

    ___ edit(self, index, trigger, event):
        if index.column() == 0:
            return super(PieView, self).edit(index, trigger, event)
        else:
            return False

    ___ indexAt(self, point):
        if self.validItems == 0:
            return QModelIndex()

        # Transform the view coordinates into contents widget coordinates.
        wx _ point.x() + self.horizontalScrollBar().value()
        wy _ point.y() + self.verticalScrollBar().value()

        if wx < self.totalSize:
            cx _ wx - self.totalSize/2
            cy _ self.totalSize/2 - wy; # positive cy for items above the center

            # Determine the distance from the center point of the pie chart.
            d _ (cx**2 + cy**2)**0.5

            if d == 0 or d > self.pieSize/2:
                return QModelIndex()

            # Determine the angle of the point.
            angle _ (180 / math.pi) * math.acos(cx/d)
            if cy < 0:
                angle _ 360 - angle

            # Find the relevant slice of the pie.
            startAngle _ 0.0

            for row in range(self.model().rowCount(self.rootIndex())):

                index _ self.model().index(row, 1, self.rootIndex())
                value _ self.model().data(index)

                if value > 0.0:
                    sliceAngle _ 360*value/self.totalValue

                    if angle >_ startAngle and angle < (startAngle + sliceAngle):
                        return self.model().index(row, 1, self.rootIndex())

                    startAngle +_ sliceAngle

        else:
            itemHeight _ QFontMetrics(self.viewOptions().font).height()
            listItem _ int((wy - self.margin) / itemHeight)
            validRow _ 0

            for row in range(self.model().rowCount(self.rootIndex())):

                index _ self.model().index(row, 1, self.rootIndex())
                if self.model().data(index) > 0.0:

                    if listItem == validRow:
                        return self.model().index(row, 0, self.rootIndex())

                    # Update the list index that corresponds to the next valid
                    # row.
                    validRow +_ 1

        return QModelIndex()

    ___ isIndexHidden(self, index):
        return False

    ___ itemRect(self, index):
        if not index.isValid
            return QRect()

        # Check whether the index's row is in the list of rows represented
        # by slices.

        if index.column() !_ 1:
            valueIndex _ self.model().index(index.row(), 1, self.rootIndex())
        else:
            valueIndex _ index

        value _ self.model().data(valueIndex)
        if value is not None and value > 0.0:

            listItem _ 0
            for row in range(index.row()-1, -1, -1):
                if self.model().data(self.model().index(row, 1, self.rootIndex())) > 0.0:
                    listItem +_ 1

            if index.column() == 0:
            
                itemHeight _ QFontMetrics(self.viewOptions().font).height()
                return QRect(self.totalSize,
                             int(self.margin + listItem*itemHeight),
                             self.totalSize - self.margin, int(itemHeight))
            elif index.column() == 1:
                return self.viewport().rect()

        return QRect()

    ___ itemRegion(self, index):
        if not index.isValid
            return QRegion()

        if index.column() !_ 1:
            return QRegion(self.itemRect(index))

        if self.model().data(index) <_ 0.0:
            return QRegion()

        startAngle _ 0.0
        for row in range(self.model().rowCount(self.rootIndex())):

            sliceIndex _ self.model().index(row, 1, self.rootIndex())
            value _ self.model().data(sliceIndex)

            if value > 0.0:
                angle _ 360*value/self.totalValue

                if sliceIndex == index:
                    slicePath _ QPainterPath()
                    slicePath.moveTo(self.totalSize/2, self.totalSize/2)
                    slicePath.arcTo(self.margin, self.margin,
                            self.margin+self.pieSize, self.margin+self.pieSize,
                            startAngle, angle)
                    slicePath.closeSubpath()

                    return QRegion(slicePath.toFillPolygon().toPolygon())

                startAngle +_ angle

        return QRegion()

    ___ horizontalOffset(self):
        return self.horizontalScrollBar().value()

    ___ mousePressEvent(self, event):
        super(PieView, self).mousePressEvent(event)

        self.origin _ event.pos()
        if not self.rubberBand:
            self.rubberBand _ QRubberBand(QRubberBand.Rectangle, self)
        self.rubberBand.setGeometry(QRect(self.origin, QSize()))
        self.rubberBand.s..

    ___ mouseMoveEvent(self, event):
        if self.rubberBand:
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

        super(PieView, self).mouseMoveEvent(event)

    ___ mouseReleaseEvent(self, event):
        super(PieView, self).mouseReleaseEvent(event)

        if self.rubberBand:
            self.rubberBand.hide()

        self.viewport().update()

    ___ moveCursor(self, cursorAction, modifiers):
        current _ self.currentIndex()

        if cursorAction in (QAbstractItemView.MoveLeft, QAbstractItemView.MoveUp):

            if current.row() > 0:
                current _ self.model().index(current.row() - 1,
                        current.column(), self.rootIndex())
            else:
                current _ self.model().index(0, current.column(),
                        self.rootIndex())

        elif cursorAction in (QAbstractItemView.MoveRight, QAbstractItemView.MoveDown):

            if current.row() < self.rows(current) - 1:
                current _ self.model().index(current.row() + 1,
                        current.column(), self.rootIndex())
            else:
                current _ self.model().index(self.rows(current) - 1,
                        current.column(), self.rootIndex())

        self.viewport().update()
        return current

    ___ paintEvent(self, event):
        selections _ self.selectionModel()
        option _ self.viewOptions()
        state _ option.state

        background _ option.palette.base()
        foreground _ QPen(option.palette.color(QPalette.WindowText))
        textPen _ QPen(option.palette.color(QPalette.Text))
        highlightedPen _ QPen(option.palette.color(QPalette.HighlightedText))

        painter _ QPainter(self.viewport())
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(event.rect(), background)
        painter.setPen(foreground)

        # Viewport rectangles
        pieRect _ QRect(self.margin, self.margin, self.pieSize,
                self.pieSize)
        keyPoint _ QPoint(self.totalSize - self.horizontalScrollBar().value(),
                self.margin - self.verticalScrollBar().value())

        if self.validItems > 0:
            painter.save()
            painter.translate(pieRect.x() - self.horizontalScrollBar().value(),
                    pieRect.y() - self.verticalScrollBar().value())
            painter.drawEllipse(0, 0, self.pieSize, self.pieSize)
            startAngle _ 0.0

            for row in range(self.model().rowCount(self.rootIndex())):

                index _ self.model().index(row, 1, self.rootIndex())
                value _ self.model().data(index)

                if value > 0.0:
                    angle _ 360*value/self.totalValue

                    colorIndex _ self.model().index(row, 0, self.rootIndex())
                    color _ self.model().data(colorIndex, Qt.DecorationRole)

                    if self.currentIndex() == index:
                        painter.setBrush(QBrush(color, Qt.Dense4Pattern))
                    elif selections.isSelected(index):
                        painter.setBrush(QBrush(color, Qt.Dense3Pattern))
                    else:
                        painter.setBrush(QBrush(color))

                    painter.drawPie(0, 0, self.pieSize, self.pieSize,
                            int(startAngle*16), int(angle*16))

                    startAngle +_ angle

            painter.restore()

            keyNumber _ 0

            for row in range(self.model().rowCount(self.rootIndex())):
                index _ self.model().index(row, 1, self.rootIndex())
                value _ self.model().data(index)

                if value > 0.0:
                    labelIndex _ self.model().index(row, 0, self.rootIndex())

                    option _ self.viewOptions()
                    option.rect _ self.visualRect(labelIndex)
                    if selections.isSelected(labelIndex):
                        option.state |_ QStyle.State_Selected
                    if self.currentIndex() == labelIndex:
                        option.state |_ QStyle.State_HasFocus
                    self.itemDelegate().paint(painter, option, labelIndex)

                    keyNumber +_ 1

    ___ resizeEvent(self, event):
        self.updateGeometries()

    ___ rows(self, index):
        return self.model().rowCount(self.model().parent(index))

    ___ rowsInserted(self, parent, start, end):
        for row in range(start, end + 1):
            index _ self.model().index(row, 1, self.rootIndex())
            value _ self.model().data(index)

            if value is not None and value > 0.0:
                self.totalValue +_ value
                self.validItems +_ 1

        super(PieView, self).rowsInserted(parent, start, end)

    ___ rowsAboutToBeRemoved(self, parent, start, end):
        for row in range(start, end + 1):
            index _ self.model().index(row, 1, self.rootIndex())
            value _ self.model().data(index)

            if value is not None and value > 0.0:
                self.totalValue -_ value
                self.validItems -_ 1

        super(PieView, self).rowsAboutToBeRemoved(parent, start, end)

    ___ scrollContentsBy(self, dx, dy):
        self.viewport().scroll(dx, dy)

    ___ scrollTo(self, index, ScrollHint):
        area _ self.viewport().rect()
        rect _ self.visualRect(index)

        if rect.left() < area.left
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() + rect.left() - area.left())
        elif rect.right() > area.right
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() + min(
                    rect.right() - area.right(), rect.left() - area.left()))

        if rect.top() < area.top
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() + rect.top() - area.top())
        elif rect.bottom() > area.bottom
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() + min(
                    rect.bottom() - area.bottom(), rect.top() - area.top()))

    ___ setSelection(self, rect, command):
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
                if region.intersects(QRegion(contentsRect)):
                    indexes.append(index)

        if len(indexes) > 0:
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
        else:
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
        return self.verticalScrollBar().value()

    ___ visualRect(self, index):
        rect _ self.itemRect(index)
        if rect.isValid
            return QRect(rect.left() - self.horizontalScrollBar().value(),
                         rect.top() - self.verticalScrollBar().value(),
                         rect.width(), rect.height())
        else:
            return rect

    ___ visualRegionForSelection(self, selection):
        region _ QRegion()

        for span in selection:
            for row in range(span.top(), span.bottom() + 1):
                for col in range(span.left(), span.right() + 1):
                    index _ self.model().index(row, col, self.rootIndex())
                    region +_ self.visualRect(index)

        return region


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        fileMenu _ QMenu("&File", self)
        openAction _ fileMenu.addAction("&Open...")
        openAction.setShortcut("Ctrl+O")
        saveAction _ fileMenu.addAction("&Save As...")
        saveAction.setShortcut("Ctrl+S")
        quitAction _ fileMenu.addAction("E&xit")
        quitAction.setShortcut("Ctrl+Q")

        self.setupModel()
        self.setupViews()

        openAction.triggered.c..(self.openFile)
        saveAction.triggered.c..(self.saveFile)
        quitAction.triggered.c..(QApplication.instance().quit)

        self.menuBar().addMenu(fileMenu)
        self.statusBar()

        self.openFile(':/Charts/qtdata.cht')

        self.setWindowTitle("Chart")
        self.resize(870, 550)

    ___ setupModel(self):
        self.model _ QStandardItemModel(8, 2, self)
        self.model.setHeaderData(0, Qt.Horizontal, "Label")
        self.model.setHeaderData(1, Qt.Horizontal, "Quantity")

    ___ setupViews(self):
        splitter _ QSplitter()
        table _ QTableView()
        self.pieChart _ PieView()
        splitter.addWidget(table)
        splitter.addWidget(self.pieChart)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)

        table.setModel(self.model)
        self.pieChart.setModel(self.model)

        self.selectionModel _ QItemSelectionModel(self.model)
        table.setSelectionModel(self.selectionModel)
        self.pieChart.setSelectionModel(self.selectionModel)

        table.horizontalHeader().setStretchLastSection(True)

        self.setCentralWidget(splitter)

    ___ openFile(self, path_None):
        if not path:
            path, _ _ QFileDialog.getOpenFileName(self, "Choose a data file",
                    '', '*.cht')

        if path:
            f _ QFile(path)

            if f.open(QFile.ReadOnly | QFile.Text):
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
                                QColor(pieces[2]), Qt.DecorationRole)

                    row +_ 1
                    line _ stream.readLine()

                f.close()
                self.statusBar().showMessage("Loaded %s" % path, 2000)

    ___ saveFile(self):
        fileName, _ _ QFileDialog.getSaveFileName(self, "Save file as", '',
                '*.cht')

        if fileName:
            f _ QFile(fileName)

            if f.open(QFile.WriteOnly | QFile.Text):
                for row in range(self.model.rowCount(QModelIndex())):
                    pieces _ []

                    pieces.append(
                            self.model.data(
                                    self.model.index(row, 0, QModelIndex()),
                                    Qt.DisplayRole))
                    pieces.append(
                            '%g' % self.model.data(
                                    self.model.index(row, 1, QModelIndex()),
                                    Qt.DisplayRole))
                    pieces.append(
                            self.model.data(
                                    self.model.index(row, 0, QModelIndex()),
                                    Qt.DecorationRole).name())

                    f.write(b','.join([p.encode('utf-8') for p in pieces]))
                    f.write(b'\n')

            f.close()
            self.statusBar().showMessage("Saved %s" % fileName, 2000)


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())
