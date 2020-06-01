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
____ ?.QtGui ______ QIcon
____ ?.?W.. ______ (QAbstractItemView, QApplication,
        QFileIconProvider, QListView, QSplitter, QTableView, QTreeView)


images_dir _ QFileInfo(__file__).absolutePath() + '/images'


class Node(object):
    ___ __init__(self, parent _ None):
        self.parent _ parent
        self.children _ []


class Model(QAbstractItemModel):
    ___ __init__(self, rows, columns, parent _ None):
        super(Model, self).__init__(parent)
        self.services _ QIcon(images_dir + '/services.png')
        self.rc _ rows
        self.cc _ columns
        self.tree _ [Node() for node in range(rows)]
        self.iconProvider _ QFileIconProvider()

    ___ index(self, row, column, parent):
        if row < self.rc and row >_ 0 and column < self.cc and column >_ 0:
            parentNode _ parent.internalPointer()
            childNode _ self.node(row, parentNode)
            if childNode is not None:
                return self.createIndex(row, column, childNode)
        return QModelIndex()

    ___ parent(self, child):
        if isinstance(child, QModelIndex):
            # parent of QModelIndex child
            if child.isValid
                childNode _ child.internalPointer()
                parentNode _ self.parent(childNode)
                if parentNode:
                    return self.createIndex(self.row(parentNode), 0, parentNode)
            return QModelIndex()
        else:
            # parent of Node
            if child:
                return child.parent

    ___ rowCount(self, parent):
        if parent.isValid() and parent.column() !_ 0:
            return 0
        return self.rc

    ___ columnCount(self, parent):
        return self.cc

    ___ data(self, index, role):
        if not index.isValid
            return None
        elif role == Qt.DisplayRole:
            return "Item %d:%s" % (index.row(), index.column())
        elif role == Qt.DecorationRole:
            if index.column() == 0:
                return self.iconProvider.icon(QFileIconProvider.Folder)
            return self.iconProvider.icon(QFileIconProvider.File)
        return None

    ___ headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            return str(section)
        if role == Qt.DecorationRole:
            return self.services
        return super(Model, self).headerData(section, orientation, role)

    ___ hasChildren(self, parent):
        if parent.isValid() and parent.column() !_ 0:
            return False
        return self.rc > 0 and self.cc > 0

    ___ flags(self, index):
        if not index.isValid
            return 0
        return Qt.ItemIsDragEnabled | super(Model, self).flags(index)

    ___ node(self, row, parent):
        if parent and not parent.children:
            parent.children _ [Node(parent) for node in range(self.rc)]
        if parent:
            return parent.children[row]
        else:
            return self.tree[row]

    ___ row(self, node):
        if node.parent:
            return node.parent.children.index(node)
        else:
            return self.tree.index(node)


___ main(args):
    app _ QApplication(args)
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
    tree.header().setStretchLastSection(False)
    tree.viewport().setAttribute(Qt.WA_StaticContents)
    # Disable the focus rect to get minimal repaints when scrolling on Mac.
    tree.setAttribute(Qt.WA_MacShowFocusRect, False)
    page.addWidget(tree)
    list _ QListView()
    list.setModel(data)
    list.setSelectionModel(selections)
    list.setViewMode(QListView.IconMode)
    list.setSelectionMode(QAbstractItemView.ExtendedSelection)
    list.setAlternatingRowColors(False)
    list.viewport().setAttribute(Qt.WA_StaticContents)
    list.setAttribute(Qt.WA_MacShowFocusRect, False)
    page.addWidget(list)
    page.setWindowIcon(QIcon(images_dir + '/interview.png'))
    page.setWindowTitle("Interview")
    page.s..
    return app.e..


if __name__ == '__main__':
    ______ sys
    main(sys.argv)
