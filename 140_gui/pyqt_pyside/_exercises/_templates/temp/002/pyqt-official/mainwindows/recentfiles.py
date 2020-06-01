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


____ ?.?C.. ______ QFile, QFileInfo, QSettings, __, QTextStream
____ ?.?G.. ______ ?KS..
____ ?.?W.. ______ (?A.., ?A.., ?FD.., QMainWindow,
        ?MB.., QTextEdit)


c_ MainWindow ?MW..
    MaxRecentFiles _ 5
    windowList _   # list

    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.recentFileActs _   # list

        self.setAttribute(__.WA_DeleteOnClose)

        self.textEdit _ QTextEdit()
        self.sCW..(self.textEdit)

        self.createActions()
        self.createMenus()
        self.statusBar()

        self.setWindowTitle("Recent Files")
        self.resize(400, 300)

    ___ newFile(self):
        other _ MainWindow()
        MainWindow.windowList.ap..(other)
        other.s..

    ___ o..(self):
        fileName, _ _ ?FD...gOFN..(self)
        __ fileName:
            self.loadFile(fileName)
        	
    ___ save(self):
        __ self.curFile:
            self.saveFile(self.curFile)
        ____
            self.saveAs()

    ___ saveAs(self):
        fileName, _ _ ?FD...getSaveFileName(self)
        __ fileName:
            self.saveFile(fileName)

    ___ openRecentFile(self):
        action _ self.sender()
        __ action:
            self.loadFile(action.data())

    ___ about(self):
        ?MB...about  "About Recent Files",
                "The <b>Recent Files</b> example demonstrates how to provide "
                "a recently used file menu in a Qt application.")

    ___ createActions(self):
        self.newAct _ ?A..("&New", self, shortcut_QKeySequence.New,
                statusTip_"Create a new file", triggered_self.newFile)

        self.openAct _ ?A..("&Open...", self, shortcut_QKeySequence.Open,
                statusTip_"Open an existing file", triggered_self.o..)

        self.saveAct _ ?A..("&Save", self, shortcut_QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_self.save)

        self.saveAsAct _ ?A..("Save &As...", self,
                shortcut_QKeySequence.SaveAs,
                statusTip_"Save the document under a new name",
                triggered_self.saveAs)

        for i in range(MainWindow.MaxRecentFiles):
            self.recentFileActs.ap..(
                    ?A..  visible_False,
                            triggered_self.openRecentFile))

        self.exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application",
                triggered_QApplication.instance().closeAllWindows)

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
        self.separatorAct _ self.fileMenu.addSeparator()
        for i in range(MainWindow.MaxRecentFiles):
            self.fileMenu.aA..(self.recentFileActs[i])
        self.fileMenu.addSeparator()
        self.fileMenu.aA..(self.exitAct)
        self.updateRecentFileActions()

        self.mB.. .addSeparator()

        self.helpMenu _ self.mB.. .aM..("&Help")
        self.helpMenu.aA..(self.aboutAct)
        self.helpMenu.aA..(self.aboutQtAct)

    ___ loadFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..( QFile.ReadOnly | QFile.Text):
            ?MB...warning  "Recent Files",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            r_

        instr _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        self.textEdit.sPT..(instr.readAll())
        ?A...restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File loaded", 2000)

    ___ saveFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..( QFile.WriteOnly | QFile.Text):
            ?MB...warning  "Recent Files",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            r_

        outstr _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        outstr << self.textEdit.toPlainText()
        ?A...restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File saved", 2000)

    ___ setCurrentFile  fileName):
        self.curFile _ fileName
        __ self.curFile:
            self.setWindowTitle("%s - Recent Files" % self.strippedName(self.curFile))
        ____
            self.setWindowTitle("Recent Files")

        settings _ QSettings('Trolltech', 'Recent Files Example')
        files _ settings.value('recentFileList',   # list)

        try:
            files.remove(fileName)
        except ValueError:
            pass

        files.insert(0, fileName)
        del files[MainWindow.MaxRecentFiles:]

        settings.setValue('recentFileList', files)

        for widget in ?A...topLevelWidgets
            __ isinstance(widget, MainWindow):
                widget.updateRecentFileActions()

    ___ updateRecentFileActions(self):
        settings _ QSettings('Trolltech', 'Recent Files Example')
        files _ settings.value('recentFileList',   # list)

        numRecentFiles _ min(le.(files), MainWindow.MaxRecentFiles)

        for i in range(numRecentFiles):
            t__ _ "&%d %s" % (i + 1, self.strippedName(files[i]))
            self.recentFileActs[i].sT..(t__)
            self.recentFileActs[i].setData(files[i])
            self.recentFileActs[i].setVisible(True)

        for j in range(numRecentFiles, MainWindow.MaxRecentFiles):
            self.recentFileActs[j].setVisible F..

        self.separatorAct.setVisible((numRecentFiles > 0))

    ___ strippedName  fullFileName):
        r_ QFileInfo(fullFileName).fileName()


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
