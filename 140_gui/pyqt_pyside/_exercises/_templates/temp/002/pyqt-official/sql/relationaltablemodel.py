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
____ ?.?W.. ______ ?A.., QTableView
____ ?.?S.. ______ (?SQ.., QSqlRelation, ?SRD..,
        QSqlRelationalTableModel, ?STM..)

______ connection


___ initializeModel(model):
    model.sT..('employee')

    model.sES..(?STM...OnManualSubmit)
    model.setRelation(2, QSqlRelation('city', 'id', 'name'))
    model.setRelation(3, QSqlRelation('country', 'id', 'name'))

    model.setHeaderData(0, __.H.., "ID")
    model.setHeaderData(1, __.H.., "Name")
    model.setHeaderData(2, __.H.., "City")
    model.setHeaderData(3, __.H.., "Country")

    model.select()


___ createView(title, model):
    view _ ?TV..
    view.sM..(model)
    view.sID..(?SRD..(view))
    view.sWT..(title)

    r_ view


___ createRelationalTables
    query _ ?SQ..()

    query.e..("create table employee(id int, name varchar(20), city int, country int)")
    query.e..("insert into employee values(1, 'Espen', 5000, 47)")
    query.e..("insert into employee values(2, 'Harald', 80000, 49)")
    query.e..("insert into employee values(3, 'Sam', 100, 41)")

    query.e..("create table city(id int, name varchar(20))")
    query.e..("insert into city values(100, 'San Jose')")
    query.e..("insert into city values(5000, 'Oslo')")
    query.e..("insert into city values(80000, 'Munich')")

    query.e..("create table country(id int, name varchar(20))")
    query.e..("insert into country values(41, 'USA')")
    query.e..("insert into country values(47, 'Norway')")
    query.e..("insert into country values(49, 'Germany')")


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    __ no. connection.createConnection
        ___.e..(1)

    createRelationalTables()

    model _ QSqlRelationalTableModel()

    initializeModel(model)

    view _ createView("Relational Table Model", model)

    view.s..

    ___.e.. ?.e..
