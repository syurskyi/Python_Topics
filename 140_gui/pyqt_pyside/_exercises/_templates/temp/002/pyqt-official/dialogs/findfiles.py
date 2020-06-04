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


____ ?.?C.. ______ (?D.., QIODevice, QFile, QFileInfo, __, QTextStream,
        ?U..)
____ ?.?G.. ______ QDesktopServices
____ ?.?W.. ______ (?AIV.., ?A.., ?CB,
        ?D.., ?FD.., QGridLayout, ?HBL.., ?HV.., ?L..,
        QProgressDialog, ?PB.., ?SP.., ?TW..,
        ?TWI..)


c_ Window(?D..):
    ___  -   parent_None):
        s__(Window, self). - (parent)

        browseButton _ createButton("&Browse...", browse)
        findButton _ createButton("&Find", find)

        fileComboBox _ createComboBox("*")
        textComboBox _ createComboBox()
        directoryComboBox _ createComboBox(?D...currentPath())

        fileLabel _ ?L..("Named:")
        textLabel _ ?L..("Containing text:")
        directoryLabel _ ?L..("In directory:")
        filesFoundLabel _ ?L..

        createFilesTable()

        buttonsLayout _ ?HBL..
        buttonsLayout.addStretch()
        buttonsLayout.aW..(findButton)

        mainLayout _ QGridLayout()
        mainLayout.aW..(fileLabel, 0, 0)
        mainLayout.aW..(fileComboBox, 0, 1, 1, 2)
        mainLayout.aW..(textLabel, 1, 0)
        mainLayout.aW..(textComboBox, 1, 1, 1, 2)
        mainLayout.aW..(directoryLabel, 2, 0)
        mainLayout.aW..(directoryComboBox, 2, 1)
        mainLayout.aW..(browseButton, 2, 2)
        mainLayout.aW..(filesTable, 3, 0, 1, 3)
        mainLayout.aW..(filesFoundLabel, 4, 0)
        mainLayout.aL..(buttonsLayout, 5, 0, 1, 3)
        sL..(mainLayout)

        sWT..("Find Files")
        r..(700, 300)

    ___ browse
        directory _ ?FD...getExistingDirectory  "Find Files",
                ?D...currentPath())

        __ directory:
            __ directoryComboBox.findText(directory) __ -1:
                directoryComboBox.aI..(directory)

            directoryComboBox.sCI..(directoryComboBox.findText(directory))

    @staticmethod
    ___ updateComboBox(comboBox):
        __ comboBox.findText(comboBox.currentText()) __ -1:
            comboBox.aI..(comboBox.currentText())

    ___ find
        filesTable.sRC..(0)

        fileName _ fileComboBox.currentText()
        t__ _ textComboBox.currentText()
        pa__ _ directoryComboBox.currentText()

        updateComboBox(fileComboBox)
        updateComboBox(textComboBox)
        updateComboBox(directoryComboBox)

        currentDir _ ?D..(pa__)
        __ no. fileName:
            fileName _ "*"
        files _ currentDir.entryList([fileName],
                ?D...Files | ?D...NSL..)

        __ t__:
            files _ findFiles(files, t__)
        showFiles(files)

    ___ findFiles  files, t__):
        progressDialog _ QProgressDialog

        progressDialog.setCancelButtonText("&Cancel")
        progressDialog.setRange(0, files.count())
        progressDialog.sWT..("Find Files")

        foundFiles _   # list

        ___ i __ ra..(files.count()):
            progressDialog.sV..(i)
            progressDialog.setLabelText("Searching file number %d of %d..." % (i, files.count()))
            ?A...processEvents()

            __ progressDialog.wasCanceled
                break

            inFile _ QFile(currentDir.absoluteFilePath(files[i]))

            __ inFile.o..(QIODevice.ReadOnly):
                stream _ QTextStream(inFile)
                w__ no. stream.atEnd
                    __ progressDialog.wasCanceled
                        break
                    line _ stream.readLine()
                    __ t__ __ line:
                        foundFiles.ap..(files[i])
                        break

        progressDialog.c..

        r_ foundFiles

    ___ showFiles  files):
        ___ fn __ files:
            file _ QFile(currentDir.absoluteFilePath(fn))
            size _ QFileInfo(file).size()

            fileNameItem _ ?TWI..(fn)
            fileNameItem.setFlags(fileNameItem.flags() ^ __.IIE..)
            sizeItem _ ?TWI..("%d KB" % (in.((size + 1023) / 1024)))
            sizeItem.setTextAlignment(__.AlignVCenter | __.AlignRight)
            sizeItem.setFlags(sizeItem.flags() ^ __.IIE..)

            row _ filesTable.rowCount()
            filesTable.insertRow(row)
            filesTable.setItem(row, 0, fileNameItem)
            filesTable.setItem(row, 1, sizeItem)

        filesFoundLabel.sT..("%d file(s) found (Double click on a file to open it)" % le.(files))

    ___ createButton  t__, member):
        button _ ?PB..(t__)
        button.c__.c..(member)
        r_ button

    ___ createComboBox  text_""):
        comboBox _ ?CB()
        comboBox.sE..( st.
        comboBox.aI..(t__)
        comboBox.sSP..(?SP...E.., ?SP...Preferred)
        r_ comboBox

    ___ createFilesTable
        filesTable _ ?TW..(0, 2)
        filesTable.setSelectionBehavior(?AIV...SelectRows)

        filesTable.sHHL..(("File Name", "Size"))
        filesTable.hH.. .sSRM..(0, ?HV...Stretch)
        filesTable.vH.. .hide()
        filesTable.setShowGrid F..

        filesTable.cellActivated.c..(openFileOfItem)

    ___ openFileOfItem  row, column):
        item _ filesTable.item(row, 0)

        QDesktopServices.openUrl(?U..(currentDir.absoluteFilePath(item.t__())))


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ Window()
    window.s..
    ___.e.. ?.e..
