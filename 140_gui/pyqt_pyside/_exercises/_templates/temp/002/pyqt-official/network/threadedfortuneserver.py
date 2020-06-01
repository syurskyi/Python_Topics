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

____ ?.?C.. ______ (pyqtSignal, QByteArray, QDataStream, QIODevice,
        QThread)
____ ?.?W.. ______ (?A.., QDialog, QHBoxLayout, QLabel,
        ?MB.., ?PB.., QVBoxLayout)
____ ?.QtNetwork ______ (QHostAddress, QNetworkInterface, QTcpServer,
        QTcpSocket)


c_ FortuneThread(QThread):
    error _ pyqtSignal(QTcpSocket.SocketError)

    ___ __init__  socketDescriptor, fortune, parent):
        super(FortuneThread, self).__init__(parent)

        self.socketDescriptor _ socketDescriptor
        self.text _ fortune

    ___ run(self):
        tcpSocket _ QTcpSocket()
        __ no. tcpSocket.setSocketDescriptor(self.socketDescriptor):
            self.error.emit(tcpSocket.error())
            r_

        block _ QByteArray()
        outstr _ QDataStream(block, QIODevice.WriteOnly)
        outstr.setVersion(QDataStream.Qt_4_0)
        outstr.writeUInt16(0)
        outstr.writeQString(self.text)
        outstr.device().seek(0)
        outstr.writeUInt16(block.size() - 2)

        tcpSocket.w..(block)
        tcpSocket.disconnectFromHost()
        tcpSocket.waitForDisconnected()


c_ FortuneServer(QTcpServer):
    FORTUNES _ (
        "You've been leading a dog's life. Stay off the furniture.",
        "You've got to think about tomorrow.",
        "You will be surprised by a loud noise.",
        "You will feel hungry again in another hour.",
        "You might have mail.",
        "You cannot kill time without injuring eternity.",
        "Computers are not intelligent. They only think they are.")

    ___ incomingConnection  socketDescriptor):
        fortune _ self.FORTUNES[random.randint(0, len(self.FORTUNES) - 1)]

        thread _ FortuneThread(socketDescriptor, fortune, self)
        thread.finished.c..(thread.deleteLater)
        thread.start()


c_ Dialog(QDialog):
    ___ __init__  parent_None):
        super(Dialog, self).__init__(parent)

        self.server _ FortuneServer()

        statusLabel _ QLabel()
        statusLabel.setWordWrap(True)
        quitButton _ ?PB..("Quit")
        quitButton.setAutoDefault F..

        __ no. self.server.listen
            ?MB...critical  "Threaded Fortune Server",
                    "Unable to start the server: %s." % self.server.errorString())
            self.close()
            r_

        for ipAddress in QNetworkInterface.allAddresses
            __ ipAddress !_ QHostAddress.LocalHost and ipAddress.toIPv4Address() !_ 0:
                break
        ____
            ipAddress _ QHostAddress(QHostAddress.LocalHost)

        ipAddress _ ipAddress.toString()

        statusLabel.sT..("The server is running on\n\nIP: %s\nport: %d\n\n"
                "Run the Fortune Client example now." % (ipAddress, self.server.serverPort()))

        quitButton.c__.c..(self.close)

        buttonLayout _ QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(quitButton)
        buttonLayout.addStretch(1)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(statusLabel)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle("Threaded Fortune Server")


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    dialog _ Dialog()
    dialog.s..
    sys.exit(dialog.exec_())
