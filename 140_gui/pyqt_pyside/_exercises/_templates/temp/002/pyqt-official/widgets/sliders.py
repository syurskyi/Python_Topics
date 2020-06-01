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


____ ?.QtCore ______ pyqtSignal, Qt
____ ?.?W.. ______ (?A.., QBoxLayout, QCheckBox, QComboBox,
        QDial, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QScrollBar,
        QSlider, QSpinBox, QStackedWidget, QWidget)


c_ SlidersGroup(QGroupBox):

    valueChanged _ pyqtSignal(int)

    ___ __init__  orientation, title, parent_None):
        super(SlidersGroup, self).__init__(title, parent)

        self.slider _ QSlider(orientation)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)

        self.scrollBar _ QScrollBar(orientation)
        self.scrollBar.setFocusPolicy(Qt.StrongFocus)

        self.dial _ QDial()
        self.dial.setFocusPolicy(Qt.StrongFocus)

        self.slider.valueChanged.c..(self.scrollBar.setValue)
        self.scrollBar.valueChanged.c..(self.dial.setValue)
        self.dial.valueChanged.c..(self.slider.setValue)
        self.dial.valueChanged.c..(self.valueChanged)

        __ orientation == Qt.Horizontal:
            direction _ QBoxLayout.TopToBottom
        ____
            direction _ QBoxLayout.LeftToRight

        slidersLayout _ QBoxLayout(direction)
        slidersLayout.addWidget(self.slider)
        slidersLayout.addWidget(self.scrollBar)
        slidersLayout.addWidget(self.dial)
        self.setLayout(slidersLayout)    

    ___ setValue  value):    
        self.slider.setValue(value)    

    ___ setMinimum  value):    
        self.slider.setMinimum(value)
        self.scrollBar.setMinimum(value)
        self.dial.setMinimum(value)    

    ___ setMaximum  value):    
        self.slider.setMaximum(value)
        self.scrollBar.setMaximum(value)
        self.dial.setMaximum(value)    

    ___ invertAppearance  invert):
        self.slider.setInvertedAppearance(invert)
        self.scrollBar.setInvertedAppearance(invert)
        self.dial.setInvertedAppearance(invert)    

    ___ invertKeyBindings  invert):
        self.slider.setInvertedControls(invert)
        self.scrollBar.setInvertedControls(invert)
        self.dial.setInvertedControls(invert)


c_ Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        self.horizontalSliders _ SlidersGroup(Qt.Horizontal,
                "Horizontal")
        self.verticalSliders _ SlidersGroup(Qt.Vertical, "Vertical")

        self.stackedWidget _ QStackedWidget()
        self.stackedWidget.addWidget(self.horizontalSliders)
        self.stackedWidget.addWidget(self.verticalSliders)

        self.createControls("Controls")

        self.horizontalSliders.valueChanged.c..(self.verticalSliders.setValue)
        self.verticalSliders.valueChanged.c..(self.valueSpinBox.setValue)
        self.valueSpinBox.valueChanged.c..(self.horizontalSliders.setValue)

        layout _ QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.minimumSpinBox.setValue(0)
        self.maximumSpinBox.setValue(20)
        self.valueSpinBox.setValue(5)

        self.setWindowTitle("Sliders")

    ___ createControls  title):
        self.controlsGroup _ QGroupBox(title)

        minimumLabel _ QLabel("Minimum value:")
        maximumLabel _ QLabel("Maximum value:")
        valueLabel _ QLabel("Current value:")

        invertedAppearance _ QCheckBox("Inverted appearance")
        invertedKeyBindings _ QCheckBox("Inverted key bindings")

        self.minimumSpinBox _ QSpinBox()
        self.minimumSpinBox.setRange(-100, 100)
        self.minimumSpinBox.setSingleStep(1)

        self.maximumSpinBox _ QSpinBox()
        self.maximumSpinBox.setRange(-100, 100)
        self.maximumSpinBox.setSingleStep(1)

        self.valueSpinBox _ QSpinBox()
        self.valueSpinBox.setRange(-100, 100)
        self.valueSpinBox.setSingleStep(1)

        orientationCombo _ QComboBox()
        orientationCombo.addItem("Horizontal slider-like widgets")
        orientationCombo.addItem("Vertical slider-like widgets")

        orientationCombo.activated.c..(self.stackedWidget.setCurrentIndex)
        self.minimumSpinBox.valueChanged.c..(self.horizontalSliders.setMinimum)
        self.minimumSpinBox.valueChanged.c..(self.verticalSliders.setMinimum)
        self.maximumSpinBox.valueChanged.c..(self.horizontalSliders.setMaximum)
        self.maximumSpinBox.valueChanged.c..(self.verticalSliders.setMaximum)
        invertedAppearance.toggled.c..(self.horizontalSliders.invertAppearance)
        invertedAppearance.toggled.c..(self.verticalSliders.invertAppearance)
        invertedKeyBindings.toggled.c..(self.horizontalSliders.invertKeyBindings)
        invertedKeyBindings.toggled.c..(self.verticalSliders.invertKeyBindings)

        controlsLayout _ QGridLayout()
        controlsLayout.addWidget(minimumLabel, 0, 0)
        controlsLayout.addWidget(maximumLabel, 1, 0)
        controlsLayout.addWidget(valueLabel, 2, 0)
        controlsLayout.addWidget(self.minimumSpinBox, 0, 1)
        controlsLayout.addWidget(self.maximumSpinBox, 1, 1)
        controlsLayout.addWidget(self.valueSpinBox, 2, 1)
        controlsLayout.addWidget(invertedAppearance, 0, 2)
        controlsLayout.addWidget(invertedKeyBindings, 1, 2)
        controlsLayout.addWidget(orientationCombo, 3, 0, 1, 3)
        self.controlsGroup.setLayout(controlsLayout)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ Window()
    window.s..
    sys.exit(app.exec_())
