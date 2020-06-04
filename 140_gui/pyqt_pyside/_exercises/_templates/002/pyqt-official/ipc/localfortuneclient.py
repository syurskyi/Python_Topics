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


____ ?.?C.. ______ ?DS.., ?T..
____ ?.?W.. ______ (?A.., ?D.., ?DBB...,
        QGridLayout, ?L.., QLineEdit, ?MB.., ?PB..)
____ ?.?N.. ______ QLocalSocket


c_ Client(?D..):
    ___  -   parent_None):
        s__(Client, self). - (parent)

        blockSize _ 0
        currentFortune _ N..

        hostLabel _ ?L..("&Server name:")
        hostLineEdit _ QLineEdit("fortune")
        hostLabel.setBuddy(hostLineEdit)

        statusLabel _ ?L..(
                "This examples requires that you run the Fortune Server "
                "example as well.")
        statusLabel.setWordWrap( st.

        getFortuneButton _ ?PB..("Get Fortune")
        getFortuneButton.setDefault( st.

        quitButton _ ?PB..("Quit")
        buttonBox _ ?DBB...()
        buttonBox.addButton(getFortuneButton, ?DBB....ActionRole)
        buttonBox.addButton(quitButton, ?DBB....RejectRole)

        socket _ QLocalSocket()

        hostLineEdit.tC...c..(enableGetFortuneButton)
        getFortuneButton.c__.c..(requestNewFortune)
        quitButton.c__.c..(close)
        socket.readyRead.c..(readFortune)
        socket.error.c..(displayError)

        mainLayout _ QGridLayout()
        mainLayout.aW..(hostLabel, 0, 0)
        mainLayout.aW..(hostLineEdit, 0, 1)
        mainLayout.aW..(statusLabel, 2, 0, 1, 2)
        mainLayout.aW..(buttonBox, 3, 0, 1, 2)
        sL..(mainLayout)

        sWT..("Fortune Client")
        hostLineEdit.setFocus()

    ___ requestNewFortune
        getFortuneButton.sE.. F..
        blockSize _ 0
        socket.abort()
        socket.connectToServer(hostLineEdit.t__())

    ___ readFortune
        ins _ ?DS..(socket)
        ins.setVersion(?DS...Qt_4_0)

        __ blockSize __ 0:
            __ socket.bA..() < 2:
                r_
            blockSize _ ins.readUInt16()

        __ ins.atEnd
            r_

        nextFortune _ ins.rQS..
        __ nextFortune __ currentFortune:
            ?T...sS..(0, requestNewFortune)
            r_
 
        currentFortune _ nextFortune
        statusLabel.sT..(currentFortune)
        getFortuneButton.sE..( st.

    ___ displayError  socketError):
        errors _ {
            QLocalSocket.ServerNotFoundError:
                "The host was not found. Please check the host name and port "
                "settings.",

            QLocalSocket.ConnectionRefusedError:
                "The connection was refused by the peer. Make sure the "
                "fortune server is running, and check that the host name and "
                "port settings are correct.",

            QLocalSocket.PeerClosedError:
                N..,
        }

        msg _ errors.g..(socketError,
                "The following error occurred: %s." % socket.errorString())
        __ msg __ no. N..:
            ?MB...i..  "Fortune Client", msg)

        getFortuneButton.sE..( st.

    ___ enableGetFortuneButton
        getFortuneButton.sE..(hostLineEdit.t__() !_ "")


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    client _ Client()
    client.s..
    ___.e.. ?.e..
