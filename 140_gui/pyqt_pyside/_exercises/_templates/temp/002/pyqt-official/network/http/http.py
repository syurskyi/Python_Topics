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


____ ?.QtCore ______ QDir, QFile, QFileInfo, QIODevice, QUrl
____ ?.?W.. ______ (?A.., QDialog, QDialogButtonBox,
        QHBoxLayout, QLabel, QLineEdit, QMessageBox, QProgressDialog,
        ?PB.., QVBoxLayout)
____ ?.QtNetwork ______ QNetworkAccessManager, QNetworkRequest


class HttpWindow(QDialog):
    ___ __init__(self, parent_None):
        super(HttpWindow, self).__init__(parent)

        self.url _ QUrl()
        self.qnam _ QNetworkAccessManager()
        self.reply _ None
        self.outFile _ None
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
        self.quitButton.setAutoDefault(False)

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
        topLayout.addWidget(urlLabel)
        topLayout.addWidget(self.urlLineEdit)

        mainLayout _ QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addWidget(self.statusLabel)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("HTTP")
        self.urlLineEdit.setFocus()

    ___ startRequest(self, url):
        self.reply _ self.qnam.get(QNetworkRequest(url))
        self.reply.finished.c..(self.httpFinished)
        self.reply.readyRead.c..(self.httpReadyRead)
        self.reply.downloadProgress.c..(self.updateDataReadProgress)

    ___ downloadFile(self):
        self.url _ QUrl(self.urlLineEdit.text())
        fileInfo _ QFileInfo(self.url.path())
        fileName _ fileInfo.fileName()

        if not fileName:
            fileName _ 'index.html'

        if QFile.exists(fileName):
            ret _ QMessageBox.question(self, "HTTP",
                    "There already exists a file called %s in the current "
                    "directory. Overwrite?" % fileName,
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if ret == QMessageBox.No:
                return

            QFile.remove(fileName)

        self.outFile _ QFile(fileName)
        if not self.outFile.open(QIODevice.WriteOnly):
            QMessageBox.information(self, "HTTP",
                    "Unable to save the file %s: %s." % (fileName, self.outFile.errorString()))
            self.outFile _ None
            return

        self.progressDialog.setWindowTitle("HTTP")
        self.progressDialog.setLabelText("Downloading %s." % fileName)
        self.downloadButton.setEnabled(False)

        self.httpRequestAborted _ False
        self.startRequest(self.url)

    ___ cancelDownload(self):
        self.statusLabel.sT..("Download canceled.")
        self.httpRequestAborted _ True
        if self.reply is not None:
            self.reply.abort()
        self.downloadButton.setEnabled(True)

    ___ httpFinished(self):
        if self.httpRequestAborted:
            if self.outFile is not None:
                self.outFile.close()
                self.outFile.remove()
                self.outFile _ None

            self.reply.deleteLater()
            self.reply _ None
            self.progressDialog.hide()
            return

        self.progressDialog.hide()
        self.outFile.flush()
        self.outFile.close()

        redirectionTarget _ self.reply.attribute(QNetworkRequest.RedirectionTargetAttribute)

        if self.reply.error
            self.outFile.remove()
            QMessageBox.information(self, "HTTP",
                    "Download failed: %s." % self.reply.errorString())
            self.downloadButton.setEnabled(True)
        elif redirectionTarget is not None:
            newUrl _ self.url.resolved(redirectionTarget)

            ret _ QMessageBox.question(self, "HTTP",
                    "Redirect to %s?" % newUrl.toString(),
                    QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.Yes:
                self.url _ newUrl
                self.reply.deleteLater()
                self.reply _ None
                self.outFile.open(QIODevice.WriteOnly)
                self.outFile.resize(0)
                self.startRequest(self.url)
                return
        else:
            fileName _ QFileInfo(QUrl(self.urlLineEdit.text()).path()).fileName()
            self.statusLabel.sT..("Downloaded %s to %s." % (fileName, QDir.currentPath()))

            self.downloadButton.setEnabled(True)

        self.reply.deleteLater()
        self.reply _ None
        self.outFile _ None

    ___ httpReadyRead(self):
        if self.outFile is not None:
            self.outFile.write(self.reply.readAll())

    ___ updateDataReadProgress(self, bytesRead, totalBytes):
        if self.httpRequestAborted:
            return

        self.progressDialog.setMaximum(totalBytes)
        self.progressDialog.setValue(bytesRead)

    ___ enableDownloadButton(self):
        self.downloadButton.setEnabled(self.urlLineEdit.text() !_ '')

    ___ slotAuthenticationRequired(self, authenticator):
        ______ os
        ____ ? ______ uic

        ui _ os.path.join(os.path.dirname(__file__), 'authenticationdialog.ui')
        dlg _ uic.loadUi(ui)
        dlg.adjustSize()
        dlg.siteDescription.sT..("%s at %s" % (authenticator.realm(), self.url.host()))

        dlg.userEdit.sT..(self.url.userName())
        dlg.passwordEdit.sT..(self.url.password())

        if dlg.e.. == QDialog.Accepted:
            authenticator.setUser(dlg.userEdit.text())
            authenticator.setPassword(dlg.passwordEdit.text())

    ___ sslErrors(self, reply, errors):
        errorString _ ", ".join([str(error.errorString()) for error in errors])

        ret _ QMessageBox.warning(self, "HTTP Example",
                "One or more SSL errors has occurred: %s" % errorString,
                QMessageBox.Ignore | QMessageBox.Abort)

        if ret == QMessageBox.Ignore:
            self.reply.ignoreSslErrors()


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    httpWin _ HttpWindow()
    httpWin.s..
    sys.exit(httpWin.exec_())
