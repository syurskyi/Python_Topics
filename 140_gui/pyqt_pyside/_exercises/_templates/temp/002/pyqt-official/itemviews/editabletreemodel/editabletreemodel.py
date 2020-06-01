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
____ ?.?W.. ______ ?A.., QMainWindow

______ editabletreemodel_rc
____ ui_mainwindow ______ Ui_MainWindow


c_ TreeItem(object):
    ___ __init__  data, parent_None):
        self.parentItem _ parent
        self.itemData _ data
        self.childItems _ []

    ___ child  row):
        r_ self.childItems[row]

    ___ childCount(self):
        r_ len(self.childItems)

    ___ childNumber(self):
        __ self.parentItem !_ N..:
            r_ self.parentItem.childItems.index(self)
        r_ 0

    ___ columnCount(self):
        r_ len(self.itemData)

    ___ data  column):
        r_ self.itemData[column]

    ___ insertChildren  position, count, columns):
        __ position < 0 or position > len(self.childItems):
            r_ False

        for row in range(count):
            data _ [N.. for v in range(columns)]
            item _ TreeItem(data, self)
            self.childItems.insert(position, item)

        r_ True

    ___ insertColumns  position, columns):
        __ position < 0 or position > len(self.itemData):
            r_ False

        for column in range(columns):
            self.itemData.insert(position, N..)

        for child in self.childItems:
            child.insertColumns(position, columns)

        r_ True

    ___ parent(self):
        r_ self.parentItem

    ___ removeChildren  position, count):
        __ position < 0 or position + count > len(self.childItems):
            r_ False

        for row in range(count):
            self.childItems.pop(position)

        r_ True

    ___ removeColumns  position, columns):
        __ position < 0 or position + columns > len(self.itemData):
            r_ False

        for column in range(columns):
            self.itemData.pop(position)

        for child in self.childItems:
            child.removeColumns(position, columns)

        r_ True

    ___ setData  column, value):
        __ column < 0 or column >_ len(self.itemData):
            r_ False

        self.itemData[column] _ value

        r_ True


c_ TreeModel(QAbstractItemModel):
    ___ __init__  headers, data, parent_None):
        super(TreeModel, self).__init__(parent)

        rootData _ [header for header in headers]
        self.rootItem _ TreeItem(rootData)
        self.setupModelData(data.split("\n"), self.rootItem)

    ___ columnCount  parent_QModelIndex()):
        r_ self.rootItem.columnCount()

    ___ data  index, role):
        __ no. index.isValid
            r_ N..

        __ role !_ __.DisplayRole and role !_ __.EditRole:
            r_ N..

        item _ self.getItem(index)
        r_ item.data(index.column())

    ___ flags  index):
        __ no. index.isValid
            r_ 0

        r_ __.ItemIsEditable | super(TreeModel, self).flags(index)

    ___ getItem  index):
        __ index.isValid
            item _ index.internalPointer()
            __ item:
                r_ item

        r_ self.rootItem

    ___ headerData  section, orientation, role_Qt.DisplayRole):
        __ orientation == __.Horizontal and role == __.DisplayRole:
            r_ self.rootItem.data(section)

        r_ N..

    ___ index  row, column, parent_QModelIndex()):
        __ parent.isValid() and parent.column() !_ 0:
            r_ QModelIndex()

        parentItem _ self.getItem(parent)
        childItem _ parentItem.child(row)
        __ childItem:
            r_ self.createIndex(row, column, childItem)
        ____
            r_ QModelIndex()

    ___ insertColumns  position, columns, parent_QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)
        success _ self.rootItem.insertColumns(position, columns)
        self.endInsertColumns()

        r_ success

    ___ insertRows  position, rows, parent_QModelIndex()):
        parentItem _ self.getItem(parent)
        self.beginInsertRows(parent, position, position + rows - 1)
        success _ parentItem.insertChildren(position, rows,
                self.rootItem.columnCount())
        self.endInsertRows()

        r_ success

    ___ parent  index):
        __ no. index.isValid
            r_ QModelIndex()

        childItem _ self.getItem(index)
        parentItem _ childItem.parent()

        __ parentItem == self.rootItem:
            r_ QModelIndex()

        r_ self.createIndex(parentItem.childNumber(), 0, parentItem)

    ___ removeColumns  position, columns, parent_QModelIndex()):
        self.beginRemoveColumns(parent, position, position + columns - 1)
        success _ self.rootItem.removeColumns(position, columns)
        self.endRemoveColumns()

        __ self.rootItem.columnCount() == 0:
            self.removeRows(0, self.rowCount())

        r_ success

    ___ removeRows  position, rows, parent_QModelIndex()):
        parentItem _ self.getItem(parent)

        self.beginRemoveRows(parent, position, position + rows - 1)
        success _ parentItem.removeChildren(position, rows)
        self.endRemoveRows()

        r_ success

    ___ rowCount  parent_QModelIndex()):
        parentItem _ self.getItem(parent)

        r_ parentItem.childCount()

    ___ setData  index, value, role_Qt.EditRole):
        __ role !_ __.EditRole:
            r_ False

        item _ self.getItem(index)
        result _ item.setData(index.column(), value)

        __ result:
            self.dataChanged.emit(index, index)

        r_ result

    ___ setHeaderData  section, orientation, value, role_Qt.EditRole):
        __ role !_ __.EditRole or orientation !_ __.Horizontal:
            r_ False

        result _ self.rootItem.setData(section, value)
        __ result:
            self.headerDataChanged.emit(orientation, section, section)

        r_ result

    ___ setupModelData  lines, parent):
        parents _ [parent]
        indentations _ [0]

        number _ 0

        while number < len(lines):
            position _ 0
            while position < len(lines[number]):
                __ lines[number][position] !_ " ":
                    break
                position +_ 1

            lineData _ lines[number][position:].trimmed()

            __ lineData:
                # Read the column data from the rest of the line.
                columnData _ [s for s in lineData.split('\t') __ s]

                __ position > indentations[-1]:
                    # The last child of the current parent is now the new
                    # parent unless the current parent has no children.

                    __ parents[-1].childCount() > 0:
                        parents.append(parents[-1].child(parents[-1].childCount() - 1))
                        indentations.append(position)

                ____
                    while position < indentations[-1] and len(parents) > 0:
                        parents.pop()
                        indentations.pop()

                # Append a new item to the current parent's list of children.
                parent _ parents[-1]
                parent.insertChildren(parent.childCount(), 1,
                        self.rootItem.columnCount())
                for column in range(len(columnData)):
                    parent.child(parent.childCount() -1).setData(column, columnData[column])

            number +_ 1


c_ MainWindow(QMainWindow, Ui_MainWindow):
    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        headers _ ("Title", "Description")

        file _ QFile(':/default.txt')
        file.o..(QIODevice.ReadOnly)
        model _ TreeModel(headers, file.readAll())
        file.close()

        self.view.setModel(model)
        for column in range(model.columnCount()):
            self.view.resizeColumnToContents(column)

        self.exitAction.t__.c..(?A...instance().quit)

        self.view.selectionModel().selectionChanged.c..(self.updateActions)

        self.actionsMenu.aboutToShow.c..(self.updateActions)
        self.insertRowAction.t__.c..(self.insertRow)
        self.insertColumnAction.t__.c..(self.insertColumn)
        self.removeRowAction.t__.c..(self.removeRow)
        self.removeColumnAction.t__.c..(self.removeColumn)
        self.insertChildAction.t__.c..(self.insertChild)

        self.updateActions()

    ___ insertChild(self):
        index _ self.view.selectionModel().currentIndex()
        model _ self.view.model()

        __ model.columnCount(index) == 0:
            __ no. model.insertColumn(0, index):
                r_

        __ no. model.insertRow(0, index):
            r_

        for column in range(model.columnCount(index)):
            child _ model.index(0, column, index)
            model.setData(child, "[No data]", __.EditRole)
            __ model.headerData(column, __.Horizontal) __ N..:
                model.setHeaderData(column, __.Horizontal, "[No header]",
                        __.EditRole)

        self.view.selectionModel().setCurrentIndex(model.index(0, 0, index),
                QItemSelectionModel.ClearAndSelect)
        self.updateActions()

    ___ insertColumn(self):
        model _ self.view.model()
        column _ self.view.selectionModel().currentIndex().column()

        changed _ model.insertColumn(column + 1)
        __ changed:
            model.setHeaderData(column + 1, __.Horizontal, "[No header]",
                    __.EditRole)

        self.updateActions()

        r_ changed

    ___ insertRow(self):
        index _ self.view.selectionModel().currentIndex()
        model _ self.view.model()

        __ no. model.insertRow(index.row()+1, index.parent()):
            r_

        self.updateActions()

        for column in range(model.columnCount(index.parent())):
            child _ model.index(index.row()+1, column, index.parent())
            model.setData(child, "[No data]", __.EditRole)

    ___ removeColumn(self):
        model _ self.view.model()
        column _ self.view.selectionModel().currentIndex().column()

        changed _ model.removeColumn(column)
        __ changed:
            self.updateActions()

        r_ changed

    ___ removeRow(self):
        index _ self.view.selectionModel().currentIndex()
        model _ self.view.model()

        __ (model.removeRow(index.row(), index.parent())):
            self.updateActions()

    ___ updateActions(self):
        hasSelection _ no. self.view.selectionModel().selection().isEmpty()
        self.removeRowAction.setEnabled(hasSelection)
        self.removeColumnAction.setEnabled(hasSelection)

        hasCurrent _ self.view.selectionModel().currentIndex().isValid()
        self.insertRowAction.setEnabled(hasCurrent)
        self.insertColumnAction.setEnabled(hasCurrent)

        __ hasCurrent:
            self.view.closePersistentEditor(self.view.selectionModel().currentIndex())

            row _ self.view.selectionModel().currentIndex().row()
            column _ self.view.selectionModel().currentIndex().column()
            __ self.view.selectionModel().currentIndex().parent().isValid
                self.statusBar().showMessage("Position: (%d,%d)" % (row, column))
            ____
                self.statusBar().showMessage("Position: (%d,%d) in top level" % (row, column))


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())
