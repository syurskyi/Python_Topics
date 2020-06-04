#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Darryl Wallace <wallacdj@gmail.com>.
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


____ ?.?C.. ______ (pS.., QAbstractListModel, ?D.., QLibraryInfo,
        QModelIndex, __)
____ ?.?W.. ______ (?A.., QGridLayout, ?L.., QLineEdit,
        ?LV.., ?SP.., QTextBrowser, ?W..)


c_ FileListModel(QAbstractListModel):
    numberPopulated _ pS..(in.)

    ___  -   parent_None):
        s__(FileListModel, self). - (parent)

        fileCount _ 0
        fileList _   # list

    ___ rowCount  parent_QModelIndex()):
        r_ fileCount

    ___ data  index, role_Qt.DR..):
        __ no. index.isValid
            r_ N..

        __ index.row() >_ le.(fileList) or index.row() < 0:
            r_ N..

        __ role __ __.DR..:
            r_ fileList[index.row()]

        __ role __ __.BackgroundRole:
            batch _ (index.row() // 100) % 2
            __ batch __ 0:
                r_ ?A...p...base()

            r_ ?A...p...alternateBase()

        r_ N..

    ___ canFetchMore  index):
        r_ fileCount < le.(fileList)

    ___ fetchMore  index):
        remainder _ le.(fileList) - fileCount
        itemsToFetch _ min(100, remainder)

        beginInsertRows(QModelIndex(), fileCount,
                fileCount + itemsToFetch)

        fileCount +_ itemsToFetch

        endInsertRows()

        numberPopulated.e..(itemsToFetch)

    ___ setDirPath  pa__):
        dir _ ?D..(pa__)

        beginResetModel()
        fileList _ dir.entryList()
        fileCount _ 0
        endResetModel()


c_ Window(?W..):
    ___  -   parent_None):
        s__(Window, self). - (parent)

        model _ FileListModel
        model.setDirPath(QLibraryInfo.location(QLibraryInfo.PrefixPath))

        label _ ?L..("Directory")
        lineEdit _ ?LE..
        label.setBuddy(lineEdit)

        view _ ?LV..
        view.sM..(model)

        logViewer _ QTextBrowser()
        logViewer.sSP..(?SP..(?SP...Preferred, ?SP...Preferred))

        lineEdit.tC...c..(model.setDirPath)
        lineEdit.tC...c..(logViewer.clear)
        model.numberPopulated.c..(updateLog)

        layout _ QGridLayout()
        layout.aW..(label, 0, 0)
        layout.aW..(lineEdit, 0, 1)
        layout.aW..(view, 1, 0, 1, 2)
        layout.aW..(logViewer, 2, 0, 1, 2)

        sL..(layout)
        sWT..("Fetch More Example")

    ___ updateLog  number):
        logViewer.ap..("%d items added." % number)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    window _ Window()
    window.s..

    ___.e.. ?.e..
