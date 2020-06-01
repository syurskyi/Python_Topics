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

____ ?.?C.. ______ (pyqtProperty, Q_CLASSINFO, QCoreApplication, QObject,
        QUrl)
____ ?.?G.. ______ ?C..
____ ?.QtQml ______ (qmlRegisterType, QQmlComponent, QQmlEngine,
        QQmlListProperty)


QML _ b'''
import People 1.0
import QtQuick 2.0

BirthdayParty {
    host: Boy {
        name: "Bob Jones"
        shoe { size: 12; color: "white"; brand: "Bikey"; price: 90.0 }
    }

    Boy {
        name: "Leo Hodges"
        shoe { size: 10; color: "black"; brand: "Thebok"; price: 59.95 }
    }

    Boy {
        name: "Jack Smith"
        shoe {
            size: 8
            color: "blue"
            brand: "Luma"
            price: 19.95
        }
    }

    Girl {
        name: "Anne Brown"
        shoe.size: 7
        shoe.color: "red"
        shoe.brand: "Job Macobs"
        shoe.price: 699.99
    }
}
'''


c_ ShoeDescription(QObject):
    ___ __init__  parent_None):
        super(ShoeDescription, self).__init__(parent)

        self._size _ 0
        self._color _ ?C..()
        self._brand _ ''
        self._price _ 0.0

    @pyqtProperty(int)
    ___ size(self):
        r_ self._size

    @size.setter
    ___ size  size):
        self._size _ size

    @pyqtProperty(?C..)
    ___ color(self):
        r_ self._color

    @color.setter
    ___ color  color):
        self._color _ color

    @pyqtProperty(str)
    ___ brand(self):
        r_ self._brand

    @brand.setter
    ___ brand  brand):
        self._brand _ brand

    @pyqtProperty(float)
    ___ price(self):
        r_ self._price

    @price.setter
    ___ price  price):
        self._price _ price


c_ Person(QObject):
    ___ __init__  parent_None):
        super(Person, self).__init__(parent)

        self._name _ ''
        self._shoe _ ShoeDescription()

    @pyqtProperty(str)
    ___ name(self):
        r_ self._name

    @name.setter
    ___ name  name):
        self._name _ name

    @pyqtProperty(ShoeDescription)
    ___ shoe(self):
        r_ self._shoe


c_ Boy(Person):
    pass


c_ Girl(Person):
    pass


c_ BirthdayParty(QObject):
    Q_CLASSINFO('DefaultProperty', 'guests')

    ___ __init__  parent_None):
        super(BirthdayParty, self).__init__(parent)

        self._host _ N..
        self._guests _   # list

    @pyqtProperty(Person)
    ___ host(self):
        r_ self._host

    @host.setter
    ___ host  host):
        self._host _ host

    @pyqtProperty(QQmlListProperty)
    ___ guests(self):
        r_ QQmlListProperty(Person, self, self._guests)


app _ QCoreApplication(___.argv)

qmlRegisterType(BirthdayParty, "People", 1, 0, "BirthdayParty")
qmlRegisterType(ShoeDescription)
qmlRegisterType(Person)
qmlRegisterType(Boy, "People", 1, 0, "Boy")
qmlRegisterType(Girl, "People", 1, 0, "Girl")

engine _ QQmlEngine()

component _ QQmlComponent(engine)
component.setData(QML, QUrl())

party _ component.create()

__ party __ no. N.. and party.host __ no. N..:
    print("\"%s\" is having a birthday!" % party.host.name)

    __ isinstance(party.host, Boy):
        print("He is inviting:")
    ____
        print("She is inviting:")

    bestShoe _ N..

    for guest in party.guests:
        print("    \"%s\"" % guest.name)

        __ bestShoe __ N.. or bestShoe.shoe.price < guest.shoe.price:
            bestShoe _ guest

    __ bestShoe __ no. N..:
        print("\"%s\" is wearing the best shoes!" % bestShoe.name)
____
    for e in component.errors
        print("Error:", e.toString());
