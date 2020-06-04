#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################


______ ___

____ ?.?C.. ______ QFile, QFileInfo, __, QTextCodec
____ ?.?G.. ______ (?F.., QFontDatabase, QFontInfo, ?I.., ?KS..,
        ?P.., QTextBlockFormat, QTextCharFormat, QTextCursor,
        QTextDocumentWriter, QTextListFormat)
____ ?.?W.. ______ (?A.., QActionGroup, ?A.., QColorDialog,
        ?CB, ?FD.., QFontComboBox, ?MW.., ?M.., ?MB..,
        ?TE.., QToolBar)
____ ?.?PS.. ______ QPrintDialog, QPrinter, QPrintPreviewDialog

______ textedit_rc


__ ___.platform.s_w_('darwin'):
    rsrcPath _ ":/images/mac"
____
    rsrcPath _ ":/images/win"


c_ TextEdit ?MW..
    ___  -   fileName_None, parent_None):
        s__(TextEdit, self). - (parent)

        sWI..(?I..(':/images/logo.png'))
        setToolButtonStyle(__.ToolButtonFollowStyle)
        setupFileActions()
        setupEditActions()
        setupTextActions()

        helpMenu _ ?M..("Help", self)
        mB.. .aM..(helpMenu)
        helpMenu.aA..("About", about)
        helpMenu.aA..("About &Qt", ?A...i.. .aboutQt)
 
        textEdit _ ?TE..
        textEdit.currentCharFormatChanged.c..(
                currentCharFormatChanged)
        textEdit.cursorPositionChanged.c..(cursorPositionChanged)
        sCW..(textEdit)
        textEdit.setFocus()
        setCurrentFileName()
        fontChanged(textEdit.font())
        colorChanged(textEdit.textColor())
        alignmentChanged(textEdit.alignment())
        textEdit.document().modificationChanged.c..(
                actionSave.sE..)
        textEdit.document().modificationChanged.c..(
                setWindowModified)
        textEdit.document().undoAvailable.c..(
                actionUndo.sE..)
        textEdit.document().redoAvailable.c..(
                actionRedo.sE..)
        setWindowModified(textEdit.document().iM..())
        actionSave.sE..(textEdit.document().iM..())
        actionUndo.sE..(textEdit.document().isUndoAvailable())
        actionRedo.sE..(textEdit.document().isRedoAvailable())
        actionUndo.t__.c..(textEdit.undo)
        actionRedo.t__.c..(textEdit.redo)
        actionCut.sE.. F..
        actionCopy.sE.. F..
        actionCut.t__.c..(textEdit.cut)
        actionCopy.t__.c..(textEdit.copy)
        actionPaste.t__.c..(textEdit.paste)
        textEdit.copyAvailable.c..(actionCut.sE..)
        textEdit.copyAvailable.c..(actionCopy.sE..)
        ?A...clipboard().dataChanged.c..(clipboardDataChanged)

        __ fileName __ N..:
            fileName _ ':/example.html'

        __ no. load(fileName):
            fileNew()

    ___ closeEvent  e):
        __ maybeSave
            e.accept()
        ____
            e.ignore()

    ___ setupFileActions 
        tb _ QToolBar
        tb.sWT..("File Actions")
        aTB..(tb)

        menu _ ?M..("&File", self)
        mB.. .aM..(menu)

        actionNew _ ?A..(
                ?I...fromTheme('document-new',
                        ?I..(rsrcPath + '/filenew.png')),
                "&New", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.New, triggered_self.fileNew)
        tb.aA..(actionNew)
        menu.aA..(actionNew)

        actionOpen _ ?A..(
                ?I...fromTheme('document-open',
                        ?I..(rsrcPath + '/fileopen.png')),
                "&Open...", self, shortcut_QKeySequence.Open,
                triggered_self.fileOpen)
        tb.aA..(actionOpen)
        menu.aA..(actionOpen)
        menu.aS..)

        actionSave _ ?A..(
                ?I...fromTheme('document-save',
                        ?I..(rsrcPath + '/filesave.png')),
                "&Save", self, shortcut_QKeySequence.Save,
                triggered_self.fileSave, enabled_False)
        tb.aA..(actionSave)
        menu.aA..(actionSave)

        actionSaveAs _ ?A..("Save &As...", self,
                priority_QAction.LowPriority,
                shortcut_Qt.CTRL + __.SHIFT + __.Key_S,
                triggered_self.fileSaveAs)
        menu.aA..(actionSaveAs)
        menu.aS..)
 
        actionPrint _ ?A..(
                ?I...fromTheme('document-print',
                        ?I..(rsrcPath + '/fileprint.png')),
                "&Print...", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Print, triggered_self.filePrint)
        tb.aA..(actionPrint)
        menu.aA..(actionPrint)

        actionPrintPreview _ ?A..(
                ?I...fromTheme('fileprint',
                        ?I..(rsrcPath + '/fileprint.png')),
                "Print Preview...", self,
                shortcut_Qt.CTRL + __.SHIFT + __.Key_P,
                triggered_self.filePrintPreview)
        menu.aA..(actionPrintPreview)

        actionPrintPdf _ ?A..(
                ?I...fromTheme('exportpdf',
                        ?I..(rsrcPath + '/exportpdf.png')),
                "&Export PDF...", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + __.Key_D,
                triggered_self.filePrintPdf)
        tb.aA..(actionPrintPdf)
        menu.aA..(actionPrintPdf)
        menu.aS..)

        actionQuit _ ?A..("&Quit", self, shortcut_QKeySequence.Quit,
                triggered_self.close)
        menu.aA..(actionQuit)

    ___ setupEditActions 
        tb _ QToolBar
        tb.sWT..("Edit Actions")
        aTB..(tb)

        menu _ ?M..("&Edit", self)
        mB.. .aM..(menu)

        actionUndo _ ?A..(
                ?I...fromTheme('edit-undo',
                        ?I..(rsrcPath + '/editundo.png')),
                "&Undo", self, shortcut_QKeySequence.Undo)
        tb.aA..(actionUndo)
        menu.aA..(actionUndo)

        actionRedo _ ?A..(
                ?I...fromTheme('edit-redo',
                        ?I..(rsrcPath + '/editredo.png')),
                "&Redo", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Redo)
        tb.aA..(actionRedo)
        menu.aA..(actionRedo)
        menu.aS..)

        actionCut _ ?A..(
                ?I...fromTheme('edit-cut', ?I..(rsrcPath + '/editcut.png')),
                "Cu&t", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Cut)
        tb.aA..(actionCut)
        menu.aA..(actionCut)

        actionCopy _ ?A..(
                ?I...fromTheme('edit-copy',
                        ?I..(rsrcPath + '/editcopy.png')),
                "&Copy", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Copy)
        tb.aA..(actionCopy)
        menu.aA..(actionCopy)

        actionPaste _ ?A..(
                ?I...fromTheme('edit-paste',
                        ?I..(rsrcPath + '/editpaste.png')),
                "&Paste", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Paste,
                enabled_(le.(?A...clipboard().t__()) !_ 0))
        tb.aA..(actionPaste)
        menu.aA..(actionPaste)

    ___ setupTextActions 
        tb _ QToolBar
        tb.sWT..("Format Actions")
        aTB..(tb)

        menu _ ?M..("F&ormat", self)
        mB.. .aM..(menu)

        actionTextBold _ ?A..(
                ?I...fromTheme('format-text-bold',
                        ?I..(rsrcPath + '/textbold.png')),
                "&Bold", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + __.Key_B, triggered_self.textBold,
                checkable_ st.
        bold _ ?F..()
        bold.setBold( st.
        actionTextBold.sF..(bold)
        tb.aA..(actionTextBold)
        menu.aA..(actionTextBold)

        actionTextItalic _ ?A..(
                ?I...fromTheme('format-text-italic',
                        ?I..(rsrcPath + '/textitalic.png')),
                "&Italic", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + __.Key_I, triggered_self.textItalic,
                checkable_ st.
        italic _ ?F..()
        italic.setItalic( st.
        actionTextItalic.sF..(italic)
        tb.aA..(actionTextItalic)
        menu.aA..(actionTextItalic)

        actionTextUnderline _ ?A..(
                ?I...fromTheme('format-text-underline',
                        ?I..(rsrcPath + '/textunder.png')),
                "&Underline", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + __.Key_U, triggered_self.textUnderline,
                checkable_ st.
        underline _ ?F..()
        underline.setUnderline( st.
        actionTextUnderline.sF..(underline)
        tb.aA..(actionTextUnderline)
        menu.aA..(actionTextUnderline)

        menu.aS..)

        grp _ QActionGroup  triggered_self.textAlign)

        # Make sure the alignLeft is always left of the alignRight.
        __ ?A...isLeftToRight
            actionAlignLeft _ ?A..(
                    ?I...fromTheme('format-justify-left',
                            ?I..(rsrcPath + '/textleft.png')),
                    "&Left", grp)
            actionAlignCenter _ ?A..(
                    ?I...fromTheme('format-justify-center',
                            ?I..(rsrcPath + '/textcenter.png')),
                    "C&enter", grp)
            actionAlignRight _ ?A..(
                    ?I...fromTheme('format-justify-right',
                            ?I..(rsrcPath + '/textright.png')),
                    "&Right", grp)
        ____
            actionAlignRight _ ?A..(
                    ?I...fromTheme('format-justify-right',
                            ?I..(rsrcPath + '/textright.png')),
                    "&Right", grp)
            actionAlignCenter _ ?A..(
                    ?I...fromTheme('format-justify-center',
                            ?I..(rsrcPath + '/textcenter.png')),
                    "C&enter", grp)
            actionAlignLeft _ ?A..(
                    ?I...fromTheme('format-justify-left',
                            ?I..(rsrcPath + '/textleft.png')),
                    "&Left", grp)
 
        actionAlignJustify _ ?A..(
                ?I...fromTheme('format-justify-fill',
                        ?I..(rsrcPath + '/textjustify.png')),
                "&Justify", grp)

        actionAlignLeft.sS..(__.CTRL + __.Key_L)
        actionAlignLeft.setCheckable( st.
        actionAlignLeft.setPriority(?A...LowPriority)

        actionAlignCenter.sS..(__.CTRL + __.Key_E)
        actionAlignCenter.setCheckable( st.
        actionAlignCenter.setPriority(?A...LowPriority)

        actionAlignRight.sS..(__.CTRL + __.Key_R)
        actionAlignRight.setCheckable( st.
        actionAlignRight.setPriority(?A...LowPriority)

        actionAlignJustify.sS..(__.CTRL + __.Key_J)
        actionAlignJustify.setCheckable( st.
        actionAlignJustify.setPriority(?A...LowPriority)

        tb.addActions(grp.actions())
        menu.addActions(grp.actions())
        menu.aS..)

        pix _ ?P..(16, 16)
        pix.fill(__.black)
        actionTextColor _ ?A..(?I..(pix), "&Color...", self,
                triggered_self.textColor)
        tb.aA..(actionTextColor)
        menu.aA..(actionTextColor)

        tb _ QToolBar
        tb.setAllowedAreas(__.TopToolBarArea | __.BottomToolBarArea)
        tb.sWT..("Format Actions")
        addToolBarBreak(__.TopToolBarArea)
        aTB..(tb)

        comboStyle _ ?CB(tb)
        tb.aW..(comboStyle)
        comboStyle.aI..("Standard")
        comboStyle.aI..("Bullet List (Disc)")
        comboStyle.aI..("Bullet List (Circle)")
        comboStyle.aI..("Bullet List (Square)")
        comboStyle.aI..("Ordered List (Decimal)")
        comboStyle.aI..("Ordered List (Alpha lower)")
        comboStyle.aI..("Ordered List (Alpha upper)")
        comboStyle.aI..("Ordered List (Roman lower)")
        comboStyle.aI..("Ordered List (Roman upper)")
        comboStyle.activated.c..(textStyle)

        comboFont _ QFontComboBox(tb)
        tb.aW..(comboFont)
        comboFont.activated[st.].c..(textFamily)

        comboSize _ ?CB(tb)
        comboSize.setObjectName("comboSize")
        tb.aW..(comboSize)
        comboSize.sE..( st.

        db _ QFontDatabase()
        ___ size __ db.standardSizes
            comboSize.aI..("%s" % (size))

        comboSize.activated[st.].c..(textSize)
        comboSize.sCI..(
                comboSize.findText(
                        "%s" % (?A...font().pointSize())))

    ___ load  f):
        __ no. QFile.e..(f):
            r_ F..

        fh _ QFile(f)
        __ no. fh.o..(QFile.ReadOnly):
            r_ F..

        data _ fh.rA..
        codec _ QTextCodec.codecForHtml(data)
        unistr _ codec.toUnicode(data)

        __ __.mightBeRichText(unistr):
            textEdit.setHtml(unistr)
        ____
            textEdit.sPT..(unistr)

        setCurrentFileName(f)
        r_ T..

    ___ maybeSave 
        __ no. textEdit.document().iM..
            r_ T..

        __ fileName.s_w_(':/'):
            r_ T..

        ret _ ?MB...w..  "Application",
                "The document has been modified.\n"
                "Do you want to save your changes?",
                ?MB...Save | ?MB...Discard | ?MB...Cancel)

        __ ret __ ?MB...Save:
            r_ fileSave()

        __ ret __ ?MB...Cancel:
            r_ F..

        r_ T..

    ___ setCurrentFileName  fileName_''):
        fileName _ fileName
        textEdit.document().setModified F..

        __ no. fileName:
            shownName _ 'untitled.txt'
        ____
            shownName _ QFileInfo(fileName).fN..

        sWT..(tr("%s[*] - %s" % (shownName, "Rich Text")))
        setWindowModified F..

    ___ fileNew 
        __ maybeSave
            textEdit.c..
            setCurrentFileName()

    ___ fileOpen 
        fn, _ _ ?FD...gOFN..  "Open File...", N..,
                "HTML-Files (*.htm *.html);;All Files (*)")

        __ fn:
            load(fn)

    ___ fileSave 
        __ no. fileName:
            r_ fileSaveAs()

        writer _ QTextDocumentWriter(fileName)
        success _ writer.w..(textEdit.document())
        __ success:
            textEdit.document().setModified F..

        r_ success

    ___ fileSaveAs 
        fn, _ _ ?FD...getSaveFileName  "Save as...", N..,
                "ODF files (*.odt);;HTML-Files (*.htm *.html);;All Files (*)")

        __ no. fn:
            r_ F..

        lfn _ fn.lower()
        __ no. lfn.endswith(('.odt', '.htm', '.html')):
            # The default.
            fn +_ '.odt'

        setCurrentFileName(fn)
        r_ fileSave()

    ___ filePrint 
        printer _ QPrinter(QPrinter.HighResolution)
        dlg _ QPrintDialog(printer, self)

        __ textEdit.textCursor().hasSelection
            dlg.addEnabledOption(QPrintDialog.PrintSelection)

        dlg.sWT..("Print Document")

        __ dlg.e.. __ QPrintDialog.Accepted:
            textEdit.print_(printer)

        del dlg

    ___ filePrintPreview 
        printer _ QPrinter(QPrinter.HighResolution)
        preview _ QPrintPreviewDialog(printer, self)
        p__.paintRequested.c..(printPreview)
        p__.e..

    ___ printPreview  printer):
        textEdit.print_(printer)

    ___ filePrintPdf 
        fn, _ _ ?FD...getSaveFileName  "Export PDF", N..,
                "PDF files (*.pdf);;All Files (*)")

        __ fn:
            __ QFileInfo(fn).suffix().isEmpty
                fn +_ '.pdf'

            printer _ QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            textEdit.document().print_(printer)

    ___ textBold 
        fmt _ QTextCharFormat()
        fmt.setFontWeight(actionTextBold.isChecked() and ?F...Bold or ?F...Normal)
        mergeFormatOnWordOrSelection(fmt)

    ___ textUnderline 
        fmt _ QTextCharFormat()
        fmt.setFontUnderline(actionTextUnderline.isChecked())
        mergeFormatOnWordOrSelection(fmt)

    ___ textItalic 
        fmt _ QTextCharFormat()
        fmt.setFontItalic(actionTextItalic.isChecked())
        mergeFormatOnWordOrSelection(fmt)

    ___ textFamily  family):
        fmt _ QTextCharFormat()
        fmt.setFontFamily(family)
        mergeFormatOnWordOrSelection(fmt)

    ___ textSize  pointSize):
        pointSize _ fl..(pointSize)
        __ pointSize > 0:
            fmt _ QTextCharFormat()
            fmt.setFontPointSize(pointSize)
            mergeFormatOnWordOrSelection(fmt)

    ___ textStyle  styleIndex):
        cursor _ textEdit.textCursor()
        __ styleIndex:
            styleDict _ {
                1: QTextListFormat.ListDisc,
                2: QTextListFormat.ListCircle,
                3: QTextListFormat.ListSquare,
                4: QTextListFormat.ListDecimal,
                5: QTextListFormat.ListLowerAlpha,
                6: QTextListFormat.ListUpperAlpha,
                7: QTextListFormat.ListLowerRoman,
                8: QTextListFormat.ListUpperRoman,
            }

            style _ styleDict.g..(styleIndex, QTextListFormat.ListDisc)
            cursor.beginEditBlock()
            blockFmt _ cursor.blockFormat()
            listFmt _ QTextListFormat()

            __ cursor.currentList
                listFmt _ cursor.currentList().f..()
            ____
                listFmt.setIndent(blockFmt.indent() + 1)
                blockFmt.setIndent(0)
                cursor.setBlockFormat(blockFmt)

            listFmt.sS..(style)
            cursor.createList(listFmt)
            cursor.endEditBlock()
        ____
            bfmt _ QTextBlockFormat()
            bfmt.setObjectIndex(-1)
            cursor.mergeBlockFormat(bfmt)

    ___ textColor 
        col _ QColorDialog.getColor(textEdit.textColor(), self)
        __ no. col.isValid
            r_

        fmt _ QTextCharFormat()
        fmt.setForeground(col)
        mergeFormatOnWordOrSelection(fmt)
        colorChanged(col)

    ___ textAlign  action):
        __ action __ actionAlignLeft:
            textEdit.setAlignment(__.AlignLeft | __.AlignAbsolute)
        ____ action __ actionAlignCenter:
            textEdit.setAlignment(__.AlignHCenter)
        ____ action __ actionAlignRight:
            textEdit.setAlignment(__.AlignRight | __.AlignAbsolute)
        ____ action __ actionAlignJustify:
            textEdit.setAlignment(__.AlignJustify)

    ___ currentCharFormatChanged  f..):
        fontChanged(f...font())
        colorChanged(f...foreground().color())

    ___ cursorPositionChanged 
        alignmentChanged(textEdit.alignment())

    ___ clipboardDataChanged 
        actionPaste.sE..(le.(?A...clipboard().t__()) !_ 0)

    ___ about 
        ?MB...about  "About",
                "This example demonstrates Qt's rich text editing facilities "
                "in action, providing an example document for you to "
                "experiment with.")

    ___ mergeFormatOnWordOrSelection  f..):
        cursor _ textEdit.textCursor()
        __ no. cursor.hasSelection
            cursor.select(QTextCursor.WordUnderCursor)

        cursor.mergeCharFormat(f..)
        textEdit.mergeCurrentCharFormat(f..)

    ___ fontChanged  font):
        comboFont.sCI..(
                comboFont.findText(QFontInfo(font).family()))
        comboSize.sCI..(
                comboSize.findText("%s" % font.pointSize()))
        actionTextBold.sC__(font.bold())
        actionTextItalic.sC__(font.italic())
        actionTextUnderline.sC__(font.underline())

    ___ colorChanged  color):
        pix _ ?P..(16, 16)
        pix.fill(color)
        actionTextColor.sI..(?I..(pix))

    ___ alignmentChanged  alignment):
        __ alignment & __.AlignLeft:
            actionAlignLeft.sC__( st.
        ____ alignment & __.AlignHCenter:
            actionAlignCenter.sC__( st.
        ____ alignment & __.AlignRight:
            actionAlignRight.sC__( st.
        ____ alignment & __.AlignJustify:
            actionAlignJustify.sC__( st.


__ ______ __ ______
    app _ ?A..(___.a..

    mainWindows _   # list
    ___ fn __ ___.argv[1:] or [N..]:
        textEdit _ TextEdit(fn)
        textEdit.r..(700, 800)
        textEdit.s..
        mainWindows.ap..(textEdit)

    ___.e.. ?.e..
