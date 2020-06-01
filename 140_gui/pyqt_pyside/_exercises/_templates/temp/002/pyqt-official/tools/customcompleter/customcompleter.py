#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2012 Digia Plc
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


____ ?.?C.. ______ QFile, QStringListModel, __
____ ?.?G.. ______ QCursor, ?KS.., QTextCursor
____ ?.?W.. ______ (?A.., ?A.., QCompleter, QMainWindow,
        ?MB.., QTextEdit)

______ customcompleter_rc


c_ TextEdit(QTextEdit):
    ___ __init__  parent_None):
        super(TextEdit, self).__init__(parent)

        self._completer _ N..

        self.sPT..(
                "This TextEdit provides autocompletions for words that have "
                "more than 3 characters. You can trigger autocompletion "
                "using %s" % ?KS..("Ctrl+E").toString(
                        ?KS...NativeText))

    ___ setCompleter  c):
        __ self._completer __ no. N..:
            self._completer.activated.disconnect()

        self._completer _ c

        c.setWidget(self)
        c.setCompletionMode(QCompleter.PopupCompletion)
        c.setCaseSensitivity(__.CaseInsensitive)
        c.activated.c..(self.insertCompletion)

    ___ completer(self):
        r_ self._completer

    ___ insertCompletion  completion):
        __ self._completer.widget() __ no. self:
            r_

        tc _ self.textCursor()
        extra _ le.(completion) - le.(self._completer.completionPrefix())
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)

    ___ textUnderCursor(self):
        tc _ self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)

        r_ tc.selectedText()

    ___ focusInEvent  e):
        __ self._completer __ no. N..:
            self._completer.setWidget(self)

        super(TextEdit, self).focusInEvent(e)

    ___ keyPressEvent  e):
        __ self._completer __ no. N.. and self._completer.popup().isVisible
            # The following keys are forwarded by the completer to the widget.
            __ e.key() in (__.Key_Enter, __.Key_Return, __.Key_Escape, __.Key_Tab, __.Key_Backtab):
                e.ignore()
                # Let the completer do default behavior.
                r_

        isShortcut _ ((e.modifiers() & __.ControlModifier) !_ 0 and e.key() == __.Key_E)
        __ self._completer __ N.. or no. isShortcut:
            # Do not process the shortcut when we have a completer.
            super(TextEdit, self).keyPressEvent(e)

        ctrlOrShift _ e.modifiers() & (__.ControlModifier | __.ShiftModifier)
        __ self._completer __ N.. or (ctrlOrShift and le.(e.t__()) == 0):
            r_

        eow _ "~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-="
        hasModifier _ (e.modifiers() !_ __.NoModifier) and no. ctrlOrShift
        completionPrefix _ self.textUnderCursor()

        __ no. isShortcut and (hasModifier or le.(e.t__()) == 0 or le.(completionPrefix) < 3 or e.t__()[-1] in eow):
            self._completer.popup().hide()
            r_

        __ completionPrefix !_ self._completer.completionPrefix
            self._completer.setCompletionPrefix(completionPrefix)
            self._completer.popup().setCurrentIndex(
                    self._completer.completionModel().index(0, 0))

        cr _ self.cursorRect()
        cr.setWidth(self._completer.popup().sizeHintForColumn(0) + self._completer.popup().verticalScrollBar().sizeHint().width())
        self._completer.complete(cr)


c_ MainWindow ?MW..
    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)

        self.createMenu()

        self.completingTextEdit _ TextEdit()
        self.completer _ QCompleter(self)
        self.completer.sM..(self.modelFromFile(':/resources/wordlist.txt'))
        self.completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)
        self.completer.setCaseSensitivity(__.CaseInsensitive)
        self.completer.setWrapAround F..
        self.completingTextEdit.setCompleter(self.completer)

        self.sCW..(self.completingTextEdit)
        self.resize(500, 300)
        self.setWindowTitle("Completer")

    ___ createMenu(self):
        exitAction _ ?A..("Exit", self)
        aboutAct _ ?A..("About", self)
        aboutQtAct _ ?A..("About Qt", self)

        exitAction.t__.c..(?A...instance().quit)
        aboutAct.t__.c..(self.about)
        aboutQtAct.t__.c..(?A...instance().aboutQt)

        fileMenu _ self.mB.. .aM..("File")
        fileMenu.aA..(exitAction)

        helpMenu _ self.mB.. .aM..("About")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ modelFromFile  fileName):
        f _ QFile(fileName)
        __ no. f.o..(QFile.ReadOnly):
            r_ QStringListModel(self.completer)

        ?A...setOverrideCursor(QCursor(__.WaitCursor))

        words _   # list
        w__ no. f.atEnd
            line _ f.readLine().trimmed()
            __ line.length() !_ 0:
                try:
                    line _ str(line, encoding_'ascii')
                except TypeError:
                    line _ str(line)

                words.ap..(line)

        ?A...restoreOverrideCursor()

        r_ QStringListModel(words, self.completer)

    ___ about(self):
        ?MB...about  "About",
                "This example demonstrates the different features of the "
                "QCompleter class.")


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    window _ MainWindow()
    window.s..
    ___.exit(app.exec_())
