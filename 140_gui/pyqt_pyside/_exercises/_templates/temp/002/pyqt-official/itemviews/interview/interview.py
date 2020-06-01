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


____ ?.QtCore ______ (QAbstractItemModel, QFileInfo, QItemSelectionModel,
        QModelIndex, Qt)
____ ?.?G.. ______ QIcon
____ ?.?W.. ______ (QAbstractItemView, ?A..,
        QFileIconProvider, QListView, QSplitter, QTableView, QTreeView)


images_dir _ QFileInfo(__file__).absolutePath() + '/images'


c_ Node(object):
    ___ __init__  parent _ N..):
        self.parent _ parent
        self.children _ []


c_ Model(QAbstractItemModel):
    ___ __init__  rows, columns, parent _ N..):
        super(Model, self).__init__(parent)
        self.services _ QIcon(images_dir + '/services.png')
        self.rc _ rows
        self.cc _ columns
        self.tree _ [Node() for node in range(rows)]
        self.iconProvider _ QFileIconProvider()

    ___ index  row, column, parent):
        __ row < self.rc and row >_ 0 and column < self.cc and column >_ 0:
            parentNode _ parent.internalPointer()
            childNode _ self.node(row, parentNode)
            __ childNode __ no. N..:
                r_ self.createIndex(row, column, childNode)
        r_ QModelIndex()

    ___ parent  child):
        __ isinstance(child, QModelIndex):
            # parent of QModelIndex child
            __ child.isValid
                childNode _ child.internalPointer()
                parentNode _ self.parent(childNode)
                __ parentNode:
                    r_ self.createIndex(self.row(parentNode), 0, parentNode)
            r_ QModelIndex()
        ____
            # parent of Node
            __ child:
                r_ child.parent

    ___ rowCount  parent):
        __ parent.isValid() and parent.column() !_ 0:
            r_ 0
        r_ self.rc

    ___ columnCount  parent):
        r_ self.cc

    ___ data  index, role):
        __ no. index.isValid
            r_ N..
        ____ role == Qt.DisplayRole:
            r_ "Item %d:%s" % (index.row(), index.column())
        ____ role == Qt.DecorationRole:
            __ index.column() == 0:
                r_ self.iconProvider.icon(QFileIconProvider.Folder)
            r_ self.iconProvider.icon(QFileIconProvider.File)
        r_ N..

    ___ headerData  section, orientation, role):
        __ role == Qt.DisplayRole:
            r_ str(section)
        __ role == Qt.DecorationRole:
            r_ self.services
        r_ super(Model, self).headerData(section, orientation, role)

    ___ hasChildren  parent):
        __ parent.isValid() and parent.column() !_ 0:
            r_ False
        r_ self.rc > 0 and self.cc > 0

    ___ flags  index):
        __ no. index.isValid
            r_ 0
        r_ Qt.ItemIsDragEnabled | super(Model, self).flags(index)

    ___ node  row, parent):
        __ parent and no. parent.children:
            parent.children _ [Node(parent) for node in range(self.rc)]
        __ parent:
            r_ parent.children[row]
        ____
            r_ self.tree[row]

    ___ row  node):
        __ node.parent:
            r_ node.parent.children.index(node)
        ____
            r_ self.tree.index(node)


___ main(args):
    app _ ?A..(args)
    page _ QSplitter()
    data _ Model(1000, 10, page)
    selections _ QItemSelectionModel(data)
    table _ QTableView()
    table.setModel(data)
    table.setSelectionModel(selections)
    table.horizontalHeader().setSectionsMovable(True)
    table.verticalHeader().setSectionsMovable(True)
    # Set StaticContents to enable minimal repaints on resizes.
    table.viewport().setAttribute(Qt.WA_StaticContents)
    page.addWidget(table)
    tree _ QTreeView()
    tree.setModel(data)
    tree.setSelectionModel(selections)
    tree.setUniformRowHeights(True)
    tree.header().setStretchLastSection F..
    tree.viewport().setAttribute(Qt.WA_StaticContents)
    # Disable the focus rect to get minimal repaints when scrolling on Mac.
    tree.setAttribute(Qt.WA_MacShowFocusRect, False)
    page.addWidget(tree)
    list _ QListView()
    list.setModel(data)
    list.setSelectionModel(selections)
    list.setViewMode(QListView.IconMode)
    list.setSelectionMode(QAbstractItemView.ExtendedSelection)
    list.setAlternatingRowColors F..
    list.viewport().setAttribute(Qt.WA_StaticContents)
    list.setAttribute(Qt.WA_MacShowFocusRect, False)
    page.addWidget(list)
    page.setWindowIcon(QIcon(images_dir + '/interview.png'))
    page.setWindowTitle("Interview")
    page.s..
    r_ app.e..


__ __name__ == '__main__':
    ______ sys
    main(sys.argv)
