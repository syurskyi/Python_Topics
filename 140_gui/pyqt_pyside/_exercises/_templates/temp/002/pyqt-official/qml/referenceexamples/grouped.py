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

____ ?.?C.. ______ (pP.., Q_CLASSINFO,  ?CA.., ?O..,
        ?U..)
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


c_ ShoeDescription(?O..):
    ___  -   parent_None):
        s__(ShoeDescription, self). - (parent)

        _size _ 0
        _color _ ?C..()
        _brand _ ''
        _price _ 0.0

    @pP..(in.)
    ___ size
        r_ _size

    @size.setter
    ___ size  size):
        _size _ size

    @pP..(?C..)
    ___ color
        r_ _color

    @color.setter
    ___ color  color):
        _color _ color

    @pP.. st.
    ___ brand
        r_ _brand

    @brand.setter
    ___ brand  brand):
        _brand _ brand

    @pP..(fl..)
    ___ price
        r_ _price

    @price.setter
    ___ price  price):
        _price _ price


c_ Person(?O..):
    ___  -   parent_None):
        s__(Person, self). - (parent)

        _name _ ''
        _shoe _ ShoeDescription()

    @pP.. st.
    ___ name
        r_ _name

    @name.setter
    ___ name  name):
        _name _ name

    @pP..(ShoeDescription)
    ___ shoe
        r_ _shoe


c_ Boy(Person):
    p..


c_ Girl(Person):
    p..


c_ BirthdayParty(?O..):
    Q_CLASSINFO('DefaultProperty', 'guests')

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
qmlRegisterType(ShoeDescription)
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

    bestShoe _ N..

    ___ guest __ party.guests:
        print("    \"%s\"" % guest.name)

        __ bestShoe __ N.. or bestShoe.shoe.price < guest.shoe.price:
            bestShoe _ guest

    __ bestShoe __ no. N..:
        print("\"%s\" is wearing the best shoes!" % bestShoe.name)
____
    ___ e __ component.errors
        print("Error:", e.toString());
