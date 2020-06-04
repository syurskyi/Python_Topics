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
____ ?.?W.. ______ ?A.., ?FD.., ?MW.., QTreeView
____ ?.QtXml ______ QDomDocument


c_ DomItem o..
    ___  -   node, row, parent_None):
        domNode _ node
        # Record the item's location within its parent.
        rowNumber _ row
        parentItem _ parent
        childItems _   # dict

    ___ node
        r_ domNode

    ___ parent
        r_ parentItem

    ___ child  i):
        __ i __ childItems:
            r_ childItems[i]

        __ i >_ 0 and i < domNode.childNodes().count
            childNode _ domNode.childNodes().item(i)
            childItem _ DomItem(childNode, i, self)
            childItems[i] _ childItem
            r_ childItem

        r_ N..

    ___ row
        r_ rowNumber


c_ DomModel(QAbstractItemModel):
    ___  -   document, parent_None):
        s__(DomModel, self). - (parent)

        domDocument _ document

        rootItem _ DomItem(domDocument, 0)

    ___ columnCount  parent):
        r_ 3

    ___ data  index, role):
        __ no. index.isValid
            r_ N..

        __ role !_ __.DR..:
            r_ N..

        item _ index.internalPointer()

        node _ item.node()
        attributes _   # list
        attributeMap _ node.attributes()

        __ index.column() __ 0:
            r_ node.nodeName()
        
        ____ index.column() __ 1:
            ___ i __ ra..(0, attributeMap.count()):
                attribute _ attributeMap.item(i)
                attributes.ap..(attribute.nodeName() + '="' +
                                  attribute.nodeValue() + '"')

            r_ " ".join(attributes)

        __ index.column() __ 2:
            value _ node.nodeValue()
            __ value __ N..:
                r_ ''

            r_ ' '.join(node.nodeValue().sp..('\n'))

        r_ N..

    ___ flags  index):
        __ no. index.isValid
            r_ __.NoItemFlags

        r_ __.ItemIsEnabled | __.ItemIsSelectable

    ___ hD..  section, orientation, role):
        __ orientation __ __.H.. and role __ __.DR..:
            __ section __ 0:
                r_ "Name"

            __ section __ 1:
                r_ "Attributes"

            __ section __ 2:
                r_ "Value"

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

    ___ parent  child):
        __ no. child.isValid
            r_ QModelIndex()

        childItem _ child.internalPointer()
        parentItem _ childItem.parent()

        __ no. parentItem or parentItem __ rootItem:
            r_ QModelIndex()

        r_ createIndex(parentItem.row(), 0, parentItem)

    ___ rowCount  parent):
        __ parent.column() > 0:
            r_ 0

        __ no. parent.isValid
            parentItem _ rootItem
        ____
            parentItem _ parent.internalPointer()

        r_ parentItem.node().childNodes().count()


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..("&Open...", openFile, "Ctrl+O")
        fileMenu.aA..("E&xit", close, "Ctrl+Q")

        xmlPath _ ""
        model _ DomModel(QDomDocument(), self)
        view _ QTreeView
        view.sM..(model)

        sCW..(view)
        sWT..("Simple DOM Model")

    ___ openFile
        fP.., _ _ ?FD...gOFN..  "Open File",
                xmlPath, "XML files (*.xml);;HTML files (*.html);;"
                "SVG files (*.svg);;User Interface files (*.ui)")

        __ fP..:
            f _ QFile(fP..)
            __ f.o..(QIODevice.ReadOnly):
                document _ QDomDocument()
                __ document.setContent(f):
                    newModel _ DomModel(document, self)
                    view.sM..(newModel)
                    model _ newModel
                    xmlPath _ fP..

                f.c..


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.r..(640, 480)
    window.s..
    ___.e.. ?.e..
