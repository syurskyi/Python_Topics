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


____ ?.QtCore ______ QAbstractItemModel, QFile, QIODevice, QModelIndex, Qt
____ ?.?W.. ______ QApplication, QTreeView

______ simpletreemodel_rc


class TreeItem(object):
    ___ __init__(self, data, parent_None):
        self.parentItem _ parent
        self.itemData _ data
        self.childItems _ []

    ___ appendChild(self, item):
        self.childItems.append(item)

    ___ child(self, row):
        return self.childItems[row]

    ___ childCount(self):
        return len(self.childItems)

    ___ columnCount(self):
        return len(self.itemData)

    ___ data(self, column):
        try:
            return self.itemData[column]
        except IndexError:
            return None

    ___ parent(self):
        return self.parentItem

    ___ row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)

        return 0


class TreeModel(QAbstractItemModel):
    ___ __init__(self, data, parent_None):
        super(TreeModel, self).__init__(parent)

        self.rootItem _ TreeItem(("Title", "Summary"))
        self.setupModelData(data.split('\n'), self.rootItem)

    ___ columnCount(self, parent):
        if parent.isValid
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    ___ data(self, index, role):
        if not index.isValid
            return None

        if role !_ Qt.DisplayRole:
            return None

        item _ index.internalPointer()

        return item.data(index.column())

    ___ flags(self, index):
        if not index.isValid
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    ___ headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    ___ index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid
            parentItem _ self.rootItem
        else:
            parentItem _ parent.internalPointer()

        childItem _ parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    ___ parent(self, index):
        if not index.isValid
            return QModelIndex()

        childItem _ index.internalPointer()
        parentItem _ childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    ___ rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid
            parentItem _ self.rootItem
        else:
            parentItem _ parent.internalPointer()

        return parentItem.childCount()

    ___ setupModelData(self, lines, parent):
        parents _ [parent]
        indentations _ [0]

        number _ 0

        while number < len(lines):
            position _ 0
            while position < len(lines[number]):
                if lines[number][position] !_ ' ':
                    break
                position +_ 1

            lineData _ lines[number][position:].trimmed()

            if lineData:
                # Read the column data from the rest of the line.
                columnData _ [s for s in lineData.split('\t') if s]

                if position > indentations[-1]:
                    # The last child of the current parent is now the new
                    # parent unless the current parent has no children.

                    if parents[-1].childCount() > 0:
                        parents.append(parents[-1].child(parents[-1].childCount() - 1))
                        indentations.append(position)

                else:
                    while position < indentations[-1] and len(parents) > 0:
                        parents.pop()
                        indentations.pop()

                # Append a new item to the current parent's list of children.
                parents[-1].appendChild(TreeItem(columnData, parents[-1]))

            number +_ 1


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)

    f _ QFile(':/default.txt')
    f.open(QIODevice.ReadOnly)
    model _ TreeModel(f.readAll())
    f.close()

    view _ QTreeView()
    view.setModel(model)
    view.setWindowTitle("Simple Tree Model")
    view.s..
    sys.exit(app.exec_())
