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


____ ?.?C.. ______ ?D.., QFile, QFileInfo, QIODevice, ?U..
____ ?.?W.. ______ (?A.., ?D.., ?DBB...,
        ?HBL.., ?L.., QLineEdit, ?MB.., QProgressDialog,
        ?PB.., ?VBL..)
____ ?.?N.. ______ ?NAM.., ?NR..


c_ HttpWindow(?D..):
    ___  -   parent_None):
        s__(HttpWindow, self). - (parent)

        url _ ?U..()
        qnam _ ?NAM..()
        reply _ N..
        outFile _ N..
        httpGetId _ 0
        httpRequestAborted _ F..

        urlLineEdit _ QLineEdit('https://www.qt.io')

        urlLabel _ ?L..("&URL:")
        urlLabel.setBuddy(urlLineEdit)
        statusLabel _ ?L..(
                "Please enter the URL of a file you want to download.")
        statusLabel.setWordWrap( st.

        downloadButton _ ?PB..("Download")
        downloadButton.setDefault( st.
        quitButton _ ?PB..("Quit")
        quitButton.setAutoDefault F..

        buttonBox _ ?DBB...()
        buttonBox.addButton(downloadButton, ?DBB....ActionRole)
        buttonBox.addButton(quitButton, ?DBB....RejectRole)

        progressDialog _ QProgressDialog

        urlLineEdit.tC...c..(enableDownloadButton)
        qnam.authenticationRequired.c..(
                slotAuthenticationRequired)
        qnam.sslErrors.c..(sslErrors)
        progressDialog.canceled.c..(cancelDownload)
        downloadButton.c__.c..(downloadFile)
        quitButton.c__.c..(close)

        topLayout _ ?HBL..
        topLayout.aW..(urlLabel)
        topLayout.aW..(urlLineEdit)

        mainLayout _ ?VBL..
        mainLayout.aL..(topLayout)
        mainLayout.aW..(statusLabel)
        mainLayout.aW..(buttonBox)
        sL..(mainLayout)

        sWT..("HTTP")
        urlLineEdit.setFocus()

    ___ startRequest  url):
        reply _ qnam.g..(?NR..(url))
        reply.finished.c..(httpFinished)
        reply.readyRead.c..(httpReadyRead)
        reply.downloadProgress.c..(updateDataReadProgress)

    ___ downloadFile 
        url _ ?U..(urlLineEdit.t__())
        fileInfo _ QFileInfo(url.pa__())
        fileName _ fileInfo.fN..

        __ no. fileName:
            fileName _ 'index.html'

        __ QFile.e..(fileName):
            ret _ ?MB...q..  "HTTP",
                    "There already exists a file called %s in the current "
                    "directory. Overwrite?" % fileName,
                    ?MB...Yes | ?MB...No, ?MB...No)

            __ ret __ ?MB...No:
                r_

            QFile.remove(fileName)

        outFile _ QFile(fileName)
        __ no. outFile.o..(QIODevice.WriteOnly):
            ?MB...i..  "HTTP",
                    "Unable to save the file %s: %s." % (fileName, outFile.errorString()))
            outFile _ N..
            r_

        progressDialog.sWT..("HTTP")
        progressDialog.setLabelText("Downloading %s." % fileName)
        downloadButton.sE.. F..

        httpRequestAborted _ F..
        startRequest(url)

    ___ cancelDownload 
        statusLabel.sT..("Download canceled.")
        httpRequestAborted _ T..
        __ reply __ no. N..:
            reply.abort()
        downloadButton.sE..( st.

    ___ httpFinished 
        __ httpRequestAborted:
            __ outFile __ no. N..:
                outFile.c..
                outFile.remove()
                outFile _ N..

            reply.deleteLater()
            reply _ N..
            progressDialog.hide()
            r_

        progressDialog.hide()
        outFile.flush()
        outFile.c..

        redirectionTarget _ reply.attribute(?NR...RedirectionTargetAttribute)

        __ reply.error
            outFile.remove()
            ?MB...i..  "HTTP",
                    "Download failed: %s." % reply.errorString())
            downloadButton.sE..( st.
        ____ redirectionTarget __ no. N..:
            newUrl _ url.resolved(redirectionTarget)

            ret _ ?MB...q..  "HTTP",
                    "Redirect to %s?" % newUrl.tS..,
                    ?MB...Yes | ?MB...No)

            __ ret __ ?MB...Yes:
                url _ newUrl
                reply.deleteLater()
                reply _ N..
                outFile.o..(QIODevice.WriteOnly)
                outFile.r..(0)
                startRequest(url)
                r_
        ____
            fileName _ QFileInfo(?U..(urlLineEdit.t__()).pa__()).fN..
            statusLabel.sT..("Downloaded %s to %s." % (fileName, ?D...currentPath()))

            downloadButton.sE..( st.

        reply.deleteLater()
        reply _ N..
        outFile _ N..

    ___ httpReadyRead 
        __ outFile __ no. N..:
            outFile.w..(reply.readAll())

    ___ updateDataReadProgress  bytesRead, totalBytes):
        __ httpRequestAborted:
            r_

        progressDialog.sM..(totalBytes)
        progressDialog.sV..(bytesRead)

    ___ enableDownloadButton 
        downloadButton.sE..(urlLineEdit.t__() !_ '')

    ___ slotAuthenticationRequired  authenticator):
        ______ __
        ____ ? ______ uic

        ui _ __.p__ .join(__.p__ .dirname(__file__), 'authenticationdialog.ui')
        dlg _ uic.loadUi(ui)
        dlg.adjustSize()
        dlg.siteDescription.sT..("%s at %s" % (authenticator.realm(), url.host()))

        dlg.userEdit.sT..(url.userName())
        dlg.passwordEdit.sT..(url.password())

        __ dlg.e.. __ ?D...Accepted:
            authenticator.setUser(dlg.userEdit.t__())
            authenticator.setPassword(dlg.passwordEdit.t__())

    ___ sslErrors  reply, errors):
        errorString _ ", ".join([st.(error.errorString()) ___ error __ errors])

        ret _ ?MB...w..  "HTTP Example",
                "One or more SSL errors has occurred: %s" % errorString,
                ?MB...Ignore | ?MB...Abort)

        __ ret __ ?MB...Ignore:
            reply.ignoreSslErrors()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    httpWin _ HttpWindow()
    httpWin.s..
    ___.e..(httpWin.e..
