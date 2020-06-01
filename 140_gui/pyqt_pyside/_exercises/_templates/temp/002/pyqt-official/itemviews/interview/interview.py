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


____ ?.?C.. ______ (QAbstractItemModel, QFileInfo, QItemSelectionModel,
        QModelIndex, __)
____ ?.?G.. ______ QIcon
____ ?.?W.. ______ (QAbstractItemView, ?A..,
        QFileIconProvider, QListView, QSplitter, QTableView, QTreeView)


images_dir _ QFileInfo(__file__).absolutePath() + '/images'


c_ Node(object):
    ___  -   parent _ N..):
        parent _ parent
        children _   # list


c_ Model(QAbstractItemModel):
    ___  -   rows, columns, parent _ N..):
        super(Model, self). - (parent)
        services _ QIcon(images_dir + '/services.png')
        rc _ rows
        cc _ columns
        tree _ [Node() ___ node __ range(rows)]
        iconProvider _ QFileIconProvider()

    ___ index  row, column, parent):
        __ row < rc and row >_ 0 and column < cc and column >_ 0:
            parentNode _ parent.internalPointer()
            childNode _ node(row, parentNode)
            __ childNode __ no. N..:
                r_ createIndex(row, column, childNode)
        r_ QModelIndex()

    ___ parent  child):
        __ isinstance(child, QModelIndex):
            # parent of QModelIndex child
            __ child.isValid
                childNode _ child.internalPointer()
                parentNode _ parent(childNode)
                __ parentNode:
                    r_ createIndex(row(parentNode), 0, parentNode)
            r_ QModelIndex()
        ____
            # parent of Node
            __ child:
                r_ child.parent

    ___ rowCount  parent):
        __ parent.isValid() and parent.column() !_ 0:
            r_ 0
        r_ rc

    ___ columnCount  parent):
        r_ cc

    ___ data  index, role):
        __ no. index.isValid
            r_ N..
        ____ role __ __.DisplayRole:
            r_ "Item %d:%s" % (index.row(), index.column())
        ____ role __ __.DecorationRole:
            __ index.column() __ 0:
                r_ iconProvider.icon(QFileIconProvider.Folder)
            r_ iconProvider.icon(QFileIconProvider.File)
        r_ N..

    ___ headerData  section, orientation, role):
        __ role __ __.DisplayRole:
            r_ str(section)
        __ role __ __.DecorationRole:
            r_ services
        r_ super(Model, self).headerData(section, orientation, role)

    ___ hasChildren  parent):
        __ parent.isValid() and parent.column() !_ 0:
            r_ False
        r_ rc > 0 and cc > 0

    ___ flags  index):
        __ no. index.isValid
            r_ 0
        r_ __.ItemIsDragEnabled | super(Model, self).flags(index)

    ___ node  row, parent):
        __ parent and no. parent.children:
            parent.children _ [Node(parent) ___ node __ range(rc)]
        __ parent:
            r_ parent.children[row]
        ____
            r_ tree[row]

    ___ row  node):
        __ node.parent:
            r_ node.parent.children.index(node)
        ____
            r_ tree.index(node)


___ main(args):
    app _ ?A..(args)
    page _ QSplitter()
    data _ Model(1000, 10, page)
    selections _ QItemSelectionModel(data)
    table _ QTableView()
    table.sM..(data)
    table.setSelectionModel(selections)
    table.horizontalHeader().setSectionsMovable( st.
    table.verticalHeader().setSectionsMovable( st.
    # Set StaticContents to enable minimal repaints on resizes.
    table.viewport().setAttribute(__.WA_StaticContents)
    page.aW..(table)
    tree _ ?TV..
    tree.sM..(data)
    tree.setSelectionModel(selections)
    tree.setUniformRowHeights( st.
    tree.header().setStretchLastSection F..
    tree.viewport().setAttribute(__.WA_StaticContents)
    # Disable the focus rect to get minimal repaints when scrolling on Mac.
    tree.setAttribute(__.WA_MacShowFocusRect, False)
    page.aW..(tree)
    list _ QListView()
    list.sM..(data)
    list.setSelectionModel(selections)
    list.setViewMode(QListView.IconMode)
    list.setSelectionMode(QAbstractItemView.ExtendedSelection)
    list.setAlternatingRowColors F..
    list.viewport().setAttribute(__.WA_StaticContents)
    list.setAttribute(__.WA_MacShowFocusRect, False)
    page.aW..(list)
    page.setWindowIcon(QIcon(images_dir + '/interview.png'))
    page.sWT..("Interview")
    page.s..
    r_ app.e..


__ ______ __ ______
    ______ ___
    main(___.a..
