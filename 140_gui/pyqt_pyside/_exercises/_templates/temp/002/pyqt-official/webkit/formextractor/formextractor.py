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


____ ?.QtCore ______ pyqtSlot, QUrl
____ ?.QtGui ______ QKeySequence
____ ?.?W.. ______ (QAction, QApplication, QMainWindow, QMessageBox,
        QWidget)

______ formextractor_rc
____ ui_formextractor ______ Ui_Form


class FormExtractor(QWidget):
    ___ __init__(self, parent_None):
        super(FormExtractor, self).__init__(parent)

        self.ui _ Ui_Form()
        self.ui.setupUi(self)

        webView _ self.ui.webView
        webView.setUrl(QUrl('qrc:/form.html'))
        webView.page().mainFrame().javaScriptWindowObjectCleared.c..(
                self.populateJavaScriptWindowObject)

        self.resize(300, 300)
 
    @pyqtSlot()
    ___ submit(self):
        frame _ self.ui.webView.page().mainFrame()
        firstName _ frame.findFirstElement('#firstname')
        lastName _ frame.findFirstElement('#lastname')
        maleGender _ frame.findFirstElement('#genderMale')
        femaleGender _ frame.findFirstElement('#genderFemale')
        updates _ frame.findFirstElement('#updates')

        self.ui.firstNameEdit.sT..(firstName.evaluateJavaScript('this.value'))
        self.ui.lastNameEdit.sT..(lastName.evaluateJavaScript('this.value'))

        if maleGender.evaluateJavaScript('this.checked'):
            self.ui.genderEdit.sT..(
                    maleGender.evaluateJavaScript('this.value'))
        elif femaleGender.evaluateJavaScript('this.checked'):
            self.ui.genderEdit.sT..(
                    femaleGender.evaluateJavaScript('this.value'))

        if updates.evaluateJavaScript('this.checked'):
            self.ui.updatesEdit.sT..("Yes")
        else:
            self.ui.updatesEdit.sT..("No")

    ___ populateJavaScriptWindowObject(self):
        self.ui.webView.page().mainFrame().addToJavaScriptWindowObject(
                'formExtractor', self)


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.createActions()
        self.createMenus()
        self.centralWidget _ FormExtractor(self)
        self.setCentralWidget(self.centralWidget)
    
    ___ createActions(self):
        self.exitAct _ QAction("E&xit", self, statusTip_"Exit the application",
                shortcut_QKeySequence.Quit, triggered_self.close)

        self.aboutAct _ QAction("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        self.aboutQtAct _ QAction("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        fileMenu _ self.menuBar().addMenu("&File")
        fileMenu.addAction(self.exitAct)
        self.menuBar().addSeparator()
        helpMenu _ self.menuBar().addMenu("&Help")
        helpMenu.addAction(self.aboutAct)
        helpMenu.addAction(self.aboutQtAct)

    ___ about(self):
        QMessageBox.about(self, "About Form Extractor",
                "The <b>Form Extractor</b> example demonstrates how to "
                "extract data from a web form using QtWebKit.")


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)

    mainWindow _ MainWindow()
    mainWindow.setWindowTitle("Form Extractor")
    mainWindow.s..

    sys.exit(app.exec_())
