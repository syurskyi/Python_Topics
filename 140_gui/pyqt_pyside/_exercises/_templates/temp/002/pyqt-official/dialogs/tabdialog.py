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


____ ?.QtCore ______ QFileInfo
____ ?.?W.. ______ (?A.., QCheckBox, QDialog,
        QDialogButtonBox, QFrame, QGroupBox, QLabel, QLineEdit, QListWidget,
        QTabWidget, QVBoxLayout, QWidget)


class TabDialog(QDialog):
    ___ __init__(self, fileName, parent_None):
        super(TabDialog, self).__init__(parent)

        fileInfo _ QFileInfo(fileName)

        tabWidget _ QTabWidget()
        tabWidget.addTab(GeneralTab(fileInfo), "General")
        tabWidget.addTab(PermissionsTab(fileInfo), "Permissions")
        tabWidget.addTab(ApplicationsTab(fileInfo), "Applications")

        buttonBox _ QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonBox.accepted.c..(self.accept)
        buttonBox.rejected.c..(self.reject)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Tab Dialog")


class GeneralTab(QWidget):
    ___ __init__(self, fileInfo, parent_None):
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

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(fileNameLabel)
        mainLayout.addWidget(fileNameEdit)
        mainLayout.addWidget(pathLabel)
        mainLayout.addWidget(pathValueLabel)
        mainLayout.addWidget(sizeLabel)
        mainLayout.addWidget(sizeValueLabel)
        mainLayout.addWidget(lastReadLabel)
        mainLayout.addWidget(lastReadValueLabel)
        mainLayout.addWidget(lastModLabel)
        mainLayout.addWidget(lastModValueLabel)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)


class PermissionsTab(QWidget):
    ___ __init__(self, fileInfo, parent_None):
        super(PermissionsTab, self).__init__(parent)

        permissionsGroup _ QGroupBox("Permissions")

        readable _ QCheckBox("Readable")
        if fileInfo.isReadable
            readable.setChecked(True)

        writable _ QCheckBox("Writable")
        if fileInfo.isWritable
            writable.setChecked(True)

        executable _ QCheckBox("Executable")
        if fileInfo.isExecutable
            executable.setChecked(True)

        ownerGroup _ QGroupBox("Ownership")

        ownerLabel _ QLabel("Owner")
        ownerValueLabel _ QLabel(fileInfo.owner())
        ownerValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        groupLabel _ QLabel("Group")
        groupValueLabel _ QLabel(fileInfo.group())
        groupValueLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        permissionsLayout _ QVBoxLayout()
        permissionsLayout.addWidget(readable)
        permissionsLayout.addWidget(writable)
        permissionsLayout.addWidget(executable)
        permissionsGroup.setLayout(permissionsLayout)

        ownerLayout _ QVBoxLayout()
        ownerLayout.addWidget(ownerLabel)
        ownerLayout.addWidget(ownerValueLabel)
        ownerLayout.addWidget(groupLabel)
        ownerLayout.addWidget(groupValueLabel)
        ownerGroup.setLayout(ownerLayout)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(permissionsGroup)
        mainLayout.addWidget(ownerGroup)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)


class ApplicationsTab(QWidget):
    ___ __init__(self, fileInfo, parent_None):
        super(ApplicationsTab, self).__init__(parent)

        topLabel _ QLabel("Open with:")

        applicationsListBox _ QListWidget()
        applications _ []

        for i in range(1, 31):
            applications.append("Application %d" % i)

        applicationsListBox.insertItems(0, applications)

        alwaysCheckBox _ QCheckBox()

        if fileInfo.suffix
            alwaysCheckBox _ QCheckBox("Always use this application to open "
                    "files with the extension '%s'" % fileInfo.suffix())
        else:
            alwaysCheckBox _ QCheckBox("Always use this application to open "
                    "this type of file")

        layout _ QVBoxLayout()
        layout.addWidget(topLabel)
        layout.addWidget(applicationsListBox)
        layout.addWidget(alwaysCheckBox)
        self.setLayout(layout)


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    if len(sys.argv) >_ 2:
        fileName _ sys.argv[1]
    else:
        fileName _ "."

    tabdialog _ TabDialog(fileName)
    tabdialog.s..
    sys.exit(app.exec_())
