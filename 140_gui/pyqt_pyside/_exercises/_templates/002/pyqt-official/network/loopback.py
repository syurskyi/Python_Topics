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


____ ?.?C.. ______ QByteArray, __
____ ?.?W.. ______ (?A.., ?D.., ?DBB..., ?L..,
        ?MB.., QProgressBar, ?PB.., ?VBL..)
____ ?.?N.. ______ ?HA.., QTcpServer, QTcpSocket


c_ Dialog(?D..):
    TotalBytes _ 50 * 1024 * 1024
    PayloadSize _ 65536

    ___  -   parent_None):
        s__(Dialog, self). - (parent)

        tcpServer _ QTcpServer()
        tcpClient _ QTcpSocket()
        bytesToWrite _ 0
        bytesWritten _ 0
        bytesReceived _ 0

        clientProgressBar _ QProgressBar()
        clientStatusLabel _ ?L..("Client ready")
        serverProgressBar _ QProgressBar()
        serverStatusLabel _ ?L..("Server ready")

        startButton _ ?PB..("&Start")
        quitButton _ ?PB..("&Quit")

        buttonBox _ ?DBB...()
        buttonBox.addButton(startButton, ?DBB....ActionRole)
        buttonBox.addButton(quitButton, ?DBB....RejectRole)

        startButton.c__.c..(start)
        quitButton.c__.c..(close)
        tcpServer.newConnection.c..(acceptConnection)
        tcpClient.connected.c..(startTransfer)
        tcpClient.bytesWritten.c..(updateClientProgress)
        tcpClient.error.c..(displayError)

        mainLayout _ ?VBL..
        mainLayout.aW..(clientProgressBar)
        mainLayout.aW..(clientStatusLabel)
        mainLayout.aW..(serverProgressBar)
        mainLayout.aW..(serverStatusLabel)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(10)
        mainLayout.aW..(buttonBox)
        sL..(mainLayout)

        sWT..("Loopback")

    ___ start
        startButton.sE.. F..

        ?A...setOverrideCursor(__.WaitCursor)

        bytesWritten _ 0
        bytesReceived _ 0

        w__ no. tcpServer.isListening() and no. tcpServer.l..
            ret _ ?MB...c..  "Loopback",
                    "Unable to start the test: %s." % tcpServer.errorString(),
                    ?MB...Retry | ?MB...Cancel)
            __ ret __ ?MB...Cancel:
                r_

        serverStatusLabel.sT..("Listening")
        clientStatusLabel.sT..("Connecting")

        tcpClient.connectToHost(?HA..(?HA...LocalHost), tcpServer.serverPort())

    ___ acceptConnection
        tcpServerConnection _ tcpServer.nPC..()
        tcpServerConnection.readyRead.c..(updateServerProgress)
        tcpServerConnection.error.c..(displayError)

        serverStatusLabel.sT..("Accepted connection")
        tcpServer.c..

    ___ startTransfer
        bytesToWrite _ Dialog.TotalBytes - tcpClient.w..(QByteArray(Dialog.PayloadSize, '@'))
        clientStatusLabel.sT..("Connected")

    ___ updateServerProgress
        bytesReceived +_ tcpServerConnection.bA..()
        tcpServerConnection.rA..

        serverProgressBar.sM..(Dialog.TotalBytes)
        serverProgressBar.sV..(bytesReceived)
        serverStatusLabel.sT..("Received %dMB" % (bytesReceived / (1024 * 1024)))

        __ bytesReceived __ Dialog.TotalBytes:
            tcpServerConnection.c..
            startButton.sE..( st.
            ?A...restoreOverrideCursor()

    ___ updateClientProgress  numBytes):
        bytesWritten +_ numBytes
        __ bytesToWrite > 0:
            bytesToWrite -_ tcpClient.w..(QByteArray(
                                        min(bytesToWrite, Dialog.PayloadSize), '@'))

        clientProgressBar.sM..(Dialog.TotalBytes)
        clientProgressBar.sV..(bytesWritten)
        clientStatusLabel.sT..("Sent %dMB" % (bytesWritten / (1024 * 1024)))

    ___ displayError  socketError):
        __ socketError __ QTcpSocket.RemoteHostClosedError:
            r_

        ?MB...i..  "Network error",
                "The following error occured: %s." % tcpClient.errorString())

        tcpClient.c..
        tcpServer.c..
        clientProgressBar.reset()
        serverProgressBar.reset()
        clientStatusLabel.sT..("Client ready")
        serverStatusLabel.sT..("Server ready")
        startButton.sE..( st.
        ?A...restoreOverrideCursor()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    dialog _ Dialog()
    dialog.s..
    ___.e..(dialog.e..
