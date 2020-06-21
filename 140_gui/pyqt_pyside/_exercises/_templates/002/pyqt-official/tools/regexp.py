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
____ ?.?W.. ______ (?A.., QCheckBox, ?CB, ?D..,
        QGridLayout, ?HBL.., ?L.., QLineEdit, ?SP..)


c_ RegExpDialog(?D..):
    MaxCaptures _ 6

    ___  -   parent_None):
        s__(RegExpDialog, self). - (parent)

        patternComboBox _ ?CB()
        patternComboBox.sE..( st.
        patternComboBox.sSP..(?SP...E..,
                ?SP...Preferred)

        patternLabel _ ?L..("&Pattern:")
        patternLabel.setBuddy(patternComboBox)

        escapedPatternLineEdit _ ?LE..
        escapedPatternLineEdit.sRO..( st.
        palette _ escapedPatternLineEdit.p..
        palette.sB..(?P...Base,
                palette.brush(?P...Disabled, ?P...Base))
        escapedPatternLineEdit.sP..(palette)

        escapedPatternLabel _ ?L..("&Escaped Pattern:")
        escapedPatternLabel.setBuddy(escapedPatternLineEdit)

        syntaxComboBox _ ?CB()
        syntaxComboBox.aI..("Regular expression v1", QRegExp.RegExp)
        syntaxComboBox.aI..("Regular expression v2", QRegExp.RegExp2)
        syntaxComboBox.aI..("Wildcard", QRegExp.Wildcard)
        syntaxComboBox.aI..("Fixed string", QRegExp.FixedString)

        syntaxLabel _ ?L..("&Pattern Syntax:")
        syntaxLabel.setBuddy(syntaxComboBox)

        textComboBox _ ?CB()
        textComboBox.sE..( st.
        textComboBox.sSP..(?SP...E..,
                ?SP...Preferred)

        textLabel _ ?L..("&Text:")
        textLabel.setBuddy(textComboBox)

        caseSensitiveCheckBox _ QCheckBox("Case &Sensitive")
        caseSensitiveCheckBox.sC__( st.
        minimalCheckBox _ QCheckBox("&Minimal")

        indexLabel _ ?L..("Index of Match:")
        indexEdit _ ?LE..
        indexEdit.sRO..( st.

        matchedLengthLabel _ ?L..("Matched Length:")
        matchedLengthEdit _ ?LE..
        matchedLengthEdit.sRO..( st.

        captureLabels _   # list
        captureEdits _   # list
        ___ i __ ra..(MaxCaptures):
            captureLabels.ap..(?L..("Capture %d:" % i))
            captureEdits.ap..(QLineEdit())
            captureEdits[i].sRO..( st.
        captureLabels[0].sT..("Match:")

        checkBoxLayout _ ?HBL..
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

        ___ i __ ra..(MaxCaptures):
            mainLayout.aW..(captureLabels[i], 7 + i, 0)
            mainLayout.aW..(captureEdits[i], 7 + i, 1)
        sL..(mainLayout)

        patternComboBox.editTextChanged.c..(refresh)
        textComboBox.editTextChanged.c..(refresh)
        caseSensitiveCheckBox.t__.c..(refresh)
        minimalCheckBox.t__.c..(refresh)
        syntaxComboBox.currentIndexChanged.c..(refresh)

        patternComboBox.aI..("[A-Za-z_]+([A-Za-z_0-9]*)")
        textComboBox.aI..("(10 + delta4)* 32")

        sWT..("RegExp")
        sFH..(sH..().height())
        refresh()

    ___ refresh 
        setUpdatesEnabled F..

        pattern _ patternComboBox.currentText()
        t__ _ textComboBox.currentText()

        escaped _ st.(pattern)
        escaped.replace('\\', '\\\\')
        escaped.replace('"', '\\"')
        escapedPatternLineEdit.sT..('"' + escaped + '"')

        rx _ QRegExp(pattern)
        cs _ __.CaseSensitive __ caseSensitiveCheckBox.isChecked() ____ __.CaseInsensitive
        rx.setCaseSensitivity(cs)
        rx.setMinimal(minimalCheckBox.isChecked())
        syntax _ syntaxComboBox.itemData(syntaxComboBox.cI..
        rx.setPatternSyntax(syntax)

        palette _ patternComboBox.p..
        __ rx.isValid
            palette.sC..(?P...Text,
                    textComboBox.p...color(?P...Text))
        ____
            palette.sC..(?P...Text, __.red)
        patternComboBox.sP..(palette)

        indexEdit.sT..(st.(rx.indexIn(t__)))
        matchedLengthEdit.sT..(st.(rx.matchedLength()))

        ___ i __ ra..(MaxCaptures):
            captureLabels[i].sE..(i <_ rx.captureCount())
            captureEdits[i].sE..(i <_ rx.captureCount())
            captureEdits[i].sT..(rx.cap(i))

        setUpdatesEnabled( st.

__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    dialog _ RegExpDialog()
    dialog.s..
    ___.e.. ?.e..
