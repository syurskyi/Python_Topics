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


______ pickle

____ ?.?C.. ______ QFile, QIODevice, __, QTextStream
____ ?.?W.. ______ (QDialog, ?FD.., QGridLayout, QHBoxLayout,
        QLabel, QLineEdit, ?MB.., ?PB.., QTextEdit, QVBoxLayout,
        QWidget)


c_ SortedDict(dict):
    c_ Iterator(object):
        ___ __init__  sorted_dict):
            self._dict _ sorted_dict
            self._keys _ sorted(self._dict.keys())
            self._nr_items _ len(self._keys)
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
        self.nameLine _ QLineEdit()
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
        self.findButton _ ?PB..("&Find")
        self.findButton.setEnabled F..
        self.submitButton _ ?PB..("&Submit")
        self.submitButton.hide()
        self.cancelButton _ ?PB..("&Cancel")
        self.cancelButton.hide()

        self.nextButton _ ?PB..("&Next")
        self.nextButton.setEnabled F..
        self.previousButton _ ?PB..("&Previous")
        self.previousButton.setEnabled F..

        self.loadButton _ ?PB..("&Load...")
        self.loadButton.setToolTip("Load contacts from a file")
        self.saveButton _ ?PB..("Sa&ve...")
        self.saveButton.setToolTip("Save contacts to a file")
        self.saveButton.setEnabled F..

        self.exportButton _ ?PB..("Ex&port")
        self.exportButton.setToolTip("Export as vCard")
        self.exportButton.setEnabled F..

        self.dialog _ FindDialog()

        self.addButton.c__.c..(self.addContact)
        self.submitButton.c__.c..(self.submitContact)
        self.editButton.c__.c..(self.editContact)
        self.removeButton.c__.c..(self.removeContact)
        self.findButton.c__.c..(self.findContact)
        self.cancelButton.c__.c..(self.cancel)
        self.nextButton.c__.c..(self.next)
        self.previousButton.c__.c..(self.previous)
        self.loadButton.c__.c..(self.loadFromFile)
        self.saveButton.c__.c..(self.saveToFile)
        self.exportButton.c__.c..(self.exportAsVCard)

        buttonLayout1 _ QVBoxLayout()
        buttonLayout1.addWidget(self.addButton)
        buttonLayout1.addWidget(self.editButton)
        buttonLayout1.addWidget(self.removeButton)
        buttonLayout1.addWidget(self.findButton)
        buttonLayout1.addWidget(self.submitButton)
        buttonLayout1.addWidget(self.cancelButton)
        buttonLayout1.addWidget(self.loadButton)
        buttonLayout1.addWidget(self.saveButton)
        buttonLayout1.addWidget(self.exportButton)
        buttonLayout1.addStretch()

        buttonLayout2 _ QHBoxLayout()
        buttonLayout2.addWidget(self.previousButton)
        buttonLayout2.addWidget(self.nextButton)

        mainLayout _ QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(addressLabel, 1, 0, __.AlignTop)
        mainLayout.addWidget(self.addressText, 1, 1)
        mainLayout.addLayout(buttonLayout1, 1, 2)
        mainLayout.addLayout(buttonLayout2, 2, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Simple Address Book")

    ___ addContact(self):
        self.oldName _ self.nameLine.text()
        self.oldAddress _ self.addressText.toPlainText()

        self.nameLine.clear()
        self.addressText.clear()

        self.updateInterface(self.AddingMode)

    ___ editContact(self):
        self.oldName _ self.nameLine.text()
        self.oldAddress _ self.addressText.toPlainText()

        self.updateInterface(self.EditingMode)

    ___ submitContact(self):
        name _ self.nameLine.text()
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
        name _ self.nameLine.text()
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
        name _ self.nameLine.text()
        it _ iter(self.contacts)

        try:
            while True:
                this_name, _ _ it.next()

                __ this_name == name:
                    next_name, next_address _ it.next()
                    break
        except StopIteration:
            next_name, next_address _ iter(self.contacts).next()

        self.nameLine.sT..(next_name)
        self.addressText.sT..(next_address)

    ___ previous(self):
        name _ self.nameLine.text()

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

    ___ findContact(self):
        self.dialog.s..

        __ self.dialog.e.. == QDialog.Accepted:
            contactName _ self.dialog.getFindText()

            __ contactName in self.contacts:
                self.nameLine.sT..(contactName)
                self.addressText.sT..(self.contacts[contactName])
            ____
                ?MB...information  "Contact Not Found",
                        "Sorry, \"%s\" is not in your address book." % contactName)
                r_

        self.updateInterface(self.NavigationMode)

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

            self.loadButton.setEnabled F..
            self.saveButton.setEnabled F..
            self.exportButton.setEnabled F..

        ____ self.currentMode == self.NavigationMode:
            __ no. self.contacts:
                self.nameLine.clear()
                self.addressText.clear()

            self.nameLine.setReadOnly(True)
            self.addressText.setReadOnly(True)
            self.addButton.setEnabled(True)

            number _ len(self.contacts)
            self.editButton.setEnabled(number >_ 1)
            self.removeButton.setEnabled(number >_ 1)
            self.findButton.setEnabled(number > 2)
            self.nextButton.setEnabled(number > 1)
            self.previousButton.setEnabled(number >1 )

            self.submitButton.hide()
            self.cancelButton.hide()

            self.exportButton.setEnabled(number >_ 1)

            self.loadButton.setEnabled(True)
            self.saveButton.setEnabled(number >_ 1)

    ___ saveToFile(self):
        fileName, _ _ ?FD...getSaveFileName  "Save Address Book",
                '', "Address Book (*.abk);;All Files (*)")

        __ no. fileName:
            r_

        try:
            out_file _ o..(str(fileName), 'wb')
        except IOError:
            ?MB...information  "Unable to open file",
                    "There was an error opening \"%s\"" % fileName)
            r_

        pickle.dump(self.contacts, out_file)
        out_file.close()

    ___ loadFromFile(self):
        fileName, _ _ ?FD...gOFN..  "Open Address Book",
                '', "Address Book (*.abk);;All Files (*)")

        __ no. fileName:
            r_

        try:
            in_file _ o..(str(fileName), 'rb')
        except IOError:
            ?MB...information  "Unable to open file",
                    "There was an error opening \"%s\"" % fileName)
            r_

        self.contacts _ pickle.load(in_file)
        in_file.close()

        __ len(self.contacts) == 0:
            ?MB...information  "No contacts in file",
                    "The file you are attempting to open contains no "
                    "contacts.")
        ____
            for name, address in self.contacts:
                self.nameLine.sT..(name)
                self.addressText.sT..(address)

        self.updateInterface(self.NavigationMode)

    ___ exportAsVCard(self):
        name _ str(self.nameLine.text())
        address _ self.addressText.toPlainText()

        nameList _ name.split()

        __ len(nameList) > 1:
            firstName _ nameList[0]
            lastName _ nameList[-1]
        ____
            firstName _ name
            lastName _ ''

        fileName, _ _ ?FD...getSaveFileName  "Export Contact", '',
                "vCard Files (*.vcf);;All Files (*)")

        __ no. fileName:
            r_

        out_file _ QFile(fileName)

        __ no. out_file.o..(QIODevice.WriteOnly):
            ?MB...information  "Unable to open file",
                    out_file.errorString())
            r_

        out_s _ QTextStream(out_file)

        out_s << 'BEGIN:VCARD' << '\n'
        out_s << 'VERSION:2.1' << '\n'
        out_s << 'N:' << lastName << ';' << firstName << '\n'
        out_s << 'FN:' << ' '.join(nameList) << '\n'

        address.replace(';', '\\;')
        address.replace('\n', ';')
        address.replace(',', ' ')

        out_s << 'ADR;HOME:;' << address << '\n'
        out_s << 'END:VCARD' << '\n'

        ?MB...information  "Export Successful",
                "\"%s\" has been exported as a vCard." % name)


c_ FindDialog(QDialog):
    ___ __init__  parent_None):
        super(FindDialog, self).__init__(parent)

        findLabel _ QLabel("Enter the name of a contact:")
        self.lineEdit _ QLineEdit()

        self.findButton _ ?PB..("&Find")
        self.findText _ ''

        layout _ QHBoxLayout()
        layout.addWidget(findLabel)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.findButton)

        self.setLayout(layout)
        self.setWindowTitle("Find a Contact")

        self.findButton.c__.c..(self.findClicked)
        self.findButton.c__.c..(self.accept)

    ___ findClicked(self):
        text _ self.lineEdit.text()

        __ no. text:
            ?MB...information  "Empty Field",
                    "Please enter a name.")
            r_

        self.findText _ text
        self.lineEdit.clear()
        self.hide()

    ___ getFindText(self):
        r_ self.findText


__ __name__ == '__main__':
    ______ sys

    ____ ?.?W.. ______ ?A..

    app _ ?A..(sys.argv)

    addressBook _ AddressBook()
    addressBook.s..

    sys.exit(app.exec_())
