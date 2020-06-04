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


____ ?.?C.. ______ ?DT__, __, ?T..
____ ?.?W.. ______ (?A.., QCheckBox, ?CB, ?DTE..,
        QDial, ?D.., QGridLayout, ?GB.., ?HBL.., ?L.., QLineEdit,
        QProgressBar, ?PB.., QRadioButton, QScrollBar, ?SP..,
        ?S.., SB.., ?SF.., ?TW.., ?TW.., ?TE..,
        ?VBL.., ?W..)


c_ WidgetGallery(?D..):
    ___  -   parent_None):
        s__(WidgetGallery, self). - (parent)

        originalPalette _ ?A...p..

        styleComboBox _ ?CB()
        styleComboBox.aI..(?SF...keys())

        styleLabel _ ?L..("&Style:")
        styleLabel.setBuddy(styleComboBox)

        useStylePaletteCheckBox _ QCheckBox("&Use style's standard palette")
        useStylePaletteCheckBox.sC__( st.

        disableWidgetsCheckBox _ QCheckBox("&Disable widgets")

        createTopLeftGroupBox()
        createTopRightGroupBox()
        createBottomLeftTabWidget()
        createBottomRightGroupBox()
        createProgressBar()

        styleComboBox.activated[st.].c..(changeStyle)
        useStylePaletteCheckBox.t__.c..(changePalette)
        disableWidgetsCheckBox.t__.c..(topLeftGroupBox.sD..)
        disableWidgetsCheckBox.t__.c..(topRightGroupBox.sD..)
        disableWidgetsCheckBox.t__.c..(bottomLeftTabWidget.sD..)
        disableWidgetsCheckBox.t__.c..(bottomRightGroupBox.sD..)

        topLayout _ ?HBL..
        topLayout.aW..(styleLabel)
        topLayout.aW..(styleComboBox)
        topLayout.addStretch(1)
        topLayout.aW..(useStylePaletteCheckBox)
        topLayout.aW..(disableWidgetsCheckBox)

        mainLayout _ QGridLayout()
        mainLayout.aL..(topLayout, 0, 0, 1, 2)
        mainLayout.aW..(topLeftGroupBox, 1, 0)
        mainLayout.aW..(topRightGroupBox, 1, 1)
        mainLayout.aW..(bottomLeftTabWidget, 2, 0)
        mainLayout.aW..(bottomRightGroupBox, 2, 1)
        mainLayout.aW..(progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        sL..(mainLayout)

        sWT..("Styles")
        changeStyle('Windows')

    ___ changeStyle  styleName):
        ?A...sS..(?SF...create(styleName))
        changePalette()

    ___ changePalette 
        __ (useStylePaletteCheckBox.isChecked()):
            ?A...sP..(?A...style().standardPalette())
        ____
            ?A...sP..(originalPalette)

    ___ advanceProgressBar 
        curVal _ progressBar.v..
        maxVal _ progressBar.maximum()
        progressBar.sV..(curVal + (maxVal - curVal) / 100)

    ___ createTopLeftGroupBox 
        topLeftGroupBox _ ?GB..("Group 1")

        radioButton1 _ QRadioButton("Radio button 1")
        radioButton2 _ QRadioButton("Radio button 2")
        radioButton3 _ QRadioButton("Radio button 3")
        radioButton1.sC__( st.

        checkBox _ QCheckBox("Tri-state check box")
        checkBox.setTristate( st.
        checkBox.setCheckState(__.PartiallyChecked)

        layout _ ?VBL..
        layout.aW..(radioButton1)
        layout.aW..(radioButton2)
        layout.aW..(radioButton3)
        layout.aW..(checkBox)
        layout.addStretch(1)
        topLeftGroupBox.sL..(layout)    

    ___ createTopRightGroupBox 
        topRightGroupBox _ ?GB..("Group 2")

        defaultPushButton _ ?PB..("Default Push Button")
        defaultPushButton.setDefault( st.

        togglePushButton _ ?PB..("Toggle Push Button")
        togglePushButton.setCheckable( st.
        togglePushButton.sC__( st.

        flatPushButton _ ?PB..("Flat Push Button")
        flatPushButton.setFlat( st.

        layout _ ?VBL..
        layout.aW..(defaultPushButton)
        layout.aW..(togglePushButton)
        layout.aW..(flatPushButton)
        layout.addStretch(1)
        topRightGroupBox.sL..(layout)

    ___ createBottomLeftTabWidget 
        bottomLeftTabWidget _ ?TW..()
        bottomLeftTabWidget.sSP..(?SP...Preferred,
                ?SP...Ignored)

        tab1 _ ?W..
        tableWidget _ ?TW..(10, 10)

        tab1hbox _ ?HBL..
        tab1hbox.sCM..(5, 5, 5, 5)
        tab1hbox.aW..(tableWidget)
        tab1.sL..(tab1hbox)

        tab2 _ ?W..
        textEdit _ ?TE..()

        textEdit.sPT..("Twinkle, twinkle, little star,\n"
                              "How I wonder what you are.\n" 
                              "Up above the world so high,\n"
                              "Like a diamond in the sky.\n"
                              "Twinkle, twinkle, little star,\n" 
                              "How I wonder what you are!\n")

        tab2hbox _ ?HBL..
        tab2hbox.sCM..(5, 5, 5, 5)
        tab2hbox.aW..(textEdit)
        tab2.sL..(tab2hbox)

        bottomLeftTabWidget.aT..(tab1, "&Table")
        bottomLeftTabWidget.aT..(tab2, "Text &Edit")

    ___ createBottomRightGroupBox 
        bottomRightGroupBox _ ?GB..("Group 3")
        bottomRightGroupBox.setCheckable( st.
        bottomRightGroupBox.sC__( st.

        lineEdit _ QLineEdit('s3cRe7')
        lineEdit.setEchoMode(QLineEdit.Password)

        spinBox _ SB..(bottomRightGroupBox)
        spinBox.sV..(50)

        dateTimeEdit _ ?DTE..(bottomRightGroupBox)
        dateTimeEdit.setDateTime(?DT__.currentDateTime())

        slider _ ?S..(__.H.., bottomRightGroupBox)
        slider.sV..(40)

        scrollBar _ QScrollBar(__.H.., bottomRightGroupBox)
        scrollBar.sV..(60)

        dial _ QDial(bottomRightGroupBox)
        dial.sV..(30)
        dial.setNotchesVisible( st.

        layout _ QGridLayout()
        layout.aW..(lineEdit, 0, 0, 1, 2)
        layout.aW..(spinBox, 1, 0, 1, 2)
        layout.aW..(dateTimeEdit, 2, 0, 1, 2)
        layout.aW..(slider, 3, 0)
        layout.aW..(scrollBar, 4, 0)
        layout.aW..(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        bottomRightGroupBox.sL..(layout)

    ___ createProgressBar 
        progressBar _ QProgressBar()
        progressBar.setRange(0, 10000)
        progressBar.sV..(0)

        timer _ ?T..
        timer.timeout.c..(advanceProgressBar)
        timer.start(1000)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    gallery _ WidgetGallery()
    gallery.s..
    ___.e.. ?.e..
