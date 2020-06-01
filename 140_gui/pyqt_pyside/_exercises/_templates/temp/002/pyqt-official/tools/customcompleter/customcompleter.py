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


____ ?.QtCore ______ QFile, QStringListModel, Qt
____ ?.QtGui ______ QCursor, QKeySequence, QTextCursor
____ ?.?W.. ______ (QAction, QApplication, QCompleter, QMainWindow,
        QMessageBox, QTextEdit)

______ customcompleter_rc


class TextEdit(QTextEdit):
    ___ __init__(self, parent_None):
        super(TextEdit, self).__init__(parent)

        self._completer _ None

        self.setPlainText(
                "This TextEdit provides autocompletions for words that have "
                "more than 3 characters. You can trigger autocompletion "
                "using %s" % QKeySequence("Ctrl+E").toString(
                        QKeySequence.NativeText))

    ___ setCompleter(self, c):
        if self._completer is not None:
            self._completer.activated.disconnect()

        self._completer _ c

        c.setWidget(self)
        c.setCompletionMode(QCompleter.PopupCompletion)
        c.setCaseSensitivity(Qt.CaseInsensitive)
        c.activated.c..(self.insertCompletion)

    ___ completer(self):
        return self._completer

    ___ insertCompletion(self, completion):
        if self._completer.widget() is not self:
            return

        tc _ self.textCursor()
        extra _ len(completion) - len(self._completer.completionPrefix())
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)

    ___ textUnderCursor(self):
        tc _ self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)

        return tc.selectedText()

    ___ focusInEvent(self, e):
        if self._completer is not None:
            self._completer.setWidget(self)

        super(TextEdit, self).focusInEvent(e)

    ___ keyPressEvent(self, e):
        if self._completer is not None and self._completer.popup().isVisible
            # The following keys are forwarded by the completer to the widget.
            if e.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Escape, Qt.Key_Tab, Qt.Key_Backtab):
                e.ignore()
                # Let the completer do default behavior.
                return

        isShortcut _ ((e.modifiers() & Qt.ControlModifier) !_ 0 and e.key() == Qt.Key_E)
        if self._completer is None or not isShortcut:
            # Do not process the shortcut when we have a completer.
            super(TextEdit, self).keyPressEvent(e)

        ctrlOrShift _ e.modifiers() & (Qt.ControlModifier | Qt.ShiftModifier)
        if self._completer is None or (ctrlOrShift and len(e.text()) == 0):
            return

        eow _ "~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-="
        hasModifier _ (e.modifiers() !_ Qt.NoModifier) and not ctrlOrShift
        completionPrefix _ self.textUnderCursor()

        if not isShortcut and (hasModifier or len(e.text()) == 0 or len(completionPrefix) < 3 or e.text()[-1] in eow):
            self._completer.popup().hide()
            return

        if completionPrefix !_ self._completer.completionPrefix
            self._completer.setCompletionPrefix(completionPrefix)
            self._completer.popup().setCurrentIndex(
                    self._completer.completionModel().index(0, 0))

        cr _ self.cursorRect()
        cr.setWidth(self._completer.popup().sizeHintForColumn(0) + self._completer.popup().verticalScrollBar().sizeHint().width())
        self._completer.complete(cr)


class MainWindow(QMainWindow):
    ___ __init__(self, parent_None):
        super(MainWindow, self).__init__(parent)

        self.createMenu()

        self.completingTextEdit _ TextEdit()
        self.completer _ QCompleter(self)
        self.completer.setModel(self.modelFromFile(':/resources/wordlist.txt'))
        self.completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setWrapAround(False)
        self.completingTextEdit.setCompleter(self.completer)

        self.setCentralWidget(self.completingTextEdit)
        self.resize(500, 300)
        self.setWindowTitle("Completer")

    ___ createMenu(self):
        exitAction _ QAction("Exit", self)
        aboutAct _ QAction("About", self)
        aboutQtAct _ QAction("About Qt", self)

        exitAction.triggered.c..(QApplication.instance().quit)
        aboutAct.triggered.c..(self.about)
        aboutQtAct.triggered.c..(QApplication.instance().aboutQt)

        fileMenu _ self.menuBar().addMenu("File")
        fileMenu.addAction(exitAction)

        helpMenu _ self.menuBar().addMenu("About")
        helpMenu.addAction(aboutAct)
        helpMenu.addAction(aboutQtAct)

    ___ modelFromFile(self, fileName):
        f _ QFile(fileName)
        if not f.open(QFile.ReadOnly):
            return QStringListModel(self.completer)

        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        words _ []
        while not f.atEnd
            line _ f.readLine().trimmed()
            if line.length() !_ 0:
                try:
                    line _ str(line, encoding_'ascii')
                except TypeError:
                    line _ str(line)

                words.append(line)

        QApplication.restoreOverrideCursor()

        return QStringListModel(words, self.completer)

    ___ about(self):
        QMessageBox.about(self, "About",
                "This example demonstrates the different features of the "
                "QCompleter class.")


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())
