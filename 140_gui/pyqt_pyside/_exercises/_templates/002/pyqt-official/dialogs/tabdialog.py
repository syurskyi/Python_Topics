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
____ ?.?W.. ______ (?A.., QCheckBox, ?D..,
        ?DBB..., QFrame, ?GB.., ?L.., QLineEdit, QListWidget,
        ?TW.., ?VBL.., ?W..)


c_ TabDialog(?D..):
    ___  -   fileName, parent_None):
        s__(TabDialog, self). - (parent)

        fileInfo _ QFileInfo(fileName)

        tabWidget _ ?TW..()
        tabWidget.aT..(GeneralTab(fileInfo), "General")
        tabWidget.aT..(PermissionsTab(fileInfo), "Permissions")
        tabWidget.aT..(ApplicationsTab(fileInfo), "Applications")

        buttonBox _ ?DBB...(?DBB....Ok | ?DBB....Cancel)

        buttonBox.a___.c..(accept)
        buttonBox.r___.c..(reject)

        mainLayout _ ?VBL..
        mainLayout.aW..(tabWidget)
        mainLayout.aW..(buttonBox)
        sL..(mainLayout)

        sWT..("Tab Dialog")


c_ GeneralTab(?W..):
    ___  -   fileInfo, parent_None):
        s__(GeneralTab, self). - (parent)

        fileNameLabel _ ?L..("File Name:")
        fileNameEdit _ QLineEdit(fileInfo.fileName())

        pathLabel _ ?L..("Path:")
        pathValueLabel _ ?L..(fileInfo.absoluteFilePath())
        pathValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        sizeLabel _ ?L..("Size:")
        size _ fileInfo.size() // 1024
        sizeValueLabel _ ?L..("%d K" % size)
        sizeValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        lastReadLabel _ ?L..("Last Read:")
        lastReadValueLabel _ ?L..(fileInfo.lastRead().toString())
        lastReadValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        lastModLabel _ ?L..("Last Modified:")
        lastModValueLabel _ ?L..(fileInfo.lastModified().toString())
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
        sL..(mainLayout)


c_ PermissionsTab(?W..):
    ___  -   fileInfo, parent_None):
        s__(PermissionsTab, self). - (parent)

        permissionsGroup _ ?GB..("Permissions")

        readable _ QCheckBox("Readable")
        __ fileInfo.isReadable
            readable.sC__( st.

        writable _ QCheckBox("Writable")
        __ fileInfo.isWritable
            writable.sC__( st.

        executable _ QCheckBox("Executable")
        __ fileInfo.isExecutable
            executable.sC__( st.

        ownerGroup _ ?GB..("Ownership")

        ownerLabel _ ?L..("Owner")
        ownerValueLabel _ ?L..(fileInfo.owner())
        ownerValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        groupLabel _ ?L..("Group")
        groupValueLabel _ ?L..(fileInfo.group())
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
        sL..(mainLayout)


c_ ApplicationsTab(?W..):
    ___  -   fileInfo, parent_None):
        s__(ApplicationsTab, self). - (parent)

        topLabel _ ?L..("Open with:")

        applicationsListBox _ QListWidget()
        applications _   # list

        ___ i __ ra..(1, 31):
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
        sL..(layout)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    __ le.(___.a.. >_ 2:
        fileName _ ___.argv[1]
    ____
        fileName _ "."

    tabdialog _ TabDialog(fileName)
    tabdialog.s..
    ___.e.. ?.e..
