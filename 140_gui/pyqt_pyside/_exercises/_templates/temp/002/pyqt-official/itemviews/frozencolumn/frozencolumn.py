#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2017 Hans-Peter Jansen <hpj@urpla.net>
## Copyright (C) 2016 The Qt Company Ltd.
##
## This file is part of the examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https:#www.qt.io/terms-conditions. For further
## information use the contact form at https:#www.qt.io/contact-us.
##
## BSD License Usage
## Alternatively, you may use self file under the terms of the BSD license
## as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, self list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, self list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from self software without specific prior written permission.
##
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
##
## $QT_END_LICENSE$
##
#############################################################################


____ ?.?C.. ______ QFile, QFileInfo, __
____ ?.?G.. ______ QStandardItem, QStandardItemModel
____ ?.?W.. ______ ?A.., QHeaderView, QTableView


c_ FreezeTableWidget(QTableView):
    ___ __init__  model):
        super(FreezeTableWidget, self).__init__()
        self.setModel(model)
        self.frozenTableView _ QTableView(self)
        self.init()
        self.horizontalHeader().sectionResized.c..(self.updateSectionWidth)
        self.verticalHeader().sectionResized.c..(self.updateSectionHeight)
        self.frozenTableView.verticalScrollBar().valueChanged.c..(
            self.verticalScrollBar().setValue)
        self.verticalScrollBar().valueChanged.c..(
            self.frozenTableView.verticalScrollBar().setValue)

    ___ init(self):
        self.frozenTableView.setModel(self.model())
        self.frozenTableView.sFP..(__.NF..)
        self.frozenTableView.verticalHeader().hide()
        self.frozenTableView.horizontalHeader().setSectionResizeMode(
                QHeaderView.Fixed)
        self.viewport().stackUnder(self.frozenTableView)

        self.frozenTableView.setStyleSheet('''
            QTableView { border: none;
                         background-color: #8EDE21;
                         selection-background-color: #999;
            }''') # for demo purposes

        self.frozenTableView.setSelectionModel(self.selectionModel())
        for col in range(1, self.model().columnCount()):
            self.frozenTableView.setColumnHidden(col, True)
        self.frozenTableView.setColumnWidth(0, self.columnWidth(0))
        self.frozenTableView.setHorizontalScrollBarPolicy(__.ScrollBarAlwaysOff)
        self.frozenTableView.setVerticalScrollBarPolicy(__.ScrollBarAlwaysOff)
        self.frozenTableView.s..
        self.updateFrozenTableGeometry()
        self.setHorizontalScrollMode(self.ScrollPerPixel)
        self.setVerticalScrollMode(self.ScrollPerPixel)
        self.frozenTableView.setVerticalScrollMode(self.ScrollPerPixel)

    ___ updateSectionWidth  logicalIndex, oldSize, newSize):
        __ self.logicalIndex == 0:
            self.frozenTableView.setColumnWidth(0, newSize)
            self.updateFrozenTableGeometry()

    ___ updateSectionHeight  logicalIndex, oldSize, newSize):
        self.frozenTableView.setRowHeight(logicalIndex, newSize)

    ___ resizeEvent  event):
        super(FreezeTableWidget, self).resizeEvent(event)
        self.updateFrozenTableGeometry()

    ___ moveCursor  cursorAction, modifiers):
        current _ super(FreezeTableWidget, self).moveCursor(cursorAction, modifiers)
        __ (cursorAction == self.MoveLeft and
                self.current.column() > 0 and
                self.visualRect(current).topLeft().x() <
                    self.frozenTableView.columnWidth(0)):
            newValue _ (self.horizontalScrollBar().value() +
                        self.visualRect(current).topLeft().x() -
                        self.frozenTableView.columnWidth(0))
            self.horizontalScrollBar().setValue(newValue)
        r_ current

    ___ scrollTo  index, hint):
        __ index.column() > 0:
            super(FreezeTableWidget, self).scrollTo(index, hint)

    ___ updateFrozenTableGeometry(self):
        self.frozenTableView.setGeometry(
                self.verticalHeader().width() + self.frameWidth(),
                self.frameWidth(), self.columnWidth(0),
                self.viewport().height() + self.horizontalHeader().height())


___ main(args):
    ___ split_and_strip(s, splitter):
        r_ [s.strip() for s in line.split(splitter)]

    app _ ?A..(args)
    model _ QStandardItemModel()
    file _ QFile(QFileInfo(__file__).absolutePath() + '/grades.txt')
    __ file.o..(QFile.ReadOnly):
        line _ file.readLine(200).decode('utf-8')
        header _ split_and_strip(line, ',')
        model.setHorizontalHeaderLabels(header)
        row _ 0
        w__ file.canReadLine
            line _ file.readLine(200).decode('utf-8')
            __ no. line.startswith('#') and ',' in line:
                fields _ split_and_strip(line, ',')
                for col, field in enumerate(fields):
                    newItem _ QStandardItem(field)
                    model.setItem(row, col, newItem)
                row +_ 1
    file.close()
    tableView _ FreezeTableWidget(model)
    tableView.setWindowTitle("Frozen Column Example")
    tableView.resize(560, 680)
    tableView.s..
    r_ app.e..


__ __name__ == '__main__':
    ______ sys
    main(sys.argv)
