#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
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


____ ?.?C.. ______ pS.., QMimeData, __
____ ?.?G.. ______ ?P.., ?P..
____ ?.?W.. ______ (QAbstractItemView, ?A.., QDialogButtonBox,
        QFrame, QLabel, ?PB.., QTableWidget, QTableWidgetItem,
        QVBoxLayout, ?W..)


c_ DropArea(QLabel):

    changed _ pS..(QMimeData)

    ___  -   parent _ N..):
        super(DropArea, self). - (parent)

        sMS..(200, 200)
        setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        setAlignment(__.AlignCenter)
        setAcceptDrops( st.
        setAutoFillBackground( st.
        c..

    ___ dragEnterEvent  event):
        sT..("<drop content>")
        setBackgroundRole(?P...Highlight)
        event.acceptProposedAction()
        changed.e..(event.mimeData())

    ___ dragMoveEvent  event):
        event.acceptProposedAction()

    ___ dropEvent  event):
        mimeData _ event.mimeData()
        __ mimeData.hasImage
            setPixmap(?P..(mimeData.imageData()))
        ____ mimeData.hasHtml
            sT..(mimeData.html())
            setTextFormat(__.RichText)
        ____ mimeData.hasText
            sT..(mimeData.t__())
            setTextFormat(__.PlainText)
        ____ mimeData.hasUrls
            sT..("\n".join([url.pa__() ___ url __ mimeData.urls()]))
        ____
            sT..("Cannot display data")

        setBackgroundRole(?P...Dark)
        event.acceptProposedAction()

    ___ dragLeaveEvent  event):
        c..
        event.accept()

    ___ clear
        sT..("<drop content>")
        setBackgroundRole(?P...Dark)
        changed.e..(N..)


c_ DropSiteWindow(?W..):

    ___  - 
        super(DropSiteWindow, self). - ()

        abstractLabel _ QLabel(
                "This example accepts drags from other applications and "
                "displays the MIME types provided by the drag object.")
        abstractLabel.setWordWrap( st.
        abstractLabel.adjustSize()

        dropArea _ DropArea()
        dropArea.changed.c..(updateFormatsTable)

        formatsTable _ QTableWidget()
        formatsTable.setColumnCount(2)
        formatsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        formatsTable.setHorizontalHeaderLabels(["Format", "Content"])
        formatsTable.horizontalHeader().setStretchLastSection( st.

        clearButton _ ?PB..("Clear")
        quitButton _ ?PB..("Quit")

        buttonBox _ QDialogButtonBox()
        buttonBox.addButton(clearButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QDialogButtonBox.RejectRole)

        quitButton.pressed.c..(close)
        clearButton.pressed.c..(dropArea.clear)

        mainLayout _ ?VBL..
        mainLayout.aW..(abstractLabel)
        mainLayout.aW..(dropArea)
        mainLayout.aW..(formatsTable)
        mainLayout.aW..(buttonBox)
        sL..(mainLayout)

        sWT..("Drop Site")
        sMS..(350, 500)

    ___ updateFormatsTable  mimeData_None):
        formatsTable.setRowCount(0)

        __ mimeData __ N..:
            r_

        ___ format __ mimeData.formats
            formatItem _ QTableWidgetItem(format)
            formatItem.setFlags(__.ItemIsEnabled)
            formatItem.setTextAlignment(__.AlignTop | __.AlignLeft)

            __ format __ 'text/plain':
                t__ _ mimeData.t__().strip()
            ____ format __ 'text/html':
                t__ _ mimeData.html().strip()
            ____ format __ 'text/uri-list':
                t__ _ " ".join([url.toString() ___ url __ mimeData.urls()])
            ____
                t__ _ " ".join(["%02X" % ord(datum) ___ datum __ mimeData.data(format)])

            row _ formatsTable.rowCount()
            formatsTable.insertRow(row)
            formatsTable.setItem(row, 0, QTableWidgetItem(format))
            formatsTable.setItem(row, 1, QTableWidgetItem(t__))

        formatsTable.resizeColumnToContents(0)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ DropSiteWindow()
    window.s..
    ___.e..(app.exec_())

