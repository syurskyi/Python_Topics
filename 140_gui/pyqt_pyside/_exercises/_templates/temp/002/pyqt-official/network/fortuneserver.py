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


______ random

____ ?.?C.. ______ QByteArray, QDataStream, QIODevice, QSettings
____ ?.?W.. ______ (?A.., QDialog, QHBoxLayout, QLabel,
        ?MB.., ?PB.., QVBoxLayout)
____ ?.QtNetwork ______ (QHostAddress, QNetworkConfiguration,
        QNetworkConfigurationManager, QNetworkInterface, QNetworkSession,
        QTcpServer)


c_ Server(QDialog):
    FORTUNES _ (
        "You've been leading a dog's life. Stay off the furniture.",
        "You've got to think about tomorrow.",
        "You will be surprised by a loud noise.",
        "You will feel hungry again in another hour.",
        "You might have mail.",
        "You cannot kill time without injuring eternity.",
        "Computers are not intelligent. They only think they are.")

    ___  -   parent_None):
        super(Server, self). - (parent)

        tcpServer _ N..
        networkSession _ N..

        statusLabel _ QLabel()
        quitButton _ ?PB..("Quit")
        quitButton.setAutoDefault F..

        manager _ QNetworkConfigurationManager()
        __ manager.capabilities() & QNetworkConfigurationManager.NetworkSessionRequired:
            settings _ QSettings(QSettings.UserScope, 'QtProject')
            settings.beginGroup('QtNetwork')
            id _ settings.value('DefaultNetworkConfiguration', '')
            settings.endGroup()

            config _ manager.configurationFromIdentifier(id)
            __ config.state() & QNetworkConfiguration.Discovered == 0:
                config _ manager.defaultConfiguration()

            networkSession _ QNetworkSession(config, self)
            networkSession.opened.c..(sessionOpened)

            statusLabel.sT..("Opening network session.")
            networkSession.o..()
        ____
            sessionOpened()

        quitButton.c__.c..(close)
        tcpServer.newConnection.c..(sendFortune)

        buttonLayout _ QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.aW..(quitButton)
        buttonLayout.addStretch(1)

        mainLayout _ ?VBL..
        mainLayout.aW..(statusLabel)
        mainLayout.aL..(buttonLayout)
        sL..(mainLayout)

        setWindowTitle("Fortune Server")

    ___ sessionOpened
        __ networkSession __ no. N..:
            config _ networkSession.configuration()

            __ config.type() == QNetworkConfiguration.UserChoice:
                id _ networkSession.sessionProperty('UserChoiceConfiguration')
            ____
                id _ config.identifier()

            settings _ QSettings(QSettings.UserScope, 'QtProject')
            settings.beginGroup('QtNetwork')
            settings.setValue('DefaultNetworkConfiguration', id)
            settings.endGroup();

        tcpServer _ QTcpServer
        __ no. tcpServer.listen
            ?MB...critical  "Fortune Server",
                    "Unable to start the server: %s." % tcpServer.errorString())
            close()
            r_

        ___ ipAddress __ QNetworkInterface.allAddresses
            __ ipAddress !_ QHostAddress.LocalHost and ipAddress.toIPv4Address() !_ 0:
                break
        ____
            ipAddress _ QHostAddress(QHostAddress.LocalHost)

        ipAddress _ ipAddress.toString()

        statusLabel.sT..("The server is running on\n\nIP: %s\nport %d\n\n"
                "Run the Fortune Client example now." % (ipAddress, tcpServer.serverPort()))

    ___ sendFortune
        fortune _ FORTUNES[random.randint(0, le.(FORTUNES) - 1)]

        block _ QByteArray()
        out _ QDataStream(block, QIODevice.WriteOnly)
        out.setVersion(QDataStream.Qt_4_0)
        out.writeUInt16(0)
        out.writeQString(fortune)
        out.device().seek(0)
        out.writeUInt16(block.size() - 2)

        clientConnection _ tcpServer.nextPendingConnection()
        clientConnection.disconnected.c..(clientConnection.deleteLater)

        clientConnection.w..(block)
        clientConnection.disconnectFromHost()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    server _ Server()
    random.seed(N..)
    ___.exit(server.exec_())
