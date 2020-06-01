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


______ sys

____ ?.QtCore ______ QFile, QFileInfo, Qt, QTextCodec
____ ?.?G.. ______ (QFont, QFontDatabase, QFontInfo, QIcon, ?KS..,
        QPixmap, QTextBlockFormat, QTextCharFormat, QTextCursor,
        QTextDocumentWriter, QTextListFormat)
____ ?.?W.. ______ (?A.., QActionGroup, ?A.., QColorDialog,
        QComboBox, ?FD.., QFontComboBox, QMainWindow, QMenu, ?MB..,
        QTextEdit, QToolBar)
____ ?.QtPrintSupport ______ QPrintDialog, QPrinter, QPrintPreviewDialog

______ textedit_rc


__ sys.platform.startswith('darwin'):
    rsrcPath _ ":/images/mac"
____
    rsrcPath _ ":/images/win"


c_ TextEdit ?MW..
    ___ __init__  fileName_None, parent_None):
        super(TextEdit, self).__init__(parent)

        self.setWindowIcon(QIcon(':/images/logo.png'))
        self.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.setupFileActions()
        self.setupEditActions()
        self.setupTextActions()

        helpMenu _ QMenu("Help", self)
        self.mB.. .aM..(helpMenu)
        helpMenu.aA..("About", self.about)
        helpMenu.aA..("About &Qt", ?A...instance().aboutQt)
 
        self.textEdit _ QTextEdit(self)
        self.textEdit.currentCharFormatChanged.c..(
                self.currentCharFormatChanged)
        self.textEdit.cursorPositionChanged.c..(self.cursorPositionChanged)
        self.sCW..(self.textEdit)
        self.textEdit.setFocus()
        self.setCurrentFileName()
        self.fontChanged(self.textEdit.font())
        self.colorChanged(self.textEdit.textColor())
        self.alignmentChanged(self.textEdit.alignment())
        self.textEdit.document().modificationChanged.c..(
                self.actionSave.setEnabled)
        self.textEdit.document().modificationChanged.c..(
                self.setWindowModified)
        self.textEdit.document().undoAvailable.c..(
                self.actionUndo.setEnabled)
        self.textEdit.document().redoAvailable.c..(
                self.actionRedo.setEnabled)
        self.setWindowModified(self.textEdit.document().iM..())
        self.actionSave.setEnabled(self.textEdit.document().iM..())
        self.actionUndo.setEnabled(self.textEdit.document().isUndoAvailable())
        self.actionRedo.setEnabled(self.textEdit.document().isRedoAvailable())
        self.actionUndo.t__.c..(self.textEdit.undo)
        self.actionRedo.t__.c..(self.textEdit.redo)
        self.actionCut.setEnabled F..
        self.actionCopy.setEnabled F..
        self.actionCut.t__.c..(self.textEdit.cut)
        self.actionCopy.t__.c..(self.textEdit.copy)
        self.actionPaste.t__.c..(self.textEdit.paste)
        self.textEdit.copyAvailable.c..(self.actionCut.setEnabled)
        self.textEdit.copyAvailable.c..(self.actionCopy.setEnabled)
        ?A...clipboard().dataChanged.c..(self.clipboardDataChanged)

        __ fileName __ N..:
            fileName _ ':/example.html'

        __ no. self.load(fileName):
            self.fileNew()

    ___ closeEvent  e):
        __ self.maybeSave
            e.accept()
        ____
            e.ignore()

    ___ setupFileActions(self):
        tb _ QToolBar(self)
        tb.setWindowTitle("File Actions")
        self.addToolBar(tb)

        menu _ QMenu("&File", self)
        self.mB.. .aM..(menu)

        self.actionNew _ ?A..(
                QIcon.fromTheme('document-new',
                        QIcon(rsrcPath + '/filenew.png')),
                "&New", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.New, triggered_self.fileNew)
        tb.aA..(self.actionNew)
        menu.aA..(self.actionNew)

        self.actionOpen _ ?A..(
                QIcon.fromTheme('document-open',
                        QIcon(rsrcPath + '/fileopen.png')),
                "&Open...", self, shortcut_QKeySequence.Open,
                triggered_self.fileOpen)
        tb.aA..(self.actionOpen)
        menu.aA..(self.actionOpen)
        menu.addSeparator()

        self.actionSave _ ?A..(
                QIcon.fromTheme('document-save',
                        QIcon(rsrcPath + '/filesave.png')),
                "&Save", self, shortcut_QKeySequence.Save,
                triggered_self.fileSave, enabled_False)
        tb.aA..(self.actionSave)
        menu.aA..(self.actionSave)

        self.actionSaveAs _ ?A..("Save &As...", self,
                priority_QAction.LowPriority,
                shortcut_Qt.CTRL + Qt.SHIFT + Qt.Key_S,
                triggered_self.fileSaveAs)
        menu.aA..(self.actionSaveAs)
        menu.addSeparator()
 
        self.actionPrint _ ?A..(
                QIcon.fromTheme('document-print',
                        QIcon(rsrcPath + '/fileprint.png')),
                "&Print...", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Print, triggered_self.filePrint)
        tb.aA..(self.actionPrint)
        menu.aA..(self.actionPrint)

        self.actionPrintPreview _ ?A..(
                QIcon.fromTheme('fileprint',
                        QIcon(rsrcPath + '/fileprint.png')),
                "Print Preview...", self,
                shortcut_Qt.CTRL + Qt.SHIFT + Qt.Key_P,
                triggered_self.filePrintPreview)
        menu.aA..(self.actionPrintPreview)

        self.actionPrintPdf _ ?A..(
                QIcon.fromTheme('exportpdf',
                        QIcon(rsrcPath + '/exportpdf.png')),
                "&Export PDF...", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + Qt.Key_D,
                triggered_self.filePrintPdf)
        tb.aA..(self.actionPrintPdf)
        menu.aA..(self.actionPrintPdf)
        menu.addSeparator()

        self.actionQuit _ ?A..("&Quit", self, shortcut_QKeySequence.Quit,
                triggered_self.close)
        menu.aA..(self.actionQuit)

    ___ setupEditActions(self):
        tb _ QToolBar(self)
        tb.setWindowTitle("Edit Actions")
        self.addToolBar(tb)

        menu _ QMenu("&Edit", self)
        self.mB.. .aM..(menu)

        self.actionUndo _ ?A..(
                QIcon.fromTheme('edit-undo',
                        QIcon(rsrcPath + '/editundo.png')),
                "&Undo", self, shortcut_QKeySequence.Undo)
        tb.aA..(self.actionUndo)
        menu.aA..(self.actionUndo)

        self.actionRedo _ ?A..(
                QIcon.fromTheme('edit-redo',
                        QIcon(rsrcPath + '/editredo.png')),
                "&Redo", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Redo)
        tb.aA..(self.actionRedo)
        menu.aA..(self.actionRedo)
        menu.addSeparator()

        self.actionCut _ ?A..(
                QIcon.fromTheme('edit-cut', QIcon(rsrcPath + '/editcut.png')),
                "Cu&t", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Cut)
        tb.aA..(self.actionCut)
        menu.aA..(self.actionCut)

        self.actionCopy _ ?A..(
                QIcon.fromTheme('edit-copy',
                        QIcon(rsrcPath + '/editcopy.png')),
                "&Copy", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Copy)
        tb.aA..(self.actionCopy)
        menu.aA..(self.actionCopy)

        self.actionPaste _ ?A..(
                QIcon.fromTheme('edit-paste',
                        QIcon(rsrcPath + '/editpaste.png')),
                "&Paste", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Paste,
                enabled_(len(?A...clipboard().text()) !_ 0))
        tb.aA..(self.actionPaste)
        menu.aA..(self.actionPaste)

    ___ setupTextActions(self):
        tb _ QToolBar(self)
        tb.setWindowTitle("Format Actions")
        self.addToolBar(tb)

        menu _ QMenu("F&ormat", self)
        self.mB.. .aM..(menu)

        self.actionTextBold _ ?A..(
                QIcon.fromTheme('format-text-bold',
                        QIcon(rsrcPath + '/textbold.png')),
                "&Bold", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + Qt.Key_B, triggered_self.textBold,
                checkable_True)
        bold _ QFont()
        bold.setBold(True)
        self.actionTextBold.setFont(bold)
        tb.aA..(self.actionTextBold)
        menu.aA..(self.actionTextBold)

        self.actionTextItalic _ ?A..(
                QIcon.fromTheme('format-text-italic',
                        QIcon(rsrcPath + '/textitalic.png')),
                "&Italic", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + Qt.Key_I, triggered_self.textItalic,
                checkable_True)
        italic _ QFont()
        italic.setItalic(True)
        self.actionTextItalic.setFont(italic)
        tb.aA..(self.actionTextItalic)
        menu.aA..(self.actionTextItalic)

        self.actionTextUnderline _ ?A..(
                QIcon.fromTheme('format-text-underline',
                        QIcon(rsrcPath + '/textunder.png')),
                "&Underline", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + Qt.Key_U, triggered_self.textUnderline,
                checkable_True)
        underline _ QFont()
        underline.setUnderline(True)
        self.actionTextUnderline.setFont(underline)
        tb.aA..(self.actionTextUnderline)
        menu.aA..(self.actionTextUnderline)

        menu.addSeparator()

        grp _ QActionGroup  triggered_self.textAlign)

        # Make sure the alignLeft is always left of the alignRight.
        __ ?A...isLeftToRight
            self.actionAlignLeft _ ?A..(
                    QIcon.fromTheme('format-justify-left',
                            QIcon(rsrcPath + '/textleft.png')),
                    "&Left", grp)
            self.actionAlignCenter _ ?A..(
                    QIcon.fromTheme('format-justify-center',
                            QIcon(rsrcPath + '/textcenter.png')),
                    "C&enter", grp)
            self.actionAlignRight _ ?A..(
                    QIcon.fromTheme('format-justify-right',
                            QIcon(rsrcPath + '/textright.png')),
                    "&Right", grp)
        ____
            self.actionAlignRight _ ?A..(
                    QIcon.fromTheme('format-justify-right',
                            QIcon(rsrcPath + '/textright.png')),
                    "&Right", grp)
            self.actionAlignCenter _ ?A..(
                    QIcon.fromTheme('format-justify-center',
                            QIcon(rsrcPath + '/textcenter.png')),
                    "C&enter", grp)
            self.actionAlignLeft _ ?A..(
                    QIcon.fromTheme('format-justify-left',
                            QIcon(rsrcPath + '/textleft.png')),
                    "&Left", grp)
 
        self.actionAlignJustify _ ?A..(
                QIcon.fromTheme('format-justify-fill',
                        QIcon(rsrcPath + '/textjustify.png')),
                "&Justify", grp)

        self.actionAlignLeft.sS..(Qt.CTRL + Qt.Key_L)
        self.actionAlignLeft.setCheckable(True)
        self.actionAlignLeft.setPriority(?A...LowPriority)

        self.actionAlignCenter.sS..(Qt.CTRL + Qt.Key_E)
        self.actionAlignCenter.setCheckable(True)
        self.actionAlignCenter.setPriority(?A...LowPriority)

        self.actionAlignRight.sS..(Qt.CTRL + Qt.Key_R)
        self.actionAlignRight.setCheckable(True)
        self.actionAlignRight.setPriority(?A...LowPriority)

        self.actionAlignJustify.sS..(Qt.CTRL + Qt.Key_J)
        self.actionAlignJustify.setCheckable(True)
        self.actionAlignJustify.setPriority(?A...LowPriority)

        tb.addActions(grp.actions())
        menu.addActions(grp.actions())
        menu.addSeparator()

        pix _ QPixmap(16, 16)
        pix.fill(Qt.black)
        self.actionTextColor _ ?A..(QIcon(pix), "&Color...", self,
                triggered_self.textColor)
        tb.aA..(self.actionTextColor)
        menu.aA..(self.actionTextColor)

        tb _ QToolBar(self)
        tb.setAllowedAreas(Qt.TopToolBarArea | Qt.BottomToolBarArea)
        tb.setWindowTitle("Format Actions")
        self.addToolBarBreak(Qt.TopToolBarArea)
        self.addToolBar(tb)

        comboStyle _ QComboBox(tb)
        tb.addWidget(comboStyle)
        comboStyle.addItem("Standard")
        comboStyle.addItem("Bullet List (Disc)")
        comboStyle.addItem("Bullet List (Circle)")
        comboStyle.addItem("Bullet List (Square)")
        comboStyle.addItem("Ordered List (Decimal)")
        comboStyle.addItem("Ordered List (Alpha lower)")
        comboStyle.addItem("Ordered List (Alpha upper)")
        comboStyle.addItem("Ordered List (Roman lower)")
        comboStyle.addItem("Ordered List (Roman upper)")
        comboStyle.activated.c..(self.textStyle)

        self.comboFont _ QFontComboBox(tb)
        tb.addWidget(self.comboFont)
        self.comboFont.activated[str].c..(self.textFamily)

        self.comboSize _ QComboBox(tb)
        self.comboSize.setObjectName("comboSize")
        tb.addWidget(self.comboSize)
        self.comboSize.setEditable(True)

        db _ QFontDatabase()
        for size in db.standardSizes
            self.comboSize.addItem("%s" % (size))

        self.comboSize.activated[str].c..(self.textSize)
        self.comboSize.setCurrentIndex(
                self.comboSize.findText(
                        "%s" % (?A...font().pointSize())))

    ___ load  f):
        __ no. QFile.exists(f):
            r_ False

        fh _ QFile(f)
        __ no. fh.o..(QFile.ReadOnly):
            r_ False

        data _ fh.readAll()
        codec _ QTextCodec.codecForHtml(data)
        unistr _ codec.toUnicode(data)

        __ Qt.mightBeRichText(unistr):
            self.textEdit.setHtml(unistr)
        ____
            self.textEdit.sPT..(unistr)

        self.setCurrentFileName(f)
        r_ True

    ___ maybeSave(self):
        __ no. self.textEdit.document().iM..
            r_ True

        __ self.fileName.startswith(':/'):
            r_ True

        ret _ ?MB...warning  "Application",
                "The document has been modified.\n"
                "Do you want to save your changes?",
                ?MB...Save | ?MB...Discard | ?MB...Cancel)

        __ ret == ?MB...Save:
            r_ self.fileSave()

        __ ret == ?MB...Cancel:
            r_ False

        r_ True

    ___ setCurrentFileName  fileName_''):
        self.fileName _ fileName
        self.textEdit.document().setModified F..

        __ no. fileName:
            shownName _ 'untitled.txt'
        ____
            shownName _ QFileInfo(fileName).fileName()

        self.setWindowTitle(self.tr("%s[*] - %s" % (shownName, "Rich Text")))
        self.setWindowModified F..

    ___ fileNew(self):
        __ self.maybeSave
            self.textEdit.clear()
            self.setCurrentFileName()

    ___ fileOpen(self):
        fn, _ _ ?FD...gOFN..  "Open File...", N..,
                "HTML-Files (*.htm *.html);;All Files (*)")

        __ fn:
            self.load(fn)

    ___ fileSave(self):
        __ no. self.fileName:
            r_ self.fileSaveAs()

        writer _ QTextDocumentWriter(self.fileName)
        success _ writer.w..(self.textEdit.document())
        __ success:
            self.textEdit.document().setModified F..

        r_ success

    ___ fileSaveAs(self):
        fn, _ _ ?FD...getSaveFileName  "Save as...", N..,
                "ODF files (*.odt);;HTML-Files (*.htm *.html);;All Files (*)")

        __ no. fn:
            r_ False

        lfn _ fn.lower()
        __ no. lfn.endswith(('.odt', '.htm', '.html')):
            # The default.
            fn +_ '.odt'

        self.setCurrentFileName(fn)
        r_ self.fileSave()

    ___ filePrint(self):
        printer _ QPrinter(QPrinter.HighResolution)
        dlg _ QPrintDialog(printer, self)

        __ self.textEdit.textCursor().hasSelection
            dlg.addEnabledOption(QPrintDialog.PrintSelection)

        dlg.setWindowTitle("Print Document")

        __ dlg.e.. == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

        del dlg

    ___ filePrintPreview(self):
        printer _ QPrinter(QPrinter.HighResolution)
        preview _ QPrintPreviewDialog(printer, self)
        preview.paintRequested.c..(self.printPreview)
        preview.e..

    ___ printPreview  printer):
        self.textEdit.print_(printer)

    ___ filePrintPdf(self):
        fn, _ _ ?FD...getSaveFileName  "Export PDF", N..,
                "PDF files (*.pdf);;All Files (*)")

        __ fn:
            __ QFileInfo(fn).suffix().isEmpty
                fn +_ '.pdf'

            printer _ QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)

    ___ textBold(self):
        fmt _ QTextCharFormat()
        fmt.setFontWeight(self.actionTextBold.isChecked() and QFont.Bold or QFont.Normal)
        self.mergeFormatOnWordOrSelection(fmt)

    ___ textUnderline(self):
        fmt _ QTextCharFormat()
        fmt.setFontUnderline(self.actionTextUnderline.isChecked())
        self.mergeFormatOnWordOrSelection(fmt)

    ___ textItalic(self):
        fmt _ QTextCharFormat()
        fmt.setFontItalic(self.actionTextItalic.isChecked())
        self.mergeFormatOnWordOrSelection(fmt)

    ___ textFamily  family):
        fmt _ QTextCharFormat()
        fmt.setFontFamily(family)
        self.mergeFormatOnWordOrSelection(fmt)

    ___ textSize  pointSize):
        pointSize _ float(pointSize)
        __ pointSize > 0:
            fmt _ QTextCharFormat()
            fmt.setFontPointSize(pointSize)
            self.mergeFormatOnWordOrSelection(fmt)

    ___ textStyle  styleIndex):
        cursor _ self.textEdit.textCursor()
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

            style _ styleDict.get(styleIndex, QTextListFormat.ListDisc)
            cursor.beginEditBlock()
            blockFmt _ cursor.blockFormat()
            listFmt _ QTextListFormat()

            __ cursor.currentList
                listFmt _ cursor.currentList().format()
            ____
                listFmt.setIndent(blockFmt.indent() + 1)
                blockFmt.setIndent(0)
                cursor.setBlockFormat(blockFmt)

            listFmt.setStyle(style)
            cursor.createList(listFmt)
            cursor.endEditBlock()
        ____
            bfmt _ QTextBlockFormat()
            bfmt.setObjectIndex(-1)
            cursor.mergeBlockFormat(bfmt)

    ___ textColor(self):
        col _ QColorDialog.getColor(self.textEdit.textColor(), self)
        __ no. col.isValid
            r_

        fmt _ QTextCharFormat()
        fmt.setForeground(col)
        self.mergeFormatOnWordOrSelection(fmt)
        self.colorChanged(col)

    ___ textAlign  action):
        __ action == self.actionAlignLeft:
            self.textEdit.setAlignment(Qt.AlignLeft | Qt.AlignAbsolute)
        ____ action == self.actionAlignCenter:
            self.textEdit.setAlignment(Qt.AlignHCenter)
        ____ action == self.actionAlignRight:
            self.textEdit.setAlignment(Qt.AlignRight | Qt.AlignAbsolute)
        ____ action == self.actionAlignJustify:
            self.textEdit.setAlignment(Qt.AlignJustify)

    ___ currentCharFormatChanged  format):
        self.fontChanged(format.font())
        self.colorChanged(format.foreground().color())

    ___ cursorPositionChanged(self):
        self.alignmentChanged(self.textEdit.alignment())

    ___ clipboardDataChanged(self):
        self.actionPaste.setEnabled(len(?A...clipboard().text()) !_ 0)

    ___ about(self):
        ?MB...about  "About",
                "This example demonstrates Qt's rich text editing facilities "
                "in action, providing an example document for you to "
                "experiment with.")

    ___ mergeFormatOnWordOrSelection  format):
        cursor _ self.textEdit.textCursor()
        __ no. cursor.hasSelection
            cursor.select(QTextCursor.WordUnderCursor)

        cursor.mergeCharFormat(format)
        self.textEdit.mergeCurrentCharFormat(format)

    ___ fontChanged  font):
        self.comboFont.setCurrentIndex(
                self.comboFont.findText(QFontInfo(font).family()))
        self.comboSize.setCurrentIndex(
                self.comboSize.findText("%s" % font.pointSize()))
        self.actionTextBold.setChecked(font.bold())
        self.actionTextItalic.setChecked(font.italic())
        self.actionTextUnderline.setChecked(font.underline())

    ___ colorChanged  color):
        pix _ QPixmap(16, 16)
        pix.fill(color)
        self.actionTextColor.setIcon(QIcon(pix))

    ___ alignmentChanged  alignment):
        __ alignment & Qt.AlignLeft:
            self.actionAlignLeft.setChecked(True)
        ____ alignment & Qt.AlignHCenter:
            self.actionAlignCenter.setChecked(True)
        ____ alignment & Qt.AlignRight:
            self.actionAlignRight.setChecked(True)
        ____ alignment & Qt.AlignJustify:
            self.actionAlignJustify.setChecked(True)


__ __name__ == '__main__':
    app _ ?A..(sys.argv)

    mainWindows _ []
    for fn in sys.argv[1:] or [N..]:
        textEdit _ TextEdit(fn)
        textEdit.resize(700, 800)
        textEdit.s..
        mainWindows.append(textEdit)

    sys.exit(app.exec_())
