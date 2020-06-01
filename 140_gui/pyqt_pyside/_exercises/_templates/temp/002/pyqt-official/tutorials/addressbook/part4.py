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
____ ?.?W.. ______ (QGridLayout, QHBoxLayout, QLabel, QLineEdit,
        ?MB.., ?PB.., QTextEdit, QVBoxLayout, QWidget)


c_ SortedDict(dict):
    c_ Iterator(object):
        ___ __init__  sorted_dict):
            self._dict _ sorted_dict
            self._keys _ sorted(self._dict.keys())
            self._nr_items _ le.(self._keys)
            self._idx _ 0

        ___ __iter__(self):
            r_ self

        ___ next(self):
            __ self._idx >_ self._nr_items:
                raise StopIteration

            key _ self._keys[self._idx]
            value _ self._dict[key]
            self._idx +_ 1

            r_ key, value

        __next__ _ next

    ___ __iter__(self):
        r_ SortedDict.Iterator(self)

    iterkeys _ __iter__


c_ AddressBook(QWidget):
    NavigationMode, AddingMode, EditingMode _ range(3)

    ___ __init__  parent_None):
        super(AddressBook, self).__init__(parent)

        self.contacts _ SortedDict()
        self.oldName _ ''
        self.oldAddress _ ''
        self.currentMode _ self.NavigationMode

        nameLabel _ QLabel("Name:")
        self.nameLine _ ?LE..
        self.nameLine.setReadOnly(True)

        addressLabel _ QLabel("Address:")
        self.addressText _ QTextEdit()
        self.addressText.setReadOnly(True)

        self.addButton _ ?PB..("&Add")
        self.addButton.s..
        self.editButton _ ?PB..("&Edit")
        self.editButton.setEnabled F..
        self.removeButton _ ?PB..("&Remove")
        self.removeButton.setEnabled F..
        self.submitButton _ ?PB..("&Submit")
        self.submitButton.hide()
        self.cancelButton _ ?PB..("&Cancel")
        self.cancelButton.hide()

        self.nextButton _ ?PB..("&Next")
        self.nextButton.setEnabled F..
        self.previousButton _ ?PB..("&Previous")
        self.previousButton.setEnabled F..

        self.addButton.c__.c..(self.addContact)
        self.submitButton.c__.c..(self.submitContact)
        self.editButton.c__.c..(self.editContact)
        self.removeButton.c__.c..(self.removeContact)
        self.cancelButton.c__.c..(self.cancel)
        self.nextButton.c__.c..(self.next)
        self.previousButton.c__.c..(self.previous)

        buttonLayout1 _ ?VBL..
        buttonLayout1.aW..(self.addButton)
        buttonLayout1.aW..(self.editButton)
        buttonLayout1.aW..(self.removeButton)
        buttonLayout1.aW..(self.submitButton)
        buttonLayout1.aW..(self.cancelButton)
        buttonLayout1.addStretch()

        buttonLayout2 _ QHBoxLayout()
        buttonLayout2.aW..(self.previousButton)
        buttonLayout2.aW..(self.nextButton)

        mainLayout _ QGridLayout()
        mainLayout.aW..(nameLabel, 0, 0)
        mainLayout.aW..(self.nameLine, 0, 1)
        mainLayout.aW..(addressLabel, 1, 0, __.AlignTop)
        mainLayout.aW..(self.addressText, 1, 1)
        mainLayout.addLayout(buttonLayout1, 1, 2)
        mainLayout.addLayout(buttonLayout2, 3, 1)

        self.sL..(mainLayout)
        self.setWindowTitle("Simple Address Book")

    ___ addContact(self):
        self.oldName _ self.nameLine.t__()
        self.oldAddress _ self.addressText.toPlainText()

        self.nameLine.clear()
        self.addressText.clear()

        self.updateInterface(self.AddingMode)

    ___ editContact(self):
        self.oldName _ self.nameLine.t__()
        self.oldAddress _ self.addressText.toPlainText()

        self.updateInterface(self.EditingMode)

    ___ submitContact(self):
        name _ self.nameLine.t__()
        address _ self.addressText.toPlainText()

        __ name == "" or address == "":
            ?MB...information  "Empty Field",
                    "Please enter a name and address.")
            r_

        __ self.currentMode == self.AddingMode:
            __ name no. in self.contacts:
                self.contacts[name] _ address
                ?MB...information  "Add Successful",
                        "\"%s\" has been added to your address book." % name)
            ____
                ?MB...information  "Add Unsuccessful",
                        "Sorry, \"%s\" is already in your address book." % name)
                r_

        ____ self.currentMode == self.EditingMode:
            __ self.oldName !_ name:
                __ name no. in self.contacts:
                    ?MB...information  "Edit Successful",
                            "\"%s\" has been edited in your address book." % self.oldName)
                    del self.contacts[self.oldName]
                    self.contacts[name] _ address
                ____
                    ?MB...information  "Edit Unsuccessful",
                            "Sorry, \"%s\" is already in your address book." % name)
                    r_
            ____ self.oldAddress !_ address:
                ?MB...information  "Edit Successful",
                        "\"%s\" has been edited in your address book." % name)
                self.contacts[name] _ address

        self.updateInterface(self.NavigationMode)

    ___ cancel(self):
        self.nameLine.sT..(self.oldName)
        self.addressText.sT..(self.oldAddress)
        self.updateInterface(self.NavigationMode)

    ___ removeContact(self):
        name _ self.nameLine.t__()
        address _ self.addressText.toPlainText()

        __ name in self.contacts:
            button _ ?MB...q..  "Confirm Remove",
                    "Are you sure you want to remove \"%s\"?" % name,
                    ?MB...Yes | ?MB...No)

            __ button == ?MB...Yes:
                self.previous()
                del self.contacts[name]

                ?MB...information  "Remove Successful",
                        "\"%s\" has been removed from your address book." % name)

        self.updateInterface(self.NavigationMode)

    ___ next(self):
        name _ self.nameLine.t__()
        it _ iter(self.contacts)

        try:
            w__ T..
                this_name, _ _ it.next()

                __ this_name == name:
                    next_name, next_address _ it.next()
                    break
        except StopIteration:
            next_name, next_address _ iter(self.contacts).next()

        self.nameLine.sT..(next_name)
        self.addressText.sT..(next_address)

    ___ previous(self):
        name _ self.nameLine.t__()

        prev_name _ prev_address _ N..
        for this_name, this_address in self.contacts:
            __ this_name == name:
                break

            prev_name _ this_name
            prev_address _ this_address
        ____
            self.nameLine.clear()
            self.addressText.clear()
            r_

        __ prev_name __ N..:
            for prev_name, prev_address in self.contacts:
                pass

        self.nameLine.sT..(prev_name)
        self.addressText.sT..(prev_address)

    ___ updateInterface  mode):
        self.currentMode _ mode

        __ self.currentMode in (self.AddingMode, self.EditingMode):
            self.nameLine.setReadOnly F..
            self.nameLine.setFocus(__.OtherFocusReason)
            self.addressText.setReadOnly F..

            self.addButton.setEnabled F..
            self.editButton.setEnabled F..
            self.removeButton.setEnabled F..

            self.nextButton.setEnabled F..
            self.previousButton.setEnabled F..

            self.submitButton.s..
            self.cancelButton.s..

        ____ self.currentMode == self.NavigationMode:
            __ no. self.contacts:
                self.nameLine.clear()
                self.addressText.clear()

            self.nameLine.setReadOnly(True)
            self.addressText.setReadOnly(True)
            self.addButton.setEnabled(True)

            number _ le.(self.contacts)
            self.editButton.setEnabled(number >_ 1)
            self.removeButton.setEnabled(number >_ 1)
            self.nextButton.setEnabled(number > 1)
            self.previousButton.setEnabled(number >1 )

            self.submitButton.hide()
            self.cancelButton.hide()


__ __name__ == '__main__':
    ______ sys

    ____ ?.?W.. ______ ?A..

    app _ ?A..(sys.argv)

    addressBook _ AddressBook()
    addressBook.s..

    sys.exit(app.exec_())
