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
        ___  -   sorted_dict):
            _dict _ sorted_dict
            _keys _ sorted(_dict.keys())
            _nr_items _ le.(_keys)
            _idx _ 0

        ___ __iter__ 
            r_ self

        ___ next 
            __ _idx >_ _nr_items:
                raise StopIteration

            key _ _keys[_idx]
            value _ _dict[key]
            _idx +_ 1

            r_ key, value

        __next__ _ next

    ___ __iter__ 
        r_ SortedDict.Iterator

    iterkeys _ __iter__


c_ AddressBook(QWidget):
    NavigationMode, AddingMode, EditingMode _ range(3)

    ___  -   parent_None):
        super(AddressBook, self). - (parent)

        contacts _ SortedDict()
        oldName _ ''
        oldAddress _ ''
        currentMode _ NavigationMode

        nameLabel _ QLabel("Name:")
        nameLine _ ?LE..
        nameLine.setReadOnly(True)

        addressLabel _ QLabel("Address:")
        addressText _ QTextEdit()
        addressText.setReadOnly(True)

        addButton _ ?PB..("&Add")
        addButton.s..
        editButton _ ?PB..("&Edit")
        editButton.setEnabled F..
        removeButton _ ?PB..("&Remove")
        removeButton.setEnabled F..
        findButton _ ?PB..("&Find")
        findButton.setEnabled F..
        submitButton _ ?PB..("&Submit")
        submitButton.hide()
        cancelButton _ ?PB..("&Cancel")
        cancelButton.hide()

        nextButton _ ?PB..("&Next")
        nextButton.setEnabled F..
        previousButton _ ?PB..("&Previous")
        previousButton.setEnabled F..

        loadButton _ ?PB..("&Load...")
        loadButton.setToolTip("Load contacts from a file")
        saveButton _ ?PB..("Sa&ve...")
        saveButton.setToolTip("Save contacts to a file")
        saveButton.setEnabled F..

        exportButton _ ?PB..("Ex&port")
        exportButton.setToolTip("Export as vCard")
        exportButton.setEnabled F..

        dialog _ FindDialog()

        addButton.c__.c..(addContact)
        submitButton.c__.c..(submitContact)
        editButton.c__.c..(editContact)
        removeButton.c__.c..(removeContact)
        findButton.c__.c..(findContact)
        cancelButton.c__.c..(cancel)
        nextButton.c__.c..(next)
        previousButton.c__.c..(previous)
        loadButton.c__.c..(loadFromFile)
        saveButton.c__.c..(saveToFile)
        exportButton.c__.c..(exportAsVCard)

        buttonLayout1 _ ?VBL..
        buttonLayout1.aW..(addButton)
        buttonLayout1.aW..(editButton)
        buttonLayout1.aW..(removeButton)
        buttonLayout1.aW..(findButton)
        buttonLayout1.aW..(submitButton)
        buttonLayout1.aW..(cancelButton)
        buttonLayout1.aW..(loadButton)
        buttonLayout1.aW..(saveButton)
        buttonLayout1.aW..(exportButton)
        buttonLayout1.addStretch()

        buttonLayout2 _ QHBoxLayout()
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
        setWindowTitle("Simple Address Book")

    ___ addContact 
        oldName _ nameLine.t__()
        oldAddress _ addressText.toPlainText()

        nameLine.clear()
        addressText.clear()

        updateInterface(AddingMode)

    ___ editContact 
        oldName _ nameLine.t__()
        oldAddress _ addressText.toPlainText()

        updateInterface(EditingMode)

    ___ submitContact 
        name _ nameLine.t__()
        address _ addressText.toPlainText()

        __ name == "" or address == "":
            ?MB...information  "Empty Field",
                    "Please enter a name and address.")
            r_

        __ currentMode == AddingMode:
            __ name no. __ contacts:
                contacts[name] _ address
                ?MB...information  "Add Successful",
                        "\"%s\" has been added to your address book." % name)
            ____
                ?MB...information  "Add Unsuccessful",
                        "Sorry, \"%s\" is already in your address book." % name)
                r_

        ____ currentMode == EditingMode:
            __ oldName !_ name:
                __ name no. __ contacts:
                    ?MB...information  "Edit Successful",
                            "\"%s\" has been edited in your address book." % oldName)
                    del contacts[oldName]
                    contacts[name] _ address
                ____
                    ?MB...information  "Edit Unsuccessful",
                            "Sorry, \"%s\" is already in your address book." % name)
                    r_
            ____ oldAddress !_ address:
                ?MB...information  "Edit Successful",
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

            __ button == ?MB...Yes:
                previous()
                del contacts[name]

                ?MB...information  "Remove Successful",
                        "\"%s\" has been removed from your address book." % name)

        updateInterface(NavigationMode)

    ___ next 
        name _ nameLine.t__()
        it _ iter(contacts)

        try:
            w__ T..
                this_name, _ _ it.next()

                __ this_name == name:
                    next_name, next_address _ it.next()
                    break
        except StopIteration:
            next_name, next_address _ iter(contacts).next()

        nameLine.sT..(next_name)
        addressText.sT..(next_address)

    ___ previous 
        name _ nameLine.t__()

        prev_name _ prev_address _ N..
        ___ this_name, this_address __ contacts:
            __ this_name == name:
                break

            prev_name _ this_name
            prev_address _ this_address
        ____
            nameLine.clear()
            addressText.clear()
            r_

        __ prev_name __ N..:
            ___ prev_name, prev_address __ contacts:
                pass

        nameLine.sT..(prev_name)
        addressText.sT..(prev_address)

    ___ findContact 
        dialog.s..

        __ dialog.e.. == QDialog.Accepted:
            contactName _ dialog.getFindText()

            __ contactName __ contacts:
                nameLine.sT..(contactName)
                addressText.sT..(contacts[contactName])
            ____
                ?MB...information  "Contact Not Found",
                        "Sorry, \"%s\" is not in your address book." % contactName)
                r_

        updateInterface(NavigationMode)

    ___ updateInterface  mode):
        currentMode _ mode

        __ currentMode __ (AddingMode, EditingMode):
            nameLine.setReadOnly F..
            nameLine.setFocus(__.OtherFocusReason)
            addressText.setReadOnly F..

            addButton.setEnabled F..
            editButton.setEnabled F..
            removeButton.setEnabled F..

            nextButton.setEnabled F..
            previousButton.setEnabled F..

            submitButton.s..
            cancelButton.s..

            loadButton.setEnabled F..
            saveButton.setEnabled F..
            exportButton.setEnabled F..

        ____ currentMode == NavigationMode:
            __ no. contacts:
                nameLine.clear()
                addressText.clear()

            nameLine.setReadOnly(True)
            addressText.setReadOnly(True)
            addButton.setEnabled(True)

            number _ le.(contacts)
            editButton.setEnabled(number >_ 1)
            removeButton.setEnabled(number >_ 1)
            findButton.setEnabled(number > 2)
            nextButton.setEnabled(number > 1)
            previousButton.setEnabled(number >1 )

            submitButton.hide()
            cancelButton.hide()

            exportButton.setEnabled(number >_ 1)

            loadButton.setEnabled(True)
            saveButton.setEnabled(number >_ 1)

    ___ saveToFile 
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

        pickle.dump(contacts, out_file)
        out_file.close()

    ___ loadFromFile 
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

        contacts _ pickle.load(in_file)
        in_file.close()

        __ le.(contacts) == 0:
            ?MB...information  "No contacts in file",
                    "The file you are attempting to open contains no "
                    "contacts.")
        ____
            ___ name, address __ contacts:
                nameLine.sT..(name)
                addressText.sT..(address)

        updateInterface(NavigationMode)

    ___ exportAsVCard 
        name _ str(nameLine.t__())
        address _ addressText.toPlainText()

        nameList _ name.split()

        __ le.(nameList) > 1:
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
    ___  -   parent_None):
        super(FindDialog, self). - (parent)

        findLabel _ QLabel("Enter the name of a contact:")
        lineEdit _ ?LE..

        findButton _ ?PB..("&Find")
        findText _ ''

        layout _ QHBoxLayout()
        layout.aW..(findLabel)
        layout.aW..(lineEdit)
        layout.aW..(findButton)

        sL..(layout)
        setWindowTitle("Find a Contact")

        findButton.c__.c..(findClicked)
        findButton.c__.c..(accept)

    ___ findClicked 
        t__ _ lineEdit.t__()

        __ no. t__:
            ?MB...information  "Empty Field",
                    "Please enter a name.")
            r_

        findText _ t__
        lineEdit.clear()
        hide()

    ___ getFindText 
        r_ findText


__ ______ __ ______
    ______ ___

    ____ ?.?W.. ______ ?A..

    app _ ?A..(___.a..

    addressBook _ AddressBook()
    addressBook.s..

    ___.exit(app.exec_())
