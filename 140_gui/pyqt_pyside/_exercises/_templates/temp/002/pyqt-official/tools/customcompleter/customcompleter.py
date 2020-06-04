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
____ ?.?G.. ______ ?C.., ?KS.., QTextCursor
____ ?.?W.. ______ (?A.., ?A.., QCompleter, ?MW..,
        ?MB.., ?TE..)

______ customcompleter_rc


c_ TextEdit(?TE..):
    ___  -   parent_None):
        s__(TextEdit, self). - (parent)

        _completer _ N..

        sPT..(
                "This TextEdit provides autocompletions for words that have "
                "more than 3 characters. You can trigger autocompletion "
                "using %s" % ?KS..("Ctrl+E").toString(
                        ?KS...NativeText))

    ___ setCompleter  c):
        __ _completer __ no. N..:
            _completer.activated.disconnect()

        _completer _ c

        c.setWidget
        c.setCompletionMode(QCompleter.PopupCompletion)
        c.setCaseSensitivity(__.CaseInsensitive)
        c.activated.c..(insertCompletion)

    ___ completer
        r_ _completer

    ___ insertCompletion  completion):
        __ _completer.widget() __ no. self:
            r_

        tc _ textCursor()
        extra _ le.(completion) - le.(_completer.completionPrefix())
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        setTextCursor(tc)

    ___ textUnderCursor
        tc _ textCursor()
        tc.select(QTextCursor.WordUnderCursor)

        r_ tc.selectedText()

    ___ focusInEvent  e):
        __ _completer __ no. N..:
            _completer.setWidget

        s__(TextEdit, self).focusInEvent(e)

    ___ keyPressEvent  e):
        __ _completer __ no. N.. and _completer.popup().isVisible
            # The following keys are forwarded by the completer to the widget.
            __ e.key() __ (__.Key_Enter, __.Key_Return, __.Key_Escape, __.Key_Tab, __.Key_Backtab):
                e.ignore()
                # Let the completer do default behavior.
                r_

        isShortcut _ ((e.modifiers() & __.ControlModifier) !_ 0 and e.key() __ __.Key_E)
        __ _completer __ N.. or no. isShortcut:
            # Do not process the shortcut when we have a completer.
            s__(TextEdit, self).keyPressEvent(e)

        ctrlOrShift _ e.modifiers() & (__.ControlModifier | __.ShiftModifier)
        __ _completer __ N.. or (ctrlOrShift and le.(e.t__()) __ 0):
            r_

        eow _ "~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-="
        hasModifier _ (e.modifiers() !_ __.NoModifier) and no. ctrlOrShift
        completionPrefix _ textUnderCursor()

        __ no. isShortcut and (hasModifier or le.(e.t__()) __ 0 or le.(completionPrefix) < 3 or e.t__()[-1] __ eow):
            _completer.popup().hide()
            r_

        __ completionPrefix !_ _completer.completionPrefix
            _completer.setCompletionPrefix(completionPrefix)
            _completer.popup().sCI..(
                    _completer.completionModel().index(0, 0))

        cr _ cursorRect()
        cr.sW..(_completer.popup().sizeHintForColumn(0) + _completer.popup().verticalScrollBar().sH..().width())
        _completer.complete(cr)


c_ MainWindow ?MW..
    ___  -   parent_None):
        s__(MainWindow, self). - (parent)

        createMenu()

        completingTextEdit _ TextEdit()
        completer _ QCompleter
        completer.sM..(modelFromFile(':/resources/wordlist.txt'))
        completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)
        completer.setCaseSensitivity(__.CaseInsensitive)
        completer.setWrapAround F..
        completingTextEdit.setCompleter(completer)

        sCW..(completingTextEdit)
        r..(500, 300)
        sWT..("Completer")

    ___ createMenu
        exitAction _ ?A..("Exit", self)
        aboutAct _ ?A..("About", self)
        aboutQtAct _ ?A..("About Qt", self)

        exitAction.t__.c..(?A...i.. .quit)
        aboutAct.t__.c..(about)
        aboutQtAct.t__.c..(?A...i.. .aboutQt)

        fileMenu _ mB.. .aM..("File")
        fileMenu.aA..(exitAction)

        helpMenu _ mB.. .aM..("About")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ modelFromFile  fileName):
        f _ QFile(fileName)
        __ no. f.o..(QFile.ReadOnly):
            r_ QStringListModel(completer)

        ?A...setOverrideCursor(?C..(__.WaitCursor))

        words _   # list
        w__ no. f.atEnd
            line _ f.readLine().trimmed()
            __ line.length() !_ 0:
                ___
                    line _ st.(line, encoding_'ascii')
                _____ TypeError:
                    line _ st.(line)

                words.ap..(line)

        ?A...restoreOverrideCursor()

        r_ QStringListModel(words, completer)

    ___ about
        ?MB...about  "About",
                "This example demonstrates the different features of the "
                "QCompleter class.")


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.s..
    ___.e.. ?.e..
