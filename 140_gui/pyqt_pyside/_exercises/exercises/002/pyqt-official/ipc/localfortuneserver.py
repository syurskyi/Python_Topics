#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################


______ random

____ ?.?C.. ______ QByteArray, ?DS.., QIODevice
____ ?.?W.. ______ (?A.., ?D.., ?L.., ?HBL..,
        ?MB.., ?PB.., ?VBL..)
____ ?.?N.. ______ QLocalServer


c_ Server(?D..):
    ___  -   parent_None):
        s__(Server, self). - (parent)

        statusLabel _ ?L..
        statusLabel.setWordWrap( st.
        quitButton _ ?PB..("Quit")
        quitButton.setAutoDefault F..

        fortunes _ (
            "You've been leading a dog's life. Stay off the furniture.",
            "You've got to think about tomorrow.",
            "You will be surprised by a loud noise.",
            "You will feel hungry again in another hour.",
            "You might have mail.",
            "You cannot kill time without injuring eternity.",
            "Computers are not intelligent. They only think they are.",
        )

        server _ QLocalServer()
        __ no. server.l..('fortune'):
            ?MB...c..  "Fortune Server",
                    "Unable to start the server: %s." % server.errorString())
            c..
            r_

        statusLabel.sT..("The server is running.\nRun the Fortune Client "
                "example now.")

        quitButton.c__.c..(close)
        server.newConnection.c..(sendFortune)

        buttonLayout _ ?HBL..
        buttonLayout.addStretch(1)
        buttonLayout.aW..(quitButton)
        buttonLayout.addStretch(1)

        mainLayout _ ?VBL..
        mainLayout.aW..(statusLabel)
        mainLayout.aL..(buttonLayout)
        sL..(mainLayout)

        sWT..("Fortune Server")

    ___ sendFortune
        block _ QByteArray()
        out _ ?DS..(block, QIODevice.WriteOnly)
        out.setVersion(?DS...Qt_4_0)
        out.writeUInt16(0)
        out.writeQString(random.choice(fortunes))
        out.device().seek(0)
        out.writeUInt16(block.size() - 2)

        clientConnection _ server.nPC..()
        clientConnection.disconnected.c..(clientConnection.deleteLater)
        clientConnection.w..(block)
        clientConnection.flush()
        clientConnection.disconnectFromServer()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    server _ Server()
    server.s..
    ___.e.. ?.e..
