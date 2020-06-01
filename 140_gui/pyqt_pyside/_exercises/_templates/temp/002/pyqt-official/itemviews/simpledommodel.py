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
____ ?.?W.. ______ ?A.., ?FD.., QMainWindow, QTreeView
____ ?.QtXml ______ QDomDocument


c_ DomItem(object):
    ___ __init__  node, row, parent_None):
        self.domNode _ node
        # Record the item's location within its parent.
        self.rowNumber _ row
        self.parentItem _ parent
        self.childItems _ {}

    ___ node(self):
        r_ self.domNode

    ___ parent(self):
        r_ self.parentItem

    ___ child  i):
        __ i in self.childItems:
            r_ self.childItems[i]

        __ i >_ 0 and i < self.domNode.childNodes().count
            childNode _ self.domNode.childNodes().item(i)
            childItem _ DomItem(childNode, i, self)
            self.childItems[i] _ childItem
            r_ childItem

        r_ N..

    ___ row(self):
        r_ self.rowNumber


c_ DomModel(QAbstractItemModel):
    ___ __init__  document, parent_None):
        super(DomModel, self).__init__(parent)

        self.domDocument _ document

        self.rootItem _ DomItem(self.domDocument, 0)

    ___ columnCount  parent):
        r_ 3

    ___ data  index, role):
        __ no. index.isValid
            r_ N..

        __ role !_ __.DisplayRole:
            r_ N..

        item _ index.internalPointer()

        node _ item.node()
        attributes _   # list
        attributeMap _ node.attributes()

        __ index.column() == 0:
            r_ node.nodeName()
        
        ____ index.column() == 1:
            for i in range(0, attributeMap.count()):
                attribute _ attributeMap.item(i)
                attributes.ap..(attribute.nodeName() + '="' +
                                  attribute.nodeValue() + '"')

            r_ " ".join(attributes)

        __ index.column() == 2:
            value _ node.nodeValue()
            __ value __ N..:
                r_ ''

            r_ ' '.join(node.nodeValue().split('\n'))

        r_ N..

    ___ flags  index):
        __ no. index.isValid
            r_ __.NoItemFlags

        r_ __.ItemIsEnabled | __.ItemIsSelectable

    ___ headerData  section, orientation, role):
        __ orientation == __.Horizontal and role == __.DisplayRole:
            __ section == 0:
                r_ "Name"

            __ section == 1:
                r_ "Attributes"

            __ section == 2:
                r_ "Value"

        r_ N..

    ___ index  row, column, parent):
        __ no. self.hasIndex(row, column, parent):
            r_ QModelIndex()

        __ no. parent.isValid
            parentItem _ self.rootItem
        ____
            parentItem _ parent.internalPointer()

        childItem _ parentItem.child(row)
        __ childItem:
            r_ self.createIndex(row, column, childItem)
        ____
            r_ QModelIndex()

    ___ parent  child):
        __ no. child.isValid
            r_ QModelIndex()

        childItem _ child.internalPointer()
        parentItem _ childItem.parent()

        __ no. parentItem or parentItem == self.rootItem:
            r_ QModelIndex()

        r_ self.createIndex(parentItem.row(), 0, parentItem)

    ___ rowCount  parent):
        __ parent.column() > 0:
            r_ 0

        __ no. parent.isValid
            parentItem _ self.rootItem
        ____
            parentItem _ parent.internalPointer()

        r_ parentItem.node().childNodes().count()


c_ MainWindow ?MW..
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.fileMenu _ self.mB.. .aM..("&File")
        self.fileMenu.aA..("&Open...", self.openFile, "Ctrl+O")
        self.fileMenu.aA..("E&xit", self.close, "Ctrl+Q")

        self.xmlPath _ ""
        self.model _ DomModel(QDomDocument(), self)
        self.view _ QTreeView(self)
        self.view.sM..(self.model)

        self.sCW..(self.view)
        self.setWindowTitle("Simple DOM Model")

    ___ openFile(self):
        filePath, _ _ ?FD...gOFN..  "Open File",
                self.xmlPath, "XML files (*.xml);;HTML files (*.html);;"
                "SVG files (*.svg);;User Interface files (*.ui)")

        __ filePath:
            f _ QFile(filePath)
            __ f.o..(QIODevice.ReadOnly):
                document _ QDomDocument()
                __ document.setContent(f):
                    newModel _ DomModel(document, self)
                    self.view.sM..(newModel)
                    self.model _ newModel
                    self.xmlPath _ filePath

                f.close()


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    window _ MainWindow()
    window.resize(640, 480)
    window.s..
    ___.exit(app.exec_())
