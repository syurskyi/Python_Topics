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


____ ?.QtCore ______ Qt
____ ?.QtGui ______ QKeySequence
____ ?.?W.. ______ (QAction, QActionGroup, QApplication, QFrame,
        QLabel, QMainWindow, QMenu, QMessageBox, QSizePolicy, QVBoxLayout,
        QWidget)


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        widget _ QWidget()
        self.setCentralWidget(widget)

        topFiller _ QWidget()
        topFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.infoLabel _ QLabel(
                "<i>Choose a menu option, or right-click to invoke a context menu</i>",
                alignment_Qt.AlignCenter)
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        bottomFiller _ QWidget()
        bottomFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        vbox _ QVBoxLayout()
        vbox.setContentsMargins(5, 5, 5, 5)
        vbox.addWidget(topFiller)
        vbox.addWidget(self.infoLabel)
        vbox.addWidget(bottomFiller)
        widget.setLayout(vbox)

        self.createActions()
        self.createMenus()

        message _ "A context menu is available by right-clicking"
        self.statusBar().showMessage(message)

        self.setWindowTitle("Menus")
        self.setMinimumSize(160,160)
        self.resize(480,320)

    ___ contextMenuEvent(self, event):
        menu _ QMenu(self)
        menu.addAction(self.cutAct)
        menu.addAction(self.copyAct)
        menu.addAction(self.pasteAct)
        menu.exec_(event.globalPos())

    ___ newFile(self):
        self.infoLabel.sT..("Invoked <b>File|New</b>")

    ___ open(self):
        self.infoLabel.sT..("Invoked <b>File|Open</b>")
        	
    ___ save(self):
        self.infoLabel.sT..("Invoked <b>File|Save</b>")

    ___ print_(self):
        self.infoLabel.sT..("Invoked <b>File|Print</b>")

    ___ undo(self):
        self.infoLabel.sT..("Invoked <b>Edit|Undo</b>")

    ___ redo(self):
        self.infoLabel.sT..("Invoked <b>Edit|Redo</b>")

    ___ cut(self):
        self.infoLabel.sT..("Invoked <b>Edit|Cut</b>")

    ___ copy(self):
        self.infoLabel.sT..("Invoked <b>Edit|Copy</b>")

    ___ paste(self):
        self.infoLabel.sT..("Invoked <b>Edit|Paste</b>")

    ___ bold(self):
        self.infoLabel.sT..("Invoked <b>Edit|Format|Bold</b>")

    ___ italic(self):
        self.infoLabel.sT..("Invoked <b>Edit|Format|Italic</b>")

    ___ leftAlign(self):
        self.infoLabel.sT..("Invoked <b>Edit|Format|Left Align</b>")

    ___ rightAlign(self):
        self.infoLabel.sT..("Invoked <b>Edit|Format|Right Align</b>")

    ___ justify(self):
        self.infoLabel.sT..("Invoked <b>Edit|Format|Justify</b>")

    ___ center(self):
        self.infoLabel.sT..("Invoked <b>Edit|Format|Center</b>")

    ___ setLineSpacing(self):
        self.infoLabel.sT..("Invoked <b>Edit|Format|Set Line Spacing</b>")

    ___ setParagraphSpacing(self):
        self.infoLabel.sT..("Invoked <b>Edit|Format|Set Paragraph Spacing</b>")

    ___ about(self):
        self.infoLabel.sT..("Invoked <b>Help|About</b>")
        QMessageBox.about(self, "About Menu",
                "The <b>Menu</b> example shows how to create menu-bar menus "
                "and context menus.")

    ___ aboutQt(self):
        self.infoLabel.sT..("Invoked <b>Help|About Qt</b>")

    ___ createActions(self):
        self.newAct _ QAction("&New", self, shortcut_QKeySequence.New,
                statusTip_"Create a new file", triggered_self.newFile)

        self.openAct _ QAction("&Open...", self, shortcut_QKeySequence.Open,
                statusTip_"Open an existing file", triggered_self.open)

        self.saveAct _ QAction("&Save", self, shortcut_QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_self.save)

        self.printAct _ QAction("&Print...", self, shortcut_QKeySequence.Print,
                statusTip_"Print the document", triggered_self.print_)

        self.exitAct _ QAction("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application", triggered_self.close)

        self.undoAct _ QAction("&Undo", self, shortcut_QKeySequence.Undo,
                statusTip_"Undo the last operation", triggered_self.undo)

        self.redoAct _ QAction("&Redo", self, shortcut_QKeySequence.Redo,
                statusTip_"Redo the last operation", triggered_self.redo)

        self.cutAct _ QAction("Cu&t", self, shortcut_QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_self.cut)

        self.copyAct _ QAction("&Copy", self, shortcut_QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_self.copy)

        self.pasteAct _ QAction("&Paste", self, shortcut_QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_self.paste)

        self.boldAct _ QAction("&Bold", self, checkable_True,
                shortcut_"Ctrl+B", statusTip_"Make the text bold",
                triggered_self.bold)

        boldFont _ self.boldAct.font()
        boldFont.setBold(True)
        self.boldAct.setFont(boldFont)

        self.italicAct _ QAction("&Italic", self, checkable_True,
                shortcut_"Ctrl+I", statusTip_"Make the text italic",
                triggered_self.italic)

        italicFont _ self.italicAct.font()
        italicFont.setItalic(True)
        self.italicAct.setFont(italicFont)

        self.setLineSpacingAct _ QAction("Set &Line Spacing...", self,
                statusTip_"Change the gap between the lines of a paragraph",
                triggered_self.setLineSpacing)

        self.setParagraphSpacingAct _ QAction("Set &Paragraph Spacing...",
                self, statusTip_"Change the gap between paragraphs",
                triggered_self.setParagraphSpacing)

        self.aboutAct _ QAction("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        self.aboutQtAct _ QAction("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_self.aboutQt)
        self.aboutQtAct.triggered.c..(QApplication.instance().aboutQt)

        self.leftAlignAct _ QAction("&Left Align", self, checkable_True,
                shortcut_"Ctrl+L", statusTip_"Left align the selected text",
                triggered_self.leftAlign)

        self.rightAlignAct _ QAction("&Right Align", self, checkable_True,
                shortcut_"Ctrl+R", statusTip_"Right align the selected text",
                triggered_self.rightAlign)

        self.justifyAct _ QAction("&Justify", self, checkable_True,
                shortcut_"Ctrl+J", statusTip_"Justify the selected text",
                triggered_self.justify)

        self.centerAct _ QAction("&Center", self, checkable_True,
                shortcut_"Ctrl+C", statusTip_"Center the selected text",
                triggered_self.center)

        self.alignmentGroup _ QActionGroup(self)
        self.alignmentGroup.addAction(self.leftAlignAct)
        self.alignmentGroup.addAction(self.rightAlignAct)
        self.alignmentGroup.addAction(self.justifyAct)
        self.alignmentGroup.addAction(self.centerAct)
        self.leftAlignAct.setChecked(True)

    ___ createMenus(self):
        self.fileMenu _ self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.editMenu _ self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.undoAct)
        self.editMenu.addAction(self.redoAct)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)
        self.editMenu.addSeparator()

        self.helpMenu _ self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.formatMenu _ self.editMenu.addMenu("&Format")
        self.formatMenu.addAction(self.boldAct)
        self.formatMenu.addAction(self.italicAct)
        self.formatMenu.addSeparator().sT..("Alignment")
        self.formatMenu.addAction(self.leftAlignAct)
        self.formatMenu.addAction(self.rightAlignAct)
        self.formatMenu.addAction(self.justifyAct)
        self.formatMenu.addAction(self.centerAct)
        self.formatMenu.addSeparator()
        self.formatMenu.addAction(self.setLineSpacingAct)
        self.formatMenu.addAction(self.setParagraphSpacingAct)


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())
