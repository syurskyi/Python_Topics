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
____ ?.QtGui ______ (QFont, QFontDatabase, QFontInfo, QIcon, QKeySequence,
        QPixmap, QTextBlockFormat, QTextCharFormat, QTextCursor,
        QTextDocumentWriter, QTextListFormat)
____ ?.?W.. ______ (QAction, QActionGroup, QApplication, QColorDialog,
        QComboBox, QFileDialog, QFontComboBox, QMainWindow, QMenu, QMessageBox,
        QTextEdit, QToolBar)
____ ?.QtPrintSupport ______ QPrintDialog, QPrinter, QPrintPreviewDialog

______ textedit_rc


if sys.platform.startswith('darwin'):
    rsrcPath _ ":/images/mac"
else:
    rsrcPath _ ":/images/win"


class TextEdit(QMainWindow):
    ___ __init__(self, fileName_None, parent_None):
        super(TextEdit, self).__init__(parent)

        self.setWindowIcon(QIcon(':/images/logo.png'))
        self.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.setupFileActions()
        self.setupEditActions()
        self.setupTextActions()

        helpMenu _ QMenu("Help", self)
        self.menuBar().addMenu(helpMenu)
        helpMenu.addAction("About", self.about)
        helpMenu.addAction("About &Qt", QApplication.instance().aboutQt)
 
        self.textEdit _ QTextEdit(self)
        self.textEdit.currentCharFormatChanged.c..(
                self.currentCharFormatChanged)
        self.textEdit.cursorPositionChanged.c..(self.cursorPositionChanged)
        self.setCentralWidget(self.textEdit)
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
        self.setWindowModified(self.textEdit.document().isModified())
        self.actionSave.setEnabled(self.textEdit.document().isModified())
        self.actionUndo.setEnabled(self.textEdit.document().isUndoAvailable())
        self.actionRedo.setEnabled(self.textEdit.document().isRedoAvailable())
        self.actionUndo.triggered.c..(self.textEdit.undo)
        self.actionRedo.triggered.c..(self.textEdit.redo)
        self.actionCut.setEnabled(False)
        self.actionCopy.setEnabled(False)
        self.actionCut.triggered.c..(self.textEdit.cut)
        self.actionCopy.triggered.c..(self.textEdit.copy)
        self.actionPaste.triggered.c..(self.textEdit.paste)
        self.textEdit.copyAvailable.c..(self.actionCut.setEnabled)
        self.textEdit.copyAvailable.c..(self.actionCopy.setEnabled)
        QApplication.clipboard().dataChanged.c..(self.clipboardDataChanged)

        if fileName is None:
            fileName _ ':/example.html'

        if not self.load(fileName):
            self.fileNew()

    ___ closeEvent(self, e):
        if self.maybeSave
            e.accept()
        else:
            e.ignore()

    ___ setupFileActions(self):
        tb _ QToolBar(self)
        tb.setWindowTitle("File Actions")
        self.addToolBar(tb)

        menu _ QMenu("&File", self)
        self.menuBar().addMenu(menu)

        self.actionNew _ QAction(
                QIcon.fromTheme('document-new',
                        QIcon(rsrcPath + '/filenew.png')),
                "&New", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.New, triggered_self.fileNew)
        tb.addAction(self.actionNew)
        menu.addAction(self.actionNew)

        self.actionOpen _ QAction(
                QIcon.fromTheme('document-open',
                        QIcon(rsrcPath + '/fileopen.png')),
                "&Open...", self, shortcut_QKeySequence.Open,
                triggered_self.fileOpen)
        tb.addAction(self.actionOpen)
        menu.addAction(self.actionOpen)
        menu.addSeparator()

        self.actionSave _ QAction(
                QIcon.fromTheme('document-save',
                        QIcon(rsrcPath + '/filesave.png')),
                "&Save", self, shortcut_QKeySequence.Save,
                triggered_self.fileSave, enabled_False)
        tb.addAction(self.actionSave)
        menu.addAction(self.actionSave)

        self.actionSaveAs _ QAction("Save &As...", self,
                priority_QAction.LowPriority,
                shortcut_Qt.CTRL + Qt.SHIFT + Qt.Key_S,
                triggered_self.fileSaveAs)
        menu.addAction(self.actionSaveAs)
        menu.addSeparator()
 
        self.actionPrint _ QAction(
                QIcon.fromTheme('document-print',
                        QIcon(rsrcPath + '/fileprint.png')),
                "&Print...", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Print, triggered_self.filePrint)
        tb.addAction(self.actionPrint)
        menu.addAction(self.actionPrint)

        self.actionPrintPreview _ QAction(
                QIcon.fromTheme('fileprint',
                        QIcon(rsrcPath + '/fileprint.png')),
                "Print Preview...", self,
                shortcut_Qt.CTRL + Qt.SHIFT + Qt.Key_P,
                triggered_self.filePrintPreview)
        menu.addAction(self.actionPrintPreview)

        self.actionPrintPdf _ QAction(
                QIcon.fromTheme('exportpdf',
                        QIcon(rsrcPath + '/exportpdf.png')),
                "&Export PDF...", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + Qt.Key_D,
                triggered_self.filePrintPdf)
        tb.addAction(self.actionPrintPdf)
        menu.addAction(self.actionPrintPdf)
        menu.addSeparator()

        self.actionQuit _ QAction("&Quit", self, shortcut_QKeySequence.Quit,
                triggered_self.close)
        menu.addAction(self.actionQuit)

    ___ setupEditActions(self):
        tb _ QToolBar(self)
        tb.setWindowTitle("Edit Actions")
        self.addToolBar(tb)

        menu _ QMenu("&Edit", self)
        self.menuBar().addMenu(menu)

        self.actionUndo _ QAction(
                QIcon.fromTheme('edit-undo',
                        QIcon(rsrcPath + '/editundo.png')),
                "&Undo", self, shortcut_QKeySequence.Undo)
        tb.addAction(self.actionUndo)
        menu.addAction(self.actionUndo)

        self.actionRedo _ QAction(
                QIcon.fromTheme('edit-redo',
                        QIcon(rsrcPath + '/editredo.png')),
                "&Redo", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Redo)
        tb.addAction(self.actionRedo)
        menu.addAction(self.actionRedo)
        menu.addSeparator()

        self.actionCut _ QAction(
                QIcon.fromTheme('edit-cut', QIcon(rsrcPath + '/editcut.png')),
                "Cu&t", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Cut)
        tb.addAction(self.actionCut)
        menu.addAction(self.actionCut)

        self.actionCopy _ QAction(
                QIcon.fromTheme('edit-copy',
                        QIcon(rsrcPath + '/editcopy.png')),
                "&Copy", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Copy)
        tb.addAction(self.actionCopy)
        menu.addAction(self.actionCopy)

        self.actionPaste _ QAction(
                QIcon.fromTheme('edit-paste',
                        QIcon(rsrcPath + '/editpaste.png')),
                "&Paste", self, priority_QAction.LowPriority,
                shortcut_QKeySequence.Paste,
                enabled_(len(QApplication.clipboard().text()) !_ 0))
        tb.addAction(self.actionPaste)
        menu.addAction(self.actionPaste)

    ___ setupTextActions(self):
        tb _ QToolBar(self)
        tb.setWindowTitle("Format Actions")
        self.addToolBar(tb)

        menu _ QMenu("F&ormat", self)
        self.menuBar().addMenu(menu)

        self.actionTextBold _ QAction(
                QIcon.fromTheme('format-text-bold',
                        QIcon(rsrcPath + '/textbold.png')),
                "&Bold", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + Qt.Key_B, triggered_self.textBold,
                checkable_True)
        bold _ QFont()
        bold.setBold(True)
        self.actionTextBold.setFont(bold)
        tb.addAction(self.actionTextBold)
        menu.addAction(self.actionTextBold)

        self.actionTextItalic _ QAction(
                QIcon.fromTheme('format-text-italic',
                        QIcon(rsrcPath + '/textitalic.png')),
                "&Italic", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + Qt.Key_I, triggered_self.textItalic,
                checkable_True)
        italic _ QFont()
        italic.setItalic(True)
        self.actionTextItalic.setFont(italic)
        tb.addAction(self.actionTextItalic)
        menu.addAction(self.actionTextItalic)

        self.actionTextUnderline _ QAction(
                QIcon.fromTheme('format-text-underline',
                        QIcon(rsrcPath + '/textunder.png')),
                "&Underline", self, priority_QAction.LowPriority,
                shortcut_Qt.CTRL + Qt.Key_U, triggered_self.textUnderline,
                checkable_True)
        underline _ QFont()
        underline.setUnderline(True)
        self.actionTextUnderline.setFont(underline)
        tb.addAction(self.actionTextUnderline)
        menu.addAction(self.actionTextUnderline)

        menu.addSeparator()

        grp _ QActionGroup(self, triggered_self.textAlign)

        # Make sure the alignLeft is always left of the alignRight.
        if QApplication.isLeftToRight
            self.actionAlignLeft _ QAction(
                    QIcon.fromTheme('format-justify-left',
                            QIcon(rsrcPath + '/textleft.png')),
                    "&Left", grp)
            self.actionAlignCenter _ QAction(
                    QIcon.fromTheme('format-justify-center',
                            QIcon(rsrcPath + '/textcenter.png')),
                    "C&enter", grp)
            self.actionAlignRight _ QAction(
                    QIcon.fromTheme('format-justify-right',
                            QIcon(rsrcPath + '/textright.png')),
                    "&Right", grp)
        else:
            self.actionAlignRight _ QAction(
                    QIcon.fromTheme('format-justify-right',
                            QIcon(rsrcPath + '/textright.png')),
                    "&Right", grp)
            self.actionAlignCenter _ QAction(
                    QIcon.fromTheme('format-justify-center',
                            QIcon(rsrcPath + '/textcenter.png')),
                    "C&enter", grp)
            self.actionAlignLeft _ QAction(
                    QIcon.fromTheme('format-justify-left',
                            QIcon(rsrcPath + '/textleft.png')),
                    "&Left", grp)
 
        self.actionAlignJustify _ QAction(
                QIcon.fromTheme('format-justify-fill',
                        QIcon(rsrcPath + '/textjustify.png')),
                "&Justify", grp)

        self.actionAlignLeft.setShortcut(Qt.CTRL + Qt.Key_L)
        self.actionAlignLeft.setCheckable(True)
        self.actionAlignLeft.setPriority(QAction.LowPriority)

        self.actionAlignCenter.setShortcut(Qt.CTRL + Qt.Key_E)
        self.actionAlignCenter.setCheckable(True)
        self.actionAlignCenter.setPriority(QAction.LowPriority)

        self.actionAlignRight.setShortcut(Qt.CTRL + Qt.Key_R)
        self.actionAlignRight.setCheckable(True)
        self.actionAlignRight.setPriority(QAction.LowPriority)

        self.actionAlignJustify.setShortcut(Qt.CTRL + Qt.Key_J)
        self.actionAlignJustify.setCheckable(True)
        self.actionAlignJustify.setPriority(QAction.LowPriority)

        tb.addActions(grp.actions())
        menu.addActions(grp.actions())
        menu.addSeparator()

        pix _ QPixmap(16, 16)
        pix.fill(Qt.black)
        self.actionTextColor _ QAction(QIcon(pix), "&Color...", self,
                triggered_self.textColor)
        tb.addAction(self.actionTextColor)
        menu.addAction(self.actionTextColor)

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
                        "%s" % (QApplication.font().pointSize())))

    ___ load(self, f):
        if not QFile.exists(f):
            return False

        fh _ QFile(f)
        if not fh.open(QFile.ReadOnly):
            return False

        data _ fh.readAll()
        codec _ QTextCodec.codecForHtml(data)
        unistr _ codec.toUnicode(data)

        if Qt.mightBeRichText(unistr):
            self.textEdit.setHtml(unistr)
        else:
            self.textEdit.setPlainText(unistr)

        self.setCurrentFileName(f)
        return True

    ___ maybeSave(self):
        if not self.textEdit.document().isModified
            return True

        if self.fileName.startswith(':/'):
            return True

        ret _ QMessageBox.warning(self, "Application",
                "The document has been modified.\n"
                "Do you want to save your changes?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

        if ret == QMessageBox.Save:
            return self.fileSave()

        if ret == QMessageBox.Cancel:
            return False

        return True

    ___ setCurrentFileName(self, fileName_''):
        self.fileName _ fileName
        self.textEdit.document().setModified(False)

        if not fileName:
            shownName _ 'untitled.txt'
        else:
            shownName _ QFileInfo(fileName).fileName()

        self.setWindowTitle(self.tr("%s[*] - %s" % (shownName, "Rich Text")))
        self.setWindowModified(False)

    ___ fileNew(self):
        if self.maybeSave
            self.textEdit.clear()
            self.setCurrentFileName()

    ___ fileOpen(self):
        fn, _ _ QFileDialog.getOpenFileName(self, "Open File...", None,
                "HTML-Files (*.htm *.html);;All Files (*)")

        if fn:
            self.load(fn)

    ___ fileSave(self):
        if not self.fileName:
            return self.fileSaveAs()

        writer _ QTextDocumentWriter(self.fileName)
        success _ writer.write(self.textEdit.document())
        if success:
            self.textEdit.document().setModified(False)

        return success

    ___ fileSaveAs(self):
        fn, _ _ QFileDialog.getSaveFileName(self, "Save as...", None,
                "ODF files (*.odt);;HTML-Files (*.htm *.html);;All Files (*)")

        if not fn:
            return False

        lfn _ fn.lower()
        if not lfn.endswith(('.odt', '.htm', '.html')):
            # The default.
            fn +_ '.odt'

        self.setCurrentFileName(fn)
        return self.fileSave()

    ___ filePrint(self):
        printer _ QPrinter(QPrinter.HighResolution)
        dlg _ QPrintDialog(printer, self)

        if self.textEdit.textCursor().hasSelection
            dlg.addEnabledOption(QPrintDialog.PrintSelection)

        dlg.setWindowTitle("Print Document")

        if dlg.e.. == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

        del dlg

    ___ filePrintPreview(self):
        printer _ QPrinter(QPrinter.HighResolution)
        preview _ QPrintPreviewDialog(printer, self)
        preview.paintRequested.c..(self.printPreview)
        preview.e..

    ___ printPreview(self, printer):
        self.textEdit.print_(printer)

    ___ filePrintPdf(self):
        fn, _ _ QFileDialog.getSaveFileName(self, "Export PDF", None,
                "PDF files (*.pdf);;All Files (*)")

        if fn:
            if QFileInfo(fn).suffix().isEmpty
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

    ___ textFamily(self, family):
        fmt _ QTextCharFormat()
        fmt.setFontFamily(family)
        self.mergeFormatOnWordOrSelection(fmt)

    ___ textSize(self, pointSize):
        pointSize _ float(pointSize)
        if pointSize > 0:
            fmt _ QTextCharFormat()
            fmt.setFontPointSize(pointSize)
            self.mergeFormatOnWordOrSelection(fmt)

    ___ textStyle(self, styleIndex):
        cursor _ self.textEdit.textCursor()
        if styleIndex:
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

            if cursor.currentList
                listFmt _ cursor.currentList().format()
            else:
                listFmt.setIndent(blockFmt.indent() + 1)
                blockFmt.setIndent(0)
                cursor.setBlockFormat(blockFmt)

            listFmt.setStyle(style)
            cursor.createList(listFmt)
            cursor.endEditBlock()
        else:
            bfmt _ QTextBlockFormat()
            bfmt.setObjectIndex(-1)
            cursor.mergeBlockFormat(bfmt)

    ___ textColor(self):
        col _ QColorDialog.getColor(self.textEdit.textColor(), self)
        if not col.isValid
            return

        fmt _ QTextCharFormat()
        fmt.setForeground(col)
        self.mergeFormatOnWordOrSelection(fmt)
        self.colorChanged(col)

    ___ textAlign(self, action):
        if action == self.actionAlignLeft:
            self.textEdit.setAlignment(Qt.AlignLeft | Qt.AlignAbsolute)
        elif action == self.actionAlignCenter:
            self.textEdit.setAlignment(Qt.AlignHCenter)
        elif action == self.actionAlignRight:
            self.textEdit.setAlignment(Qt.AlignRight | Qt.AlignAbsolute)
        elif action == self.actionAlignJustify:
            self.textEdit.setAlignment(Qt.AlignJustify)

    ___ currentCharFormatChanged(self, format):
        self.fontChanged(format.font())
        self.colorChanged(format.foreground().color())

    ___ cursorPositionChanged(self):
        self.alignmentChanged(self.textEdit.alignment())

    ___ clipboardDataChanged(self):
        self.actionPaste.setEnabled(len(QApplication.clipboard().text()) !_ 0)

    ___ about(self):
        QMessageBox.about(self, "About", 
                "This example demonstrates Qt's rich text editing facilities "
                "in action, providing an example document for you to "
                "experiment with.")

    ___ mergeFormatOnWordOrSelection(self, format):
        cursor _ self.textEdit.textCursor()
        if not cursor.hasSelection
            cursor.select(QTextCursor.WordUnderCursor)

        cursor.mergeCharFormat(format)
        self.textEdit.mergeCurrentCharFormat(format)

    ___ fontChanged(self, font):
        self.comboFont.setCurrentIndex(
                self.comboFont.findText(QFontInfo(font).family()))
        self.comboSize.setCurrentIndex(
                self.comboSize.findText("%s" % font.pointSize()))
        self.actionTextBold.setChecked(font.bold())
        self.actionTextItalic.setChecked(font.italic())
        self.actionTextUnderline.setChecked(font.underline())

    ___ colorChanged(self, color):
        pix _ QPixmap(16, 16)
        pix.fill(color)
        self.actionTextColor.setIcon(QIcon(pix))

    ___ alignmentChanged(self, alignment):
        if alignment & Qt.AlignLeft:
            self.actionAlignLeft.setChecked(True)
        elif alignment & Qt.AlignHCenter:
            self.actionAlignCenter.setChecked(True)
        elif alignment & Qt.AlignRight:
            self.actionAlignRight.setChecked(True)
        elif alignment & Qt.AlignJustify:
            self.actionAlignJustify.setChecked(True)


if __name__ == '__main__':
    app _ QApplication(sys.argv)

    mainWindows _ []
    for fn in sys.argv[1:] or [None]:
        textEdit _ TextEdit(fn)
        textEdit.resize(700, 800)
        textEdit.s..
        mainWindows.append(textEdit)

    sys.exit(app.exec_())
