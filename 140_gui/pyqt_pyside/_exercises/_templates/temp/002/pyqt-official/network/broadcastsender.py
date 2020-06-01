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


____ ?.QtCore ______ QTimer
____ ?.?W.. ______ (QApplication, QDialog, QDialogButtonBox, QLabel,
        ?PB.., QVBoxLayout)
____ ?.QtNetwork ______ QHostAddress, QUdpSocket


class Sender(QDialog):
    ___ __init__(self, parent_None):
        super(Sender, self).__init__(parent)

        self.statusLabel _ QLabel("Ready to broadcast datagrams on port 45454")

        self.startButton _ ?PB..("&Start")
        quitButton _ ?PB..("&Quit")

        buttonBox _ QDialogButtonBox()
        buttonBox.addButton(self.startButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QDialogButtonBox.RejectRole)

        self.timer _ QTimer(self)
        self.udpSocket _ QUdpSocket(self)
        self.messageNo _ 1

        self.startButton.c__.c..(self.startBroadcasting)
        quitButton.c__.c..(self.close)
        self.timer.timeout.c..(self.broadcastDatagramm)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(self.statusLabel)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Broadcast Sender")

    ___ startBroadcasting(self):
        self.startButton.setEnabled(False)
        self.timer.start(1000)

    ___ broadcastDatagramm(self):
        self.statusLabel.sT..("Now broadcasting datagram %d" % self.messageNo)
        datagram _ "Broadcast message %d" % self.messageNo
        self.udpSocket.writeDatagram(datagram, QHostAddress(QHostAddress.Broadcast), 45454)
        self.messageNo +_ 1


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    sender _ Sender()
    sender.s..
    sys.exit(sender.exec_())
