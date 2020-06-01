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
____ ?.?W.. ______ QApplication, QFileDialog, QMainWindow, QTreeView
____ ?.QtXml ______ QDomDocument


class DomItem(object):
    ___ __init__(self, node, row, parent_None):
        self.domNode _ node
        # Record the item's location within its parent.
        self.rowNumber _ row
        self.parentItem _ parent
        self.childItems _ {}

    ___ node(self):
        return self.domNode

    ___ parent(self):
        return self.parentItem

    ___ child(self, i):
        if i in self.childItems:
            return self.childItems[i]

        if i >_ 0 and i < self.domNode.childNodes().count
            childNode _ self.domNode.childNodes().item(i)
            childItem _ DomItem(childNode, i, self)
            self.childItems[i] _ childItem
            return childItem

        return None

    ___ row(self):
        return self.rowNumber


class DomModel(QAbstractItemModel):
    ___ __init__(self, document, parent_None):
        super(DomModel, self).__init__(parent)

        self.domDocument _ document

        self.rootItem _ DomItem(self.domDocument, 0)

    ___ columnCount(self, parent):
        return 3

    ___ data(self, index, role):
        if not index.isValid
            return None

        if role !_ Qt.DisplayRole:
            return None

        item _ index.internalPointer()

        node _ item.node()
        attributes _ []
        attributeMap _ node.attributes()

        if index.column() == 0:
            return node.nodeName()
        
        elif index.column() == 1:
            for i in range(0, attributeMap.count()):
                attribute _ attributeMap.item(i)
                attributes.append(attribute.nodeName() + '="' +
                                  attribute.nodeValue() + '"')

            return " ".join(attributes)

        if index.column() == 2:
            value _ node.nodeValue()
            if value is None:
                return ''

            return ' '.join(node.nodeValue().split('\n'))

        return None

    ___ flags(self, index):
        if not index.isValid
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    ___ headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return "Name"

            if section == 1:
                return "Attributes"

            if section == 2:
                return "Value"

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

    ___ parent(self, child):
        if not child.isValid
            return QModelIndex()

        childItem _ child.internalPointer()
        parentItem _ childItem.parent()

        if not parentItem or parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    ___ rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid
            parentItem _ self.rootItem
        else:
            parentItem _ parent.internalPointer()

        return parentItem.node().childNodes().count()


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.fileMenu _ self.menuBar().addMenu("&File")
        self.fileMenu.addAction("&Open...", self.openFile, "Ctrl+O")
        self.fileMenu.addAction("E&xit", self.close, "Ctrl+Q")

        self.xmlPath _ ""
        self.model _ DomModel(QDomDocument(), self)
        self.view _ QTreeView(self)
        self.view.setModel(self.model)

        self.setCentralWidget(self.view)
        self.setWindowTitle("Simple DOM Model")

    ___ openFile(self):
        filePath, _ _ QFileDialog.getOpenFileName(self, "Open File",
                self.xmlPath, "XML files (*.xml);;HTML files (*.html);;"
                "SVG files (*.svg);;User Interface files (*.ui)")

        if filePath:
            f _ QFile(filePath)
            if f.open(QIODevice.ReadOnly):
                document _ QDomDocument()
                if document.setContent(f):
                    newModel _ DomModel(document, self)
                    self.view.setModel(newModel)
                    self.model _ newModel
                    self.xmlPath _ filePath

                f.close()


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    window _ MainWindow()
    window.resize(640, 480)
    window.s..
    sys.exit(app.exec_())
