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
        QSize, QTextStream, __)
____ ?.?G.. ______ QIcon, ?KS..
____ ?.?W.. ______ (?A.., ?A.., ?FD.., QMainWindow,
        QMdiArea, ?MB.., QTextEdit, QWidget)

______ mdi_rc


c_ MdiChild(QTextEdit):
    sequenceNumber _ 1

    ___ __init__(self):
        super(MdiChild, self).__init__()

        self.setAttribute(__.WA_DeleteOnClose)
        self.isUntitled _ True

    ___ newFile(self):
        self.isUntitled _ True
        self.curFile _ "document%d.txt" % MdiChild.sequenceNumber
        MdiChild.sequenceNumber +_ 1
        self.setWindowTitle(self.curFile + '[*]')

        self.document().contentsChanged.c..(self.documentWasModified)

    ___ loadFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..(QFile.ReadOnly | QFile.Text):
            ?MB...warning  "MDI",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            r_ False

        instr _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        self.sPT..(instr.readAll())
        ?A...restoreOverrideCursor()

        self.setCurrentFile(fileName)

        self.document().contentsChanged.c..(self.documentWasModified)

        r_ True

    ___ save(self):
        __ self.isUntitled:
            r_ self.saveAs()
        ____
            r_ self.saveFile(self.curFile)

    ___ saveAs(self):
        fileName, _ _ ?FD...getSaveFileName  "Save As", self.curFile)
        __ no. fileName:
            r_ False

        r_ self.saveFile(fileName)

    ___ saveFile  fileName):
        file _ QFile(fileName)

        __ no. file.o..(QFile.WriteOnly | QFile.Text):
            ?MB...warning  "MDI",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            r_ False

        outstr _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        outstr << self.toPlainText()
        ?A...restoreOverrideCursor()

        self.setCurrentFile(fileName)
        r_ True

    ___ userFriendlyCurrentFile(self):
        r_ self.strippedName(self.curFile)

    ___ currentFile(self):
        r_ self.curFile

    ___ closeEvent  event):
        __ self.maybeSave
            event.accept()
        ____
            event.ignore()

    ___ documentWasModified(self):
        self.setWindowModified(self.document().iM..())

    ___ maybeSave(self):
        __ self.document().iM..
            ret _ ?MB...warning  "MDI",
                    "'%s' has been modified.\nDo you want to save your "
                    "changes?" % self.userFriendlyCurrentFile(),
                    ?MB...Save | ?MB...Discard | ?MB...Cancel)

            __ ret == ?MB...Save:
                r_ self.save()

            __ ret == ?MB...Cancel:
                r_ False

        r_ True

    ___ setCurrentFile  fileName):
        self.curFile _ QFileInfo(fileName).canonicalFilePath()
        self.isUntitled _ False
        self.document().setModified F..
        self.setWindowModified F..
        self.setWindowTitle(self.userFriendlyCurrentFile() + "[*]")

    ___ strippedName  fullFileName):
        r_ QFileInfo(fullFileName).fileName()


c_ MainWindow ?MW..
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.mdiArea _ QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(__.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(__.ScrollBarAsNeeded)
        self.sCW..(self.mdiArea)

        self.mdiArea.subWindowActivated.c..(self.updateMenus)
        self.windowMapper _ QSignalMapper(self)
        self.windowMapper.mapped[QWidget].c..(self.setActiveSubWindow)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.updateMenus()

        self.readSettings()

        self.setWindowTitle("MDI")

    ___ closeEvent  event):
        self.mdiArea.closeAllSubWindows()
        __ self.mdiArea.currentSubWindow
            event.ignore()
        ____
            self.writeSettings()
            event.accept()

    ___ newFile(self):
        child _ self.createMdiChild()
        child.newFile()
        child.s..

    ___ o..(self):
        fileName, _ _ ?FD...gOFN..(self)
        __ fileName:
            existing _ self.findMdiChild(fileName)
            __ existing:
                self.mdiArea.setActiveSubWindow(existing)
                r_

            child _ self.createMdiChild()
            __ child.loadFile(fileName):
                self.statusBar().showMessage("File loaded", 2000)
                child.s..
            ____
                child.close()

    ___ save(self):
        __ self.activeMdiChild() and self.activeMdiChild().save
            self.statusBar().showMessage("File saved", 2000)

    ___ saveAs(self):
        __ self.activeMdiChild() and self.activeMdiChild().saveAs
            self.statusBar().showMessage("File saved", 2000)

    ___ cut(self):
        __ self.activeMdiChild
            self.activeMdiChild().cut()

    ___ copy(self):
        __ self.activeMdiChild
            self.activeMdiChild().copy()

    ___ paste(self):
        __ self.activeMdiChild
            self.activeMdiChild().paste()

    ___ about(self):
        ?MB...about  "About MDI",
                "The <b>MDI</b> example demonstrates how to write multiple "
                "document interface applications using Qt.")

    ___ updateMenus(self):
        hasMdiChild _ (self.activeMdiChild() __ no. N..)
        self.saveAct.setEnabled(hasMdiChild)
        self.saveAsAct.setEnabled(hasMdiChild)
        self.pasteAct.setEnabled(hasMdiChild)
        self.closeAct.setEnabled(hasMdiChild)
        self.closeAllAct.setEnabled(hasMdiChild)
        self.tileAct.setEnabled(hasMdiChild)
        self.cascadeAct.setEnabled(hasMdiChild)
        self.nextAct.setEnabled(hasMdiChild)
        self.previousAct.setEnabled(hasMdiChild)
        self.separatorAct.setVisible(hasMdiChild)

        hasSelection _ (self.activeMdiChild() __ no. N.. and
                        self.activeMdiChild().textCursor().hasSelection())
        self.cutAct.setEnabled(hasSelection)
        self.copyAct.setEnabled(hasSelection)

    ___ updateWindowMenu(self):
        self.windowMenu.clear()
        self.windowMenu.aA..(self.closeAct)
        self.windowMenu.aA..(self.closeAllAct)
        self.windowMenu.addSeparator()
        self.windowMenu.aA..(self.tileAct)
        self.windowMenu.aA..(self.cascadeAct)
        self.windowMenu.addSeparator()
        self.windowMenu.aA..(self.nextAct)
        self.windowMenu.aA..(self.previousAct)
        self.windowMenu.aA..(self.separatorAct)

        windows _ self.mdiArea.subWindowList()
        self.separatorAct.setVisible(le.(windows) !_ 0)

        for i, window in enumerate(windows):
            child _ window.widget()

            t__ _ "%d %s" % (i + 1, child.userFriendlyCurrentFile())
            __ i < 9:
                t__ _ '&' + t__

            action _ self.windowMenu.aA..(t__)
            action.setCheckable(True)
            action.setChecked(child __ self.activeMdiChild())
            action.t__.c..(self.windowMapper.map)
            self.windowMapper.setMapping(action, window)

    ___ createMdiChild(self):
        child _ MdiChild()
        self.mdiArea.addSubWindow(child)

        child.copyAvailable.c..(self.cutAct.setEnabled)
        child.copyAvailable.c..(self.copyAct.setEnabled)

        r_ child

    ___ createActions(self):
        self.newAct _ ?A..(QIcon(':/images/new.png'), "&New", self,
                shortcut_QKeySequence.New, statusTip_"Create a new file",
                triggered_self.newFile)

        self.openAct _ ?A..(QIcon(':/images/open.png'), "&Open...", self,
                shortcut_QKeySequence.Open, statusTip_"Open an existing file",
                triggered_self.o..)

        self.saveAct _ ?A..(QIcon(':/images/save.png'), "&Save", self,
                shortcut_QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_self.save)

        self.saveAsAct _ ?A..("Save &As...", self,
                shortcut_QKeySequence.SaveAs,
                statusTip_"Save the document under a new name",
                triggered_self.saveAs)

        self.exitAct _ ?A..("E&xit", self, shortcut_QKeySequence.Quit,
                statusTip_"Exit the application",
                triggered_QApplication.instance().closeAllWindows)

        self.cutAct _ ?A..(QIcon(':/images/cut.png'), "Cu&t", self,
                shortcut_QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_self.cut)

        self.copyAct _ ?A..(QIcon(':/images/copy.png'), "&Copy", self,
                shortcut_QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_self.copy)

        self.pasteAct _ ?A..(QIcon(':/images/paste.png'), "&Paste", self,
                shortcut_QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_self.paste)

        self.closeAct _ ?A..("Cl&ose", self,
                statusTip_"Close the active window",
                triggered_self.mdiArea.closeActiveSubWindow)

        self.closeAllAct _ ?A..("Close &All", self,
                statusTip_"Close all the windows",
                triggered_self.mdiArea.closeAllSubWindows)

        self.tileAct _ ?A..("&Tile", self, statusTip_"Tile the windows",
                triggered_self.mdiArea.tileSubWindows)

        self.cascadeAct _ ?A..("&Cascade", self,
                statusTip_"Cascade the windows",
                triggered_self.mdiArea.cascadeSubWindows)

        self.nextAct _ ?A..("Ne&xt", self, shortcut_QKeySequence.NextChild,
                statusTip_"Move the focus to the next window",
                triggered_self.mdiArea.activateNextSubWindow)

        self.previousAct _ ?A..("Pre&vious", self,
                shortcut_QKeySequence.PreviousChild,
                statusTip_"Move the focus to the previous window",
                triggered_self.mdiArea.activatePreviousSubWindow)

        self.separatorAct _ ?A..(self)
        self.separatorAct.setSeparator(True)

        self.aboutAct _ ?A..("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        self.aboutQtAct _ ?A..("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.fileMenu _ self.mB.. .aM..("&File")
        self.fileMenu.aA..(self.newAct)
        self.fileMenu.aA..(self.openAct)
        self.fileMenu.aA..(self.saveAct)
        self.fileMenu.aA..(self.saveAsAct)
        self.fileMenu.addSeparator()
        action _ self.fileMenu.aA..("Switch layout direction")
        action.t__.c..(self.switchLayoutDirection)
        self.fileMenu.aA..(self.exitAct)

        self.editMenu _ self.mB.. .aM..("&Edit")
        self.editMenu.aA..(self.cutAct)
        self.editMenu.aA..(self.copyAct)
        self.editMenu.aA..(self.pasteAct)

        self.windowMenu _ self.mB.. .aM..("&Window")
        self.updateWindowMenu()
        self.windowMenu.aboutToShow.c..(self.updateWindowMenu)

        self.mB.. .addSeparator()

        self.helpMenu _ self.mB.. .aM..("&Help")
        self.helpMenu.aA..(self.aboutAct)
        self.helpMenu.aA..(self.aboutQtAct)

    ___ createToolBars(self):
        self.fileToolBar _ self.addToolBar("File")
        self.fileToolBar.aA..(self.newAct)
        self.fileToolBar.aA..(self.openAct)
        self.fileToolBar.aA..(self.saveAct)

        self.editToolBar _ self.addToolBar("Edit")
        self.editToolBar.aA..(self.cutAct)
        self.editToolBar.aA..(self.copyAct)
        self.editToolBar.aA..(self.pasteAct)

    ___ createStatusBar(self):
        self.statusBar().showMessage("Ready")

    ___ readSettings(self):
        settings _ QSettings('Trolltech', 'MDI Example')
        pos _ settings.value('pos', QPoint(200, 200))
        size _ settings.value('size', QSize(400, 400))
        self.move(pos)
        self.resize(size)

    ___ writeSettings(self):
        settings _ QSettings('Trolltech', 'MDI Example')
        settings.setValue('pos', self.pos())
        settings.setValue('size', self.size())

    ___ activeMdiChild(self):
        activeSubWindow _ self.mdiArea.activeSubWindow()
        __ activeSubWindow:
            r_ activeSubWindow.widget()
        r_ N..

    ___ findMdiChild  fileName):
        canonicalFilePath _ QFileInfo(fileName).canonicalFilePath()

        for window in self.mdiArea.subWindowList
            __ window.widget().currentFile() == canonicalFilePath:
                r_ window
        r_ N..

    ___ switchLayoutDirection(self):
        __ self.layoutDirection() == __.LeftToRight:
            ?A...setLayoutDirection(__.RightToLeft)
        ____
            ?A...setLayoutDirection(__.LeftToRight)

    ___ setActiveSubWindow  window):
        __ window:
            self.mdiArea.setActiveSubWindow(window)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
