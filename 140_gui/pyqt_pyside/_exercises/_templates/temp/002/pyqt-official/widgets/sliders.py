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


____ ?.?C.. ______ pyqtSignal, __
____ ?.?W.. ______ (?A.., QBoxLayout, QCheckBox, QComboBox,
        QDial, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QScrollBar,
        QSlider, QSpinBox, QStackedWidget, QWidget)


c_ SlidersGroup(QGroupBox):

    valueChanged _ pyqtSignal(int)

    ___  -   orientation, title, parent_None):
        super(SlidersGroup, self). - (title, parent)

        slider _ QSlider(orientation)
        slider.sFP..(__.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(1)

        scrollBar _ QScrollBar(orientation)
        scrollBar.sFP..(__.StrongFocus)

        dial _ QDial()
        dial.sFP..(__.StrongFocus)

        slider.valueChanged.c..(scrollBar.setValue)
        scrollBar.valueChanged.c..(dial.setValue)
        dial.valueChanged.c..(slider.setValue)
        dial.valueChanged.c..(valueChanged)

        __ orientation == __.Horizontal:
            direction _ QBoxLayout.TopToBottom
        ____
            direction _ QBoxLayout.LeftToRight

        slidersLayout _ QBoxLayout(direction)
        slidersLayout.aW..(slider)
        slidersLayout.aW..(scrollBar)
        slidersLayout.aW..(dial)
        sL..(slidersLayout)

    ___ setValue  value):    
        slider.setValue(value)

    ___ setMinimum  value):    
        slider.setMinimum(value)
        scrollBar.setMinimum(value)
        dial.setMinimum(value)

    ___ setMaximum  value):    
        slider.setMaximum(value)
        scrollBar.setMaximum(value)
        dial.setMaximum(value)

    ___ invertAppearance  invert):
        slider.setInvertedAppearance(invert)
        scrollBar.setInvertedAppearance(invert)
        dial.setInvertedAppearance(invert)

    ___ invertKeyBindings  invert):
        slider.setInvertedControls(invert)
        scrollBar.setInvertedControls(invert)
        dial.setInvertedControls(invert)


c_ Window(QWidget):
    ___  -
        super(Window, self). - ()

        horizontalSliders _ SlidersGroup(__.Horizontal,
                "Horizontal")
        verticalSliders _ SlidersGroup(__.Vertical, "Vertical")

        stackedWidget _ QStackedWidget()
        stackedWidget.aW..(horizontalSliders)
        stackedWidget.aW..(verticalSliders)

        createControls("Controls")

        horizontalSliders.valueChanged.c..(verticalSliders.setValue)
        verticalSliders.valueChanged.c..(valueSpinBox.setValue)
        valueSpinBox.valueChanged.c..(horizontalSliders.setValue)

        layout _ QHBoxLayout()
        layout.aW..(controlsGroup)
        layout.aW..(stackedWidget)
        sL..(layout)

        minimumSpinBox.setValue(0)
        maximumSpinBox.setValue(20)
        valueSpinBox.setValue(5)

        sWT..("Sliders")

    ___ createControls  title):
        controlsGroup _ QGroupBox(title)

        minimumLabel _ QLabel("Minimum value:")
        maximumLabel _ QLabel("Maximum value:")
        valueLabel _ QLabel("Current value:")

        invertedAppearance _ QCheckBox("Inverted appearance")
        invertedKeyBindings _ QCheckBox("Inverted key bindings")

        minimumSpinBox _ QSpinBox()
        minimumSpinBox.setRange(-100, 100)
        minimumSpinBox.setSingleStep(1)

        maximumSpinBox _ QSpinBox()
        maximumSpinBox.setRange(-100, 100)
        maximumSpinBox.setSingleStep(1)

        valueSpinBox _ QSpinBox()
        valueSpinBox.setRange(-100, 100)
        valueSpinBox.setSingleStep(1)

        orientationCombo _ QComboBox()
        orientationCombo.addItem("Horizontal slider-like widgets")
        orientationCombo.addItem("Vertical slider-like widgets")

        orientationCombo.activated.c..(stackedWidget.setCurrentIndex)
        minimumSpinBox.valueChanged.c..(horizontalSliders.setMinimum)
        minimumSpinBox.valueChanged.c..(verticalSliders.setMinimum)
        maximumSpinBox.valueChanged.c..(horizontalSliders.setMaximum)
        maximumSpinBox.valueChanged.c..(verticalSliders.setMaximum)
        invertedAppearance.toggled.c..(horizontalSliders.invertAppearance)
        invertedAppearance.toggled.c..(verticalSliders.invertAppearance)
        invertedKeyBindings.toggled.c..(horizontalSliders.invertKeyBindings)
        invertedKeyBindings.toggled.c..(verticalSliders.invertKeyBindings)

        controlsLayout _ QGridLayout()
        controlsLayout.aW..(minimumLabel, 0, 0)
        controlsLayout.aW..(maximumLabel, 1, 0)
        controlsLayout.aW..(valueLabel, 2, 0)
        controlsLayout.aW..(minimumSpinBox, 0, 1)
        controlsLayout.aW..(maximumSpinBox, 1, 1)
        controlsLayout.aW..(valueSpinBox, 2, 1)
        controlsLayout.aW..(invertedAppearance, 0, 2)
        controlsLayout.aW..(invertedKeyBindings, 1, 2)
        controlsLayout.aW..(orientationCombo, 3, 0, 1, 3)
        controlsGroup.sL..(controlsLayout)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ Window()
    window.s..
    ___.e..(app.exec_())
