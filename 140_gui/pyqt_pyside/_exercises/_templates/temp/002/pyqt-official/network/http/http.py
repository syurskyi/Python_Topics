#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
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


____ ?.?C.. ______ QDir, QFile, QFileInfo, QIODevice, QUrl
____ ?.?W.. ______ (?A.., QDialog, QDialogButtonBox,
        QHBoxLayout, QLabel, QLineEdit, ?MB.., QProgressDialog,
        ?PB.., QVBoxLayout)
____ ?.QtNetwork ______ QNetworkAccessManager, QNetworkRequest


c_ HttpWindow(QDialog):
    ___ __init__  parent_None):
        super(HttpWindow, self).__init__(parent)

        self.url _ QUrl()
        self.qnam _ QNetworkAccessManager()
        self.reply _ N..
        self.outFile _ N..
        self.httpGetId _ 0
        self.httpRequestAborted _ False

        self.urlLineEdit _ QLineEdit('https://www.qt.io')

        urlLabel _ QLabel("&URL:")
        urlLabel.setBuddy(self.urlLineEdit)
        self.statusLabel _ QLabel(
                "Please enter the URL of a file you want to download.")
        self.statusLabel.setWordWrap(True)

        self.downloadButton _ ?PB..("Download")
        self.downloadButton.setDefault(True)
        self.quitButton _ ?PB..("Quit")
        self.quitButton.setAutoDefault F..

        buttonBox _ QDialogButtonBox()
        buttonBox.addButton(self.downloadButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(self.quitButton, QDialogButtonBox.RejectRole)

        self.progressDialog _ QProgressDialog(self)

        self.urlLineEdit.textChanged.c..(self.enableDownloadButton)
        self.qnam.authenticationRequired.c..(
                self.slotAuthenticationRequired)
        self.qnam.sslErrors.c..(self.sslErrors)
        self.progressDialog.canceled.c..(self.cancelDownload)
        self.downloadButton.c__.c..(self.downloadFile)
        self.quitButton.c__.c..(self.close)

        topLayout _ QHBoxLayout()
        topLayout.aW..(urlLabel)
        topLayout.aW..(self.urlLineEdit)

        mainLayout _ ?VBL..
        mainLayout.addLayout(topLayout)
        mainLayout.aW..(self.statusLabel)
        mainLayout.aW..(buttonBox)
        self.sL..(mainLayout)

        self.setWindowTitle("HTTP")
        self.urlLineEdit.setFocus()

    ___ startRequest  url):
        self.reply _ self.qnam.g..(QNetworkRequest(url))
        self.reply.finished.c..(self.httpFinished)
        self.reply.readyRead.c..(self.httpReadyRead)
        self.reply.downloadProgress.c..(self.updateDataReadProgress)

    ___ downloadFile(self):
        self.url _ QUrl(self.urlLineEdit.t__())
        fileInfo _ QFileInfo(self.url.path())
        fileName _ fileInfo.fileName()

        __ no. fileName:
            fileName _ 'index.html'

        __ QFile.exists(fileName):
            ret _ ?MB...q..  "HTTP",
                    "There already exists a file called %s in the current "
                    "directory. Overwrite?" % fileName,
                    ?MB...Yes | ?MB...No, ?MB...No)

            __ ret == ?MB...No:
                r_

            QFile.remove(fileName)

        self.outFile _ QFile(fileName)
        __ no. self.outFile.o..(QIODevice.WriteOnly):
            ?MB...information  "HTTP",
                    "Unable to save the file %s: %s." % (fileName, self.outFile.errorString()))
            self.outFile _ N..
            r_

        self.progressDialog.setWindowTitle("HTTP")
        self.progressDialog.setLabelText("Downloading %s." % fileName)
        self.downloadButton.setEnabled F..

        self.httpRequestAborted _ False
        self.startRequest(self.url)

    ___ cancelDownload(self):
        self.statusLabel.sT..("Download canceled.")
        self.httpRequestAborted _ True
        __ self.reply __ no. N..:
            self.reply.abort()
        self.downloadButton.setEnabled(True)

    ___ httpFinished(self):
        __ self.httpRequestAborted:
            __ self.outFile __ no. N..:
                self.outFile.close()
                self.outFile.remove()
                self.outFile _ N..

            self.reply.deleteLater()
            self.reply _ N..
            self.progressDialog.hide()
            r_

        self.progressDialog.hide()
        self.outFile.flush()
        self.outFile.close()

        redirectionTarget _ self.reply.attribute(QNetworkRequest.RedirectionTargetAttribute)

        __ self.reply.error
            self.outFile.remove()
            ?MB...information  "HTTP",
                    "Download failed: %s." % self.reply.errorString())
            self.downloadButton.setEnabled(True)
        ____ redirectionTarget __ no. N..:
            newUrl _ self.url.resolved(redirectionTarget)

            ret _ ?MB...q..  "HTTP",
                    "Redirect to %s?" % newUrl.toString(),
                    ?MB...Yes | ?MB...No)

            __ ret == ?MB...Yes:
                self.url _ newUrl
                self.reply.deleteLater()
                self.reply _ N..
                self.outFile.o..(QIODevice.WriteOnly)
                self.outFile.resize(0)
                self.startRequest(self.url)
                r_
        ____
            fileName _ QFileInfo(QUrl(self.urlLineEdit.t__()).path()).fileName()
            self.statusLabel.sT..("Downloaded %s to %s." % (fileName, QDir.currentPath()))

            self.downloadButton.setEnabled(True)

        self.reply.deleteLater()
        self.reply _ N..
        self.outFile _ N..

    ___ httpReadyRead(self):
        __ self.outFile __ no. N..:
            self.outFile.w..(self.reply.readAll())

    ___ updateDataReadProgress  bytesRead, totalBytes):
        __ self.httpRequestAborted:
            r_

        self.progressDialog.setMaximum(totalBytes)
        self.progressDialog.setValue(bytesRead)

    ___ enableDownloadButton(self):
        self.downloadButton.setEnabled(self.urlLineEdit.t__() !_ '')

    ___ slotAuthenticationRequired  authenticator):
        ______ os
        ____ ? ______ uic

        ui _ __.p__ .join(__.p__ .dirname(__file__), 'authenticationdialog.ui')
        dlg _ uic.loadUi(ui)
        dlg.adjustSize()
        dlg.siteDescription.sT..("%s at %s" % (authenticator.realm(), self.url.host()))

        dlg.userEdit.sT..(self.url.userName())
        dlg.passwordEdit.sT..(self.url.password())

        __ dlg.e.. == QDialog.Accepted:
            authenticator.setUser(dlg.userEdit.t__())
            authenticator.setPassword(dlg.passwordEdit.t__())

    ___ sslErrors  reply, errors):
        errorString _ ", ".join([str(error.errorString()) for error in errors])

        ret _ ?MB...warning  "HTTP Example",
                "One or more SSL errors has occurred: %s" % errorString,
                ?MB...Ignore | ?MB...Abort)

        __ ret == ?MB...Ignore:
            self.reply.ignoreSslErrors()


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    httpWin _ HttpWindow()
    httpWin.s..
    sys.exit(httpWin.exec_())
