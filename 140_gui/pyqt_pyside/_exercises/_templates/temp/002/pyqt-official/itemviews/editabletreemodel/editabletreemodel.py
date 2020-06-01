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


____ ?.QtCore ______ (QAbstractItemModel, QFile, QIODevice,
        QItemSelectionModel, QModelIndex, Qt)
____ ?.?W.. ______ QApplication, QMainWindow

______ editabletreemodel_rc
____ ui_mainwindow ______ Ui_MainWindow


class TreeItem(object):
    ___ __init__(self, data, parent_None):
        self.parentItem _ parent
        self.itemData _ data
        self.childItems _ []

    ___ child(self, row):
        return self.childItems[row]

    ___ childCount(self):
        return len(self.childItems)

    ___ childNumber(self):
        if self.parentItem !_ None:
            return self.parentItem.childItems.index(self)
        return 0

    ___ columnCount(self):
        return len(self.itemData)

    ___ data(self, column):
        return self.itemData[column]

    ___ insertChildren(self, position, count, columns):
        if position < 0 or position > len(self.childItems):
            return False

        for row in range(count):
            data _ [None for v in range(columns)]
            item _ TreeItem(data, self)
            self.childItems.insert(position, item)

        return True

    ___ insertColumns(self, position, columns):
        if position < 0 or position > len(self.itemData):
            return False

        for column in range(columns):
            self.itemData.insert(position, None)

        for child in self.childItems:
            child.insertColumns(position, columns)

        return True

    ___ parent(self):
        return self.parentItem

    ___ removeChildren(self, position, count):
        if position < 0 or position + count > len(self.childItems):
            return False

        for row in range(count):
            self.childItems.pop(position)

        return True

    ___ removeColumns(self, position, columns):
        if position < 0 or position + columns > len(self.itemData):
            return False

        for column in range(columns):
            self.itemData.pop(position)

        for child in self.childItems:
            child.removeColumns(position, columns)

        return True

    ___ setData(self, column, value):
        if column < 0 or column >_ len(self.itemData):
            return False

        self.itemData[column] _ value

        return True


class TreeModel(QAbstractItemModel):
    ___ __init__(self, headers, data, parent_None):
        super(TreeModel, self).__init__(parent)

        rootData _ [header for header in headers]
        self.rootItem _ TreeItem(rootData)
        self.setupModelData(data.split("\n"), self.rootItem)

    ___ columnCount(self, parent_QModelIndex()):
        return self.rootItem.columnCount()

    ___ data(self, index, role):
        if not index.isValid
            return None

        if role !_ Qt.DisplayRole and role !_ Qt.EditRole:
            return None

        item _ self.getItem(index)
        return item.data(index.column())

    ___ flags(self, index):
        if not index.isValid
            return 0

        return Qt.ItemIsEditable | super(TreeModel, self).flags(index)

    ___ getItem(self, index):
        if index.isValid
            item _ index.internalPointer()
            if item:
                return item

        return self.rootItem

    ___ headerData(self, section, orientation, role_Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    ___ index(self, row, column, parent_QModelIndex()):
        if parent.isValid() and parent.column() !_ 0:
            return QModelIndex()

        parentItem _ self.getItem(parent)
        childItem _ parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    ___ insertColumns(self, position, columns, parent_QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)
        success _ self.rootItem.insertColumns(position, columns)
        self.endInsertColumns()

        return success

    ___ insertRows(self, position, rows, parent_QModelIndex()):
        parentItem _ self.getItem(parent)
        self.beginInsertRows(parent, position, position + rows - 1)
        success _ parentItem.insertChildren(position, rows,
                self.rootItem.columnCount())
        self.endInsertRows()

        return success

    ___ parent(self, index):
        if not index.isValid
            return QModelIndex()

        childItem _ self.getItem(index)
        parentItem _ childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.childNumber(), 0, parentItem)

    ___ removeColumns(self, position, columns, parent_QModelIndex()):
        self.beginRemoveColumns(parent, position, position + columns - 1)
        success _ self.rootItem.removeColumns(position, columns)
        self.endRemoveColumns()

        if self.rootItem.columnCount() == 0:
            self.removeRows(0, self.rowCount())

        return success

    ___ removeRows(self, position, rows, parent_QModelIndex()):
        parentItem _ self.getItem(parent)

        self.beginRemoveRows(parent, position, position + rows - 1)
        success _ parentItem.removeChildren(position, rows)
        self.endRemoveRows()

        return success

    ___ rowCount(self, parent_QModelIndex()):
        parentItem _ self.getItem(parent)

        return parentItem.childCount()

    ___ setData(self, index, value, role_Qt.EditRole):
        if role !_ Qt.EditRole:
            return False

        item _ self.getItem(index)
        result _ item.setData(index.column(), value)

        if result:
            self.dataChanged.emit(index, index)

        return result

    ___ setHeaderData(self, section, orientation, value, role_Qt.EditRole):
        if role !_ Qt.EditRole or orientation !_ Qt.Horizontal:
            return False

        result _ self.rootItem.setData(section, value)
        if result:
            self.headerDataChanged.emit(orientation, section, section)

        return result

    ___ setupModelData(self, lines, parent):
        parents _ [parent]
        indentations _ [0]

        number _ 0

        while number < len(lines):
            position _ 0
            while position < len(lines[number]):
                if lines[number][position] !_ " ":
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
                parent _ parents[-1]
                parent.insertChildren(parent.childCount(), 1,
                        self.rootItem.columnCount())
                for column in range(len(columnData)):
                    parent.child(parent.childCount() -1).setData(column, columnData[column])

            number +_ 1


class MainWindow(QMainWindow, Ui_MainWindow):
    ___ __init__(self, parent_None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        headers _ ("Title", "Description")

        file _ QFile(':/default.txt')
        file.open(QIODevice.ReadOnly)
        model _ TreeModel(headers, file.readAll())
        file.close()

        self.view.setModel(model)
        for column in range(model.columnCount()):
            self.view.resizeColumnToContents(column)

        self.exitAction.triggered.c..(QApplication.instance().quit)

        self.view.selectionModel().selectionChanged.c..(self.updateActions)

        self.actionsMenu.aboutToShow.c..(self.updateActions)
        self.insertRowAction.triggered.c..(self.insertRow)
        self.insertColumnAction.triggered.c..(self.insertColumn)
        self.removeRowAction.triggered.c..(self.removeRow)
        self.removeColumnAction.triggered.c..(self.removeColumn)
        self.insertChildAction.triggered.c..(self.insertChild)

        self.updateActions()

    ___ insertChild(self):
        index _ self.view.selectionModel().currentIndex()
        model _ self.view.model()

        if model.columnCount(index) == 0:
            if not model.insertColumn(0, index):
                return

        if not model.insertRow(0, index):
            return

        for column in range(model.columnCount(index)):
            child _ model.index(0, column, index)
            model.setData(child, "[No data]", Qt.EditRole)
            if model.headerData(column, Qt.Horizontal) is None:
                model.setHeaderData(column, Qt.Horizontal, "[No header]",
                        Qt.EditRole)

        self.view.selectionModel().setCurrentIndex(model.index(0, 0, index),
                QItemSelectionModel.ClearAndSelect)
        self.updateActions()

    ___ insertColumn(self):
        model _ self.view.model()
        column _ self.view.selectionModel().currentIndex().column()

        changed _ model.insertColumn(column + 1)
        if changed:
            model.setHeaderData(column + 1, Qt.Horizontal, "[No header]",
                    Qt.EditRole)

        self.updateActions()

        return changed

    ___ insertRow(self):
        index _ self.view.selectionModel().currentIndex()
        model _ self.view.model()

        if not model.insertRow(index.row()+1, index.parent()):
            return

        self.updateActions()

        for column in range(model.columnCount(index.parent())):
            child _ model.index(index.row()+1, column, index.parent())
            model.setData(child, "[No data]", Qt.EditRole)

    ___ removeColumn(self):
        model _ self.view.model()
        column _ self.view.selectionModel().currentIndex().column()

        changed _ model.removeColumn(column)
        if changed:
            self.updateActions()

        return changed

    ___ removeRow(self):
        index _ self.view.selectionModel().currentIndex()
        model _ self.view.model()

        if (model.removeRow(index.row(), index.parent())):
            self.updateActions()

    ___ updateActions(self):
        hasSelection _ not self.view.selectionModel().selection().isEmpty()
        self.removeRowAction.setEnabled(hasSelection)
        self.removeColumnAction.setEnabled(hasSelection)

        hasCurrent _ self.view.selectionModel().currentIndex().isValid()
        self.insertRowAction.setEnabled(hasCurrent)
        self.insertColumnAction.setEnabled(hasCurrent)

        if hasCurrent:
            self.view.closePersistentEditor(self.view.selectionModel().currentIndex())

            row _ self.view.selectionModel().currentIndex().row()
            column _ self.view.selectionModel().currentIndex().column()
            if self.view.selectionModel().currentIndex().parent().isValid
                self.statusBar().showMessage("Position: (%d,%d)" % (row, column))
            else:
                self.statusBar().showMessage("Position: (%d,%d) in top level" % (row, column))


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())
