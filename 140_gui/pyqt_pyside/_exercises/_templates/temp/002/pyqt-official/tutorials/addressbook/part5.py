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
____ ?.?W.. ______ (QDialog, QGridLayout, QHBoxLayout, QLabel,
        QLineEdit, QMessageBox, ?PB.., QTextEdit, QVBoxLayout, QWidget)


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
    NavigationMode, AddingMode, EditingMode _ range(3)

    ___ __init__(self, parent_None):
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
        self.editButton.setEnabled(False)
        self.removeButton _ ?PB..("&Remove")
        self.removeButton.setEnabled(False)
        self.findButton _ ?PB..("&Find")
        self.findButton.setEnabled(False)
        self.submitButton _ ?PB..("&Submit")
        self.submitButton.hide()
        self.cancelButton _ ?PB..("&Cancel")
        self.cancelButton.hide()

        self.nextButton _ ?PB..("&Next")
        self.nextButton.setEnabled(False)
        self.previousButton _ ?PB..("&Previous")
        self.previousButton.setEnabled(False)

        self.dialog _ FindDialog()

        self.addButton.c__.c..(self.addContact)
        self.submitButton.c__.c..(self.submitContact)
        self.editButton.c__.c..(self.editContact)
        self.removeButton.c__.c..(self.removeContact)
        self.findButton.c__.c..(self.findContact)
        self.cancelButton.c__.c..(self.cancel)
        self.nextButton.c__.c..(self.next)
        self.previousButton.c__.c..(self.previous)

        buttonLayout1 _ QVBoxLayout()
        buttonLayout1.addWidget(self.addButton)
        buttonLayout1.addWidget(self.editButton)
        buttonLayout1.addWidget(self.removeButton)
        buttonLayout1.addWidget(self.findButton)
        buttonLayout1.addWidget(self.submitButton)
        buttonLayout1.addWidget(self.cancelButton)
        buttonLayout1.addStretch()

        buttonLayout2 _ QHBoxLayout()
        buttonLayout2.addWidget(self.previousButton)
        buttonLayout2.addWidget(self.nextButton)

        mainLayout _ QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(addressLabel, 1, 0, Qt.AlignTop)
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

        if name == "" or address == "":
            QMessageBox.information(self, "Empty Field",
                    "Please enter a name and address.")
            return

        if self.currentMode == self.AddingMode:
            if name not in self.contacts:
                self.contacts[name] _ address
                QMessageBox.information(self, "Add Successful",
                        "\"%s\" has been added to your address book." % name)
            else:
                QMessageBox.information(self, "Add Unsuccessful",
                        "Sorry, \"%s\" is already in your address book." % name)
                return

        elif self.currentMode == self.EditingMode:
            if self.oldName !_ name:
                if name not in self.contacts:
                    QMessageBox.information(self, "Edit Successful",
                            "\"%s\" has been edited in your address book." % self.oldName)
                    del self.contacts[self.oldName]
                    self.contacts[name] _ address
                else:
                    QMessageBox.information(self, "Edit Unsuccessful",
                            "Sorry, \"%s\" is already in your address book." % name)
                    return
            elif self.oldAddress !_ address:
                QMessageBox.information(self, "Edit Successful",
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

        if name in self.contacts:
            button _ QMessageBox.question(self, "Confirm Remove",
                    "Are you sure you want to remove \"%s\"?" % name,
                    QMessageBox.Yes | QMessageBox.No)

            if button == QMessageBox.Yes:
                self.previous()
                del self.contacts[name]

                QMessageBox.information(self, "Remove Successful",
                        "\"%s\" has been removed from your address book." % name)

        self.updateInterface(self.NavigationMode)

    ___ next(self):
        name _ self.nameLine.text()
        it _ iter(self.contacts)

        try:
            while True:
                this_name, _ _ it.next()

                if this_name == name:
                    next_name, next_address _ it.next()
                    break
        except StopIteration:
            next_name, next_address _ iter(self.contacts).next()

        self.nameLine.sT..(next_name)
        self.addressText.sT..(next_address)

    ___ previous(self):
        name _ self.nameLine.text()

        prev_name _ prev_address _ None
        for this_name, this_address in self.contacts:
            if this_name == name:
                break

            prev_name _ this_name
            prev_address _ this_address
        else:
            self.nameLine.clear()
            self.addressText.clear()
            return

        if prev_name is None:
            for prev_name, prev_address in self.contacts:
                pass

        self.nameLine.sT..(prev_name)
        self.addressText.sT..(prev_address)

    ___ findContact(self):
        self.dialog.s..

        if self.dialog.e.. == QDialog.Accepted:
            contactName _ self.dialog.getFindText()

            if contactName in self.contacts:
                self.nameLine.sT..(contactName)
                self.addressText.sT..(self.contacts[contactName])
            else:
                QMessageBox.information(self, "Contact Not Found",
                        "Sorry, \"%s\" is not in your address book." % contactName)
                return

        self.updateInterface(self.NavigationMode)

    ___ updateInterface(self, mode):
        self.currentMode _ mode

        if self.currentMode in (self.AddingMode, self.EditingMode):
            self.nameLine.setReadOnly(False)
            self.nameLine.setFocus(Qt.OtherFocusReason)
            self.addressText.setReadOnly(False)

            self.addButton.setEnabled(False)
            self.editButton.setEnabled(False)
            self.removeButton.setEnabled(False)

            self.nextButton.setEnabled(False)
            self.previousButton.setEnabled(False)

            self.submitButton.s..
            self.cancelButton.s..

        elif self.currentMode == self.NavigationMode:
            if not self.contacts:
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


class FindDialog(QDialog):
    ___ __init__(self, parent_None):
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

        if not text:
            QMessageBox.information(self, "Empty Field",
                    "Please enter a name.")
            return
        else:
            self.findText _ text
            self.lineEdit.clear()
            self.hide()

    ___ getFindText(self):
        return self.findText


if __name__ == '__main__':
    ______ sys

    ____ ?.?W.. ______ ?A..

    app _ ?A..(sys.argv)

    addressBook _ AddressBook()
    addressBook.s..

    sys.exit(app.exec_())
