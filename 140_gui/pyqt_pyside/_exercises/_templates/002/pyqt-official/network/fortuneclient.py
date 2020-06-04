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


____ ?.?C.. ______ ?DS.., QSettings, ?T..
____ ?.?G.. ______ QIntValidator
____ ?.?W.. ______ (?A.., ?CB, ?D..,
        ?DBB..., QGridLayout, ?L.., QLineEdit, ?MB..,
        ?PB..)
____ ?.?N.. ______ (?AS.., QHostInfo, QNetworkConfiguration,
        QNetworkConfigurationManager, QNetworkInterface, QNetworkSession,
        QTcpSocket)


c_ Client(?D..):
    ___  -   parent_None):
        s__(Client, self). - (parent)

        networkSession _ N..
        blockSize _ 0
        currentFortune _ ''

        hostLabel _ ?L..("&Server name:")
        portLabel _ ?L..("S&erver port:")

        hostCombo _ ?CB()
        hostCombo.sE..( st.

        name _ QHostInfo.localHostName()
        __ name !_ '':
            hostCombo.aI..(name)

            domain _ QHostInfo.localDomainName()
            __ domain !_ '':
                hostCombo.aI..(name + '.' + domain)

        __ name !_ 'localhost':
            hostCombo.aI..('localhost')

        ipAddressesList _ QNetworkInterface.allAddresses()

        ___ ipAddress __ ipAddressesList:
            __ no. ipAddress.isLoopback
                hostCombo.aI..(ipAddress.toString())

        ___ ipAddress __ ipAddressesList:
            __ ipAddress.isLoopback
                hostCombo.aI..(ipAddress.toString())

        portLineEdit _ ?LE..
        portLineEdit.sV..(QIntValidator(1, 65535, self))

        hostLabel.setBuddy(hostCombo)
        portLabel.setBuddy(portLineEdit)

        statusLabel _ ?L..("This examples requires that you run "
                "the Fortune Server example as well.")

        getFortuneButton _ ?PB..("Get Fortune")
        getFortuneButton.setDefault( st.
        getFortuneButton.sE.. F..

        quitButton _ ?PB..("Quit")

        buttonBox _ ?DBB...()
        buttonBox.addButton(getFortuneButton, ?DBB....ActionRole)
        buttonBox.addButton(quitButton, ?DBB....RejectRole)

        tcpSocket _ QTcpSocket

        hostCombo.editTextChanged.c..(enableGetFortuneButton)
        portLineEdit.tC...c..(enableGetFortuneButton)
        getFortuneButton.c__.c..(requestNewFortune)
        quitButton.c__.c..(close)
        tcpSocket.readyRead.c..(readFortune)
        tcpSocket.error.c..(displayError)

        mainLayout _ QGridLayout()
        mainLayout.aW..(hostLabel, 0, 0)
        mainLayout.aW..(hostCombo, 0, 1)
        mainLayout.aW..(portLabel, 1, 0)
        mainLayout.aW..(portLineEdit, 1, 1)
        mainLayout.aW..(statusLabel, 2, 0, 1, 2)
        mainLayout.aW..(buttonBox, 3, 0, 1, 2)
        sL..(mainLayout)

        sWT..("Fortune Client")
        portLineEdit.setFocus()

        manager _ QNetworkConfigurationManager()
        __ manager.capabilities() & QNetworkConfigurationManager.NetworkSessionRequired:
            settings _ QSettings(QSettings.UserScope, 'QtProject')
            settings.beginGroup('QtNetwork')
            id _ settings.value('DefaultNetworkConfiguration')
            settings.endGroup()

            c.. _ manager.configurationFromIdentifier(id)
            __ c...s.. & QNetworkConfiguration.Discovered __ 0:
                c.. _ manager.defaultConfiguration()

            networkSession _ QNetworkSession(c.., self)
            networkSession.opened.c..(sessionOpened)

            getFortuneButton.sE.. F..
            statusLabel.sT..("Opening network session.")
            networkSession.o..()

    ___ requestNewFortune
        getFortuneButton.sE.. F..
        blockSize _ 0
        tcpSocket.abort()
        tcpSocket.connectToHost(hostCombo.currentText(),
                in.(portLineEdit.t__()))

    ___ readFortune
        instr _ ?DS..(tcpSocket)
        instr.setVersion(?DS...Qt_4_0)

        __ blockSize __ 0:
            __ tcpSocket.bA..() < 2:
                r_

            blockSize _ instr.readUInt16()

        __ tcpSocket.bA..() < blockSize:
            r_

        nextFortune _ instr.rQS..
        __ nextFortune __ currentFortune:
            ?T...sS..(0, requestNewFortune)
            r_

        currentFortune _ nextFortune
        statusLabel.sT..(currentFortune)
        getFortuneButton.sE..( st.

    ___ displayError  socketError):
        __ socketError __ ?AS...RemoteHostClosedError:
            p..
        ____ socketError __ ?AS...HostNotFoundError:
            ?MB...i..  "Fortune Client",
                    "The host was not found. Please check the host name and "
                    "port settings.")
        ____ socketError __ ?AS...ConnectionRefusedError:
            ?MB...i..  "Fortune Client",
                    "The connection was refused by the peer. Make sure the "
                    "fortune server is running, and check that the host name "
                    "and port settings are correct.")
        ____
            ?MB...i..  "Fortune Client",
                    "The following error occurred: %s." % tcpSocket.errorString())

        getFortuneButton.sE..( st.

    ___ enableGetFortuneButton
        getFortuneButton.sE..(
                (networkSession __ N.. or networkSession.isOpen())
                and hostCombo.currentText() !_ ''
                and portLineEdit.t__() !_ '')

    ___ sessionOpened
        c.. _ networkSession.configuration()

        __ c...type() __ QNetworkConfiguration.UserChoice:
            id _ networkSession.sessionProperty('UserChoiceConfiguration')
        ____
            id _ c...identifier()

        settings _ QSettings(QSettings.UserScope, 'QtProject')
        settings.beginGroup('QtNetwork')
        settings.sV..('DefaultNetworkConfiguration', id)
        settings.endGroup()

        statusLabel.sT..("This examples requires that you run the "
                            "Fortune Server example as well.")

        enableGetFortuneButton()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    client _ Client()
    client.s..
    ___.e..(client.e..
