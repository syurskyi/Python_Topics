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


____ ?.?C.. ______ (QFile, QFileInfo, QPoint, QSettings, ?S.., __,
        QTextStream)
____ ?.?G.. ______ ?I.., ?KS..
____ ?.?W.. ______ (?A.., ?A.., ?FD.., ?MW..,
        ?MB.., ?TE..)

______ sdi_rc


c_ MainWindow ?MW..
    sequenceNumber _ 1
    windowList _   # list

    ___  -   fileName_None):
        s__(MainWindow, self). - ()

        init()
        __ fileName:
            loadFile(fileName)
        ____
            setCurrentFile('')

    ___ closeEvent  event):
        __ maybeSave
            writeSettings()
            event.accept()
        ____
            event.ignore()

    ___ newFile
        other _ MainWindow()
        MainWindow.windowList.ap..(other)
        other.move(x() + 40, y() + 40)
        other.s..

    ___ o..
        fileName, _ _ ?FD...gOFN..
        __ fileName:
            existing _ findMainWindow(fileName)
            __ existing:
                existing.s..
                existing.raise_()
                existing.activateWindow()
                r_

            __ isUntitled and textEdit.document().isEmpty() and no. isWindowModified
                loadFile(fileName)
            ____
                other _ MainWindow(fileName)
                __ other.isUntitled:
                    del other
                    r_

                MainWindow.windowList.ap..(other)
                other.move(x() + 40, y() + 40)
                other.s..

    ___ save
        __ isUntitled:
            r_ saveAs()
        ____
            r_ saveFile(curFile)

    ___ saveAs
        fileName, _ _ ?FD...getSaveFileName  "Save As",
                curFile)
        __ no. fileName:
            r_ F..

        r_ saveFile(fileName)

    ___ about
        ?MB...about  "About SDI",
                "The <b>SDI</b> example demonstrates how to write single "
                "document interface applications using Qt.")

    ___ documentWasModified
        setWindowModified( st.

    ___ init
        setAttribute(__.WA_DeleteOnClose)
        isUntitled _ T..
        textEdit _ ?TE..()
        sCW..(textEdit)

        createActions()
        createMenus()
        createToolBars()
        createStatusBar()

        readSettings()

        textEdit.document().contentsChanged.c..(documentWasModified)

    ___ createActions
        newAct _ ?A..(?I..(':/images/new.png'), "&New", self,
                shortcut_QKeySequence.New, statusTip_"Create a new file",
                triggered_self.newFile)

        openAct _ ?A..(?I..(':/images/open.png'), "&Open...", self,
                shortcut_QKeySequence.Open, statusTip_"Open an existing file",
                triggered_self.o..)

        saveAct _ ?A..(?I..(':/images/save.png'), "&Save", self,
                shortcut_QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_self.save)

        saveAsAct _ ?A..("Save &As...", self,
                shortcut_QKeySequence.SaveAs,
                statusTip_"Save the document under a new name",
                triggered_self.saveAs)

        closeAct _ ?A..("&Close", self, shortcut_"Ctrl+W",
                statusTip_"Close this window", triggered_self.close)

        exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application",
                triggered_QApplication.i.. .closeAllWindows)

        cutAct _ ?A..(?I..(':/images/cut.png'), "Cu&t", self,
                enabled_False, shortcut_QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_self.textEdit.cut)

        copyAct _ ?A..(?I..(':/images/copy.png'), "&Copy", self,
                enabled_False, shortcut_QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_self.textEdit.copy)

        pasteAct _ ?A..(?I..(':/images/paste.png'), "&Paste", self,
                shortcut_QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_self.textEdit.paste)

        aboutAct _ ?A..("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.i.. .aboutQt)

        textEdit.copyAvailable.c..(cutAct.sE..)
        textEdit.copyAvailable.c..(copyAct.sE..)

    ___ createMenus
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(newAct)
        fileMenu.aA..(openAct)
        fileMenu.aA..(saveAct)
        fileMenu.aA..(saveAsAct)
        fileMenu.aS..)
        fileMenu.aA..(closeAct)
        fileMenu.aA..(exitAct)

        editMenu _ mB.. .aM..("&Edit")
        editMenu.aA..(cutAct)
        editMenu.aA..(copyAct)
        editMenu.aA..(pasteAct)

        mB.. .aS..)

        helpMenu _ mB.. .aM..("&Help")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ createToolBars
        fileToolBar _ aTB..("File")
        fileToolBar.aA..(newAct)
        fileToolBar.aA..(openAct)
        fileToolBar.aA..(saveAct)

        editToolBar _ aTB..("Edit")
        editToolBar.aA..(cutAct)
        editToolBar.aA..(copyAct)
        editToolBar.aA..(pasteAct)

    ___ createStatusBar
        sB.. .sM..("Ready")

    ___ readSettings
        settings _ QSettings('Trolltech', 'SDI Example')
        pos _ settings.value('pos', QPoint(200, 200))
        size _ settings.value('size', ?S..(400, 400))
        move(pos)
        r..(size)

    ___ writeSettings
        settings _ QSettings('Trolltech', 'SDI Example')
        settings.sV..('pos', pos())
        settings.sV..('size', size())

    ___ maybeSave
        __ textEdit.document().iM..
            ret _ ?MB...w..  "SDI",
                    "The document has been modified.\nDo you want to save "
                    "your changes?",
                    ?MB...Save | ?MB...Discard |
                    ?MB...Cancel)

            __ ret __ ?MB...Save:
                r_ save()

            __ ret __ ?MB...Cancel:
                r_ F..

        r_ T..

    ___ loadFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..(QFile.ReadOnly | QFile.Text):
            ?MB...w..  "SDI",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            r_

        instr _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        textEdit.sPT..(instr.readAll())
        ?A...restoreOverrideCursor()

        setCurrentFile(fileName)
        sB.. .sM..("File loaded", 2000)

    ___ saveFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..(QFile.WriteOnly | QFile.Text):
            ?MB...w..  "SDI",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            r_ F..

        outstr _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        outstr << textEdit.toPlainText()
        ?A...restoreOverrideCursor()

        setCurrentFile(fileName)
        sB.. .sM..("File saved", 2000)
        r_ T..

    ___ setCurrentFile  fileName):
        isUntitled _ no. fileName
        __ isUntitled:
            curFile _ "document%d.txt" % MainWindow.sequenceNumber
            MainWindow.sequenceNumber +_ 1
        ____
            curFile _ QFileInfo(fileName).canonicalFilePath()

        textEdit.document().setModified F..
        setWindowModified F..

        sWT..("%s[*] - SDI" % strippedName(curFile))

    ___ strippedName  fullFileName):
        r_ QFileInfo(fullFileName).fN..

    ___ findMainWindow  fileName):
        canonicalFilePath _ QFileInfo(fileName).canonicalFilePath()

        ___ widget __ ?A...i.. .topLevelWidgets
            __ isinstance(widget, MainWindow) and widget.curFile __ canonicalFilePath:
                r_ widget

        r_ N..


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    mainWin _ MainWindow()
    mainWin.s..
    ___.e.. ?.e..
