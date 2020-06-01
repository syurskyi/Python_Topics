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

____ ?.QtCore ______ QByteArray, QDataStream, QIODevice, QSettings
____ ?.?W.. ______ (?A.., QDialog, QHBoxLayout, QLabel,
        QMessageBox, ?PB.., QVBoxLayout)
____ ?.QtNetwork ______ (QHostAddress, QNetworkConfiguration,
        QNetworkConfigurationManager, QNetworkInterface, QNetworkSession,
        QTcpServer)


class Server(QDialog):
    FORTUNES _ (
        "You've been leading a dog's life. Stay off the furniture.",
        "You've got to think about tomorrow.",
        "You will be surprised by a loud noise.",
        "You will feel hungry again in another hour.",
        "You might have mail.",
        "You cannot kill time without injuring eternity.",
        "Computers are not intelligent. They only think they are.")

    ___ __init__(self, parent_None):
        super(Server, self).__init__(parent)

        self.tcpServer _ None
        self.networkSession _ None

        self.statusLabel _ QLabel()
        quitButton _ ?PB..("Quit")
        quitButton.setAutoDefault(False)

        manager _ QNetworkConfigurationManager()
        if manager.capabilities() & QNetworkConfigurationManager.NetworkSessionRequired:
            settings _ QSettings(QSettings.UserScope, 'QtProject')
            settings.beginGroup('QtNetwork')
            id _ settings.value('DefaultNetworkConfiguration', '')
            settings.endGroup()

            config _ manager.configurationFromIdentifier(id)
            if config.state() & QNetworkConfiguration.Discovered == 0:
                config _ manager.defaultConfiguration()

            self.networkSession _ QNetworkSession(config, self)
            self.networkSession.opened.c..(self.sessionOpened)

            self.statusLabel.sT..("Opening network session.")
            self.networkSession.open()
        else:
            self.sessionOpened()

        quitButton.c__.c..(self.close)
        self.tcpServer.newConnection.c..(self.sendFortune)

        buttonLayout _ QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(quitButton)
        buttonLayout.addStretch(1)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(self.statusLabel)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle("Fortune Server")

    ___ sessionOpened(self):
        if self.networkSession is not None:
            config _ self.networkSession.configuration()

            if config.type() == QNetworkConfiguration.UserChoice:
                id _ self.networkSession.sessionProperty('UserChoiceConfiguration')
            else:
                id _ config.identifier()

            settings _ QSettings(QSettings.UserScope, 'QtProject')
            settings.beginGroup('QtNetwork')
            settings.setValue('DefaultNetworkConfiguration', id)
            settings.endGroup();

        self.tcpServer _ QTcpServer(self)
        if not self.tcpServer.listen
            QMessageBox.critical(self, "Fortune Server",
                    "Unable to start the server: %s." % self.tcpServer.errorString())
            self.close()
            return

        for ipAddress in QNetworkInterface.allAddresses
            if ipAddress !_ QHostAddress.LocalHost and ipAddress.toIPv4Address() !_ 0:
                break
        else:
            ipAddress _ QHostAddress(QHostAddress.LocalHost)

        ipAddress _ ipAddress.toString()

        self.statusLabel.sT..("The server is running on\n\nIP: %s\nport %d\n\n"
                "Run the Fortune Client example now." % (ipAddress, self.tcpServer.serverPort()))

    ___ sendFortune(self):
        fortune _ self.FORTUNES[random.randint(0, len(self.FORTUNES) - 1)]

        block _ QByteArray()
        out _ QDataStream(block, QIODevice.WriteOnly)
        out.setVersion(QDataStream.Qt_4_0)
        out.writeUInt16(0)
        out.writeQString(fortune)
        out.device().seek(0)
        out.writeUInt16(block.size() - 2)

        clientConnection _ self.tcpServer.nextPendingConnection()
        clientConnection.disconnected.c..(clientConnection.deleteLater)

        clientConnection.write(block)
        clientConnection.disconnectFromHost()


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    server _ Server()
    random.seed(None)
    sys.exit(server.exec_())
