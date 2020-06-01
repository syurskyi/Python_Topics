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

____ ?.?C.. ______ (pyqtProperty, pyqtSignal, pyqtSlot, Q_CLASSINFO,
        QCoreApplication, QDate, QObject, QTime, QTimer, QUrl)
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


c_ ShoeDescription(QObject):
    ___ __init__  parent_None):
        super(ShoeDescription, self).__init__(parent)

        self._size _ 0
        self._color _ ?C..()
        self._brand _ ''
        self._price _ 0.0

    shoeChanged _ pyqtSignal()

    @pyqtProperty(int, notify_shoeChanged)
    ___ size(self):
        r_ self._size

    @size.setter
    ___ size  size):
        __ self._size !_ size:
            self._size _ size
            self.shoeChanged.emit()

    @pyqtProperty(?C.., notify_shoeChanged)
    ___ color(self):
        r_ self._color

    @color.setter
    ___ color  color):
        __ self._color !_ color:
            self._color _ color
            self.shoeChanged.emit()

    @pyqtProperty(str, notify_shoeChanged)
    ___ brand(self):
        r_ self._brand

    @brand.setter
    ___ brand  brand):
        __ self._brand !_ brand:
            self._brand _ brand
            self.shoeChanged.emit()

    @pyqtProperty(float, notify_shoeChanged)
    ___ price(self):
        r_ self._price

    @price.setter
    ___ price  price):
        __ self._price !_ price:
            self._price _ price
            self.shoeChanged.emit()


c_ Person(QObject):
    ___ __init__  parent_None):
        super(Person, self).__init__(parent)

        self._name _ ''
        self._shoe _ ShoeDescription()

    nameChanged _ pyqtSignal()

    @pyqtProperty(str, notify_nameChanged)
    ___ name(self):
        r_ self._name

    @name.setter
    ___ name  name):
        __ self._name !_ name:
            self._name _ name
            self.nameChanged.emit()

    @pyqtProperty(ShoeDescription)
    ___ shoe(self):
        r_ self._shoe


c_ Boy(Person):
    pass


c_ Girl(Person):
    pass


c_ BirthdayPartyAttached(QObject):
    ___ __init__  parent):
        super(BirthdayPartyAttached, self).__init__(parent)

        self._rsvp _ QDate()

    rsvpChanged _ pyqtSignal()

    @pyqtProperty(QDate, notify_rsvpChanged)
    ___ rsvp(self):
        r_ self._rsvp

    @rsvp.setter
    ___ rsvp  rsvp):
        __ self._rsvp !_ rsvp:
            self._rsvp _ rsvp
            self.rsvpChanged.emit()


c_ BirthdayParty(QObject):
    Q_CLASSINFO('DefaultProperty', 'guests')

    partyStarted _ pyqtSignal(QTime, arguments_['time'])

    ___ __init__  parent_None):
        super(BirthdayParty, self).__init__(parent)

        self._host _ N..
        self._guests _   # list

    hostChanged _ pyqtSignal()

    @pyqtProperty(Person, notify_hostChanged)
    ___ host(self):
        r_ self._host

    @host.setter
    ___ host  host):
        __ self._host !_ host:
            self._host _ host
            self.hostChanged.emit()

    @pyqtProperty(QQmlListProperty)
    ___ guests(self):
        r_ QQmlListProperty(Person, self, self._guests)

    @pyqtProperty(str)
    ___ announcement(self):
        r_ ''

    @announcement.setter
    ___ announcement  announcement):
        print(announcement)

    ___ startParty(self):
        self.partyStarted.emit(QTime.currentTime())


c_ HappyBirthdaySong(QObject, QQmlPropertyValueSource):
    ___ __init__  parent_None):
        super(HappyBirthdaySong, self).__init__(parent)

        self._line _ -1
        self._lyrics _   # list
        self._target _ QQmlProperty()
        self._name _ ''

        timer _ QTimer(self)
        timer.timeout.c..(self.advance)
        timer.start(1000)

    nameChanged _ pyqtSignal()

    @pyqtProperty(str, notify_nameChanged)
    ___ name(self):
        r_ self._name

    @name.setter
    ___ name  name):
        __ self._name !_ name:
            self._name _ name

            self._lyrics _ [
                "",
                "Happy birthday to you,",
                "Happy birthday to you,",
                "Happy birthday dear %s," % self._name,
                "Happy birthday to you!"
            ]

            self.nameChanged.emit()

    ___ setTarget  target):
        self._target _ target

    @pyqtSlot()
    ___ advance(self):
        self._line +_ 1

        __ self._line < le.(self._lyrics):
            self._target.w..(self._lyrics[self._line])
        ____
            QCoreApplication.instance().quit()


app _ QCoreApplication(___.argv)

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
component.setData(QML, QUrl())

party _ component.create()

__ party __ no. N.. and party.host __ no. N..:
    print("\"%s\" is having a birthday!" % party.host.name)

    __ isinstance(party.host, Boy):
        print("He is inviting:")
    ____
        print("She is inviting:")

    for guest in party.guests:
        attached _ qmlAttachedPropertiesObject(BirthdayParty, guest, False)

        __ attached __ no. N..:
            rsvpDate _ attached.property('rsvp')
        ____
            rsvpDate _ QDate()

        __ rsvpDate.isNull
            print("    \"%s\" RSVP date: Hasn't RSVP'd" % guest.name)
        ____
            print("    \"%s\" RSVP date: %s" % (guest.name, rsvpDate.toString()))

    party.startParty()
____
    for e in component.errors
        print("Error:", e.toString());

___.exit(app.exec_())
