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

____ ?.?C.. ______ (pP.., pS.., pyqtSlot, Q_CLASSINFO,
         ?CA.., ?D.., ?O.., ?T.., ?T.., ?U..)
____ ?.?G.. ______ ?C..
____ ?.QtQml ______ (qmlAttachedPropertiesObject, qmlRegisterType,
        QQmlComponent, QQmlEngine, QQmlListProperty, QQmlProperty,
        QQmlPropertyValueSource)


QML _ b'''
import People 1.0
import QtQuick 2.0

BirthdayParty {
    id: theParty

    HappyBirthdaySong on announcement { name: theParty.host.name }

    host: Boy {
        name: "Bob Jones"
        shoe { size: 12; color: "white"; brand: "Nike"; price: 90.0 }
    }

    onPartyStarted: console.log("This party started rockin' at " + time);

    Boy {
        name: "Leo Hodges"
        BirthdayParty.rsvp: "2009-07-06"
        shoe { size: 10; color: "black"; brand: "Reebok"; price: 59.95 }
    }

    Boy {
        name: "Jack Smith"
        shoe { size: 8; color: "blue"; brand: "Puma"; price: 19.95 }
    }

    Girl {
        name: "Anne Brown"
        BirthdayParty.rsvp: "2009-07-01"
        shoe.size: 7
        shoe.color: "red"
        shoe.brand: "Marc Jacobs"
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

    shoeChanged _ pS..()

    @pP..(in., notify_shoeChanged)
    ___ size
        r_ _size

    @size.setter
    ___ size  size):
        __ _size !_ size:
            _size _ size
            shoeChanged.e..()

    @pP..(?C.., notify_shoeChanged)
    ___ color
        r_ _color

    @color.setter
    ___ color  color):
        __ _color !_ color:
            _color _ color
            shoeChanged.e..()

    @pP..(st., notify_shoeChanged)
    ___ brand
        r_ _brand

    @brand.setter
    ___ brand  brand):
        __ _brand !_ brand:
            _brand _ brand
            shoeChanged.e..()

    @pP..(fl.., notify_shoeChanged)
    ___ price
        r_ _price

    @price.setter
    ___ price  price):
        __ _price !_ price:
            _price _ price
            shoeChanged.e..()


c_ Person(?O..):
    ___  -   parent_None):
        s__(Person, self). - (parent)

        _name _ ''
        _shoe _ ShoeDescription()

    nameChanged _ pS..()

    @pP..(st., notify_nameChanged)
    ___ name
        r_ _name

    @name.setter
    ___ name  name):
        __ _name !_ name:
            _name _ name
            nameChanged.e..()

    @pP..(ShoeDescription)
    ___ shoe
        r_ _shoe


c_ Boy(Person):
    p..


c_ Girl(Person):
    p..


c_ BirthdayPartyAttached(?O..):
    ___  -   parent):
        s__(BirthdayPartyAttached, self). - (parent)

        _rsvp _ ?D..()

    rsvpChanged _ pS..()

    @pP..(?D.., notify_rsvpChanged)
    ___ rsvp
        r_ _rsvp

    @rsvp.setter
    ___ rsvp  rsvp):
        __ _rsvp !_ rsvp:
            _rsvp _ rsvp
            rsvpChanged.e..()


c_ BirthdayParty(?O..):
    Q_CLASSINFO('DefaultProperty', 'guests')

    partyStarted _ pS..(?T.., arguments_['time'])

    ___  -   parent_None):
        s__(BirthdayParty, self). - (parent)

        _host _ N..
        _guests _   # list

    hostChanged _ pS..()

    @pP..(Person, notify_hostChanged)
    ___ host
        r_ _host

    @host.setter
    ___ host  host):
        __ _host !_ host:
            _host _ host
            hostChanged.e..()

    @pP..(QQmlListProperty)
    ___ guests
        r_ QQmlListProperty(Person, self, _guests)

    @pP.. st.
    ___ announcement
        r_ ''

    @announcement.setter
    ___ announcement  announcement):
        print(announcement)

    ___ startParty
        partyStarted.e..(?T...currentTime())


c_ HappyBirthdaySong(?O.., QQmlPropertyValueSource):
    ___  -   parent_None):
        s__(HappyBirthdaySong, self). - (parent)

        _line _ -1
        _lyrics _   # list
        _target _ QQmlProperty()
        _name _ ''

        timer _ ?T..
        timer.timeout.c..(advance)
        timer.start(1000)

    nameChanged _ pS..()

    @pP..(st., notify_nameChanged)
    ___ name
        r_ _name

    @name.setter
    ___ name  name):
        __ _name !_ name:
            _name _ name

            _lyrics _ [
                "",
                "Happy birthday to you,",
                "Happy birthday to you,",
                "Happy birthday dear %s," % _name,
                "Happy birthday to you!"
            ]

            nameChanged.e..()

    ___ setTarget  target):
        _target _ target

    @pyqtSlot()
    ___ advance
        _line +_ 1

        __ _line < le.(_lyrics):
            _target.w..(_lyrics[_line])
        ____
             ?CA...i.. .quit()


app _  ?CA..(___.a..

qmlRegisterType(BirthdayPartyAttached)
qmlRegisterType(BirthdayParty, "People", 1, 0, "BirthdayParty",
        attachedProperties_BirthdayPartyAttached)
qmlRegisterType(HappyBirthdaySong, "People", 1, 0, "HappyBirthdaySong")
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

    ___ guest __ party.guests:
        attached _ qmlAttachedPropertiesObject(BirthdayParty, guest, F..)

        __ attached __ no. N..:
            rsvpDate _ attached.property('rsvp')
        ____
            rsvpDate _ ?D..()

        __ rsvpDate.isNull
            print("    \"%s\" RSVP date: Hasn't RSVP'd" % guest.name)
        ____
            print("    \"%s\" RSVP date: %s" % (guest.name, rsvpDate.toString()))

    party.startParty()
____
    ___ e __ component.errors
        print("Error:", e.toString());

___.e.. ?.e..
