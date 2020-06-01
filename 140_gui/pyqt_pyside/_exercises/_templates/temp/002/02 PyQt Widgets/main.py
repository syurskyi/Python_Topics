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


____ ?.?C.. ______ QDateTime, __, QTimer
____ ?.?W.. ______ (?A.., QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, ?PB.., QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)


c_ WidgetGallery(QDialog):
    ___ __init__  parent_None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette _ ?A...palette()

        styleComboBox _ QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel _ QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox _ QCheckBox("&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox _ QCheckBox("&Disable widgets")

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()
        self.createProgressBar()

        styleComboBox.activated[str].c..(self.changeStyle)
        self.useStylePaletteCheckBox.toggled.c..(self.changePalette)
        disableWidgetsCheckBox.toggled.c..(self.topLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.c..(self.topRightGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.c..(self.bottomLeftTabWidget.setDisabled)
        disableWidgetsCheckBox.toggled.c..(self.bottomRightGroupBox.setDisabled)

        topLayout _ QHBoxLayout()
        topLayout.aW..(styleLabel)
        topLayout.aW..(styleComboBox)
        topLayout.addStretch(1)
        topLayout.aW..(self.useStylePaletteCheckBox)
        topLayout.aW..(disableWidgetsCheckBox)

        mainLayout _ QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.aW..(self.topLeftGroupBox, 1, 0)
        mainLayout.aW..(self.topRightGroupBox, 1, 1)
        mainLayout.aW..(self.bottomLeftTabWidget, 2, 0)
        mainLayout.aW..(self.bottomRightGroupBox, 2, 1)
        mainLayout.aW..(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.sL..(mainLayout)

        self.setWindowTitle("Styles")
        self.changeStyle('Windows')

    ___ changeStyle  styleName):
        ?A...setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    ___ changePalette(self):
        __ (self.useStylePaletteCheckBox.isChecked()):
            ?A...sP..(?A...style().standardPalette())
        ____
            ?A...sP..(self.originalPalette)

    ___ advanceProgressBar(self):
        curVal _ self.progressBar.value()
        maxVal _ self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    ___ createTopLeftGroupBox(self):
        self.topLeftGroupBox _ QGroupBox("Group 1")

        radioButton1 _ QRadioButton("Radio button 1")
        radioButton2 _ QRadioButton("Radio button 2")
        radioButton3 _ QRadioButton("Radio button 3")
        radioButton1.setChecked(True)

        checkBox _ QCheckBox("Tri-state check box")
        checkBox.setTristate(True)
        checkBox.setCheckState(__.PartiallyChecked)

        layout _ ?VBL..
        layout.aW..(radioButton1)
        layout.aW..(radioButton2)
        layout.aW..(radioButton3)
        layout.aW..(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.sL..(layout)    

    ___ createTopRightGroupBox(self):
        self.topRightGroupBox _ QGroupBox("Group 2")

        defaultPushButton _ ?PB..("Default Push Button")
        defaultPushButton.setDefault(True)

        togglePushButton _ ?PB..("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton _ ?PB..("Flat Push Button")
        flatPushButton.setFlat(True)

        layout _ ?VBL..
        layout.aW..(defaultPushButton)
        layout.aW..(togglePushButton)
        layout.aW..(flatPushButton)
        layout.addStretch(1)
        self.topRightGroupBox.sL..(layout)

    ___ createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget _ QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 _ ?W..
        tableWidget _ QTableWidget(10, 10)

        tab1hbox _ QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.aW..(tableWidget)
        tab1.sL..(tab1hbox)

        tab2 _ ?W..
        textEdit _ QTextEdit()

        textEdit.sPT..("Twinkle, twinkle, little star,\n"
                              "How I wonder what you are.\n" 
                              "Up above the world so high,\n"
                              "Like a diamond in the sky.\n"
                              "Twinkle, twinkle, little star,\n" 
                              "How I wonder what you are!\n")

        tab2hbox _ QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.aW..(textEdit)
        tab2.sL..(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Table")
        self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")

    ___ createBottomRightGroupBox(self):
        self.bottomRightGroupBox _ QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        lineEdit _ QLineEdit('s3cRe7')
        lineEdit.setEchoMode(QLineEdit.Password)

        spinBox _ QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        dateTimeEdit _ QDateTimeEdit(self.bottomRightGroupBox)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        slider _ QSlider(__.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        scrollBar _ QScrollBar(__.Horizontal, self.bottomRightGroupBox)
        scrollBar.setValue(60)

        dial _ QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        layout _ QGridLayout()
        layout.aW..(lineEdit, 0, 0, 1, 2)
        layout.aW..(spinBox, 1, 0, 1, 2)
        layout.aW..(dateTimeEdit, 2, 0, 1, 2)
        layout.aW..(slider, 3, 0)
        layout.aW..(scrollBar, 4, 0)
        layout.aW..(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.sL..(layout)

    ___ createProgressBar(self):
        self.progressBar _ QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer _ QTimer(self)
        timer.timeout.c..(self.advanceProgressBar)
        timer.start(1000)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    gallery _ WidgetGallery()
    gallery.s..
    sys.exit(app.exec_()) 
