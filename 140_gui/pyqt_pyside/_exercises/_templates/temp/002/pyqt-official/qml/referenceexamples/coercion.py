#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
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


______ ___

____ ?.?C.. ______ pP..,  ?CA.., ?O.., ?U..
____ ?.QtQml ______ (qmlRegisterType, QQmlComponent, QQmlEngine,
        QQmlListProperty)


QML _ b'''
import People 1.0

BirthdayParty {
    host: Boy {
        name: "Bob Jones"
        shoeSize: 12
    }

    guests: [
        Boy { name: "Leo Hodges" },
        Boy { name: "Jack Smith" },
        Girl { name: "Anne Brown" }
    ]
}
'''


c_ Person(?O..):
    ___  -   parent_None):
        s__(Person, self). - (parent)

        _name _ ''
        _shoeSize _ 0

    @pP.. st.
    ___ name
        r_ _name

    @name.setter
    ___ name  name):
        _name _ name

    @pP..(in.)
    ___ shoeSize
        r_ _shoeSize

    @shoeSize.setter
    ___ shoeSize  shoeSize):
        _shoeSize _ shoeSize


c_ Boy(Person):
    p..


c_ Girl(Person):
    p..


c_ BirthdayParty(?O..):
    ___  -   parent_None):
        s__(BirthdayParty, self). - (parent)

        _host _ N..
        _guests _   # list

    @pP..(Person)
    ___ host
        r_ _host

    @host.setter
    ___ host  host):
        _host _ host

    @pP..(QQmlListProperty)
    ___ guests
        r_ QQmlListProperty(Person, self, _guests)


app _  ?CA..(___.a..

qmlRegisterType(BirthdayParty, "People", 1, 0, "BirthdayParty")
qmlRegisterType(Person)
qmlRegisterType(Boy, "People", 1, 0, "Boy")
qmlRegisterType(Girl, "People", 1, 0, "Girl")

engine _ QQmlEngine()

component _ QQmlComponent(engine)
component.setData(QML, ?U..())

party _ component.create()

__ party __ no. N.. and party.host __ no. N..:
    print("\"%s\" is having a birthday!" % party.host.name)

    __ isinstance(party.host, Boy):
        print("He is inviting:")
    ____
        print("She is inviting:")

    ___ guest __ party.guests:
        print("    \"%s\"" % guest.name)
____
    ___ e __ component.errors
        print("Error:", e.toString());
