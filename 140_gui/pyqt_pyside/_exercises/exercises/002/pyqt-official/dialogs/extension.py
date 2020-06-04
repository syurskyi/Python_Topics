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
____ ?.?W.. ______ (?A.., QCheckBox, ?D..,
        ?DBB..., QGridLayout, ?HBL.., ?L.., QLayout, QLineEdit,
        ?PB.., ?VBL.., ?W..)


c_ FindDialog(?D..):
    ___  -   parent_None):
        s__(FindDialog, self). - (parent)

        label _ ?L..("Find &what:")
        lineEdit _ ?LE..
        label.setBuddy(lineEdit)

        caseCheckBox _ QCheckBox("Match &case")
        fromStartCheckBox _ QCheckBox("Search from &start")
        fromStartCheckBox.sC__( st.

        findButton _ ?PB..("&Find")
        findButton.setDefault( st.

        moreButton _ ?PB..("&More")
        moreButton.setCheckable( st.
        moreButton.setAutoDefault F..

        extension _ ?W..

        wholeWordsCheckBox _ QCheckBox("&Whole words")
        backwardCheckBox _ QCheckBox("Search &backward")
        searchSelectionCheckBox _ QCheckBox("Search se&lection")

        buttonBox _ ?DBB...(__.Vertical)
        buttonBox.addButton(findButton, ?DBB....ActionRole)
        buttonBox.addButton(moreButton, ?DBB....ActionRole)

        moreButton.t__.c..(extension.setVisible)

        extensionLayout _ ?VBL..
        extensionLayout.sCM..(0, 0, 0, 0)
        extensionLayout.aW..(wholeWordsCheckBox)
        extensionLayout.aW..(backwardCheckBox)
        extensionLayout.aW..(searchSelectionCheckBox)
        extension.sL..(extensionLayout)

        topLeftLayout _ ?HBL..
        topLeftLayout.aW..(label)
        topLeftLayout.aW..(lineEdit)

        leftLayout _ ?VBL..
        leftLayout.aL..(topLeftLayout)
        leftLayout.aW..(caseCheckBox)
        leftLayout.aW..(fromStartCheckBox)

        mainLayout _ QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.aL..(leftLayout, 0, 0)
        mainLayout.aW..(buttonBox, 0, 1)
        mainLayout.aW..(extension, 1, 0, 1, 2)
        mainLayout.setRowStretch(2, 1)
        sL..(mainLayout)

        sWT..("Extension")
        extension.hide()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    dialog _ FindDialog()
    dialog.s..
    ___.e.. ?.e..
