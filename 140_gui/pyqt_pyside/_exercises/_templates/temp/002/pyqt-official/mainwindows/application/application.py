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


____ ?.QtCore ______ (QFile, QFileInfo, QPoint, QRect, QSettings, QSize,
        Qt, QTextStream)
____ ?.?G.. ______ QIcon, ?KS..
____ ?.?W.. ______ (?A.., ?A.., ?FD.., QMainWindow,
        ?MB.., QTextEdit)


c_ MainWindow ?MW..
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.curFile _ ''

        self.textEdit _ QTextEdit()
        self.sCW..(self.textEdit)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()

        self.readSettings()

        self.textEdit.document().contentsChanged.c..(self.documentWasModified)

        self.setCurrentFile('')

    ___ closeEvent  event):
        __ self.maybeSave
            self.writeSettings()
            event.accept()
        ____
            event.ignore()

    ___ newFile(self):
        __ self.maybeSave
            self.textEdit.clear()
            self.setCurrentFile('')

    ___ o..(self):
        __ self.maybeSave
            fileName, _ _ ?FD...gOFN..(self)
            __ fileName:
                self.loadFile(fileName)

    ___ save(self):
        __ self.curFile:
            r_ self.saveFile(self.curFile)

        r_ self.saveAs()

    ___ saveAs(self):
        fileName, _ _ ?FD...getSaveFileName(self)
        __ fileName:
            r_ self.saveFile(fileName)

        r_ False

    ___ about(self):
        ?MB...about  "About Application",
                "The <b>Application</b> example demonstrates how to write "
                "modern GUI applications using Qt, with a menu bar, "
                "toolbars, and a status bar.")

    ___ documentWasModified(self):
        self.setWindowModified(self.textEdit.document().iM..())

    ___ createActions(self):
        root _ QFileInfo(__file__).absolutePath()

        self.newAct _ ?A..(QIcon(root + '/images/new.png'), "&New", self,
                shortcut_QKeySequence.New, statusTip_"Create a new file",
                triggered_self.newFile)

        self.openAct _ ?A..(QIcon(root + '/images/open.png'), "&Open...",
                self, shortcut_QKeySequence.Open,
                statusTip_"Open an existing file", triggered_self.o..)

        self.saveAct _ ?A..(QIcon(root + '/images/save.png'), "&Save", self,
                shortcut_QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_self.save)

        self.saveAsAct _ ?A..("Save &As...", self,
                shortcut_QKeySequence.SaveAs,
                statusTip_"Save the document under a new name",
                triggered_self.saveAs)

        self.exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application", triggered_self.close)

        self.cutAct _ ?A..(QIcon(root + '/images/cut.png'), "Cu&t", self,
                shortcut_QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_self.textEdit.cut)

        self.copyAct _ ?A..(QIcon(root + '/images/copy.png'), "&Copy", self,
                shortcut_QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_self.textEdit.copy)

        self.pasteAct _ ?A..(QIcon(root + '/images/paste.png'), "&Paste",
                self, shortcut_QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_self.textEdit.paste)

        self.aboutAct _ ?A..("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        self.aboutQtAct _ ?A..("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.instance().aboutQt)

        self.cutAct.setEnabled F..
        self.copyAct.setEnabled F..
        self.textEdit.copyAvailable.c..(self.cutAct.setEnabled)
        self.textEdit.copyAvailable.c..(self.copyAct.setEnabled)

    ___ createMenus(self):
        self.fileMenu _ self.mB.. .aM..("&File")
        self.fileMenu.aA..(self.newAct)
        self.fileMenu.aA..(self.openAct)
        self.fileMenu.aA..(self.saveAct)
        self.fileMenu.aA..(self.saveAsAct)
        self.fileMenu.addSeparator();
        self.fileMenu.aA..(self.exitAct)

        self.editMenu _ self.mB.. .aM..("&Edit")
        self.editMenu.aA..(self.cutAct)
        self.editMenu.aA..(self.copyAct)
        self.editMenu.aA..(self.pasteAct)

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
        settings _ QSettings("Trolltech", "Application Example")
        pos _ settings.value("pos", QPoint(200, 200))
        size _ settings.value("size", QSize(400, 400))
        self.resize(size)
        self.move(pos)

    ___ writeSettings(self):
        settings _ QSettings("Trolltech", "Application Example")
        settings.setValue("pos", self.pos())
        settings.setValue("size", self.size())

    ___ maybeSave(self):
        __ self.textEdit.document().iM..
            ret _ ?MB...warning  "Application",
                    "The document has been modified.\nDo you want to save "
                    "your changes?",
                    ?MB...Save | ?MB...Discard | ?MB...Cancel)

            __ ret == ?MB...Save:
                r_ self.save()

            __ ret == ?MB...Cancel:
                r_ False

        r_ True

    ___ loadFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..(QFile.ReadOnly | QFile.Text):
            ?MB...warning  "Application",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            r_

        inf _ QTextStream(file)
        ?A...setOverrideCursor(Qt.WaitCursor)
        self.textEdit.sPT..(inf.readAll())
        ?A...restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File loaded", 2000)

    ___ saveFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..(QFile.WriteOnly | QFile.Text):
            ?MB...warning  "Application",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            r_ False

        outf _ QTextStream(file)
        ?A...setOverrideCursor(Qt.WaitCursor)
        outf << self.textEdit.toPlainText()
        ?A...restoreOverrideCursor()

        self.setCurrentFile(fileName);
        self.statusBar().showMessage("File saved", 2000)
        r_ True

    ___ setCurrentFile  fileName):
        self.curFile _ fileName
        self.textEdit.document().setModified F..
        self.setWindowModified F..

        __ self.curFile:
            shownName _ self.strippedName(self.curFile)
        ____
            shownName _ 'untitled.txt'

        self.setWindowTitle("%s[*] - Application" % shownName)

    ___ strippedName  fullFileName):
        r_ QFileInfo(fullFileName).fileName()


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
