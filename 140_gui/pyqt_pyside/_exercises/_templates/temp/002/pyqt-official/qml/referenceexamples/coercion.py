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


______ sys

____ ?.QtCore ______ pyqtProperty, QCoreApplication, QObject, QUrl
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


class Person(QObject):
    ___ __init__(self, parent_None):
        super(Person, self).__init__(parent)

        self._name _ ''
        self._shoeSize _ 0

    @pyqtProperty(str)
    ___ name(self):
        return self._name

    @name.setter
    ___ name(self, name):
        self._name _ name

    @pyqtProperty(int)
    ___ shoeSize(self):
        return self._shoeSize

    @shoeSize.setter
    ___ shoeSize(self, shoeSize):
        self._shoeSize _ shoeSize


class Boy(Person):
    pass


class Girl(Person):
    pass


class BirthdayParty(QObject):
    ___ __init__(self, parent_None):
        super(BirthdayParty, self).__init__(parent)

        self._host _ None
        self._guests _ []

    @pyqtProperty(Person)
    ___ host(self):
        return self._host

    @host.setter
    ___ host(self, host):
        self._host _ host

    @pyqtProperty(QQmlListProperty)
    ___ guests(self):
        return QQmlListProperty(Person, self, self._guests)


app _ QCoreApplication(sys.argv)

qmlRegisterType(BirthdayParty, "People", 1, 0, "BirthdayParty")
qmlRegisterType(Person)
qmlRegisterType(Boy, "People", 1, 0, "Boy")
qmlRegisterType(Girl, "People", 1, 0, "Girl")

engine _ QQmlEngine()

component _ QQmlComponent(engine)
component.setData(QML, QUrl())

party _ component.create()

if party is not None and party.host is not None:
    print("\"%s\" is having a birthday!" % party.host.name)

    if isinstance(party.host, Boy):
        print("He is inviting:")
    else:
        print("She is inviting:")

    for guest in party.guests:
        print("    \"%s\"" % guest.name)
else:
    for e in component.errors
        print("Error:", e.toString());
