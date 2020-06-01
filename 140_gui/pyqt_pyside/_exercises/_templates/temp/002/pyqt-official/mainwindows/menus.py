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


____ ?.?C.. ______ __
____ ?.?G.. ______ ?KS..
____ ?.?W.. ______ (?A.., QActionGroup, ?A.., QFrame,
        QLabel, QMainWindow, QMenu, ?MB.., QSizePolicy, QVBoxLayout,
        QWidget)


c_ MainWindow ?MW..
    ___ __init__(self):
        super(MainWindow, self).__init__()

        widget _ ?W..
        self.sCW..(widget)

        topFiller _ ?W..
        topFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.infoLabel _ QLabel(
                "<i>Choose a menu option, or right-click to invoke a context menu</i>",
                alignment_Qt.AlignCenter)
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        bottomFiller _ ?W..
        bottomFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        vbox _ ?VBL..
        vbox.setContentsMargins(5, 5, 5, 5)
        vbox.aW..(topFiller)
        vbox.aW..(self.infoLabel)
        vbox.aW..(bottomFiller)
        widget.sL..(vbox)

        self.createActions()
        self.createMenus()

        message _ "A context menu is available by right-clicking"
        self.statusBar().showMessage(message)

        self.setWindowTitle("Menus")
        self.setMinimumSize(160,160)
        self.resize(480,320)

    ___ contextMenuEvent  event):
        menu _ QMenu(self)
        menu.aA..(self.cutAct)
        menu.aA..(self.copyAct)
        menu.aA..(self.pasteAct)
        menu.exec_(event.globalPos())

    ___ newFile(self):
        self.infoLabel.sT..("Invoked <b>File|New</b>")

    ___ o..(self):
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
        ?MB...about  "About Menu",
                "The <b>Menu</b> example shows how to create menu-bar menus "
                "and context menus.")

    ___ aboutQt(self):
        self.infoLabel.sT..("Invoked <b>Help|About Qt</b>")

    ___ createActions(self):
        self.newAct _ ?A..("&New", self, shortcut_QKeySequence.New,
                statusTip_"Create a new file", triggered_self.newFile)

        self.openAct _ ?A..("&Open...", self, shortcut_QKeySequence.Open,
                statusTip_"Open an existing file", triggered_self.o..)

        self.saveAct _ ?A..("&Save", self, shortcut_QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_self.save)

        self.printAct _ ?A..("&Print...", self, shortcut_QKeySequence.Print,
                statusTip_"Print the document", triggered_self.print_)

        self.exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application", triggered_self.close)

        self.undoAct _ ?A..("&Undo", self, shortcut_QKeySequence.Undo,
                statusTip_"Undo the last operation", triggered_self.undo)

        self.redoAct _ ?A..("&Redo", self, shortcut_QKeySequence.Redo,
                statusTip_"Redo the last operation", triggered_self.redo)

        self.cutAct _ ?A..("Cu&t", self, shortcut_QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_self.cut)

        self.copyAct _ ?A..("&Copy", self, shortcut_QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_self.copy)

        self.pasteAct _ ?A..("&Paste", self, shortcut_QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_self.paste)

        self.boldAct _ ?A..("&Bold", self, checkable_True,
                shortcut_"Ctrl+B", statusTip_"Make the text bold",
                triggered_self.bold)

        boldFont _ self.boldAct.font()
        boldFont.setBold(True)
        self.boldAct.setFont(boldFont)

        self.italicAct _ ?A..("&Italic", self, checkable_True,
                shortcut_"Ctrl+I", statusTip_"Make the text italic",
                triggered_self.italic)

        italicFont _ self.italicAct.font()
        italicFont.setItalic(True)
        self.italicAct.setFont(italicFont)

        self.setLineSpacingAct _ ?A..("Set &Line Spacing...", self,
                statusTip_"Change the gap between the lines of a paragraph",
                triggered_self.setLineSpacing)

        self.setParagraphSpacingAct _ ?A..("Set &Paragraph Spacing...",
                self, statusTip_"Change the gap between paragraphs",
                triggered_self.setParagraphSpacing)

        self.aboutAct _ ?A..("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        self.aboutQtAct _ ?A..("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_self.aboutQt)
        self.aboutQtAct.t__.c..(?A...instance().aboutQt)

        self.leftAlignAct _ ?A..("&Left Align", self, checkable_True,
                shortcut_"Ctrl+L", statusTip_"Left align the selected text",
                triggered_self.leftAlign)

        self.rightAlignAct _ ?A..("&Right Align", self, checkable_True,
                shortcut_"Ctrl+R", statusTip_"Right align the selected text",
                triggered_self.rightAlign)

        self.justifyAct _ ?A..("&Justify", self, checkable_True,
                shortcut_"Ctrl+J", statusTip_"Justify the selected text",
                triggered_self.justify)

        self.centerAct _ ?A..("&Center", self, checkable_True,
                shortcut_"Ctrl+C", statusTip_"Center the selected text",
                triggered_self.center)

        self.alignmentGroup _ QActionGroup(self)
        self.alignmentGroup.aA..(self.leftAlignAct)
        self.alignmentGroup.aA..(self.rightAlignAct)
        self.alignmentGroup.aA..(self.justifyAct)
        self.alignmentGroup.aA..(self.centerAct)
        self.leftAlignAct.setChecked(True)

    ___ createMenus(self):
        self.fileMenu _ self.mB.. .aM..("&File")
        self.fileMenu.aA..(self.newAct)
        self.fileMenu.aA..(self.openAct)
        self.fileMenu.aA..(self.saveAct)
        self.fileMenu.aA..(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.aA..(self.exitAct)

        self.editMenu _ self.mB.. .aM..("&Edit")
        self.editMenu.aA..(self.undoAct)
        self.editMenu.aA..(self.redoAct)
        self.editMenu.addSeparator()
        self.editMenu.aA..(self.cutAct)
        self.editMenu.aA..(self.copyAct)
        self.editMenu.aA..(self.pasteAct)
        self.editMenu.addSeparator()

        self.helpMenu _ self.mB.. .aM..("&Help")
        self.helpMenu.aA..(self.aboutAct)
        self.helpMenu.aA..(self.aboutQtAct)

        self.formatMenu _ self.editMenu.aM..("&Format")
        self.formatMenu.aA..(self.boldAct)
        self.formatMenu.aA..(self.italicAct)
        self.formatMenu.addSeparator().sT..("Alignment")
        self.formatMenu.aA..(self.leftAlignAct)
        self.formatMenu.aA..(self.rightAlignAct)
        self.formatMenu.aA..(self.justifyAct)
        self.formatMenu.aA..(self.centerAct)
        self.formatMenu.addSeparator()
        self.formatMenu.aA..(self.setLineSpacingAct)
        self.formatMenu.aA..(self.setParagraphSpacingAct)


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    window _ MainWindow()
    window.s..
    ___.exit(app.exec_())
