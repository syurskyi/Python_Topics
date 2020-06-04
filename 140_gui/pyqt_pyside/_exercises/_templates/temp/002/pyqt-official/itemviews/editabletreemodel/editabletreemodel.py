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


____ ?.?C.. ______ (QAbstractItemModel, QFile, QIODevice,
        QItemSelectionModel, QModelIndex, __)
____ ?.?W.. ______ ?A.., ?MW..

______ editabletreemodel_rc
____ ui_mainwindow ______ Ui_MainWindow


c_ TreeItem o..
    ___  -   data, parent_None):
        parentItem _ parent
        itemData _ data
        childItems _   # list

    ___ child  row):
        r_ childItems[row]

    ___ childCount
        r_ le.(childItems)

    ___ childNumber
        __ parentItem !_ N..:
            r_ parentItem.childItems.index
        r_ 0

    ___ columnCount
        r_ le.(itemData)

    ___ data  column):
        r_ itemData[column]

    ___ insertChildren  position, count, columns):
        __ position < 0 or position > le.(childItems):
            r_ F..

        ___ row __ ra..(count):
            data _ [N.. ___ v __ ra..(columns)]
            item _ TreeItem(data, self)
            childItems.insert(position, item)

        r_ T..

    ___ insertColumns  position, columns):
        __ position < 0 or position > le.(itemData):
            r_ F..

        ___ column __ ra..(columns):
            itemData.insert(position, N..)

        ___ child __ childItems:
            child.insertColumns(position, columns)

        r_ T..

    ___ parent
        r_ parentItem

    ___ removeChildren  position, count):
        __ position < 0 or position + count > le.(childItems):
            r_ F..

        ___ row __ ra..(count):
            childItems.p.. position)

        r_ T..

    ___ removeColumns  position, columns):
        __ position < 0 or position + columns > le.(itemData):
            r_ F..

        ___ column __ ra..(columns):
            itemData.p.. position)

        ___ child __ childItems:
            child.removeColumns(position, columns)

        r_ T..

    ___ setData  column, value):
        __ column < 0 or column >_ le.(itemData):
            r_ F..

        itemData[column] _ value

        r_ T..


c_ TreeModel(QAbstractItemModel):
    ___  -   headers, data, parent_None):
        s__(TreeModel, self). - (parent)

        rootData _ [header ___ header __ headers]
        rootItem _ TreeItem(rootData)
        setupModelData(data.sp..("\n"), rootItem)

    ___ columnCount  parent_QModelIndex()):
        r_ rootItem.columnCount()

    ___ data  index, role):
        __ no. index.isValid
            r_ N..

        __ role !_ __.DR.. and role !_ __.ER..:
            r_ N..

        item _ getItem(index)
        r_ item.data(index.column())

    ___ flags  index):
        __ no. index.isValid
            r_ 0

        r_ __.IIE.. | s__(TreeModel, self).flags(index)

    ___ getItem  index):
        __ index.isValid
            item _ index.internalPointer()
            __ item:
                r_ item

        r_ rootItem

    ___ hD..  section, orientation, role_Qt.DR..):
        __ orientation __ __.H.. and role __ __.DR..:
            r_ rootItem.data(section)

        r_ N..

    ___ index  row, column, parent_QModelIndex()):
        __ parent.iV.. and parent.column() !_ 0:
            r_ QModelIndex()

        parentItem _ getItem(parent)
        childItem _ parentItem.child(row)
        __ childItem:
            r_ createIndex(row, column, childItem)
        ____
            r_ QModelIndex()

    ___ insertColumns  position, columns, parent_QModelIndex()):
        beginInsertColumns(parent, position, position + columns - 1)
        success _ rootItem.insertColumns(position, columns)
        endInsertColumns()

        r_ success

    ___ insertRows  position, rows, parent_QModelIndex()):
        parentItem _ getItem(parent)
        beginInsertRows(parent, position, position + rows - 1)
        success _ parentItem.insertChildren(position, rows,
                rootItem.columnCount())
        endInsertRows()

        r_ success

    ___ parent  index):
        __ no. index.isValid
            r_ QModelIndex()

        childItem _ getItem(index)
        parentItem _ childItem.parent()

        __ parentItem __ rootItem:
            r_ QModelIndex()

        r_ createIndex(parentItem.childNumber(), 0, parentItem)

    ___ removeColumns  position, columns, parent_QModelIndex()):
        beginRemoveColumns(parent, position, position + columns - 1)
        success _ rootItem.removeColumns(position, columns)
        endRemoveColumns()

        __ rootItem.columnCount() __ 0:
            removeRows(0, rowCount())

        r_ success

    ___ removeRows  position, rows, parent_QModelIndex()):
        parentItem _ getItem(parent)

        beginRemoveRows(parent, position, position + rows - 1)
        success _ parentItem.removeChildren(position, rows)
        endRemoveRows()

        r_ success

    ___ rowCount  parent_QModelIndex()):
        parentItem _ getItem(parent)

        r_ parentItem.childCount()

    ___ setData  index, value, role_Qt.ER..):
        __ role !_ __.ER..:
            r_ F..

        item _ getItem(index)
        result _ item.setData(index.column(), value)

        __ result:
            dataChanged.e..(index, index)

        r_ result

    ___ setHeaderData  section, orientation, value, role_Qt.ER..):
        __ role !_ __.ER.. or orientation !_ __.H..:
            r_ F..

        result _ rootItem.setData(section, value)
        __ result:
            headerDataChanged.e..(orientation, section, section)

        r_ result

    ___ setupModelData  lines, parent):
        parents _ [parent]
        indentations _ [0]

        number _ 0

        w__ number < le.(lines):
            position _ 0
            w__ position < le.(lines[number]):
                __ lines[number][position] !_ " ":
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
                parent _ parents[-1]
                parent.insertChildren(parent.childCount(), 1,
                        rootItem.columnCount())
                ___ column __ ra..(le.(columnData)):
                    parent.child(parent.childCount() -1).setData(column, columnData[column])

            number +_ 1


c_ MainWindow(?MW.., Ui_MainWindow):
    ___  -   parent_None):
        s__(MainWindow, self). - (parent)

        setupUi

        headers _ ("Title", "Description")

        file _ QFile(':/default.txt')
        file.o..(QIODevice.ReadOnly)
        model _ TreeModel(headers, file.readAll())
        file.c..

        view.sM..(model)
        ___ column __ ra..(model.columnCount()):
            view.resizeColumnToContents(column)

        exitAction.t__.c..(?A...i.. .quit)

        view.selectionModel().sC__.c..(updateActions)

        actionsMenu.aboutToShow.c..(updateActions)
        insertRowAction.t__.c..(insertRow)
        insertColumnAction.t__.c..(insertColumn)
        removeRowAction.t__.c..(removeRow)
        removeColumnAction.t__.c..(removeColumn)
        insertChildAction.t__.c..(insertChild)

        updateActions()

    ___ insertChild
        index _ view.selectionModel().currentIndex()
        model _ view.model()

        __ model.columnCount(index) __ 0:
            __ no. model.insertColumn(0, index):
                r_

        __ no. model.insertRow(0, index):
            r_

        ___ column __ ra..(model.columnCount(index)):
            child _ model.index(0, column, index)
            model.setData(child, "[No data]", __.ER..)
            __ model.hD..(column, __.H..) __ N..:
                model.setHeaderData(column, __.H.., "[No header]",
                        __.ER..)

        view.selectionModel().sCI..(model.index(0, 0, index),
                QItemSelectionModel.ClearAndSelect)
        updateActions()

    ___ insertColumn
        model _ view.model()
        column _ view.selectionModel().currentIndex().column()

        changed _ model.insertColumn(column + 1)
        __ changed:
            model.setHeaderData(column + 1, __.H.., "[No header]",
                    __.ER..)

        updateActions()

        r_ changed

    ___ insertRow
        index _ view.selectionModel().currentIndex()
        model _ view.model()

        __ no. model.insertRow(index.row()+1, index.parent()):
            r_

        updateActions()

        ___ column __ ra..(model.columnCount(index.parent())):
            child _ model.index(index.row()+1, column, index.parent())
            model.setData(child, "[No data]", __.ER..)

    ___ removeColumn
        model _ view.model()
        column _ view.selectionModel().currentIndex().column()

        changed _ model.removeColumn(column)
        __ changed:
            updateActions()

        r_ changed

    ___ removeRow
        index _ view.selectionModel().currentIndex()
        model _ view.model()

        __ (model.removeRow(index.row(), index.parent())):
            updateActions()

    ___ updateActions
        hasSelection _ no. view.selectionModel().selection().isEmpty()
        removeRowAction.sE..(hasSelection)
        removeColumnAction.sE..(hasSelection)

        hasCurrent _ view.selectionModel().currentIndex().iV..
        insertRowAction.sE..(hasCurrent)
        insertColumnAction.sE..(hasCurrent)

        __ hasCurrent:
            view.closePersistentEditor(view.selectionModel().cI..

            row _ view.selectionModel().currentIndex().row()
            column _ view.selectionModel().currentIndex().column()
            __ view.selectionModel().currentIndex().parent().isValid
                sB.. .sM..("Position: (%d,%d)" % (row, column))
            ____
                sB.. .sM..("Position: (%d,%d) in top level" % (row, column))


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.s..
    ___.e.. ?.e..
