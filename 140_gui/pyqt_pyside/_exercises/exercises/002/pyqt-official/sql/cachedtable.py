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


____ ?.?C.. ______ __
____ ?.?W.. ______ (?A.., ?D.., ?DBB...,
        ?HBL.., ?MB.., ?PB.., QTableView)
____ ?.?S.. ______ ?STM..

______ connection


c_ TableEditor(?D..):
    ___  -   tableName, parent_None):
        s__(TableEditor, self). - (parent)

        model _ ?STM..
        model.sT..(tableName)
        model.sES..(?STM...OnManualSubmit)
        model.select()

        model.setHeaderData(0, __.H.., "ID")
        model.setHeaderData(1, __.H.., "First name")
        model.setHeaderData(2, __.H.., "Last name")

        view _ ?TV..
        view.sM..(model)

        submitButton _ ?PB..("Submit")
        submitButton.setDefault( st.
        revertButton _ ?PB..("&Revert")
        quitButton _ ?PB..("Quit")

        buttonBox _ ?DBB...(__.Vertical)
        buttonBox.addButton(submitButton, ?DBB....ActionRole)
        buttonBox.addButton(revertButton, ?DBB....ActionRole)
        buttonBox.addButton(quitButton, ?DBB....RejectRole)

        submitButton.c__.c..(submit)
        revertButton.c__.c..(model.revertAll)
        quitButton.c__.c..(close)

        mainLayout _ ?HBL..
        mainLayout.aW..(view)
        mainLayout.aW..(buttonBox)
        sL..(mainLayout)

        sWT..("Cached Table")

    ___ submit 
        model.database().transaction()
        __ model.submitAll
            model.database().c__
        ____
            model.database().rollback()
            ?MB...w..  "Cached Table",
                        "The database reported an error: %s" % model.lastError().t__())


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    __ no. connection.createConnection
        ___.e..(1)

    editor _ TableEditor('person')
    editor.s..
    ___.e..(editor.e..
