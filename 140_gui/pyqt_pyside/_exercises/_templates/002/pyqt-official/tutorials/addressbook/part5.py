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
____ ?.?W.. ______ (?D.., QGridLayout, ?HBL.., ?L..,
        QLineEdit, ?MB.., ?PB.., ?TE.., ?VBL.., ?W..)


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
    NavigationMode, AddingMode, EditingMode _ ra..(3)

    ___  -   parent_None):
        s__(AddressBook, self). - (parent)

        contacts _ SortedDict()
        oldName _ ''
        oldAddress _ ''
        currentMode _ NavigationMode

        nameLabel _ ?L..("Name:")
        nameLine _ ?LE..
        nameLine.sRO..( st.

        addressLabel _ ?L..("Address:")
        addressText _ ?TE..()
        addressText.sRO..( st.

        addButton _ ?PB..("&Add")
        addButton.s..
        editButton _ ?PB..("&Edit")
        editButton.sE.. F..
        removeButton _ ?PB..("&Remove")
        removeButton.sE.. F..
        findButton _ ?PB..("&Find")
        findButton.sE.. F..
        submitButton _ ?PB..("&Submit")
        submitButton.hide()
        cancelButton _ ?PB..("&Cancel")
        cancelButton.hide()

        nextButton _ ?PB..("&Next")
        nextButton.sE.. F..
        previousButton _ ?PB..("&Previous")
        previousButton.sE.. F..

        dialog _ FindDialog()

        addButton.c__.c..(addContact)
        submitButton.c__.c..(submitContact)
        editButton.c__.c..(editContact)
        removeButton.c__.c..(removeContact)
        findButton.c__.c..(findContact)
        cancelButton.c__.c..(cancel)
        nextButton.c__.c..(next)
        previousButton.c__.c..(previous)

        buttonLayout1 _ ?VBL..
        buttonLayout1.aW..(addButton)
        buttonLayout1.aW..(editButton)
        buttonLayout1.aW..(removeButton)
        buttonLayout1.aW..(findButton)
        buttonLayout1.aW..(submitButton)
        buttonLayout1.aW..(cancelButton)
        buttonLayout1.addStretch()

        buttonLayout2 _ ?HBL..
        buttonLayout2.aW..(previousButton)
        buttonLayout2.aW..(nextButton)

        mainLayout _ QGridLayout()
        mainLayout.aW..(nameLabel, 0, 0)
        mainLayout.aW..(nameLine, 0, 1)
        mainLayout.aW..(addressLabel, 1, 0, __.AlignTop)
        mainLayout.aW..(addressText, 1, 1)
        mainLayout.aL..(buttonLayout1, 1, 2)
        mainLayout.aL..(buttonLayout2, 2, 1)

        sL..(mainLayout)
        sWT..("Simple Address Book")

    ___ addContact
        oldName _ nameLine.t__()
        oldAddress _ addressText.toPlainText()

        nameLine.c..
        addressText.c..

        updateInterface(AddingMode)

    ___ editContact
        oldName _ nameLine.t__()
        oldAddress _ addressText.toPlainText()

        updateInterface(EditingMode)

    ___ submitContact
        name _ nameLine.t__()
        address _ addressText.toPlainText()

        __ name __ "" or address __ "":
            ?MB...i..  "Empty Field",
                    "Please enter a name and address.")
            r_

        __ currentMode __ AddingMode:
            __ name no. __ contacts:
                contacts[name] _ address
                ?MB...i..  "Add Successful",
                        "\"%s\" has been added to your address book." % name)
            ____
                ?MB...i..  "Add Unsuccessful",
                        "Sorry, \"%s\" is already in your address book." % name)
                r_

        ____ currentMode __ EditingMode:
            __ oldName !_ name:
                __ name no. __ contacts:
                    ?MB...i..  "Edit Successful",
                            "\"%s\" has been edited in your address book." % oldName)
                    del contacts[oldName]
                    contacts[name] _ address
                ____
                    ?MB...i..  "Edit Unsuccessful",
                            "Sorry, \"%s\" is already in your address book." % name)
                    r_
            ____ oldAddress !_ address:
                ?MB...i..  "Edit Successful",
                        "\"%s\" has been edited in your address book." % name)
                contacts[name] _ address

        updateInterface(NavigationMode)

    ___ cancel
        nameLine.sT..(oldName)
        addressText.sT..(oldAddress)
        updateInterface(NavigationMode)

    ___ removeContact
        name _ nameLine.t__()
        address _ addressText.toPlainText()

        __ name __ contacts:
            button _ ?MB...q..  "Confirm Remove",
                    "Are you sure you want to remove \"%s\"?" % name,
                    ?MB...Yes | ?MB...No)

            __ button __ ?MB...Yes:
                previous()
                del contacts[name]

                ?MB...i..  "Remove Successful",
                        "\"%s\" has been removed from your address book." % name)

        updateInterface(NavigationMode)

    ___ next
        name _ nameLine.t__()
        it _ iter(contacts)

        ___
            w__ T..
                this_name, _ _ it.next()

                __ this_name __ name:
                    next_name, next_address _ it.next()
                    break
        _____ StopIteration:
            next_name, next_address _ iter(contacts).next()

        nameLine.sT..(next_name)
        addressText.sT..(next_address)

    ___ previous
        name _ nameLine.t__()

        prev_name _ prev_address _ N..
        ___ this_name, this_address __ contacts:
            __ this_name __ name:
                break

            prev_name _ this_name
            prev_address _ this_address
        ____
            nameLine.c..
            addressText.c..
            r_

        __ prev_name __ N..:
            ___ prev_name, prev_address __ contacts:
                p..

        nameLine.sT..(prev_name)
        addressText.sT..(prev_address)

    ___ findContact
        dialog.s..

        __ dialog.e.. __ ?D...Accepted:
            contactName _ dialog.getFindText()

            __ contactName __ contacts:
                nameLine.sT..(contactName)
                addressText.sT..(contacts[contactName])
            ____
                ?MB...i..  "Contact Not Found",
                        "Sorry, \"%s\" is not in your address book." % contactName)
                r_

        updateInterface(NavigationMode)

    ___ updateInterface  mode):
        currentMode _ mode

        __ currentMode __ (AddingMode, EditingMode):
            nameLine.sRO.. F..
            nameLine.setFocus(__.OtherFocusReason)
            addressText.sRO.. F..

            addButton.sE.. F..
            editButton.sE.. F..
            removeButton.sE.. F..

            nextButton.sE.. F..
            previousButton.sE.. F..

            submitButton.s..
            cancelButton.s..

        ____ currentMode __ NavigationMode:
            __ no. contacts:
                nameLine.c..
                addressText.c..

            nameLine.sRO..( st.
            addressText.sRO..( st.
            addButton.sE..( st.

            number _ le.(contacts)
            editButton.sE..(number >_ 1)
            removeButton.sE..(number >_ 1)
            findButton.sE..(number > 2)
            nextButton.sE..(number > 1)
            previousButton.sE..(number >1 )

            submitButton.hide()
            cancelButton.hide()


c_ FindDialog(?D..):
    ___  -   parent_None):
        s__(FindDialog, self). - (parent)

        findLabel _ ?L..("Enter the name of a contact:")
        lineEdit _ ?LE..

        findButton _ ?PB..("&Find")
        findText _ ''

        layout _ ?HBL..
        layout.aW..(findLabel)
        layout.aW..(lineEdit)
        layout.aW..(findButton)

        sL..(layout)
        sWT..("Find a Contact")

        findButton.c__.c..(findClicked)
        findButton.c__.c..(accept)

    ___ findClicked
        t__ _ lineEdit.t__()

        __ no. t__:
            ?MB...i..  "Empty Field",
                    "Please enter a name.")
            r_
        ____
            findText _ t__
            lineEdit.c..
            hide()

    ___ getFindText
        r_ findText


__ ______ __ ______
    ______ ___

    ____ ?.?W.. ______ ?A..

    app _ ?A..(___.a..

    addressBook _ AddressBook()
    addressBook.s..

    ___.e.. ?.e..
