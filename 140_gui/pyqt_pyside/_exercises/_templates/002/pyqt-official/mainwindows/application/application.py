#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2014 Riverbank Computing Limited.
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


____ ?.?C.. ______ (QFile, QFileInfo, QPoint, QRect, QSettings, ?S..,
        __, QTextStream)
____ ?.?G.. ______ ?I.., ?KS..
____ ?.?W.. ______ (?A.., ?A.., ?FD.., ?MW..,
        ?MB.., ?TE..)


c_ MainWindow ?MW..
    ___  -  
        s__(MainWindow, self). - ()

        curFile _ ''

        textEdit _ ?TE..()
        sCW..(textEdit)

        createActions()
        createMenus()
        createToolBars()
        createStatusBar()

        readSettings()

        textEdit.document().contentsChanged.c..(documentWasModified)

        setCurrentFile('')

    ___ closeEvent  event):
        __ maybeSave
            writeSettings()
            event.accept()
        ____
            event.ignore()

    ___ newFile 
        __ maybeSave
            textEdit.c..
            setCurrentFile('')

    ___ o.. 
        __ maybeSave
            fileName, _ _ ?FD...gOFN..
            __ fileName:
                loadFile(fileName)

    ___ save 
        __ curFile:
            r_ saveFile(curFile)

        r_ saveAs()

    ___ saveAs 
        fileName, _ _ ?FD...getSaveFileName
        __ fileName:
            r_ saveFile(fileName)

        r_ F..

    ___ about 
        ?MB...about  "About Application",
                "The <b>Application</b> example demonstrates how to write "
                "modern GUI applications using Qt, with a menu bar, "
                "toolbars, and a status bar.")

    ___ documentWasModified 
        setWindowModified(textEdit.document().iM..())

    ___ createActions 
        root _ QFileInfo(__file__).absolutePath()

        newAct _ ?A..(?I..(root + '/images/new.png'), "&New", self,
                shortcut_QKeySequence.New, statusTip_"Create a new file",
                triggered_self.newFile)

        openAct _ ?A..(?I..(root + '/images/open.png'), "&Open...",
                self, shortcut_QKeySequence.Open,
                statusTip_"Open an existing file", triggered_self.o..)

        saveAct _ ?A..(?I..(root + '/images/save.png'), "&Save", self,
                shortcut_QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_self.save)

        saveAsAct _ ?A..("Save &As...", self,
                shortcut_QKeySequence.SaveAs,
                statusTip_"Save the document under a new name",
                triggered_self.saveAs)

        exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application", triggered_self.close)

        cutAct _ ?A..(?I..(root + '/images/cut.png'), "Cu&t", self,
                shortcut_QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_self.textEdit.cut)

        copyAct _ ?A..(?I..(root + '/images/copy.png'), "&Copy", self,
                shortcut_QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_self.textEdit.copy)

        pasteAct _ ?A..(?I..(root + '/images/paste.png'), "&Paste",
                self, shortcut_QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_self.textEdit.paste)

        aboutAct _ ?A..("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.i.. .aboutQt)

        cutAct.sE.. F..
        copyAct.sE.. F..
        textEdit.copyAvailable.c..(cutAct.sE..)
        textEdit.copyAvailable.c..(copyAct.sE..)

    ___ createMenus 
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(newAct)
        fileMenu.aA..(openAct)
        fileMenu.aA..(saveAct)
        fileMenu.aA..(saveAsAct)
        fileMenu.aS..);
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
        settings _ QSettings("Trolltech", "Application Example")
        pos _ settings.value("pos", QPoint(200, 200))
        size _ settings.value("size", ?S..(400, 400))
        r..(size)
        move(pos)

    ___ writeSettings 
        settings _ QSettings("Trolltech", "Application Example")
        settings.sV..("pos", pos())
        settings.sV..("size", size())

    ___ maybeSave 
        __ textEdit.document().iM..
            ret _ ?MB...w..  "Application",
                    "The document has been modified.\nDo you want to save "
                    "your changes?",
                    ?MB...Save | ?MB...Discard | ?MB...Cancel)

            __ ret __ ?MB...Save:
                r_ save()

            __ ret __ ?MB...Cancel:
                r_ F..

        r_ T..

    ___ loadFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..(QFile.ReadOnly | QFile.Text):
            ?MB...w..  "Application",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            r_

        inf _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        textEdit.sPT..(inf.readAll())
        ?A...restoreOverrideCursor()

        setCurrentFile(fileName)
        sB.. .sM..("File loaded", 2000)

    ___ saveFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..(QFile.WriteOnly | QFile.Text):
            ?MB...w..  "Application",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            r_ F..

        outf _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        outf << textEdit.toPlainText()
        ?A...restoreOverrideCursor()

        setCurrentFile(fileName);
        sB.. .sM..("File saved", 2000)
        r_ T..

    ___ setCurrentFile  fileName):
        curFile _ fileName
        textEdit.document().setModified F..
        setWindowModified F..

        __ curFile:
            shownName _ strippedName(curFile)
        ____
            shownName _ 'untitled.txt'

        sWT..("%s[*] - Application" % shownName)

    ___ strippedName  fullFileName):
        r_ QFileInfo(fullFileName).fN..


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    mainWin _ MainWindow()
    mainWin.s..
    ___.e.. ?.e..
