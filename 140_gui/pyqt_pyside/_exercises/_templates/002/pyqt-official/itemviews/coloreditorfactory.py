#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
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


____ ?.?C.. ______ pP.., __, QVariant
____ ?.?G.. ______ ?C..
____ ?.?W.. ______ (?A.., ?CB, QGridLayout,
        QItemEditorCreatorBase, QItemEditorFactory, ?TW..,
        ?TWI.., ?W..)


c_ ColorListEditor(?CB):
    ___  -   widget_None):
        s__(ColorListEditor, self). - (widget)

        populateList()

    ___ getColor
        color _ itemData(currentIndex(), __.DecorationRole)
        r_ color

    ___ sC..  color):
        sCI..(findData(color, __.DecorationRole))

    color _ pP..(?C.., getColor, sC.., user_ st.

    ___ populateList
        ___ i, colorName __ en..(?C...colorNames()):
            color _ ?C..(colorName)
            iI..(i, colorName)
            setItemData(i, color, __.DecorationRole)


c_ ColorListItemEditorCreator(QItemEditorCreatorBase):
    ___ createWidget  parent):
        r_ ColorListEditor(parent)


c_ Window(?W..):
    ___  -   parent_None):
        s__(Window, self). - (parent)

        factory _ QItemEditorFactory()
        factory.registerEditor(QVariant.Color, ColorListItemEditorCreator())
        QItemEditorFactory.setDefaultFactory(factory)

        createGUI()

    ___ createGUI
        tableData _ [
            ("Alice", ?C..('aliceblue')),
            ("Neptun", ?C..('aquamarine')),
            ("Ferdinand", ?C..('springgreen'))
        ]

        table _ ?TW..(3, 2)
        table.sHHL..(["Name", "Hair Color"])
        table.vH.. .setVisible F..
        table.r..(150, 50)

        ___ i, (name, color) __ en..(tableData):
            nameItem _ ?TWI..(name)
            colorItem _ ?TWI..()
            colorItem.setData(__.DR.., color)
            table.setItem(i, 0, nameItem)
            table.setItem(i, 1, colorItem)

        table.resizeColumnToContents(0)
        table.hH.. .setStretchLastSection( st.

        layout _ QGridLayout()
        layout.aW..(table, 0, 0)
        sL..(layout)

        sWT..("Color Editor Factory")


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    window _ Window()
    window.s..

    ___.e.. ?.e..
