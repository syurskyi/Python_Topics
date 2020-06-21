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
###########################################################################


____ ?.?C.. ______ pyqtSlot, ?U..
____ ?.?G.. ______ ?KS..
____ ?.?W.. ______ (?A.., ?A.., ?MW.., ?MB..,
        ?W..)

______ formextractor_rc
____ ui_formextractor ______ Ui_Form


c_ FormExtractor(?W..):
    ___  -   parent_None):
        s__(FormExtractor, self). - (parent)

        ui _ Ui_Form()
        ui.setupUi

        webView _ ui.webView
        webView.setUrl(?U..('qrc:/form.html'))
        webView.page().mainFrame().javaScriptWindowObjectCleared.c..(
                populateJavaScriptWindowObject)

        r..(300, 300)
 
    @pyqtSlot()
    ___ submit 
        frame _ ui.webView.page().mainFrame()
        firstName _ frame.findFirstElement('#firstname')
        lastName _ frame.findFirstElement('#lastname')
        maleGender _ frame.findFirstElement('#genderMale')
        femaleGender _ frame.findFirstElement('#genderFemale')
        updates _ frame.findFirstElement('#updates')

        ui.firstNameEdit.sT..(firstName.evaluateJavaScript('this.value'))
        ui.lastNameEdit.sT..(lastName.evaluateJavaScript('this.value'))

        __ maleGender.evaluateJavaScript('this.checked'):
            ui.genderEdit.sT..(
                    maleGender.evaluateJavaScript('this.value'))
        ____ femaleGender.evaluateJavaScript('this.checked'):
            ui.genderEdit.sT..(
                    femaleGender.evaluateJavaScript('this.value'))

        __ updates.evaluateJavaScript('this.checked'):
            ui.updatesEdit.sT..("Yes")
        ____
            ui.updatesEdit.sT..("No")

    ___ populateJavaScriptWindowObject 
        ui.webView.page().mainFrame().addToJavaScriptWindowObject(
                'formExtractor', self)


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        createActions()
        createMenus()
        centralWidget _ FormExtractor
        sCW..(centralWidget)
    
    ___ createActions 
        exitAct _ ?A..("E&xit", self, statusTip_"Exit the application",
                shortcut_QKeySequence.Quit, triggered_self.close)

        aboutAct _ ?A..("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.i.. .aboutQt)

    ___ createMenus 
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(exitAct)
        mB.. .aS..)
        helpMenu _ mB.. .aM..("&Help")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ about 
        ?MB...about  "About Form Extractor",
                "The <b>Form Extractor</b> example demonstrates how to "
                "extract data from a web form using QtWebKit.")


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    mainWindow _ MainWindow()
    mainWindow.sWT..("Form Extractor")
    mainWindow.s..

    ___.e.. ?.e..
