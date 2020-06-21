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


____ ?.?C.. ______ __
____ ?.?W.. ______ QGridLayout, ?L.., QLineEdit, ?MB.., ?PB.., ?TE.., ?VBL.., ?W..


c_ SortedDict(dict):
    c_ Iterator o..
        ___  -   sorted_dict):
            _dict _ sorted_dict
            _keys _ so..(_dict.keys())
            _nr_items _ le.(_keys)
            _idx _ 0

        ___ __iter__ 
            r_ self

        ___ next 
            __ _idx >_ _nr_items:
                r_ StopIteration

            key _ _keys[_idx]
            value _ _dict[key]
            _idx +_ 1

            r_ key, value

        __next__ _ next

    ___ __iter__ 
        r_ SortedDict.Iterator

    iterkeys _ __iter__


c_ AddressBook(?W..):
    ___  -   parent_None):
        s__(AddressBook, self). - (parent)

        contacts _ SortedDict()
        oldName _ ''
        oldAddress _ ''

        nameLabel _ ?L..("Name:")
        nameLine _ ?LE..
        nameLine.sRO..( st.

        addressLabel _ ?L..("Address:")
        addressText _ ?TE..()
        addressText.sRO..( st.

        addButton _ ?PB..("&Add")
        addButton.s..
        submitButton _ ?PB..("&Submit")
        submitButton.hide()
        cancelButton _ ?PB..("&Cancel")
        cancelButton.hide()

        addButton.c__.c..(addContact)
        submitButton.c__.c..(submitContact)
        cancelButton.c__.c..(cancel)

        buttonLayout1 _ ?VBL..
        buttonLayout1.aW..(addButton, __.AlignTop)
        buttonLayout1.aW..(submitButton)
        buttonLayout1.aW..(cancelButton)
        buttonLayout1.addStretch()

        mainLayout _ QGridLayout()
        mainLayout.aW..(nameLabel, 0, 0)
        mainLayout.aW..(nameLine, 0, 1)
        mainLayout.aW..(addressLabel, 1, 0, __.AlignTop)
        mainLayout.aW..(addressText, 1, 1)
        mainLayout.aL..(buttonLayout1, 1, 2)

        sL..(mainLayout)
        sWT..("Simple Address Book")

    ___ addContact 
        oldName _ nameLine.t__()
        oldAddress _ addressText.toPlainText()

        nameLine.c..
        addressText.c..

        nameLine.sRO.. F..
        nameLine.setFocus(__.OtherFocusReason)
        addressText.sRO.. F..

        addButton.sE.. F..
        submitButton.s..
        cancelButton.s..

    ___ submitContact 
        name _ nameLine.t__()
        address _ addressText.toPlainText()

        __ name __ "" or address __ "":
            ?MB...i..  "Empty Field",
                    "Please enter a name and address.")
            r_

        __ name no. __ contacts:
            contacts[name] _ address
            ?MB...i..  "Add Successful",
                    "\"%s\" has been added to your address book." % name)
        ____
            ?MB...i..  "Add Unsuccessful",
                    "Sorry, \"%s\" is already in your address book." % name)
            r_

        __ no. contacts:
            nameLine.c..
            addressText.c..

        nameLine.sRO..( st.
        addressText.sRO..( st.
        addButton.sE..( st.
        submitButton.hide()
        cancelButton.hide()

    ___ cancel 
        nameLine.sT..(oldName)
        nameLine.sRO..( st.

        addressText.sT..(oldAddress)
        addressText.sRO..( st.

        addButton.sE..( st.
        submitButton.hide()
        cancelButton.hide()


__ ______ __ ______
    ______ ___

    ____ ?.?W.. ______ ?A..

    app _ ?A..(___.a..

    addressBook _ AddressBook()
    addressBook.s..

    ___.e.. ?.e..
