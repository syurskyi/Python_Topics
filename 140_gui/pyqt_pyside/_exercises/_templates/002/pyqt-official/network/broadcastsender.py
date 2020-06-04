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


____ ?.?C.. ______ ?T..
____ ?.?W.. ______ (?A.., ?D.., ?DBB..., ?L..,
        ?PB.., ?VBL..)
____ ?.?N.. ______ ?HA.., QUdpSocket


c_ Sender(?D..):
    ___  -   parent_None):
        s__(Sender, self). - (parent)

        statusLabel _ ?L..("Ready to broadcast datagrams on port 45454")

        startButton _ ?PB..("&Start")
        quitButton _ ?PB..("&Quit")

        buttonBox _ ?DBB...()
        buttonBox.addButton(startButton, ?DBB....ActionRole)
        buttonBox.addButton(quitButton, ?DBB....RejectRole)

        timer _ ?T..
        udpSocket _ QUdpSocket
        messageNo _ 1

        startButton.c__.c..(startBroadcasting)
        quitButton.c__.c..(close)
        timer.timeout.c..(broadcastDatagramm)

        mainLayout _ ?VBL..
        mainLayout.aW..(statusLabel)
        mainLayout.aW..(buttonBox)
        sL..(mainLayout)

        sWT..("Broadcast Sender")

    ___ startBroadcasting 
        startButton.sE.. F..
        timer.start(1000)

    ___ broadcastDatagramm 
        statusLabel.sT..("Now broadcasting datagram %d" % messageNo)
        datagram _ "Broadcast message %d" % messageNo
        udpSocket.writeDatagram(datagram, ?HA..(?HA...Broadcast), 45454)
        messageNo +_ 1


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    sender _ Sender()
    sender.s..
    ___.e..(sender.e..
