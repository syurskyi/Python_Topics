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

    ___  -   parent_None):
        super(RegExpDialog, self). - (parent)

        patternComboBox _ QComboBox()
        patternComboBox.setEditable(True)
        patternComboBox.sSP..(QSizePolicy.E..,
                QSizePolicy.Preferred)

        patternLabel _ QLabel("&Pattern:")
        patternLabel.setBuddy(patternComboBox)

        escapedPatternLineEdit _ ?LE..
        escapedPatternLineEdit.setReadOnly(True)
        palette _ escapedPatternLineEdit.palette()
        palette.setBrush(?P...Base,
                palette.brush(?P...Disabled, ?P...Base))
        escapedPatternLineEdit.sP..(palette)

        escapedPatternLabel _ QLabel("&Escaped Pattern:")
        escapedPatternLabel.setBuddy(escapedPatternLineEdit)

        syntaxComboBox _ QComboBox()
        syntaxComboBox.addItem("Regular expression v1", QRegExp.RegExp)
        syntaxComboBox.addItem("Regular expression v2", QRegExp.RegExp2)
        syntaxComboBox.addItem("Wildcard", QRegExp.Wildcard)
        syntaxComboBox.addItem("Fixed string", QRegExp.FixedString)

        syntaxLabel _ QLabel("&Pattern Syntax:")
        syntaxLabel.setBuddy(syntaxComboBox)

        textComboBox _ QComboBox()
        textComboBox.setEditable(True)
        textComboBox.sSP..(QSizePolicy.E..,
                QSizePolicy.Preferred)

        textLabel _ QLabel("&Text:")
        textLabel.setBuddy(textComboBox)

        caseSensitiveCheckBox _ QCheckBox("Case &Sensitive")
        caseSensitiveCheckBox.setChecked(True)
        minimalCheckBox _ QCheckBox("&Minimal")

        indexLabel _ QLabel("Index of Match:")
        indexEdit _ ?LE..
        indexEdit.setReadOnly(True)

        matchedLengthLabel _ QLabel("Matched Length:")
        matchedLengthEdit _ ?LE..
        matchedLengthEdit.setReadOnly(True)

        captureLabels _   # list
        captureEdits _   # list
        ___ i __ range(MaxCaptures):
            captureLabels.ap..(QLabel("Capture %d:" % i))
            captureEdits.ap..(QLineEdit())
            captureEdits[i].setReadOnly(True)
        captureLabels[0].sT..("Match:")

        checkBoxLayout _ QHBoxLayout()
        checkBoxLayout.aW..(caseSensitiveCheckBox)
        checkBoxLayout.aW..(minimalCheckBox)
        checkBoxLayout.addStretch(1)

        mainLayout _ QGridLayout()
        mainLayout.aW..(patternLabel, 0, 0)
        mainLayout.aW..(patternComboBox, 0, 1)
        mainLayout.aW..(escapedPatternLabel, 1, 0)
        mainLayout.aW..(escapedPatternLineEdit, 1, 1)
        mainLayout.aW..(syntaxLabel, 2, 0)
        mainLayout.aW..(syntaxComboBox, 2, 1)
        mainLayout.aL..(checkBoxLayout, 3, 0, 1, 2)
        mainLayout.aW..(textLabel, 4, 0)
        mainLayout.aW..(textComboBox, 4, 1)
        mainLayout.aW..(indexLabel, 5, 0)
        mainLayout.aW..(indexEdit, 5, 1)
        mainLayout.aW..(matchedLengthLabel, 6, 0)
        mainLayout.aW..(matchedLengthEdit, 6, 1)

        ___ i __ range(MaxCaptures):
            mainLayout.aW..(captureLabels[i], 7 + i, 0)
            mainLayout.aW..(captureEdits[i], 7 + i, 1)
        sL..(mainLayout)

        patternComboBox.editTextChanged.c..(refresh)
        textComboBox.editTextChanged.c..(refresh)
        caseSensitiveCheckBox.toggled.c..(refresh)
        minimalCheckBox.toggled.c..(refresh)
        syntaxComboBox.currentIndexChanged.c..(refresh)

        patternComboBox.addItem("[A-Za-z_]+([A-Za-z_0-9]*)")
        textComboBox.addItem("(10 + delta4)* 32")

        setWindowTitle("RegExp")
        setFixedHeight(sizeHint().height())
        refresh()

    ___ refresh 
        setUpdatesEnabled F..

        pattern _ patternComboBox.currentText()
        t__ _ textComboBox.currentText()

        escaped _ str(pattern)
        escaped.replace('\\', '\\\\')
        escaped.replace('"', '\\"')
        escapedPatternLineEdit.sT..('"' + escaped + '"')

        rx _ QRegExp(pattern)
        cs _ __.CaseSensitive __ caseSensitiveCheckBox.isChecked() else __.CaseInsensitive
        rx.setCaseSensitivity(cs)
        rx.setMinimal(minimalCheckBox.isChecked())
        syntax _ syntaxComboBox.itemData(syntaxComboBox.currentIndex())
        rx.setPatternSyntax(syntax)

        palette _ patternComboBox.palette()
        __ rx.isValid
            palette.sC..(?P...Text,
                    textComboBox.palette().color(?P...Text))
        ____
            palette.sC..(?P...Text, __.red)
        patternComboBox.sP..(palette)

        indexEdit.sT..(str(rx.indexIn(t__)))
        matchedLengthEdit.sT..(str(rx.matchedLength()))

        ___ i __ range(MaxCaptures):
            captureLabels[i].setEnabled(i <_ rx.captureCount())
            captureEdits[i].setEnabled(i <_ rx.captureCount())
            captureEdits[i].sT..(rx.cap(i))

        setUpdatesEnabled(True)

__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    dialog _ RegExpDialog()
    dialog.s..
    ___.exit(app.exec_())
