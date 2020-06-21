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


____ ?.?W.. ______ (?A.., ?CB, ?D..,
        ?DBB..., ?FL.., QGridLayout, ?GB.., ?HBL..,
        ?L.., QLineEdit, ?M.., QMenuBar, ?PB.., SB.., ?TE..,
        ?VBL..)


c_ Dialog(?D..):
    NumGridRows _ 3
    NumButtons _ 4

    ___  -  
        s__(Dialog, self). - ()

        createMenu()
        createHorizontalGroupBox()
        createGridGroupBox()
        createFormGroupBox()

        bigEditor _ ?TE..()
        bigEditor.sPT..("This widget takes up all the remaining space "
                "in the top-level layout.")

        buttonBox _ ?DBB...(?DBB....Ok | ?DBB....Cancel)

        buttonBox.a___.c..(accept)
        buttonBox.r___.c..(reject)

        mainLayout _ ?VBL..
        mainLayout.setMenuBar(menuBar)
        mainLayout.aW..(horizontalGroupBox)
        mainLayout.aW..(gridGroupBox)
        mainLayout.aW..(formGroupBox)
        mainLayout.aW..(bigEditor)
        mainLayout.aW..(buttonBox)
        sL..(mainLayout)

        sWT..("Basic Layouts")

    ___ createMenu 
        menuBar _ QMenuBar()

        fileMenu _ ?M..("&File", self)
        exitAction _ fileMenu.aA..("E&xit")
        menuBar.aM..(fileMenu)

        exitAction.t__.c..(accept)

    ___ createHorizontalGroupBox 
        horizontalGroupBox _ ?GB..("Horizontal layout")
        layout _ ?HBL..

        ___ i __ ra..(Dialog.NumButtons):
            button _ ?PB..("Button %d" % (i + 1))
            layout.aW..(button)

        horizontalGroupBox.sL..(layout)

    ___ createGridGroupBox 
        gridGroupBox _ ?GB..("Grid layout")
        layout _ QGridLayout()

        ___ i __ ra..(Dialog.NumGridRows):
            label _ ?L..("Line %d:" % (i + 1))
            lineEdit _ ?LE..
            layout.aW..(label, i + 1, 0)
            layout.aW..(lineEdit, i + 1, 1)

        smallEditor _ ?TE..()
        smallEditor.sPT..("This widget takes up about two thirds "
                "of the grid layout.")

        layout.aW..(smallEditor, 0, 2, 4, 1)

        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)
        gridGroupBox.sL..(layout)

    ___ createFormGroupBox 
        formGroupBox _ ?GB..("Form layout")
        layout _ ?FL..
        layout.aR..(?L..("Line 1:"), QLineEdit())
        layout.aR..(?L..("Line 2, long text:"), ?CB())
        layout.aR..(?L..("Line 3:"), SB..())
        formGroupBox.sL..(layout)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    dialog _ Dialog()
    ___.e..(dialog.e..
