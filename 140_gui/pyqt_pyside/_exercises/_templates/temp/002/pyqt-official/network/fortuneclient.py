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


____ ?.?C.. ______ QDataStream, QSettings, QTimer
____ ?.?G.. ______ QIntValidator
____ ?.?W.. ______ (?A.., QComboBox, QDialog,
        QDialogButtonBox, QGridLayout, QLabel, QLineEdit, ?MB..,
        ?PB..)
____ ?.QtNetwork ______ (QAbstractSocket, QHostInfo, QNetworkConfiguration,
        QNetworkConfigurationManager, QNetworkInterface, QNetworkSession,
        QTcpSocket)


c_ Client(QDialog):
    ___ __init__  parent_None):
        super(Client, self).__init__(parent)

        self.networkSession _ N..
        self.blockSize _ 0
        self.currentFortune _ ''

        hostLabel _ QLabel("&Server name:")
        portLabel _ QLabel("S&erver port:")

        self.hostCombo _ QComboBox()
        self.hostCombo.setEditable(True)

        name _ QHostInfo.localHostName()
        __ name !_ '':
            self.hostCombo.addItem(name)

            domain _ QHostInfo.localDomainName()
            __ domain !_ '':
                self.hostCombo.addItem(name + '.' + domain)

        __ name !_ 'localhost':
            self.hostCombo.addItem('localhost')

        ipAddressesList _ QNetworkInterface.allAddresses()

        for ipAddress in ipAddressesList:
            __ no. ipAddress.isLoopback
                self.hostCombo.addItem(ipAddress.toString())

        for ipAddress in ipAddressesList:
            __ ipAddress.isLoopback
                self.hostCombo.addItem(ipAddress.toString())

        self.portLineEdit _ QLineEdit()
        self.portLineEdit.setValidator(QIntValidator(1, 65535, self))

        hostLabel.setBuddy(self.hostCombo)
        portLabel.setBuddy(self.portLineEdit)

        self.statusLabel _ QLabel("This examples requires that you run "
                "the Fortune Server example as well.")

        self.getFortuneButton _ ?PB..("Get Fortune")
        self.getFortuneButton.setDefault(True)
        self.getFortuneButton.setEnabled F..

        quitButton _ ?PB..("Quit")

        buttonBox _ QDialogButtonBox()
        buttonBox.addButton(self.getFortuneButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QDialogButtonBox.RejectRole)

        self.tcpSocket _ QTcpSocket(self)

        self.hostCombo.editTextChanged.c..(self.enableGetFortuneButton)
        self.portLineEdit.textChanged.c..(self.enableGetFortuneButton)
        self.getFortuneButton.c__.c..(self.requestNewFortune)
        quitButton.c__.c..(self.close)
        self.tcpSocket.readyRead.c..(self.readFortune)
        self.tcpSocket.error.c..(self.displayError)

        mainLayout _ QGridLayout()
        mainLayout.addWidget(hostLabel, 0, 0)
        mainLayout.addWidget(self.hostCombo, 0, 1)
        mainLayout.addWidget(portLabel, 1, 0)
        mainLayout.addWidget(self.portLineEdit, 1, 1)
        mainLayout.addWidget(self.statusLabel, 2, 0, 1, 2)
        mainLayout.addWidget(buttonBox, 3, 0, 1, 2)
        self.setLayout(mainLayout)

        self.setWindowTitle("Fortune Client")
        self.portLineEdit.setFocus()

        manager _ QNetworkConfigurationManager()
        __ manager.capabilities() & QNetworkConfigurationManager.NetworkSessionRequired:
            settings _ QSettings(QSettings.UserScope, 'QtProject')
            settings.beginGroup('QtNetwork')
            id _ settings.value('DefaultNetworkConfiguration')
            settings.endGroup()

            config _ manager.configurationFromIdentifier(id)
            __ config.state() & QNetworkConfiguration.Discovered == 0:
                config _ manager.defaultConfiguration()

            self.networkSession _ QNetworkSession(config, self)
            self.networkSession.opened.c..(self.sessionOpened)

            self.getFortuneButton.setEnabled F..
            self.statusLabel.sT..("Opening network session.")
            self.networkSession.o..()

    ___ requestNewFortune(self):
        self.getFortuneButton.setEnabled F..
        self.blockSize _ 0
        self.tcpSocket.abort()
        self.tcpSocket.connectToHost(self.hostCombo.currentText(),
                int(self.portLineEdit.text()))

    ___ readFortune(self):
        instr _ QDataStream(self.tcpSocket)
        instr.setVersion(QDataStream.Qt_4_0)

        __ self.blockSize == 0:
            __ self.tcpSocket.bytesAvailable() < 2:
                r_

            self.blockSize _ instr.readUInt16()

        __ self.tcpSocket.bytesAvailable() < self.blockSize:
            r_

        nextFortune _ instr.readQString()
        __ nextFortune == self.currentFortune:
            QTimer.singleShot(0, self.requestNewFortune)
            r_

        self.currentFortune _ nextFortune
        self.statusLabel.sT..(self.currentFortune)
        self.getFortuneButton.setEnabled(True)

    ___ displayError  socketError):
        __ socketError == QAbstractSocket.RemoteHostClosedError:
            pass
        ____ socketError == QAbstractSocket.HostNotFoundError:
            ?MB...information  "Fortune Client",
                    "The host was not found. Please check the host name and "
                    "port settings.")
        ____ socketError == QAbstractSocket.ConnectionRefusedError:
            ?MB...information  "Fortune Client",
                    "The connection was refused by the peer. Make sure the "
                    "fortune server is running, and check that the host name "
                    "and port settings are correct.")
        ____
            ?MB...information  "Fortune Client",
                    "The following error occurred: %s." % self.tcpSocket.errorString())

        self.getFortuneButton.setEnabled(True)

    ___ enableGetFortuneButton(self):
        self.getFortuneButton.setEnabled(
                (self.networkSession __ N.. or self.networkSession.isOpen())
                and self.hostCombo.currentText() !_ ''
                and self.portLineEdit.text() !_ '')

    ___ sessionOpened(self):
        config _ self.networkSession.configuration()

        __ config.type() == QNetworkConfiguration.UserChoice:
            id _ self.networkSession.sessionProperty('UserChoiceConfiguration')
        ____
            id _ config.identifier()

        settings _ QSettings(QSettings.UserScope, 'QtProject')
        settings.beginGroup('QtNetwork')
        settings.setValue('DefaultNetworkConfiguration', id)
        settings.endGroup()

        self.statusLabel.sT..("This examples requires that you run the "
                            "Fortune Server example as well.")

        self.enableGetFortuneButton()


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    client _ Client()
    client.s..
    sys.exit(client.exec_())
