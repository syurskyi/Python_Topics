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


____ ?.QtCore ______ (QFile, QFileInfo, QPoint, QSettings, QSignalMapper,
        QSize, QTextStream, Qt)
____ ?.QtGui ______ QIcon, QKeySequence
____ ?.?W.. ______ (QAction, ?A.., QFileDialog, QMainWindow,
        QMdiArea, QMessageBox, QTextEdit, QWidget)

______ mdi_rc


class MdiChild(QTextEdit):
    sequenceNumber _ 1

    ___ __init__(self):
        super(MdiChild, self).__init__()

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.isUntitled _ True

    ___ newFile(self):
        self.isUntitled _ True
        self.curFile _ "document%d.txt" % MdiChild.sequenceNumber
        MdiChild.sequenceNumber +_ 1
        self.setWindowTitle(self.curFile + '[*]')

        self.document().contentsChanged.c..(self.documentWasModified)

    ___ loadFile(self, fileName):
        file _ QFile(fileName)
        if not file.open(QFile.ReadOnly | QFile.Text):
            QMessageBox.warning(self, "MDI",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            return False

        instr _ QTextStream(file)
        ?A...setOverrideCursor(Qt.WaitCursor)
        self.setPlainText(instr.readAll())
        ?A...restoreOverrideCursor()

        self.setCurrentFile(fileName)

        self.document().contentsChanged.c..(self.documentWasModified)

        return True

    ___ save(self):
        if self.isUntitled:
            return self.saveAs()
        else:
            return self.saveFile(self.curFile)

    ___ saveAs(self):
        fileName, _ _ QFileDialog.getSaveFileName(self, "Save As", self.curFile)
        if not fileName:
            return False

        return self.saveFile(fileName)

    ___ saveFile(self, fileName):
        file _ QFile(fileName)

        if not file.open(QFile.WriteOnly | QFile.Text):
            QMessageBox.warning(self, "MDI",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            return False

        outstr _ QTextStream(file)
        ?A...setOverrideCursor(Qt.WaitCursor)
        outstr << self.toPlainText()
        ?A...restoreOverrideCursor()

        self.setCurrentFile(fileName)
        return True

    ___ userFriendlyCurrentFile(self):
        return self.strippedName(self.curFile)

    ___ currentFile(self):
        return self.curFile

    ___ closeEvent(self, event):
        if self.maybeSave
            event.accept()
        else:
            event.ignore()

    ___ documentWasModified(self):
        self.setWindowModified(self.document().isModified())

    ___ maybeSave(self):
        if self.document().isModified
            ret _ QMessageBox.warning(self, "MDI",
                    "'%s' has been modified.\nDo you want to save your "
                    "changes?" % self.userFriendlyCurrentFile(),
                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

            if ret == QMessageBox.Save:
                return self.save()

            if ret == QMessageBox.Cancel:
                return False

        return True

    ___ setCurrentFile(self, fileName):
        self.curFile _ QFileInfo(fileName).canonicalFilePath()
        self.isUntitled _ False
        self.document().setModified(False)
        self.setWindowModified(False)
        self.setWindowTitle(self.userFriendlyCurrentFile() + "[*]")

    ___ strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.mdiArea _ QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)

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

    ___ closeEvent(self, event):
        self.mdiArea.closeAllSubWindows()
        if self.mdiArea.currentSubWindow
            event.ignore()
        else:
            self.writeSettings()
            event.accept()

    ___ newFile(self):
        child _ self.createMdiChild()
        child.newFile()
        child.s..

    ___ open(self):
        fileName, _ _ QFileDialog.getOpenFileName(self)
        if fileName:
            existing _ self.findMdiChild(fileName)
            if existing:
                self.mdiArea.setActiveSubWindow(existing)
                return

            child _ self.createMdiChild()
            if child.loadFile(fileName):
                self.statusBar().showMessage("File loaded", 2000)
                child.s..
            else:
                child.close()

    ___ save(self):
        if self.activeMdiChild() and self.activeMdiChild().save
            self.statusBar().showMessage("File saved", 2000)

    ___ saveAs(self):
        if self.activeMdiChild() and self.activeMdiChild().saveAs
            self.statusBar().showMessage("File saved", 2000)

    ___ cut(self):
        if self.activeMdiChild
            self.activeMdiChild().cut()

    ___ copy(self):
        if self.activeMdiChild
            self.activeMdiChild().copy()

    ___ paste(self):
        if self.activeMdiChild
            self.activeMdiChild().paste()

    ___ about(self):
        QMessageBox.about(self, "About MDI",
                "The <b>MDI</b> example demonstrates how to write multiple "
                "document interface applications using Qt.")

    ___ updateMenus(self):
        hasMdiChild _ (self.activeMdiChild() is not None)
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

        hasSelection _ (self.activeMdiChild() is not None and
                        self.activeMdiChild().textCursor().hasSelection())
        self.cutAct.setEnabled(hasSelection)
        self.copyAct.setEnabled(hasSelection)

    ___ updateWindowMenu(self):
        self.windowMenu.clear()
        self.windowMenu.addAction(self.closeAct)
        self.windowMenu.addAction(self.closeAllAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.tileAct)
        self.windowMenu.addAction(self.cascadeAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.nextAct)
        self.windowMenu.addAction(self.previousAct)
        self.windowMenu.addAction(self.separatorAct)

        windows _ self.mdiArea.subWindowList()
        self.separatorAct.setVisible(len(windows) !_ 0)

        for i, window in enumerate(windows):
            child _ window.widget()

            text _ "%d %s" % (i + 1, child.userFriendlyCurrentFile())
            if i < 9:
                text _ '&' + text

            action _ self.windowMenu.addAction(text)
            action.setCheckable(True)
            action.setChecked(child is self.activeMdiChild())
            action.triggered.c..(self.windowMapper.map)
            self.windowMapper.setMapping(action, window)

    ___ createMdiChild(self):
        child _ MdiChild()
        self.mdiArea.addSubWindow(child)

        child.copyAvailable.c..(self.cutAct.setEnabled)
        child.copyAvailable.c..(self.copyAct.setEnabled)

        return child

    ___ createActions(self):
        self.newAct _ QAction(QIcon(':/images/new.png'), "&New", self,
                shortcut_QKeySequence.New, statusTip_"Create a new file",
                triggered_self.newFile)

        self.openAct _ QAction(QIcon(':/images/open.png'), "&Open...", self,
                shortcut_QKeySequence.Open, statusTip_"Open an existing file",
                triggered_self.open)

        self.saveAct _ QAction(QIcon(':/images/save.png'), "&Save", self,
                shortcut_QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_self.save)

        self.saveAsAct _ QAction("Save &As...", self,
                shortcut_QKeySequence.SaveAs,
                statusTip_"Save the document under a new name",
                triggered_self.saveAs)

        self.exitAct _ QAction("E&xit", self, shortcut_QKeySequence.Quit,
                statusTip_"Exit the application",
                triggered_QApplication.instance().closeAllWindows)

        self.cutAct _ QAction(QIcon(':/images/cut.png'), "Cu&t", self,
                shortcut_QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_self.cut)

        self.copyAct _ QAction(QIcon(':/images/copy.png'), "&Copy", self,
                shortcut_QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_self.copy)

        self.pasteAct _ QAction(QIcon(':/images/paste.png'), "&Paste", self,
                shortcut_QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_self.paste)

        self.closeAct _ QAction("Cl&ose", self,
                statusTip_"Close the active window",
                triggered_self.mdiArea.closeActiveSubWindow)

        self.closeAllAct _ QAction("Close &All", self,
                statusTip_"Close all the windows",
                triggered_self.mdiArea.closeAllSubWindows)

        self.tileAct _ QAction("&Tile", self, statusTip_"Tile the windows",
                triggered_self.mdiArea.tileSubWindows)

        self.cascadeAct _ QAction("&Cascade", self,
                statusTip_"Cascade the windows",
                triggered_self.mdiArea.cascadeSubWindows)

        self.nextAct _ QAction("Ne&xt", self, shortcut_QKeySequence.NextChild,
                statusTip_"Move the focus to the next window",
                triggered_self.mdiArea.activateNextSubWindow)

        self.previousAct _ QAction("Pre&vious", self,
                shortcut_QKeySequence.PreviousChild,
                statusTip_"Move the focus to the previous window",
                triggered_self.mdiArea.activatePreviousSubWindow)

        self.separatorAct _ QAction(self)
        self.separatorAct.setSeparator(True)

        self.aboutAct _ QAction("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        self.aboutQtAct _ QAction("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.fileMenu _ self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addSeparator()
        action _ self.fileMenu.addAction("Switch layout direction")
        action.triggered.c..(self.switchLayoutDirection)
        self.fileMenu.addAction(self.exitAct)

        self.editMenu _ self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)

        self.windowMenu _ self.menuBar().addMenu("&Window")
        self.updateWindowMenu()
        self.windowMenu.aboutToShow.c..(self.updateWindowMenu)

        self.menuBar().addSeparator()

        self.helpMenu _ self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    ___ createToolBars(self):
        self.fileToolBar _ self.addToolBar("File")
        self.fileToolBar.addAction(self.newAct)
        self.fileToolBar.addAction(self.openAct)
        self.fileToolBar.addAction(self.saveAct)

        self.editToolBar _ self.addToolBar("Edit")
        self.editToolBar.addAction(self.cutAct)
        self.editToolBar.addAction(self.copyAct)
        self.editToolBar.addAction(self.pasteAct)

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
        if activeSubWindow:
            return activeSubWindow.widget()
        return None

    ___ findMdiChild(self, fileName):
        canonicalFilePath _ QFileInfo(fileName).canonicalFilePath()

        for window in self.mdiArea.subWindowList
            if window.widget().currentFile() == canonicalFilePath:
                return window
        return None

    ___ switchLayoutDirection(self):
        if self.layoutDirection() == Qt.LeftToRight:
            ?A...setLayoutDirection(Qt.RightToLeft)
        else:
            ?A...setLayoutDirection(Qt.LeftToRight)

    ___ setActiveSubWindow(self, window):
        if window:
            self.mdiArea.setActiveSubWindow(window)


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
