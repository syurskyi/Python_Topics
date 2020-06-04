#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2018 Riverbank Computing Limited.
## Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
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
##   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
##     of its contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
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


____ ?.?C.. ______ QAbstractListModel, QModelIndex, __, ?U.., QVariant
____ ?.?G.. ______ QGuiApplication
____ ?.QtQuick ______ QQuickView

______ abstractitemmodel_rc


c_ Animal o..

    ___  -   type, size):
        _type _ type
        _size _ size

    ___ type
        r_ _type

    ___ size
        r_ _size


c_ AnimalModel(QAbstractListModel):

    TypeRole _ __.UserRole + 1
    SizeRole _ __.UserRole + 2

    _roles _ {TypeRole: b"type", SizeRole: b"size"}

    ___  -   parent_None):
        s__(AnimalModel, self). - (parent)

        _animals _   # list

    ___ addAnimal  animal):
        beginInsertRows(QModelIndex(), rowCount(), rowCount())
        _animals.ap..(animal)
        endInsertRows()

    ___ rowCount  parent_QModelIndex()):
        r_ le.(_animals)

    ___ data  index, role_Qt.DR..):
        ___
            animal _ _animals[index.row()]
        _____ IE..
            r_ ?V..

        __ role __ TypeRole:
            r_ animal.type()

        __ role __ SizeRole:
            r_ animal.size()

        r_ ?V..

    ___ roleNames
        r_ _roles


__ ______ __ ______
    ______ __
    ______ ___

    # This is necessary to avoid a possible crash when running from another
    # directory by ensuring the compiled version of the embedded QML file
    # doesn't get mixed up with another of the same name.
    __.chdir(__.p__ .dirname(__.p__ .abspath(__file__)))

    app _ QGuiApplication(___.a..

    model _ AnimalModel()
    model.addAnimal(Animal("Wolf", "Medium"))
    model.addAnimal(Animal("Polar bear", "Large"))
    model.addAnimal(Animal("Quoll", "Small"))

    view _ QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    ctxt _ view.rootContext()
    ctxt.setContextProperty('myModel', model)

    view.setSource(?U..('qrc:view.qml'))
    view.s..

    ___.e.. ?.e..
