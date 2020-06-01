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


____ ?.?C.. ______ QFileInfo
____ ?.?W.. ______ (?A.., QCheckBox, QDialog,
        QDialogButtonBox, QFrame, QGroupBox, QLabel, QLineEdit, QListWidget,
        QTabWidget, QVBoxLayout, QWidget)


c_ TabDialog(QDialog):
    ___ __init__  fileName, parent_None):
        super(TabDialog, self).__init__(parent)

        fileInfo _ QFileInfo(fileName)

        tabWidget _ QTabWidget()
        tabWidget.addTab(GeneralTab(fileInfo), "General")
        tabWidget.addTab(PermissionsTab(fileInfo), "Permissions")
        tabWidget.addTab(ApplicationsTab(fileInfo), "Applications")

        buttonBox _ QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonBox.accepted.c..(self.accept)
        buttonBox.rejected.c..(self.reject)

        mainLayout _ ?VBL..
        mainLayout.aW..(tabWidget)
        mainLayout.aW..(buttonBox)
        self.sL..(mainLayout)

        self.setWindowTitle("Tab Dialog")


c_ GeneralTab(QWidget):
    ___ __init__  fileInfo, parent_None):
        super(GeneralTab, self).__init__(parent)

        fileNameLabel _ QLabel("File Name:")
        fileNameEdit _ QLineEdit(fileInfo.fileName())

        pathLabel _ QLabel("Path:")
        pathValueLabel _ QLabel(fileInfo.absoluteFilePath())
        pathValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        sizeLabel _ QLabel("Size:")
        size _ fileInfo.size() // 1024
        sizeValueLabel _ QLabel("%d K" % size)
        sizeValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        lastReadLabel _ QLabel("Last Read:")
        lastReadValueLabel _ QLabel(fileInfo.lastRead().toString())
        lastReadValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        lastModLabel _ QLabel("Last Modified:")
        lastModValueLabel _ QLabel(fileInfo.lastModified().toString())
        lastModValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        mainLayout _ ?VBL..
        mainLayout.aW..(fileNameLabel)
        mainLayout.aW..(fileNameEdit)
        mainLayout.aW..(pathLabel)
        mainLayout.aW..(pathValueLabel)
        mainLayout.aW..(sizeLabel)
        mainLayout.aW..(sizeValueLabel)
        mainLayout.aW..(lastReadLabel)
        mainLayout.aW..(lastReadValueLabel)
        mainLayout.aW..(lastModLabel)
        mainLayout.aW..(lastModValueLabel)
        mainLayout.addStretch(1)
        self.sL..(mainLayout)


c_ PermissionsTab(QWidget):
    ___ __init__  fileInfo, parent_None):
        super(PermissionsTab, self).__init__(parent)

        permissionsGroup _ QGroupBox("Permissions")

        readable _ QCheckBox("Readable")
        __ fileInfo.isReadable
            readable.setChecked(True)

        writable _ QCheckBox("Writable")
        __ fileInfo.isWritable
            writable.setChecked(True)

        executable _ QCheckBox("Executable")
        __ fileInfo.isExecutable
            executable.setChecked(True)

        ownerGroup _ QGroupBox("Ownership")

        ownerLabel _ QLabel("Owner")
        ownerValueLabel _ QLabel(fileInfo.owner())
        ownerValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        groupLabel _ QLabel("Group")
        groupValueLabel _ QLabel(fileInfo.group())
        groupValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        permissionsLayout _ ?VBL..
        permissionsLayout.aW..(readable)
        permissionsLayout.aW..(writable)
        permissionsLayout.aW..(executable)
        permissionsGroup.sL..(permissionsLayout)

        ownerLayout _ ?VBL..
        ownerLayout.aW..(ownerLabel)
        ownerLayout.aW..(ownerValueLabel)
        ownerLayout.aW..(groupLabel)
        ownerLayout.aW..(groupValueLabel)
        ownerGroup.sL..(ownerLayout)

        mainLayout _ ?VBL..
        mainLayout.aW..(permissionsGroup)
        mainLayout.aW..(ownerGroup)
        mainLayout.addStretch(1)
        self.sL..(mainLayout)


c_ ApplicationsTab(QWidget):
    ___ __init__  fileInfo, parent_None):
        super(ApplicationsTab, self).__init__(parent)

        topLabel _ QLabel("Open with:")

        applicationsListBox _ QListWidget()
        applications _   # list

        for i in range(1, 31):
            applications.ap..("Application %d" % i)

        applicationsListBox.insertItems(0, applications)

        alwaysCheckBox _ QCheckBox()

        __ fileInfo.suffix
            alwaysCheckBox _ QCheckBox("Always use this application to open "
                    "files with the extension '%s'" % fileInfo.suffix())
        ____
            alwaysCheckBox _ QCheckBox("Always use this application to open "
                    "this type of file")

        layout _ ?VBL..
        layout.aW..(topLabel)
        layout.aW..(applicationsListBox)
        layout.aW..(alwaysCheckBox)
        self.sL..(layout)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    __ le.(sys.argv) >_ 2:
        fileName _ sys.argv[1]
    ____
        fileName _ "."

    tabdialog _ TabDialog(fileName)
    tabdialog.s..
    sys.exit(app.exec_())
