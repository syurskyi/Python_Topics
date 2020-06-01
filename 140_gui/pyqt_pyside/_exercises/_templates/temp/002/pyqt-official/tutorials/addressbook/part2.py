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


____ ?.QtCore ______ Qt
____ ?.?W.. ______ QGridLayout, QLabel, QLineEdit, QMessageBox, ?PB.., QTextEdit, QVBoxLayout, QWidget


class SortedDict(dict):
    class Iterator(object):
        ___ __init__(self, sorted_dict):
            self._dict _ sorted_dict
            self._keys _ sorted(self._dict.keys())
            self._nr_items _ len(self._keys)
            self._idx _ 0

        ___ __iter__(self):
            return self

        ___ next(self):
            if self._idx >_ self._nr_items:
                raise StopIteration

            key _ self._keys[self._idx]
            value _ self._dict[key]
            self._idx +_ 1

            return key, value

        __next__ _ next

    ___ __iter__(self):
        return SortedDict.Iterator(self)

    iterkeys _ __iter__


class AddressBook(QWidget):
    ___ __init__(self, parent_None):
        super(AddressBook, self).__init__(parent)

        self.contacts _ SortedDict()
        self.oldName _ ''
        self.oldAddress _ ''

        nameLabel _ QLabel("Name:")
        self.nameLine _ QLineEdit()
        self.nameLine.setReadOnly(True)

        addressLabel _ QLabel("Address:")
        self.addressText _ QTextEdit()
        self.addressText.setReadOnly(True)

        self.addButton _ ?PB..("&Add")
        self.addButton.s..
        self.submitButton _ ?PB..("&Submit")
        self.submitButton.hide()
        self.cancelButton _ ?PB..("&Cancel")
        self.cancelButton.hide()

        self.addButton.c__.c..(self.addContact)
        self.submitButton.c__.c..(self.submitContact)
        self.cancelButton.c__.c..(self.cancel)

        buttonLayout1 _ QVBoxLayout()
        buttonLayout1.addWidget(self.addButton, Qt.AlignTop)
        buttonLayout1.addWidget(self.submitButton)
        buttonLayout1.addWidget(self.cancelButton)
        buttonLayout1.addStretch()

        mainLayout _ QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(addressLabel, 1, 0, Qt.AlignTop)
        mainLayout.addWidget(self.addressText, 1, 1)
        mainLayout.addLayout(buttonLayout1, 1, 2)

        self.setLayout(mainLayout)
        self.setWindowTitle("Simple Address Book")

    ___ addContact(self):
        self.oldName _ self.nameLine.text()
        self.oldAddress _ self.addressText.toPlainText()

        self.nameLine.clear()
        self.addressText.clear()

        self.nameLine.setReadOnly(False)
        self.nameLine.setFocus(Qt.OtherFocusReason)
        self.addressText.setReadOnly(False)

        self.addButton.setEnabled(False)
        self.submitButton.s..
        self.cancelButton.s..

    ___ submitContact(self):
        name _ self.nameLine.text()
        address _ self.addressText.toPlainText()

        if name == "" or address == "":
            QMessageBox.information(self, "Empty Field",
                    "Please enter a name and address.")
            return

        if name not in self.contacts:
            self.contacts[name] _ address
            QMessageBox.information(self, "Add Successful",
                    "\"%s\" has been added to your address book." % name)
        else:
            QMessageBox.information(self, "Add Unsuccessful",
                    "Sorry, \"%s\" is already in your address book." % name)
            return

        if not self.contacts:
            self.nameLine.clear()
            self.addressText.clear()

        self.nameLine.setReadOnly(True)
        self.addressText.setReadOnly(True)
        self.addButton.setEnabled(True)
        self.submitButton.hide()
        self.cancelButton.hide()

    ___ cancel(self):
        self.nameLine.sT..(self.oldName)
        self.nameLine.setReadOnly(True)

        self.addressText.sT..(self.oldAddress)
        self.addressText.setReadOnly(True)

        self.addButton.setEnabled(True)
        self.submitButton.hide()
        self.cancelButton.hide()


if __name__ == '__main__':
    ______ sys

    ____ ?.?W.. ______ ?A..

    app _ ?A..(sys.argv)

    addressBook _ AddressBook()
    addressBook.s..

    sys.exit(app.exec_())
