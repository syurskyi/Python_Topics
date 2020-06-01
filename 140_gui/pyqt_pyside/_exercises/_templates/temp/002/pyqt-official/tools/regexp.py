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


____ ?.?C.. ______ QRegExp, __
____ ?.?G.. ______ ?P..
____ ?.?W.. ______ (?A.., QCheckBox, QComboBox, QDialog,
        QGridLayout, QHBoxLayout, QLabel, QLineEdit, QSizePolicy)


c_ RegExpDialog(QDialog):
    MaxCaptures _ 6

    ___ __init__  parent_None):
        super(RegExpDialog, self).__init__(parent)

        self.patternComboBox _ QComboBox()
        self.patternComboBox.setEditable(True)
        self.patternComboBox.setSizePolicy(QSizePolicy.Expanding,
                QSizePolicy.Preferred)

        patternLabel _ QLabel("&Pattern:")
        patternLabel.setBuddy(self.patternComboBox)

        self.escapedPatternLineEdit _ ?LE..
        self.escapedPatternLineEdit.setReadOnly(True)
        palette _ self.escapedPatternLineEdit.palette()
        palette.setBrush(?P...Base,
                palette.brush(?P...Disabled, ?P...Base))
        self.escapedPatternLineEdit.sP..(palette)

        escapedPatternLabel _ QLabel("&Escaped Pattern:")
        escapedPatternLabel.setBuddy(self.escapedPatternLineEdit)

        self.syntaxComboBox _ QComboBox()
        self.syntaxComboBox.addItem("Regular expression v1", QRegExp.RegExp)
        self.syntaxComboBox.addItem("Regular expression v2", QRegExp.RegExp2)
        self.syntaxComboBox.addItem("Wildcard", QRegExp.Wildcard)
        self.syntaxComboBox.addItem("Fixed string", QRegExp.FixedString)

        syntaxLabel _ QLabel("&Pattern Syntax:")
        syntaxLabel.setBuddy(self.syntaxComboBox)

        self.textComboBox _ QComboBox()
        self.textComboBox.setEditable(True)
        self.textComboBox.setSizePolicy(QSizePolicy.Expanding,
                QSizePolicy.Preferred)

        textLabel _ QLabel("&Text:")
        textLabel.setBuddy(self.textComboBox)

        self.caseSensitiveCheckBox _ QCheckBox("Case &Sensitive")
        self.caseSensitiveCheckBox.setChecked(True)
        self.minimalCheckBox _ QCheckBox("&Minimal")

        indexLabel _ QLabel("Index of Match:")
        self.indexEdit _ ?LE..
        self.indexEdit.setReadOnly(True)

        matchedLengthLabel _ QLabel("Matched Length:")
        self.matchedLengthEdit _ ?LE..
        self.matchedLengthEdit.setReadOnly(True)

        self.captureLabels _   # list
        self.captureEdits _   # list
        for i in range(self.MaxCaptures):
            self.captureLabels.ap..(QLabel("Capture %d:" % i))
            self.captureEdits.ap..(QLineEdit())
            self.captureEdits[i].setReadOnly(True)
        self.captureLabels[0].sT..("Match:")

        checkBoxLayout _ QHBoxLayout()
        checkBoxLayout.aW..(self.caseSensitiveCheckBox)
        checkBoxLayout.aW..(self.minimalCheckBox)
        checkBoxLayout.addStretch(1)

        mainLayout _ QGridLayout()
        mainLayout.aW..(patternLabel, 0, 0)
        mainLayout.aW..(self.patternComboBox, 0, 1)
        mainLayout.aW..(escapedPatternLabel, 1, 0)
        mainLayout.aW..(self.escapedPatternLineEdit, 1, 1)
        mainLayout.aW..(syntaxLabel, 2, 0)
        mainLayout.aW..(self.syntaxComboBox, 2, 1)
        mainLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        mainLayout.aW..(textLabel, 4, 0)
        mainLayout.aW..(self.textComboBox, 4, 1)
        mainLayout.aW..(indexLabel, 5, 0)
        mainLayout.aW..(self.indexEdit, 5, 1)
        mainLayout.aW..(matchedLengthLabel, 6, 0)
        mainLayout.aW..(self.matchedLengthEdit, 6, 1)

        for i in range(self.MaxCaptures):
            mainLayout.aW..(self.captureLabels[i], 7 + i, 0)
            mainLayout.aW..(self.captureEdits[i], 7 + i, 1)
        self.sL..(mainLayout)

        self.patternComboBox.editTextChanged.c..(self.refresh)
        self.textComboBox.editTextChanged.c..(self.refresh)
        self.caseSensitiveCheckBox.toggled.c..(self.refresh)
        self.minimalCheckBox.toggled.c..(self.refresh)
        self.syntaxComboBox.currentIndexChanged.c..(self.refresh)

        self.patternComboBox.addItem("[A-Za-z_]+([A-Za-z_0-9]*)")
        self.textComboBox.addItem("(10 + delta4)* 32")

        self.setWindowTitle("RegExp")
        self.setFixedHeight(self.sizeHint().height())
        self.refresh()

    ___ refresh(self):
        self.setUpdatesEnabled F..

        pattern _ self.patternComboBox.currentText()
        t__ _ self.textComboBox.currentText()

        escaped _ str(pattern)
        escaped.replace('\\', '\\\\')
        escaped.replace('"', '\\"')
        self.escapedPatternLineEdit.sT..('"' + escaped + '"')

        rx _ QRegExp(pattern)
        cs _ __.CaseSensitive __ self.caseSensitiveCheckBox.isChecked() else __.CaseInsensitive
        rx.setCaseSensitivity(cs)
        rx.setMinimal(self.minimalCheckBox.isChecked())
        syntax _ self.syntaxComboBox.itemData(self.syntaxComboBox.currentIndex())
        rx.setPatternSyntax(syntax)

        palette _ self.patternComboBox.palette()
        __ rx.isValid
            palette.sC..(?P...Text,
                    self.textComboBox.palette().color(?P...Text))
        ____
            palette.sC..(?P...Text, __.red)
        self.patternComboBox.sP..(palette)

        self.indexEdit.sT..(str(rx.indexIn(t__)))
        self.matchedLengthEdit.sT..(str(rx.matchedLength()))

        for i in range(self.MaxCaptures):
            self.captureLabels[i].setEnabled(i <_ rx.captureCount())
            self.captureEdits[i].setEnabled(i <_ rx.captureCount())
            self.captureEdits[i].sT..(rx.cap(i))

        self.setUpdatesEnabled(True)

__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    dialog _ RegExpDialog()
    dialog.s..
    ___.exit(app.exec_())
