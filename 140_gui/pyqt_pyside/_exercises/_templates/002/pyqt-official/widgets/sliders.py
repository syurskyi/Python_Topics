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


____ ?.?C.. ______ pS.., __
____ ?.?W.. ______ (?A.., QBoxLayout, QCheckBox, ?CB,
        QDial, QGridLayout, ?GB.., ?HBL.., ?L.., QScrollBar,
        ?S.., SB.., ?SW.., ?W..)


c_ SlidersGroup(?GB..):

    valueChanged _ pS..(in.)

    ___  -   orientation, title, parent_None):
        s__(SlidersGroup, self). - (title, parent)

        slider _ ?S..(orientation)
        slider.sFP..(__.StrongFocus)
        slider.setTickPosition(?S...TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(1)

        scrollBar _ QScrollBar(orientation)
        scrollBar.sFP..(__.StrongFocus)

        dial _ QDial()
        dial.sFP..(__.StrongFocus)

        slider.valueChanged.c..(scrollBar.sV..)
        scrollBar.valueChanged.c..(dial.sV..)
        dial.valueChanged.c..(slider.sV..)
        dial.valueChanged.c..(valueChanged)

        __ orientation __ __.H..:
            direction _ QBoxLayout.TopToBottom
        ____
            direction _ QBoxLayout.LeftToRight

        slidersLayout _ QBoxLayout(direction)
        slidersLayout.aW..(slider)
        slidersLayout.aW..(scrollBar)
        slidersLayout.aW..(dial)
        sL..(slidersLayout)

    ___ sV..  value):    
        slider.sV..(value)

    ___ setMinimum  value):    
        slider.setMinimum(value)
        scrollBar.setMinimum(value)
        dial.setMinimum(value)

    ___ sM..  value):
        slider.sM..(value)
        scrollBar.sM..(value)
        dial.sM..(value)

    ___ invertAppearance  invert):
        slider.setInvertedAppearance(invert)
        scrollBar.setInvertedAppearance(invert)
        dial.setInvertedAppearance(invert)

    ___ invertKeyBindings  invert):
        slider.setInvertedControls(invert)
        scrollBar.setInvertedControls(invert)
        dial.setInvertedControls(invert)


c_ Window(?W..):
    ___  -
        s__(Window, self). - ()

        horizontalSliders _ SlidersGroup(__.H..,
                "Horizontal")
        verticalSliders _ SlidersGroup(__.Vertical, "Vertical")

        stackedWidget _ ?SW..()
        stackedWidget.aW..(horizontalSliders)
        stackedWidget.aW..(verticalSliders)

        createControls("Controls")

        horizontalSliders.valueChanged.c..(verticalSliders.sV..)
        verticalSliders.valueChanged.c..(valueSpinBox.sV..)
        valueSpinBox.valueChanged.c..(horizontalSliders.sV..)

        layout _ ?HBL..
        layout.aW..(controlsGroup)
        layout.aW..(stackedWidget)
        sL..(layout)

        minimumSpinBox.sV..(0)
        maximumSpinBox.sV..(20)
        valueSpinBox.sV..(5)

        sWT..("Sliders")

    ___ createControls  title):
        controlsGroup _ ?GB..(title)

        minimumLabel _ ?L..("Minimum value:")
        maximumLabel _ ?L..("Maximum value:")
        valueLabel _ ?L..("Current value:")

        invertedAppearance _ QCheckBox("Inverted appearance")
        invertedKeyBindings _ QCheckBox("Inverted key bindings")

        minimumSpinBox _ SB..()
        minimumSpinBox.setRange(-100, 100)
        minimumSpinBox.setSingleStep(1)

        maximumSpinBox _ SB..()
        maximumSpinBox.setRange(-100, 100)
        maximumSpinBox.setSingleStep(1)

        valueSpinBox _ SB..()
        valueSpinBox.setRange(-100, 100)
        valueSpinBox.setSingleStep(1)

        orientationCombo _ ?CB()
        orientationCombo.aI..("Horizontal slider-like widgets")
        orientationCombo.aI..("Vertical slider-like widgets")

        orientationCombo.activated.c..(stackedWidget.sCI..)
        minimumSpinBox.valueChanged.c..(horizontalSliders.setMinimum)
        minimumSpinBox.valueChanged.c..(verticalSliders.setMinimum)
        maximumSpinBox.valueChanged.c..(horizontalSliders.sM..)
        maximumSpinBox.valueChanged.c..(verticalSliders.sM..)
        invertedAppearance.t__.c..(horizontalSliders.invertAppearance)
        invertedAppearance.t__.c..(verticalSliders.invertAppearance)
        invertedKeyBindings.t__.c..(horizontalSliders.invertKeyBindings)
        invertedKeyBindings.t__.c..(verticalSliders.invertKeyBindings)

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
    ___.e.. ?.e..
