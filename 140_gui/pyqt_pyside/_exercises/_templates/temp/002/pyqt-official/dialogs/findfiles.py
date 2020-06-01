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


____ ?.?C.. ______ (QDir, QIODevice, QFile, QFileInfo, __, QTextStream,
        QUrl)
____ ?.?G.. ______ QDesktopServices
____ ?.?W.. ______ (QAbstractItemView, ?A.., QComboBox,
        QDialog, ?FD.., QGridLayout, QHBoxLayout, QHeaderView, QLabel,
        QProgressDialog, ?PB.., QSizePolicy, QTableWidget,
        QTableWidgetItem)


c_ Window(QDialog):
    ___ __init__  parent_None):
        super(Window, self).__init__(parent)

        browseButton _ self.createButton("&Browse...", self.browse)
        findButton _ self.createButton("&Find", self.find)

        self.fileComboBox _ self.createComboBox("*")
        self.textComboBox _ self.createComboBox()
        self.directoryComboBox _ self.createComboBox(QDir.currentPath())

        fileLabel _ QLabel("Named:")
        textLabel _ QLabel("Containing text:")
        directoryLabel _ QLabel("In directory:")
        self.filesFoundLabel _ QLabel()

        self.createFilesTable()

        buttonsLayout _ QHBoxLayout()
        buttonsLayout.addStretch()
        buttonsLayout.aW..(findButton)

        mainLayout _ QGridLayout()
        mainLayout.aW..(fileLabel, 0, 0)
        mainLayout.aW..(self.fileComboBox, 0, 1, 1, 2)
        mainLayout.aW..(textLabel, 1, 0)
        mainLayout.aW..(self.textComboBox, 1, 1, 1, 2)
        mainLayout.aW..(directoryLabel, 2, 0)
        mainLayout.aW..(self.directoryComboBox, 2, 1)
        mainLayout.aW..(browseButton, 2, 2)
        mainLayout.aW..(self.filesTable, 3, 0, 1, 3)
        mainLayout.aW..(self.filesFoundLabel, 4, 0)
        mainLayout.addLayout(buttonsLayout, 5, 0, 1, 3)
        self.sL..(mainLayout)

        self.setWindowTitle("Find Files")
        self.resize(700, 300)

    ___ browse(self):
        directory _ ?FD...getExistingDirectory  "Find Files",
                QDir.currentPath())

        __ directory:
            __ self.directoryComboBox.findText(directory) == -1:
                self.directoryComboBox.addItem(directory)

            self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))

    @staticmethod
    ___ updateComboBox(comboBox):
        __ comboBox.findText(comboBox.currentText()) == -1:
            comboBox.addItem(comboBox.currentText())

    ___ find(self):
        self.filesTable.setRowCount(0)

        fileName _ self.fileComboBox.currentText()
        t__ _ self.textComboBox.currentText()
        path _ self.directoryComboBox.currentText()

        self.updateComboBox(self.fileComboBox)
        self.updateComboBox(self.textComboBox)
        self.updateComboBox(self.directoryComboBox)

        self.currentDir _ QDir(path)
        __ no. fileName:
            fileName _ "*"
        files _ self.currentDir.entryList([fileName],
                QDir.Files | QDir.NoSymLinks)

        __ t__:
            files _ self.findFiles(files, t__)
        self.showFiles(files)

    ___ findFiles  files, t__):
        progressDialog _ QProgressDialog(self)

        progressDialog.setCancelButtonText("&Cancel")
        progressDialog.setRange(0, files.count())
        progressDialog.setWindowTitle("Find Files")

        foundFiles _   # list

        for i in range(files.count()):
            progressDialog.setValue(i)
            progressDialog.setLabelText("Searching file number %d of %d..." % (i, files.count()))
            ?A...processEvents()

            __ progressDialog.wasCanceled
                break

            inFile _ QFile(self.currentDir.absoluteFilePath(files[i]))

            __ inFile.o..(QIODevice.ReadOnly):
                stream _ QTextStream(inFile)
                w__ no. stream.atEnd
                    __ progressDialog.wasCanceled
                        break
                    line _ stream.readLine()
                    __ t__ in line:
                        foundFiles.ap..(files[i])
                        break

        progressDialog.close()

        r_ foundFiles

    ___ showFiles  files):
        for fn in files:
            file _ QFile(self.currentDir.absoluteFilePath(fn))
            size _ QFileInfo(file).size()

            fileNameItem _ QTableWidgetItem(fn)
            fileNameItem.setFlags(fileNameItem.flags() ^ __.ItemIsEditable)
            sizeItem _ QTableWidgetItem("%d KB" % (int((size + 1023) / 1024)))
            sizeItem.setTextAlignment(__.AlignVCenter | __.AlignRight)
            sizeItem.setFlags(sizeItem.flags() ^ __.ItemIsEditable)

            row _ self.filesTable.rowCount()
            self.filesTable.insertRow(row)
            self.filesTable.setItem(row, 0, fileNameItem)
            self.filesTable.setItem(row, 1, sizeItem)

        self.filesFoundLabel.sT..("%d file(s) found (Double click on a file to open it)" % le.(files))

    ___ createButton  t__, member):
        button _ ?PB..(t__)
        button.c__.c..(member)
        r_ button

    ___ createComboBox  text_""):
        comboBox _ QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(t__)
        comboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        r_ comboBox

    ___ createFilesTable(self):
        self.filesTable _ QTableWidget(0, 2)
        self.filesTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.filesTable.setHorizontalHeaderLabels(("File Name", "Size"))
        self.filesTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.filesTable.verticalHeader().hide()
        self.filesTable.setShowGrid F..

        self.filesTable.cellActivated.c..(self.openFileOfItem)

    ___ openFileOfItem  row, column):
        item _ self.filesTable.item(row, 0)

        QDesktopServices.openUrl(QUrl(self.currentDir.absoluteFilePath(item.t__())))


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    window _ Window()
    window.s..
    ___.exit(app.exec_())
