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


____ ?.QtCore ______ (pyqtSignal, QDataStream, QMutex, QMutexLocker,
        QThread, QWaitCondition)
____ ?.QtGui ______ QIntValidator
____ ?.?W.. ______ (?A.., QDialogButtonBox, QGridLayout,
        QLabel, QLineEdit, QMessageBox, ?PB.., QWidget)
____ ?.QtNetwork ______ (QAbstractSocket, QHostAddress, QNetworkInterface,
        QTcpSocket)


class FortuneThread(QThread):
    newFortune _ pyqtSignal(str)

    error _ pyqtSignal(int, str)

    ___ __init__(self, parent_None):
        super(FortuneThread, self).__init__(parent)

        self.quit _ False
        self.hostName _ ''
        self.cond _ QWaitCondition()
        self.mutex _ QMutex()
        self.port _ 0

    ___ __del__(self):
        self.mutex.lock()
        self.quit _ True
        self.cond.wakeOne()
        self.mutex.unlock()
        self.wait()

    ___ requestNewFortune(self, hostname, port):
        locker _ QMutexLocker(self.mutex)
        self.hostName _ hostname
        self.port _ port
        if not self.isRunning
            self.start()
        else:
            self.cond.wakeOne()

    ___ run(self):
        self.mutex.lock()
        serverName _ self.hostName
        serverPort _ self.port
        self.mutex.unlock()

        while not self.quit:
            Timeout _ 5 * 1000

            socket _ QTcpSocket()
            socket.connectToHost(serverName, serverPort)

            if not socket.waitForConnected(Timeout):
                self.error.emit(socket.error(), socket.errorString())
                return

            while socket.bytesAvailable() < 2:
                if not socket.waitForReadyRead(Timeout):
                    self.error.emit(socket.error(), socket.errorString())
                    return 

            instr _ QDataStream(socket)
            instr.setVersion(QDataStream.Qt_4_0)
            blockSize _ instr.readUInt16()

            while socket.bytesAvailable() < blockSize:
                if not socket.waitForReadyRead(Timeout):
                    self.error.emit(socket.error(), socket.errorString())
                    return

            self.mutex.lock()
            fortune _ instr.readQString()
            self.newFortune.emit(fortune)

            self.cond.wait(self.mutex)
            serverName _ self.hostName
            serverPort _ self.port
            self.mutex.unlock()


class BlockingClient(QWidget):
    ___ __init__(self, parent_None):
        super(BlockingClient, self).__init__(parent)

        self.thread _ FortuneThread()
        self.currentFortune _ ''

        hostLabel _ QLabel("&Server name:")
        portLabel _ QLabel("S&erver port:")

        for ipAddress in QNetworkInterface.allAddresses
            if ipAddress !_ QHostAddress.LocalHost and ipAddress.toIPv4Address() !_ 0:
                break
        else:
            ipAddress _ QHostAddress(QHostAddress.LocalHost)

        ipAddress _ ipAddress.toString()

        self.hostLineEdit _ QLineEdit(ipAddress)
        self.portLineEdit _ QLineEdit()
        self.portLineEdit.setValidator(QIntValidator(1, 65535, self))

        hostLabel.setBuddy(self.hostLineEdit)
        portLabel.setBuddy(self.portLineEdit)

        self.statusLabel _ QLabel(
                "This example requires that you run the Fortune Server example as well.")
        self.statusLabel.setWordWrap(True)

        self.getFortuneButton _ ?PB..("Get Fortune")
        self.getFortuneButton.setDefault(True)
        self.getFortuneButton.setEnabled(False)

        quitButton _ ?PB..("Quit")

        buttonBox _ QDialogButtonBox()
        buttonBox.addButton(self.getFortuneButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QDialogButtonBox.RejectRole)

        self.getFortuneButton.c__.c..(self.requestNewFortune)
        quitButton.c__.c..(self.close)
        self.hostLineEdit.textChanged.c..(self.enableGetFortuneButton)
        self.portLineEdit.textChanged.c..(self.enableGetFortuneButton)
        self.thread.newFortune.c..(self.showFortune)
        self.thread.error.c..(self.displayError)

        mainLayout _ QGridLayout()
        mainLayout.addWidget(hostLabel, 0, 0)
        mainLayout.addWidget(self.hostLineEdit, 0, 1)
        mainLayout.addWidget(portLabel, 1, 0)
        mainLayout.addWidget(self.portLineEdit, 1, 1)
        mainLayout.addWidget(self.statusLabel, 2, 0, 1, 2)
        mainLayout.addWidget(buttonBox, 3, 0, 1, 2)
        self.setLayout(mainLayout)

        self.setWindowTitle("Blocking Fortune Client")
        self.portLineEdit.setFocus()

    ___ requestNewFortune(self):
        self.getFortuneButton.setEnabled(False)
        self.thread.requestNewFortune(self.hostLineEdit.text(),
                int(self.portLineEdit.text()))

    ___ showFortune(self, nextFortune):
        if nextFortune == self.currentFortune:
            self.requestNewFortune()
            return

        self.currentFortune _ nextFortune
        self.statusLabel.sT..(self.currentFortune)
        self.getFortuneButton.setEnabled(True)

    ___ displayError(self, socketError, message):
        if socketError == QAbstractSocket.HostNotFoundError:
            QMessageBox.information(self, "Blocking Fortune Client",
                    "The host was not found. Please check the host and port "
                    "settings.")
        elif socketError == QAbstractSocket.ConnectionRefusedError:
            QMessageBox.information(self, "Blocking Fortune Client",
                    "The connection was refused by the peer. Make sure the "
                    "fortune server is running, and check that the host name "
                    "and port settings are correct.")
        else:
            QMessageBox.information(self, "Blocking Fortune Client",
                    "The following error occurred: %s." % message)

        self.getFortuneButton.setEnabled(True)

    ___ enableGetFortuneButton(self):
        self.getFortuneButton.setEnabled(self.hostLineEdit.text() !_ '' and
                self.portLineEdit.text() !_ '')


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    client _ BlockingClient()
    client.s..
    sys.exit(app.exec_())
