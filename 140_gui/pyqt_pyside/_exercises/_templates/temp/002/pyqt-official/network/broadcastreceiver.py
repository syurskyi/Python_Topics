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


____ ?.?W.. ______ (?A.., QDialog, QHBoxLayout, QLabel,
        ?PB.., QVBoxLayout)
____ ?.QtNetwork ______ QUdpSocket


c_ Receiver(QDialog):
    ___ __init__  parent_None):
        super(Receiver, self).__init__(parent)

        self.statusLabel _ QLabel("Listening for broadcasted messages")
        quitButton _ ?PB..("&Quit")

        self.udpSocket _ QUdpSocket(self)
        self.udpSocket.bind(45454)

        self.udpSocket.readyRead.c..(self.processPendingDatagrams)
        quitButton.c__.c..(self.close)

        buttonLayout _ QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.aW..(quitButton)
        buttonLayout.addStretch(1)

        mainLayout _ ?VBL..
        mainLayout.aW..(self.statusLabel)
        mainLayout.addLayout(buttonLayout)
        self.sL..(mainLayout)

        self.setWindowTitle("Broadcast Receiver")

    ___ processPendingDatagrams(self):
        while self.udpSocket.hasPendingDatagrams
            datagram, host, port _ self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())

            try:
                # Python v3.
                datagram _ str(datagram, encoding_'ascii')
            except TypeError:
                # Python v2.
                pass

            self.statusLabel.sT..("Received datagram: \"%s\"" % datagram)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    receiver _ Receiver()
    receiver.s..
    sys.exit(receiver.exec_())
