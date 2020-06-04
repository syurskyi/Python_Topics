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


____ ?.?C.. ______ (pS.., ?DS.., QMutex, ?ML..,
        ?T.., QWaitCondition)
____ ?.?G.. ______ QIntValidator
____ ?.?W.. ______ (?A.., ?DBB..., QGridLayout,
        ?L.., QLineEdit, ?MB.., ?PB.., ?W..)
____ ?.?N.. ______ (?AS.., ?HA.., QNetworkInterface,
        QTcpSocket)


c_ FortuneThread(?T..):
    newFortune _ pS.. st.

    error _ pS..(in., st.)

    ___  -   parent_None):
        s__(FortuneThread, self). - (parent)

        quit _ F..
        hostName _ ''
        cond _ QWaitCondition()
        mutex _ QMutex()
        port _ 0

    ___ __del__
        mutex.lock()
        quit _ T..
        cond.wakeOne()
        mutex.unlock()
        wait()

    ___ requestNewFortune  hostname, port):
        locker _ ?ML..(mutex)
        hostName _ hostname
        port _ port
        __ no. isRunning
            start()
        ____
            cond.wakeOne()

    ___ run
        mutex.lock()
        serverName _ hostName
        serverPort _ port
        mutex.unlock()

        w__ no. quit:
            Timeout _ 5 * 1000

            socket _ QTcpSocket()
            socket.connectToHost(serverName, serverPort)

            __ no. socket.waitForConnected(Timeout):
                error.e..(socket.error(), socket.errorString())
                r_

            w__ socket.bA..() < 2:
                __ no. socket.waitForReadyRead(Timeout):
                    error.e..(socket.error(), socket.errorString())
                    r_

            instr _ ?DS..(socket)
            instr.setVersion(?DS...Qt_4_0)
            blockSize _ instr.readUInt16()

            w__ socket.bA..() < blockSize:
                __ no. socket.waitForReadyRead(Timeout):
                    error.e..(socket.error(), socket.errorString())
                    r_

            mutex.lock()
            fortune _ instr.rQS..
            newFortune.e..(fortune)

            cond.wait(mutex)
            serverName _ hostName
            serverPort _ port
            mutex.unlock()


c_ BlockingClient(?W..):
    ___  -   parent_None):
        s__(BlockingClient, self). - (parent)

        thread _ FortuneThread()
        currentFortune _ ''

        hostLabel _ ?L..("&Server name:")
        portLabel _ ?L..("S&erver port:")

        ___ ipAddress __ QNetworkInterface.allAddresses
            __ ipAddress !_ ?HA...LocalHost and ipAddress.toIPv4Address() !_ 0:
                break
        ____
            ipAddress _ ?HA..(?HA...LocalHost)

        ipAddress _ ipAddress.tS..

        hostLineEdit _ QLineEdit(ipAddress)
        portLineEdit _ ?LE..
        portLineEdit.sV..(QIntValidator(1, 65535, self))

        hostLabel.setBuddy(hostLineEdit)
        portLabel.setBuddy(portLineEdit)

        statusLabel _ ?L..(
                "This example requires that you run the Fortune Server example as well.")
        statusLabel.setWordWrap( st.

        getFortuneButton _ ?PB..("Get Fortune")
        getFortuneButton.setDefault( st.
        getFortuneButton.sE.. F..

        quitButton _ ?PB..("Quit")

        buttonBox _ ?DBB...()
        buttonBox.addButton(getFortuneButton, ?DBB....ActionRole)
        buttonBox.addButton(quitButton, ?DBB....RejectRole)

        getFortuneButton.c__.c..(requestNewFortune)
        quitButton.c__.c..(close)
        hostLineEdit.tC...c..(enableGetFortuneButton)
        portLineEdit.tC...c..(enableGetFortuneButton)
        thread.newFortune.c..(showFortune)
        thread.error.c..(displayError)

        mainLayout _ QGridLayout()
        mainLayout.aW..(hostLabel, 0, 0)
        mainLayout.aW..(hostLineEdit, 0, 1)
        mainLayout.aW..(portLabel, 1, 0)
        mainLayout.aW..(portLineEdit, 1, 1)
        mainLayout.aW..(statusLabel, 2, 0, 1, 2)
        mainLayout.aW..(buttonBox, 3, 0, 1, 2)
        sL..(mainLayout)

        sWT..("Blocking Fortune Client")
        portLineEdit.setFocus()

    ___ requestNewFortune
        getFortuneButton.sE.. F..
        thread.requestNewFortune(hostLineEdit.t__(),
                in.(portLineEdit.t__()))

    ___ showFortune  nextFortune):
        __ nextFortune __ currentFortune:
            requestNewFortune()
            r_

        currentFortune _ nextFortune
        statusLabel.sT..(currentFortune)
        getFortuneButton.sE..( st.

    ___ displayError  socketError, message):
        __ socketError __ ?AS...HostNotFoundError:
            ?MB...i..  "Blocking Fortune Client",
                    "The host was not found. Please check the host and port "
                    "settings.")
        ____ socketError __ ?AS...ConnectionRefusedError:
            ?MB...i..  "Blocking Fortune Client",
                    "The connection was refused by the peer. Make sure the "
                    "fortune server is running, and check that the host name "
                    "and port settings are correct.")
        ____
            ?MB...i..  "Blocking Fortune Client",
                    "The following error occurred: %s." % message)

        getFortuneButton.sE..( st.

    ___ enableGetFortuneButton
        getFortuneButton.sE..(hostLineEdit.t__() !_ '' and
                portLineEdit.t__() !_ '')


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    client _ BlockingClient()
    client.s..
    ___.e.. ?.e..
