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


____ ?.QtCore ______ (QFile, QFileInfo, QPoint, QSettings, QSize, Qt,
        QTextStream)
____ ?.QtGui ______ QIcon, QKeySequence
____ ?.?W.. ______ (QAction, QApplication, QFileDialog, QMainWindow,
        QMessageBox, QTextEdit)

______ sdi_rc


class MainWindow(QMainWindow):
    sequenceNumber _ 1
    windowList _ []

    ___ __init__(self, fileName_None):
        super(MainWindow, self).__init__()

        self.init()
        if fileName:
            self.loadFile(fileName)
        else:
            self.setCurrentFile('')

    ___ closeEvent(self, event):
        if self.maybeSave
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    ___ newFile(self):
        other _ MainWindow()
        MainWindow.windowList.append(other)
        other.move(self.x() + 40, self.y() + 40)
        other.s..

    ___ open(self):
        fileName, _ _ QFileDialog.getOpenFileName(self)
        if fileName:
            existing _ self.findMainWindow(fileName)
            if existing:
                existing.s..
                existing.raise_()
                existing.activateWindow()
                return

            if self.isUntitled and self.textEdit.document().isEmpty() and not self.isWindowModified
                self.loadFile(fileName)
            else:
                other _ MainWindow(fileName)
                if other.isUntitled:
                    del other
                    return

                MainWindow.windowList.append(other)
                other.move(self.x() + 40, self.y() + 40)
                other.s..

    ___ save(self):
        if self.isUntitled:
            return self.saveAs()
        else:
            return self.saveFile(self.curFile)

    ___ saveAs(self):
        fileName, _ _ QFileDialog.getSaveFileName(self, "Save As",
                self.curFile)
        if not fileName:
            return False

        return self.saveFile(fileName)

    ___ about(self):
        QMessageBox.about(self, "About SDI",
                "The <b>SDI</b> example demonstrates how to write single "
                "document interface applications using Qt.")

    ___ documentWasModified(self):
        self.setWindowModified(True)

    ___ init(self):
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.isUntitled _ True
        self.textEdit _ QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()

        self.readSettings()

        self.textEdit.document().contentsChanged.c..(self.documentWasModified)

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

        self.closeAct _ QAction("&Close", self, shortcut_"Ctrl+W",
                statusTip_"Close this window", triggered_self.close)

        self.exitAct _ QAction("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application",
                triggered_QApplication.instance().closeAllWindows)

        self.cutAct _ QAction(QIcon(':/images/cut.png'), "Cu&t", self,
                enabled_False, shortcut_QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_self.textEdit.cut)

        self.copyAct _ QAction(QIcon(':/images/copy.png'), "&Copy", self,
                enabled_False, shortcut_QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_self.textEdit.copy)

        self.pasteAct _ QAction(QIcon(':/images/paste.png'), "&Paste", self,
                shortcut_QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_self.textEdit.paste)

        self.aboutAct _ QAction("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        self.aboutQtAct _ QAction("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.instance().aboutQt)

        self.textEdit.copyAvailable.c..(self.cutAct.setEnabled)
        self.textEdit.copyAvailable.c..(self.copyAct.setEnabled)

    ___ createMenus(self):
        self.fileMenu _ self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.closeAct)
        self.fileMenu.addAction(self.exitAct)

        self.editMenu _ self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)

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
        settings _ QSettings('Trolltech', 'SDI Example')
        pos _ settings.value('pos', QPoint(200, 200))
        size _ settings.value('size', QSize(400, 400))
        self.move(pos)
        self.resize(size)

    ___ writeSettings(self):
        settings _ QSettings('Trolltech', 'SDI Example')
        settings.setValue('pos', self.pos())
        settings.setValue('size', self.size())

    ___ maybeSave(self):
        if self.textEdit.document().isModified
            ret _ QMessageBox.warning(self, "SDI",
                    "The document has been modified.\nDo you want to save "
                    "your changes?",
                    QMessageBox.Save | QMessageBox.Discard |
                    QMessageBox.Cancel)

            if ret == QMessageBox.Save:
                return self.save()

            if ret == QMessageBox.Cancel:
                return False

        return True

    ___ loadFile(self, fileName):
        file _ QFile(fileName)
        if not file.open(QFile.ReadOnly | QFile.Text):
            QMessageBox.warning(self, "SDI",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            return

        instr _ QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.textEdit.setPlainText(instr.readAll())
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File loaded", 2000)

    ___ saveFile(self, fileName):
        file _ QFile(fileName)
        if not file.open(QFile.WriteOnly | QFile.Text):
            QMessageBox.warning(self, "SDI",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            return False

        outstr _ QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        outstr << self.textEdit.toPlainText()
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File saved", 2000)
        return True

    ___ setCurrentFile(self, fileName):
        self.isUntitled _ not fileName
        if self.isUntitled:
            self.curFile _ "document%d.txt" % MainWindow.sequenceNumber
            MainWindow.sequenceNumber +_ 1
        else:
            self.curFile _ QFileInfo(fileName).canonicalFilePath()

        self.textEdit.document().setModified(False)
        self.setWindowModified(False)

        self.setWindowTitle("%s[*] - SDI" % self.strippedName(self.curFile))

    ___ strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()

    ___ findMainWindow(self, fileName):
        canonicalFilePath _ QFileInfo(fileName).canonicalFilePath()

        for widget in QApplication.instance().topLevelWidgets
            if isinstance(widget, MainWindow) and widget.curFile == canonicalFilePath:
                return widget

        return None


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
