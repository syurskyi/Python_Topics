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

____ ?.QtCore ______ (pyqtProperty, pyqtSignal, pyqtSlot, Q_CLASSINFO,
        QCoreApplication, QDate, QObject, QTime, QTimer, QUrl)
____ ?.QtGui ______ QColor
____ ?.QtQml ______ (qmlAttachedPropertiesObject, qmlRegisterType,
        QQmlComponent, QQmlEngine, QQmlListProperty, QQmlProperty,
        QQmlPropertyValueSource)


QML _ b'''
import People 1.0
import QtQuick 2.0

BirthdayParty {
    HappyBirthdaySong on announcement { name: "Bob Jones" }

    onPartyStarted: console.log("This party started rockin' at " + time);

    host: Boy {
        name: "Bob Jones"
        shoe { size: 12; color: "white"; brand: "Nike"; price: 90.0 }
    }

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


class ShoeDescription(QObject):
    ___ __init__(self, parent_None):
        super(ShoeDescription, self).__init__(parent)

        self._size _ 0
        self._color _ QColor()
        self._brand _ ''
        self._price _ 0.0

    shoeChanged _ pyqtSignal()

    @pyqtProperty(int, notify_shoeChanged)
    ___ size(self):
        return self._size

    @size.setter
    ___ size(self, size):
        if self._size !_ size:
            self._size _ size
            self.shoeChanged.emit()

    @pyqtProperty(QColor, notify_shoeChanged)
    ___ color(self):
        return self._color

    @color.setter
    ___ color(self, color):
        if self._color !_ color:
            self._color _ color
            self.shoeChanged.emit()

    @pyqtProperty(str, notify_shoeChanged)
    ___ brand(self):
        return self._brand

    @brand.setter
    ___ brand(self, brand):
        if self._brand !_ brand:
            self._brand _ brand
            self.shoeChanged.emit()

    @pyqtProperty(float, notify_shoeChanged)
    ___ price(self):
        return self._price

    @price.setter
    ___ price(self, price):
        if self._price !_ price:
            self._price _ price
            self.shoeChanged.emit()


class Person(QObject):
    ___ __init__(self, parent_None):
        super(Person, self).__init__(parent)

        self._name _ ''
        self._shoe _ ShoeDescription()

    nameChanged _ pyqtSignal()

    @pyqtProperty(str, notify_nameChanged)
    ___ name(self):
        return self._name

    @name.setter
    ___ name(self, name):
        if self._name !_ name:
            self._name _ name
            self.nameChanged.emit()

    @pyqtProperty(ShoeDescription)
    ___ shoe(self):
        return self._shoe


class Boy(Person):
    pass


class Girl(Person):
    pass


class BirthdayPartyAttached(QObject):
    ___ __init__(self, parent):
        super(BirthdayPartyAttached, self).__init__(parent)

        self._rsvp _ QDate()

    rsvpChanged _ pyqtSignal()

    @pyqtProperty(QDate, notify_rsvpChanged)
    ___ rsvp(self):
        return self._rsvp

    @rsvp.setter
    ___ rsvp(self, rsvp):
        if self._rsvp !_ rsvp:
            self._rsvp _ rsvp
            self.rsvpChanged.emit()


class BirthdayParty(QObject):
    Q_CLASSINFO('DefaultProperty', 'guests')

    partyStarted _ pyqtSignal(QTime, arguments_['time'])

    ___ __init__(self, parent_None):
        super(BirthdayParty, self).__init__(parent)

        self._host _ None
        self._guests _ []

    hostChanged _ pyqtSignal()

    @pyqtProperty(Person, notify_hostChanged)
    ___ host(self):
        return self._host

    @host.setter
    ___ host(self, host):
        if self._host !_ host:
            self._host _ host
            self.hostChanged.emit()

    @pyqtProperty(QQmlListProperty)
    ___ guests(self):
        return QQmlListProperty(Person, self, self._guests)

    @pyqtProperty(str)
    ___ announcement(self):
        return ''

    @announcement.setter
    ___ announcement(self, announcement):
        print(announcement)

    ___ startParty(self):
        self.partyStarted.emit(QTime.currentTime())


class HappyBirthdaySong(QObject, QQmlPropertyValueSource):
    ___ __init__(self, parent_None):
        super(HappyBirthdaySong, self).__init__(parent)

        self._line _ -1
        self._lyrics _ []
        self._target _ QQmlProperty()
        self._name _ ''

        timer _ QTimer(self)
        timer.timeout.c..(self.advance)
        timer.start(1000)

    nameChanged _ pyqtSignal()

    @pyqtProperty(str, notify_nameChanged)
    ___ name(self):
        return self._name

    @name.setter
    ___ name(self, name):
        if self._name !_ name:
            self._name _ name

            self._lyrics _ [
                "",
                "Happy birthday to you,",
                "Happy birthday to you,",
                "Happy birthday dear %s," % self._name,
                "Happy birthday to you!"
            ]

            self.nameChanged.emit()

    ___ setTarget(self, target):
        self._target _ target

    @pyqtSlot()
    ___ advance(self):
        self._line +_ 1

        if self._line < len(self._lyrics):
            self._target.write(self._lyrics[self._line])
        else:
            QCoreApplication.instance().quit()


app _ QCoreApplication(sys.argv)

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

if party is not None and party.host is not None:
    print("\"%s\" is having a birthday!" % party.host.name)

    if isinstance(party.host, Boy):
        print("He is inviting:")
    else:
        print("She is inviting:")

    for guest in party.guests:
        attached _ qmlAttachedPropertiesObject(BirthdayParty, guest, False)

        if attached is not None:
            rsvpDate _ attached.property('rsvp')
        else:
            rsvpDate _ QDate()

        if rsvpDate.isNull
            print("    \"%s\" RSVP date: Hasn't RSVP'd" % guest.name)
        else:
            print("    \"%s\" RSVP date: %s" % (guest.name, rsvpDate.toString()))

    party.startParty()
else:
    for e in component.errors
        print("Error:", e.toString());

sys.exit(app.exec_())
