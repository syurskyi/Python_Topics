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
____ ?.?G.. ______ QStandardItem, QStandardItemModel
____ ?.?W.. ______ (?A.., QComboBox, QDataWidgetMapper,
        QGridLayout, QLabel, QLineEdit, ?PB.., QTextEdit, QWidget)


c_ Window(QWidget):
    ___ __init__  parent_None):
        super(Window, self).__init__(parent)

        # Set up the model.
        self.setupModel()

        # Set up the widgets.
        nameLabel _ QLabel("Na&me:")
        nameEdit _ ?LE..
        addressLabel _ QLabel("&Address:")
        addressEdit _ QTextEdit()
        typeLabel _ QLabel("&Type:")
        typeComboBox _ QComboBox()
        self.nextButton _ ?PB..("&Next")
        self.previousButton _ ?PB..("&Previous")

        nameLabel.setBuddy(nameEdit)
        addressLabel.setBuddy(addressEdit)
        typeLabel.setBuddy(typeComboBox)

        typeComboBox.setModel(self.typeModel)

        # Set up the mapper.
        self.mapper _ QDataWidgetMapper(self)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(nameEdit, 0)
        self.mapper.addMapping(addressEdit, 1)
        self.mapper.addMapping(typeComboBox, 2, b'currentIndex')

        # Set up connections and layouts.
        self.previousButton.c__.c..(self.mapper.toPrevious)
        self.nextButton.c__.c..(self.mapper.toNext)
        self.mapper.currentIndexChanged.c..(self.updateButtons)

        layout _ QGridLayout()
        layout.aW..(nameLabel, 0, 0, 1, 1)
        layout.aW..(nameEdit, 0, 1, 1, 1)
        layout.aW..(self.previousButton, 0, 2, 1, 1)
        layout.aW..(addressLabel, 1, 0, 1, 1)
        layout.aW..(addressEdit, 1, 1, 2, 1)
        layout.aW..(self.nextButton, 1, 2, 1, 1)
        layout.aW..(typeLabel, 3, 0, 1, 1)
        layout.aW..(typeComboBox, 3, 1, 1, 1)
        self.sL..(layout)

        self.setWindowTitle("Delegate Widget Mapper")
        self.mapper.toFirst()
 
    ___ setupModel(self):
        items _ ("Home", "Work", "Other")
        self.typeModel _ QStringListModel(items, self)

        self.model _ QStandardItemModel(5, 3, self)

        names _ ("Alice", "Bob", "Carol", "Donald", "Emma")
        addresses _ ("<qt>123 Main Street<br/>Market Town</qt>",
                     "<qt>PO Box 32<br/>Mail Handling Service"
                     "<br/>Service City</qt>",
                     "<qt>The Lighthouse<br/>Remote Island</qt>",
                     "<qt>47338 Park Avenue<br/>Big City</qt>",
                     "<qt>Research Station<br/>Base Camp<br/>Big Mountain</qt>")
        types _ ("0", "1", "2", "0", "2")
        
        for row, name in enumerate(names):
            self.model.setItem(row, 0, QStandardItem(name))
            self.model.setItem(row, 1, QStandardItem(addresses[row]))
            self.model.setItem(row, 2, QStandardItem(types[row]))
 
    ___ updateButtons  row):
        self.previousButton.setEnabled(row > 0)
        self.nextButton.setEnabled(row < self.model.rowCount() - 1)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    window _ Window()
    window.s..

    sys.exit(app.exec_())
