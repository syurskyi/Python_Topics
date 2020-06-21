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
____ ?.?G.. ______ ?C..
____ ?.?W.. ______ ?A.., QTableView
____ ?.?S.. ______ ?SQ.., QSqlQueryModel

______ connection


c_ CustomSqlModel(QSqlQueryModel):
    ___ data  index, role):
        value _ s__(CustomSqlModel, self).data(index, role)
        __ value __ no. N.. and role __ __.DR..:
            __ i...column() __ 0:
                r_ '#%d' % value
            ____ i...column() __ 2:
                r_ value.upper()

        __ role __ __.TextColorRole and i...column() __ 1:
            r_ ?C..(__.blue)

        r_ value


c_ EditableSqlModel(QSqlQueryModel):
    ___ flags  index):
        flags _ s__(EditableSqlModel, self).flags(index)

        __ i...column() __ (1, 2):
            flags |_ __.IIE..

        r_ flags

    ___ setData  index, value, role):
        __ i...column() no. __ (1, 2):
            r_ F..

        primaryKeyIndex _ index(i...row(), 0)
        id _ data(primaryKeyIndex)

        c..

        __ i...column() __ 1:
            ok _ setFirstName(id, value)
        ____
            ok _ setLastName(id, value)

        refresh()
        r_ ok

    ___ refresh
        setQuery('select * from person')
        setHeaderData(0, __.H.., "ID")
        setHeaderData(1, __.H.., "First name")
        setHeaderData(2, __.H.., "Last name")

    ___ setFirstName  personId, firstName):
        query _ ?SQ..()
        query.prepare('update person set firstname = ? where id = ?')
        query.addBindValue(firstName)
        query.addBindValue(personId)
        r_ query.e..

    ___ setLastName  personId, lastName):
        query _ ?SQ..()
        query.prepare('update person set lastname = ? where id = ?')
        query.addBindValue(lastName)
        query.addBindValue(personId)
        r_ query.e..


___ initializeModel(model):
    model.setQuery('select * from person')
    model.setHeaderData(0, __.H.., "ID")
    model.setHeaderData(1, __.H.., "First name")
    model.setHeaderData(2, __.H.., "Last name")


offset _ 0
views _   # list

___ createView(title, model):
    gl.. offset, views

    view _ ?TV..
    views.ap..(view)
    view.sM..(model)
    view.sWT..(title)
    view.move(100 + offset, 100 + offset)
    offset +_ 20
    view.s..


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    __ no. connection.createConnection
        ___.e..(1)

    plainModel _ QSqlQueryModel()
    editableModel _ EditableSqlModel()
    customModel _ CustomSqlModel()

    initializeModel(plainModel)
    initializeModel(editableModel)
    initializeModel(customModel)

    createView("Plain Query Model", plainModel)
    createView("Editable Query Model", editableModel)
    createView("Custom Query Model", customModel)

    ___.e.. ?.e..
