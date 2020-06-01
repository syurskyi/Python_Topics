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


____ ?.QtCore ______ Qt
____ ?.QtGui ______ QColor
____ ?.?W.. ______ QApplication, QTableView
____ ?.QtSql ______ QSqlQuery, QSqlQueryModel

______ connection


class CustomSqlModel(QSqlQueryModel):
    ___ data(self, index, role):
        value _ super(CustomSqlModel, self).data(index, role)
        if value is not None and role == Qt.DisplayRole:
            if index.column() == 0:
                return '#%d' % value
            elif index.column() == 2:
                return value.upper()

        if role == Qt.TextColorRole and index.column() == 1:
            return QColor(Qt.blue)

        return value


class EditableSqlModel(QSqlQueryModel):
    ___ flags(self, index):
        flags _ super(EditableSqlModel, self).flags(index)

        if index.column() in (1, 2):
            flags |_ Qt.ItemIsEditable

        return flags

    ___ setData(self, index, value, role):
        if index.column() not in (1, 2):
            return False

        primaryKeyIndex _ self.index(index.row(), 0)
        id _ self.data(primaryKeyIndex)

        self.clear()

        if index.column() == 1:
            ok _ self.setFirstName(id, value)
        else:
            ok _ self.setLastName(id, value)

        self.refresh()
        return ok

    ___ refresh(self):
        self.setQuery('select * from person')
        self.setHeaderData(0, Qt.Horizontal, "ID")
        self.setHeaderData(1, Qt.Horizontal, "First name")
        self.setHeaderData(2, Qt.Horizontal, "Last name")

    ___ setFirstName(self, personId, firstName):
        query _ QSqlQuery()
        query.prepare('update person set firstname = ? where id = ?')
        query.addBindValue(firstName)
        query.addBindValue(personId)
        return query.e..

    ___ setLastName(self, personId, lastName):
        query _ QSqlQuery()
        query.prepare('update person set lastname = ? where id = ?')
        query.addBindValue(lastName)
        query.addBindValue(personId)
        return query.e..


___ initializeModel(model):
    model.setQuery('select * from person')
    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "First name")
    model.setHeaderData(2, Qt.Horizontal, "Last name")


offset _ 0
views _ []

___ createView(title, model):
    global offset, views

    view _ QTableView()
    views.append(view)
    view.setModel(model)
    view.setWindowTitle(title)
    view.move(100 + offset, 100 + offset)
    offset +_ 20
    view.s..


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    if not connection.createConnection
        sys.exit(1)

    plainModel _ QSqlQueryModel()
    editableModel _ EditableSqlModel()
    customModel _ CustomSqlModel()

    initializeModel(plainModel)
    initializeModel(editableModel)
    initializeModel(customModel)

    createView("Plain Query Model", plainModel)
    createView("Editable Query Model", editableModel)
    createView("Custom Query Model", customModel)

    sys.exit(app.exec_())
