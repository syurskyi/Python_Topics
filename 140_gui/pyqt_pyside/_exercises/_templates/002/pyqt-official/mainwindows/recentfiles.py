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
____ ?.?W.. ______ (?A.., ?A.., ?FD.., ?MW..,
        ?MB.., ?TE..)


c_ MainWindow ?MW..
    MaxRecentFiles _ 5
    windowList _   # list

    ___  -  
        s__(MainWindow, self). - ()

        recentFileActs _   # list

        setAttribute(__.WA_DeleteOnClose)

        textEdit _ ?TE..()
        sCW..(textEdit)

        createActions()
        createMenus()
        sB..

        sWT..("Recent Files")
        r..(400, 300)

    ___ newFile 
        other _ MainWindow()
        MainWindow.windowList.ap..(other)
        other.s..

    ___ o.. 
        fileName, _ _ ?FD...gOFN..
        __ fileName:
            loadFile(fileName)
        	
    ___ save 
        __ curFile:
            saveFile(curFile)
        ____
            saveAs()

    ___ saveAs 
        fileName, _ _ ?FD...getSaveFileName
        __ fileName:
            saveFile(fileName)

    ___ openRecentFile 
        action _ sender()
        __ action:
            loadFile(action.data())

    ___ about 
        ?MB...about  "About Recent Files",
                "The <b>Recent Files</b> example demonstrates how to provide "
                "a recently used file menu in a Qt application.")

    ___ createActions 
        newAct _ ?A..("&New", self, shortcut_QKeySequence.New,
                statusTip_"Create a new file", triggered_self.newFile)

        openAct _ ?A..("&Open...", self, shortcut_QKeySequence.Open,
                statusTip_"Open an existing file", triggered_self.o..)

        saveAct _ ?A..("&Save", self, shortcut_QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_self.save)

        saveAsAct _ ?A..("Save &As...", self,
                shortcut_QKeySequence.SaveAs,
                statusTip_"Save the document under a new name",
                triggered_self.saveAs)

        ___ i __ ra..(MainWindow.MaxRecentFiles):
            recentFileActs.ap..(
                    ?A..  visible_False,
                            triggered_self.openRecentFile))

        exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application",
                triggered_QApplication.i.. .closeAllWindows)

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
        separatorAct _ fileMenu.aS..)
        ___ i __ ra..(MainWindow.MaxRecentFiles):
            fileMenu.aA..(recentFileActs[i])
        fileMenu.aS..)
        fileMenu.aA..(exitAct)
        updateRecentFileActions()

        mB.. .aS..)

        helpMenu _ mB.. .aM..("&Help")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ loadFile  fileName):
        file _ QFile(fileName)
        __ no. file.o..( QFile.ReadOnly | QFile.Text):
            ?MB...w..  "Recent Files",
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
        __ no. file.o..( QFile.WriteOnly | QFile.Text):
            ?MB...w..  "Recent Files",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            r_

        outstr _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        outstr << textEdit.toPlainText()
        ?A...restoreOverrideCursor()

        setCurrentFile(fileName)
        sB.. .sM..("File saved", 2000)

    ___ setCurrentFile  fileName):
        curFile _ fileName
        __ curFile:
            sWT..("%s - Recent Files" % strippedName(curFile))
        ____
            sWT..("Recent Files")

        settings _ QSettings('Trolltech', 'Recent Files Example')
        files _ settings.value('recentFileList',   # list)

        ___
            files.remove(fileName)
        _____ V..:
            p..

        files.insert(0, fileName)
        del files[MainWindow.MaxRecentFiles:]

        settings.sV..('recentFileList', files)

        ___ widget __ ?A...topLevelWidgets
            __ isinstance(widget, MainWindow):
                widget.updateRecentFileActions()

    ___ updateRecentFileActions 
        settings _ QSettings('Trolltech', 'Recent Files Example')
        files _ settings.value('recentFileList',   # list)

        numRecentFiles _ min(le.(files), MainWindow.MaxRecentFiles)

        ___ i __ ra..(numRecentFiles):
            t__ _ "&%d %s" % (i + 1, strippedName(files[i]))
            recentFileActs[i].sT..(t__)
            recentFileActs[i].setData(files[i])
            recentFileActs[i].setVisible( st.

        ___ j __ ra..(numRecentFiles, MainWindow.MaxRecentFiles):
            recentFileActs[j].setVisible F..

        separatorAct.setVisible((numRecentFiles > 0))

    ___ strippedName  fullFileName):
        r_ QFileInfo(fullFileName).fN..


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    mainWin _ MainWindow()
    mainWin.s..
    ___.e.. ?.e..
