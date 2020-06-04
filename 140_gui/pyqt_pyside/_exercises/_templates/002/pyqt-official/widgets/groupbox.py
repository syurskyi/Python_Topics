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
____ ?.?W.. ______ (?A.., QCheckBox, QGridLayout, ?GB..,
        ?M.., ?PB.., QRadioButton, ?VBL.., ?W..)


c_ Window(?W..):
    ___  -   parent_None):
        s__(Window, self). - (parent)

        grid _ QGridLayout()
        grid.aW..(createFirstExclusiveGroup(), 0, 0)
        grid.aW..(createSecondExclusiveGroup(), 1, 0)
        grid.aW..(createNonExclusiveGroup(), 0, 1)
        grid.aW..(createPushButtonGroup(), 1, 1)
        sL..(grid)

        sWT..("Group Box")
        r..(480, 320)

    ___ createFirstExclusiveGroup 
        groupBox _ ?GB..("Exclusive Radio Buttons")

        radio1 _ QRadioButton("&Radio button 1")
        radio2 _ QRadioButton("R&adio button 2")
        radio3 _ QRadioButton("Ra&dio button 3")

        radio1.sC__( st.

        vbox _ ?VBL..
        vbox.aW..(radio1)
        vbox.aW..(radio2)
        vbox.aW..(radio3)
        vbox.addStretch(1)
        groupBox.sL..(vbox)

        r_ groupBox

    ___ createSecondExclusiveGroup 
        groupBox _ ?GB..("E&xclusive Radio Buttons")
        groupBox.setCheckable( st.
        groupBox.sC__ F..

        radio1 _ QRadioButton("Rad&io button 1")
        radio2 _ QRadioButton("Radi&o button 2")
        radio3 _ QRadioButton("Radio &button 3")
        radio1.sC__( st.
        checkBox _ QCheckBox("Ind&ependent checkbox")
        checkBox.sC__( st.

        vbox _ ?VBL..
        vbox.aW..(radio1)
        vbox.aW..(radio2)
        vbox.aW..(radio3)
        vbox.aW..(checkBox)
        vbox.addStretch(1)
        groupBox.sL..(vbox)

        r_ groupBox

    ___ createNonExclusiveGroup 
        groupBox _ ?GB..("Non-Exclusive Checkboxes")
        groupBox.setFlat( st.

        checkBox1 _ QCheckBox("&Checkbox 1")
        checkBox2 _ QCheckBox("C&heckbox 2")
        checkBox2.sC__( st.
        tristateBox _ QCheckBox("Tri-&state button")
        tristateBox.setTristate( st.
        tristateBox.setCheckState(__.PartiallyChecked)

        vbox _ ?VBL..
        vbox.aW..(checkBox1)
        vbox.aW..(checkBox2)
        vbox.aW..(tristateBox)
        vbox.addStretch(1)
        groupBox.sL..(vbox)

        r_ groupBox

    ___ createPushButtonGroup 
        groupBox _ ?GB..("&Push Buttons")
        groupBox.setCheckable( st.
        groupBox.sC__( st.

        pushButton _ ?PB..("&Normal Button")
        toggleButton _ ?PB..("&Toggle Button")
        toggleButton.setCheckable( st.
        toggleButton.sC__( st.
        flatButton _ ?PB..("&Flat Button")
        flatButton.setFlat( st.

        popupButton _ ?PB..("Pop&up Button")
        menu _ ?M..
        menu.aA..("&First Item")
        menu.aA..("&Second Item")
        menu.aA..("&Third Item")
        menu.aA..("F&ourth Item")
        popupButton.setMenu(menu)

        newAction _ menu.aA..("Submenu")
        subMenu _ ?M..("Popup Submenu", self)
        subMenu.aA..("Item 1")
        subMenu.aA..("Item 2")
        subMenu.aA..("Item 3")
        newAction.setMenu(subMenu)

        vbox _ ?VBL..
        vbox.aW..(pushButton)
        vbox.aW..(toggleButton)
        vbox.aW..(flatButton)
        vbox.aW..(popupButton)
        vbox.addStretch(1)
        groupBox.sL..(vbox)

        r_ groupBox


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    clock _ Window()
    clock.s..
    ___.e.. ?.e..
