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


____ ?.?C.. ______ QDataStream, QTimer
____ ?.?W.. ______ (?A.., QDialog, QDialogButtonBox,
        QGridLayout, QLabel, QLineEdit, ?MB.., ?PB..)
____ ?.QtNetwork ______ QLocalSocket


c_ Client(QDialog):
    ___ __init__  parent_None):
        super(Client, self).__init__(parent)

        self.blockSize _ 0
        self.currentFortune _ N..

        hostLabel _ QLabel("&Server name:")
        self.hostLineEdit _ QLineEdit("fortune")
        hostLabel.setBuddy(self.hostLineEdit)

        self.statusLabel _ QLabel(
                "This examples requires that you run the Fortune Server "
                "example as well.")
        self.statusLabel.setWordWrap(True)

        self.getFortuneButton _ ?PB..("Get Fortune")
        self.getFortuneButton.setDefault(True)

        quitButton _ ?PB..("Quit")
        buttonBox _ QDialogButtonBox()
        buttonBox.addButton(self.getFortuneButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QDialogButtonBox.RejectRole)

        self.socket _ QLocalSocket()

        self.hostLineEdit.textChanged.c..(self.enableGetFortuneButton)
        self.getFortuneButton.c__.c..(self.requestNewFortune)
        quitButton.c__.c..(self.close)
        self.socket.readyRead.c..(self.readFortune)
        self.socket.error.c..(self.displayError)

        mainLayout _ QGridLayout()
        mainLayout.aW..(hostLabel, 0, 0)
        mainLayout.aW..(self.hostLineEdit, 0, 1)
        mainLayout.aW..(self.statusLabel, 2, 0, 1, 2)
        mainLayout.aW..(buttonBox, 3, 0, 1, 2)
        self.sL..(mainLayout)

        self.setWindowTitle("Fortune Client")
        self.hostLineEdit.setFocus()

    ___ requestNewFortune(self):
        self.getFortuneButton.setEnabled F..
        self.blockSize _ 0
        self.socket.abort()
        self.socket.connectToServer(self.hostLineEdit.t__())

    ___ readFortune(self):
        ins _ QDataStream(self.socket)
        ins.setVersion(QDataStream.Qt_4_0)

        __ self.blockSize == 0:
            __ self.socket.bytesAvailable() < 2:
                r_
            self.blockSize _ ins.readUInt16()

        __ ins.atEnd
            r_

        nextFortune _ ins.readQString()
        __ nextFortune == self.currentFortune:
            QTimer.singleShot(0, self.requestNewFortune)
            r_
 
        self.currentFortune _ nextFortune
        self.statusLabel.sT..(self.currentFortune)
        self.getFortuneButton.setEnabled(True)

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
                "The following error occurred: %s." % self.socket.errorString())
        __ msg __ no. N..:
            ?MB...information  "Fortune Client", msg)

        self.getFortuneButton.setEnabled(True)

    ___ enableGetFortuneButton(self):
        self.getFortuneButton.setEnabled(self.hostLineEdit.t__() !_ "")


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    client _ Client()
    client.s..
    sys.exit(app.exec_())
