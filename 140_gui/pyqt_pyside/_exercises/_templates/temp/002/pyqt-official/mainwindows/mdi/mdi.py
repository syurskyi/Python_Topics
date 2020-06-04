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


____ ?.?C.. ______ (QFile, QFileInfo, QPoint, QSettings, QSignalMapper,
        ?S.., QTextStream, __)
____ ?.?G.. ______ ?I.., ?KS..
____ ?.?W.. ______ (?A.., ?A.., ?FD.., ?MW..,
        QMdiArea, ?MB.., ?TE.., ?W..)

______ mdi_rc


c_ MdiChild(?TE..):
    sequenceNumber _ 1

    ___  -
        s__(MdiChild, self). - ()

        setAttribute(__.WA_DeleteOnClose)
        isUntitled _ T..

    ___ newFile
        isUntitled _ T..
        curFile _ "document%d.txt" % MdiChild.sequenceNumber
        MdiChild.sequenceNumber +_ 1
        sWT..(curFile + '[*]')

        document().contentsChanged.c..(documentWasModified)

    ___ loadFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..(QFile.ReadOnly | QFile.Text):
            ?MB...w..  "MDI",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            r_ F..

        instr _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        sPT..(instr.readAll())
        ?A...restoreOverrideCursor()

        setCurrentFile(fileName)

        document().contentsChanged.c..(documentWasModified)

        r_ T..

    ___ save
        __ isUntitled:
            r_ saveAs()
        ____
            r_ saveFile(curFile)

    ___ saveAs
        fileName, _ _ ?FD...getSaveFileName  "Save As", curFile)
        __ no. fileName:
            r_ F..

        r_ saveFile(fileName)

    ___ saveFile  fileName):
        file _ QFile(fileName)

        __ no. file.o..(QFile.WriteOnly | QFile.Text):
            ?MB...w..  "MDI",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            r_ F..

        outstr _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        outstr << toPlainText()
        ?A...restoreOverrideCursor()

        setCurrentFile(fileName)
        r_ T..

    ___ userFriendlyCurrentFile
        r_ strippedName(curFile)

    ___ currentFile
        r_ curFile

    ___ closeEvent  event):
        __ maybeSave
            event.accept()
        ____
            event.ignore()

    ___ documentWasModified
        setWindowModified(document().iM..())

    ___ maybeSave
        __ document().iM..
            ret _ ?MB...w..  "MDI",
                    "'%s' has been modified.\nDo you want to save your "
                    "changes?" % userFriendlyCurrentFile(),
                    ?MB...Save | ?MB...Discard | ?MB...Cancel)

            __ ret __ ?MB...Save:
                r_ save()

            __ ret __ ?MB...Cancel:
                r_ F..

        r_ T..

    ___ setCurrentFile  fileName):
        curFile _ QFileInfo(fileName).canonicalFilePath()
        isUntitled _ F..
        document().setModified F..
        setWindowModified F..
        sWT..(userFriendlyCurrentFile() + "[*]")

    ___ strippedName  fullFileName):
        r_ QFileInfo(fullFileName).fN..


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        mdiArea _ QMdiArea()
        mdiArea.setHorizontalScrollBarPolicy(__.ScrollBarAsNeeded)
        mdiArea.setVerticalScrollBarPolicy(__.ScrollBarAsNeeded)
        sCW..(mdiArea)

        mdiArea.subWindowActivated.c..(updateMenus)
        windowMapper _ QSignalMapper
        windowMapper.mapped[?W..].c..(setActiveSubWindow)

        createActions()
        createMenus()
        createToolBars()
        createStatusBar()
        updateMenus()

        readSettings()

        sWT..("MDI")

    ___ closeEvent  event):
        mdiArea.closeAllSubWindows()
        __ mdiArea.currentSubWindow
            event.ignore()
        ____
            writeSettings()
            event.accept()

    ___ newFile
        child _ createMdiChild()
        child.newFile()
        child.s..

    ___ o..
        fileName, _ _ ?FD...gOFN..
        __ fileName:
            existing _ findMdiChild(fileName)
            __ existing:
                mdiArea.setActiveSubWindow(existing)
                r_

            child _ createMdiChild()
            __ child.loadFile(fileName):
                sB.. .sM..("File loaded", 2000)
                child.s..
            ____
                child.c..

    ___ save
        __ activeMdiChild() and activeMdiChild().save
            sB.. .sM..("File saved", 2000)

    ___ saveAs
        __ activeMdiChild() and activeMdiChild().saveAs
            sB.. .sM..("File saved", 2000)

    ___ cut
        __ activeMdiChild
            activeMdiChild().cut()

    ___ copy
        __ activeMdiChild
            activeMdiChild().copy()

    ___ paste
        __ activeMdiChild
            activeMdiChild().paste()

    ___ about
        ?MB...about  "About MDI",
                "The <b>MDI</b> example demonstrates how to write multiple "
                "document interface applications using Qt.")

    ___ updateMenus
        hasMdiChild _ (activeMdiChild() __ no. N..)
        saveAct.sE..(hasMdiChild)
        saveAsAct.sE..(hasMdiChild)
        pasteAct.sE..(hasMdiChild)
        closeAct.sE..(hasMdiChild)
        closeAllAct.sE..(hasMdiChild)
        tileAct.sE..(hasMdiChild)
        cascadeAct.sE..(hasMdiChild)
        nextAct.sE..(hasMdiChild)
        previousAct.sE..(hasMdiChild)
        separatorAct.setVisible(hasMdiChild)

        hasSelection _ (activeMdiChild() __ no. N.. and
                        activeMdiChild().textCursor().hasSelection())
        cutAct.sE..(hasSelection)
        copyAct.sE..(hasSelection)

    ___ updateWindowMenu
        windowMenu.c..
        windowMenu.aA..(closeAct)
        windowMenu.aA..(closeAllAct)
        windowMenu.aS..)
        windowMenu.aA..(tileAct)
        windowMenu.aA..(cascadeAct)
        windowMenu.aS..)
        windowMenu.aA..(nextAct)
        windowMenu.aA..(previousAct)
        windowMenu.aA..(separatorAct)

        windows _ mdiArea.subWindowList()
        separatorAct.setVisible(le.(windows) !_ 0)

        ___ i, window __ en..(windows):
            child _ window.widget()

            t__ _ "%d %s" % (i + 1, child.userFriendlyCurrentFile())
            __ i < 9:
                t__ _ '&' + t__

            action _ windowMenu.aA..(t__)
            action.setCheckable( st.
            action.sC__(child __ activeMdiChild())
            action.t__.c..(windowMapper.map)
            windowMapper.setMapping(action, window)

    ___ createMdiChild
        child _ MdiChild()
        mdiArea.addSubWindow(child)

        child.copyAvailable.c..(cutAct.sE..)
        child.copyAvailable.c..(copyAct.sE..)

        r_ child

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

        exitAct _ ?A..("E&xit", self, shortcut_QKeySequence.Quit,
                statusTip_"Exit the application",
                triggered_QApplication.i.. .closeAllWindows)

        cutAct _ ?A..(?I..(':/images/cut.png'), "Cu&t", self,
                shortcut_QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_self.cut)

        copyAct _ ?A..(?I..(':/images/copy.png'), "&Copy", self,
                shortcut_QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_self.copy)

        pasteAct _ ?A..(?I..(':/images/paste.png'), "&Paste", self,
                shortcut_QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_self.paste)

        closeAct _ ?A..("Cl&ose", self,
                statusTip_"Close the active window",
                triggered_self.mdiArea.closeActiveSubWindow)

        closeAllAct _ ?A..("Close &All", self,
                statusTip_"Close all the windows",
                triggered_self.mdiArea.closeAllSubWindows)

        tileAct _ ?A..("&Tile", self, statusTip_"Tile the windows",
                triggered_self.mdiArea.tileSubWindows)

        cascadeAct _ ?A..("&Cascade", self,
                statusTip_"Cascade the windows",
                triggered_self.mdiArea.cascadeSubWindows)

        nextAct _ ?A..("Ne&xt", self, shortcut_QKeySequence.NextChild,
                statusTip_"Move the focus to the next window",
                triggered_self.mdiArea.activateNextSubWindow)

        previousAct _ ?A..("Pre&vious", self,
                shortcut_QKeySequence.PreviousChild,
                statusTip_"Move the focus to the previous window",
                triggered_self.mdiArea.activatePreviousSubWindow)

        separatorAct _ ?A..
        separatorAct.setSeparator( st.

        aboutAct _ ?A..("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.i.. .aboutQt)

    ___ createMenus
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(newAct)
        fileMenu.aA..(openAct)
        fileMenu.aA..(saveAct)
        fileMenu.aA..(saveAsAct)
        fileMenu.aS..)
        action _ fileMenu.aA..("Switch layout direction")
        action.t__.c..(switchLayoutDirection)
        fileMenu.aA..(exitAct)

        editMenu _ mB.. .aM..("&Edit")
        editMenu.aA..(cutAct)
        editMenu.aA..(copyAct)
        editMenu.aA..(pasteAct)

        windowMenu _ mB.. .aM..("&Window")
        updateWindowMenu()
        windowMenu.aboutToShow.c..(updateWindowMenu)

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
        settings _ QSettings('Trolltech', 'MDI Example')
        pos _ settings.value('pos', QPoint(200, 200))
        size _ settings.value('size', ?S..(400, 400))
        move(pos)
        r..(size)

    ___ writeSettings
        settings _ QSettings('Trolltech', 'MDI Example')
        settings.sV..('pos', pos())
        settings.sV..('size', size())

    ___ activeMdiChild
        activeSubWindow _ mdiArea.activeSubWindow()
        __ activeSubWindow:
            r_ activeSubWindow.widget()
        r_ N..

    ___ findMdiChild  fileName):
        canonicalFilePath _ QFileInfo(fileName).canonicalFilePath()

        ___ window __ mdiArea.subWindowList
            __ window.widget().currentFile() __ canonicalFilePath:
                r_ window
        r_ N..

    ___ switchLayoutDirection
        __ layoutDirection() __ __.LeftToRight:
            ?A...setLayoutDirection(__.RightToLeft)
        ____
            ?A...setLayoutDirection(__.LeftToRight)

    ___ setActiveSubWindow  window):
        __ window:
            mdiArea.setActiveSubWindow(window)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    mainWin _ MainWindow()
    mainWin.s..
    ___.e.. ?.e..
