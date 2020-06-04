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


____ ?.?C.. ______ QAbstractItemModel, QFile, QIODevice, QModelIndex, __
____ ?.?W.. ______ ?A.., QTreeView

______ simpletreemodel_rc


c_ TreeItem o..
    ___  -   data, parent_None):
        parentItem _ parent
        itemData _ data
        childItems _   # list

    ___ appendChild  item):
        childItems.ap..(item)

    ___ child  row):
        r_ childItems[row]

    ___ childCount 
        r_ le.(childItems)

    ___ columnCount 
        r_ le.(itemData)

    ___ data  column):
        ___
            r_ itemData[column]
        _____ IE..
            r_ N..

    ___ parent 
        r_ parentItem

    ___ row 
        __ parentItem:
            r_ parentItem.childItems.index

        r_ 0


c_ TreeModel(QAbstractItemModel):
    ___  -   data, parent_None):
        s__(TreeModel, self). - (parent)

        rootItem _ TreeItem(("Title", "Summary"))
        setupModelData(data.sp..('\n'), rootItem)

    ___ columnCount  parent):
        __ parent.isValid
            r_ parent.internalPointer().columnCount()
        ____
            r_ rootItem.columnCount()

    ___ data  index, role):
        __ no. index.isValid
            r_ N..

        __ role !_ __.DR..:
            r_ N..

        item _ index.internalPointer()

        r_ item.data(index.column())

    ___ flags  index):
        __ no. index.isValid
            r_ __.NoItemFlags

        r_ __.ItemIsEnabled | __.ItemIsSelectable

    ___ hD..  section, orientation, role):
        __ orientation __ __.H.. and role __ __.DR..:
            r_ rootItem.data(section)

        r_ N..

    ___ index  row, column, parent):
        __ no. hasIndex(row, column, parent):
            r_ QModelIndex()

        __ no. parent.isValid
            parentItem _ rootItem
        ____
            parentItem _ parent.internalPointer()

        childItem _ parentItem.child(row)
        __ childItem:
            r_ createIndex(row, column, childItem)
        ____
            r_ QModelIndex()

    ___ parent  index):
        __ no. index.isValid
            r_ QModelIndex()

        childItem _ index.internalPointer()
        parentItem _ childItem.parent()

        __ parentItem __ rootItem:
            r_ QModelIndex()

        r_ createIndex(parentItem.row(), 0, parentItem)

    ___ rowCount  parent):
        __ parent.column() > 0:
            r_ 0

        __ no. parent.isValid
            parentItem _ rootItem
        ____
            parentItem _ parent.internalPointer()

        r_ parentItem.childCount()

    ___ setupModelData  lines, parent):
        parents _ [parent]
        indentations _ [0]

        number _ 0

        w__ number < le.(lines):
            position _ 0
            w__ position < le.(lines[number]):
                __ lines[number][position] !_ ' ':
                    break
                position +_ 1

            lineData _ lines[number][position:].trimmed()

            __ lineData:
                # Read the column data from the rest of the line.
                columnData _ [s ___ s __ lineData.sp..('\t') __ s]

                __ position > indentations[-1]:
                    # The last child of the current parent is now the new
                    # parent unless the current parent has no children.

                    __ parents[-1].childCount() > 0:
                        parents.ap..(parents[-1].child(parents[-1].childCount() - 1))
                        indentations.ap..(position)

                ____
                    w__ position < indentations[-1] and le.(parents) > 0:
                        parents.p.. )
                        indentations.p.. )

                # Append a new item to the current parent's list of children.
                parents[-1].appendChild(TreeItem(columnData, parents[-1]))

            number +_ 1


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    f _ QFile(':/default.txt')
    f.o..(QIODevice.ReadOnly)
    model _ TreeModel(f.readAll())
    f.c..

    view _ ?TV..
    view.sM..(model)
    view.sWT..("Simple Tree Model")
    view.s..
    ___.e.. ?.e..
