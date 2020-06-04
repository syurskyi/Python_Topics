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
        ?L.., ?MW.., ?M.., ?MB.., ?SP.., ?VBL..,
        ?W..)


c_ MainWindow ?MW..
    ___  - 
        s__(MainWindow, self). - ()

        widget _ ?W..
        sCW..(widget)

        topFiller _ ?W..
        topFiller.sSP..(?SP...E.., ?SP...E..)

        infoLabel _ ?L..(
                "<i>Choose a menu option, or right-click to invoke a context menu</i>",
                alignment_Qt.AlignCenter)
        infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        bottomFiller _ ?W..
        bottomFiller.sSP..(?SP...E.., ?SP...E..)

        vbox _ ?VBL..
        vbox.sCM..(5, 5, 5, 5)
        vbox.aW..(topFiller)
        vbox.aW..(infoLabel)
        vbox.aW..(bottomFiller)
        widget.sL..(vbox)

        createActions()
        createMenus()

        message _ "A context menu is available by right-clicking"
        sB.. .sM..(message)

        sWT..("Menus")
        sMS..(160,160)
        r..(480,320)

    ___ contextMenuEvent  event):
        menu _ ?M..
        menu.aA..(cutAct)
        menu.aA..(copyAct)
        menu.aA..(pasteAct)
        menu.e..(event.globalPos())

    ___ newFile
        infoLabel.sT..("Invoked <b>File|New</b>")

    ___ o..
        infoLabel.sT..("Invoked <b>File|Open</b>")
        	
    ___ save
        infoLabel.sT..("Invoked <b>File|Save</b>")

    ___ print_
        infoLabel.sT..("Invoked <b>File|Print</b>")

    ___ undo
        infoLabel.sT..("Invoked <b>Edit|Undo</b>")

    ___ redo
        infoLabel.sT..("Invoked <b>Edit|Redo</b>")

    ___ cut
        infoLabel.sT..("Invoked <b>Edit|Cut</b>")

    ___ copy
        infoLabel.sT..("Invoked <b>Edit|Copy</b>")

    ___ paste
        infoLabel.sT..("Invoked <b>Edit|Paste</b>")

    ___ bold
        infoLabel.sT..("Invoked <b>Edit|Format|Bold</b>")

    ___ italic
        infoLabel.sT..("Invoked <b>Edit|Format|Italic</b>")

    ___ leftAlign
        infoLabel.sT..("Invoked <b>Edit|Format|Left Align</b>")

    ___ rightAlign
        infoLabel.sT..("Invoked <b>Edit|Format|Right Align</b>")

    ___ justify
        infoLabel.sT..("Invoked <b>Edit|Format|Justify</b>")

    ___ center
        infoLabel.sT..("Invoked <b>Edit|Format|Center</b>")

    ___ setLineSpacing
        infoLabel.sT..("Invoked <b>Edit|Format|Set Line Spacing</b>")

    ___ setParagraphSpacing
        infoLabel.sT..("Invoked <b>Edit|Format|Set Paragraph Spacing</b>")

    ___ about
        infoLabel.sT..("Invoked <b>Help|About</b>")
        ?MB...about  "About Menu",
                "The <b>Menu</b> example shows how to create menu-bar menus "
                "and context menus.")

    ___ aboutQt
        infoLabel.sT..("Invoked <b>Help|About Qt</b>")

    ___ createActions
        newAct _ ?A..("&New", self, shortcut_QKeySequence.New,
                statusTip_"Create a new file", triggered_self.newFile)

        openAct _ ?A..("&Open...", self, shortcut_QKeySequence.Open,
                statusTip_"Open an existing file", triggered_self.o..)

        saveAct _ ?A..("&Save", self, shortcut_QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_self.save)

        printAct _ ?A..("&Print...", self, shortcut_QKeySequence.Print,
                statusTip_"Print the document", triggered_self.print_)

        exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application", triggered_self.close)

        undoAct _ ?A..("&Undo", self, shortcut_QKeySequence.Undo,
                statusTip_"Undo the last operation", triggered_self.undo)

        redoAct _ ?A..("&Redo", self, shortcut_QKeySequence.Redo,
                statusTip_"Redo the last operation", triggered_self.redo)

        cutAct _ ?A..("Cu&t", self, shortcut_QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_self.cut)

        copyAct _ ?A..("&Copy", self, shortcut_QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_self.copy)

        pasteAct _ ?A..("&Paste", self, shortcut_QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_self.paste)

        boldAct _ ?A..("&Bold", self, checkable_True,
                shortcut_"Ctrl+B", statusTip_"Make the text bold",
                triggered_self.bold)

        boldFont _ boldAct.font()
        boldFont.setBold( st.
        boldAct.sF..(boldFont)

        italicAct _ ?A..("&Italic", self, checkable_True,
                shortcut_"Ctrl+I", statusTip_"Make the text italic",
                triggered_self.italic)

        italicFont _ italicAct.font()
        italicFont.setItalic( st.
        italicAct.sF..(italicFont)

        setLineSpacingAct _ ?A..("Set &Line Spacing...", self,
                statusTip_"Change the gap between the lines of a paragraph",
                triggered_self.setLineSpacing)

        setParagraphSpacingAct _ ?A..("Set &Paragraph Spacing...",
                self, statusTip_"Change the gap between paragraphs",
                triggered_self.setParagraphSpacing)

        aboutAct _ ?A..("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_self.aboutQt)
        aboutQtAct.t__.c..(?A...i.. .aboutQt)

        leftAlignAct _ ?A..("&Left Align", self, checkable_True,
                shortcut_"Ctrl+L", statusTip_"Left align the selected text",
                triggered_self.leftAlign)

        rightAlignAct _ ?A..("&Right Align", self, checkable_True,
                shortcut_"Ctrl+R", statusTip_"Right align the selected text",
                triggered_self.rightAlign)

        justifyAct _ ?A..("&Justify", self, checkable_True,
                shortcut_"Ctrl+J", statusTip_"Justify the selected text",
                triggered_self.justify)

        centerAct _ ?A..("&Center", self, checkable_True,
                shortcut_"Ctrl+C", statusTip_"Center the selected text",
                triggered_self.center)

        alignmentGroup _ QActionGroup
        alignmentGroup.aA..(leftAlignAct)
        alignmentGroup.aA..(rightAlignAct)
        alignmentGroup.aA..(justifyAct)
        alignmentGroup.aA..(centerAct)
        leftAlignAct.sC__( st.

    ___ createMenus
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(newAct)
        fileMenu.aA..(openAct)
        fileMenu.aA..(saveAct)
        fileMenu.aA..(printAct)
        fileMenu.aS..)
        fileMenu.aA..(exitAct)

        editMenu _ mB.. .aM..("&Edit")
        editMenu.aA..(undoAct)
        editMenu.aA..(redoAct)
        editMenu.aS..)
        editMenu.aA..(cutAct)
        editMenu.aA..(copyAct)
        editMenu.aA..(pasteAct)
        editMenu.aS..)

        helpMenu _ mB.. .aM..("&Help")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

        formatMenu _ editMenu.aM..("&Format")
        formatMenu.aA..(boldAct)
        formatMenu.aA..(italicAct)
        formatMenu.aS..).sT..("Alignment")
        formatMenu.aA..(leftAlignAct)
        formatMenu.aA..(rightAlignAct)
        formatMenu.aA..(justifyAct)
        formatMenu.aA..(centerAct)
        formatMenu.aS..)
        formatMenu.aA..(setLineSpacingAct)
        formatMenu.aA..(setParagraphSpacingAct)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.s..
    ___.e.. ?.e..
