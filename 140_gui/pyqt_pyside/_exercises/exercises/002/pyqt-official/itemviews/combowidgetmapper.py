#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2017 Riverbank Computing Limited
## Copyright (C) 2017 Hans-Peter Jansen <hpj@urpla.net>.
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


____ ?.?C.. ______ QStringListModel
____ ?.?G.. ______ ?SI.., ?SIM..
____ ?.?W.. ______ (?A.., ?CB, QDataWidgetMapper,
        QGridLayout, ?L.., QLineEdit, ?PB.., ?TE.., ?W..)


c_ Window(?W..):
    ___  -   parent_None):
        s__(Window, self). - (parent)

        # Set up the model.
        setupModel()

        # Set up the widgets.
        nameLabel _ ?L..("Na&me:")
        nameEdit _ ?LE..
        addressLabel _ ?L..("&Address:")
        addressEdit _ ?TE..()
        typeLabel _ ?L..("&Type:")
        typeComboBox _ ?CB()
        nextButton _ ?PB..("&Next")
        previousButton _ ?PB..("&Previous")

        nameLabel.setBuddy(nameEdit)
        addressLabel.setBuddy(addressEdit)
        typeLabel.setBuddy(typeComboBox)

        typeComboBox.sM..(typeModel)

        # Set up the mapper.
        mapper _ QDataWidgetMapper
        mapper.sM..(model)
        mapper.aM..(nameEdit, 0)
        mapper.aM..(addressEdit, 1)
        mapper.aM..(typeComboBox, 2, b'currentIndex')

        # Set up connections and layouts.
        previousButton.c__.c..(mapper.toPrevious)
        nextButton.c__.c..(mapper.toNext)
        mapper.currentIndexChanged.c..(updateButtons)

        layout _ QGridLayout()
        layout.aW..(nameLabel, 0, 0, 1, 1)
        layout.aW..(nameEdit, 0, 1, 1, 1)
        layout.aW..(previousButton, 0, 2, 1, 1)
        layout.aW..(addressLabel, 1, 0, 1, 1)
        layout.aW..(addressEdit, 1, 1, 2, 1)
        layout.aW..(nextButton, 1, 2, 1, 1)
        layout.aW..(typeLabel, 3, 0, 1, 1)
        layout.aW..(typeComboBox, 3, 1, 1, 1)
        sL..(layout)

        sWT..("Delegate Widget Mapper")
        mapper.toFirst()
 
    ___ setupModel 
        i.. _ ("Home", "Work", "Other")
        typeModel _ QStringListModel(i.., self)

        model _ ?SIM..(5, 3, self)

        names _ ("Alice", "Bob", "Carol", "Donald", "Emma")
        addresses _ ("<qt>123 Main Street<br/>Market Town</qt>",
                     "<qt>PO Box 32<br/>Mail Handling Service"
                     "<br/>Service City</qt>",
                     "<qt>The Lighthouse<br/>Remote Island</qt>",
                     "<qt>47338 Park Avenue<br/>Big City</qt>",
                     "<qt>Research Station<br/>Base Camp<br/>Big Mountain</qt>")
        types _ ("0", "1", "2", "0", "2")
        
        ___ row, name __ en..(names):
            model.setItem(row, 0, ?SI..(name))
            model.setItem(row, 1, ?SI..(addresses[row]))
            model.setItem(row, 2, ?SI..(types[row]))
 
    ___ updateButtons  row):
        previousButton.sE..(row > 0)
        nextButton.sE..(row < model.rowCount() - 1)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    window _ Window()
    window.s..

    ___.e.. ?.e..
