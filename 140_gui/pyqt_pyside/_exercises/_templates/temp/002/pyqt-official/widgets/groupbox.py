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


____ ?.QtCore ______ Qt
____ ?.?W.. ______ (?A.., QCheckBox, QGridLayout, QGroupBox,
        QMenu, ?PB.., QRadioButton, QVBoxLayout, QWidget)


c_ Window(QWidget):
    ___ __init__  parent_None):
        super(Window, self).__init__(parent)

        grid _ QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)
        self.setLayout(grid)

        self.setWindowTitle("Group Box")
        self.resize(480, 320)

    ___ createFirstExclusiveGroup(self):
        groupBox _ QGroupBox("Exclusive Radio Buttons")

        radio1 _ QRadioButton("&Radio button 1")
        radio2 _ QRadioButton("R&adio button 2")
        radio3 _ QRadioButton("Ra&dio button 3")

        radio1.setChecked(True)

        vbox _ QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        r_ groupBox

    ___ createSecondExclusiveGroup(self):
        groupBox _ QGroupBox("E&xclusive Radio Buttons")
        groupBox.setCheckable(True)
        groupBox.setChecked F..

        radio1 _ QRadioButton("Rad&io button 1")
        radio2 _ QRadioButton("Radi&o button 2")
        radio3 _ QRadioButton("Radio &button 3")
        radio1.setChecked(True)
        checkBox _ QCheckBox("Ind&ependent checkbox")
        checkBox.setChecked(True)

        vbox _ QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkBox)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        r_ groupBox

    ___ createNonExclusiveGroup(self):
        groupBox _ QGroupBox("Non-Exclusive Checkboxes")
        groupBox.setFlat(True)

        checkBox1 _ QCheckBox("&Checkbox 1")
        checkBox2 _ QCheckBox("C&heckbox 2")
        checkBox2.setChecked(True)
        tristateBox _ QCheckBox("Tri-&state button")
        tristateBox.setTristate(True)
        tristateBox.setCheckState(Qt.PartiallyChecked)

        vbox _ QVBoxLayout()
        vbox.addWidget(checkBox1)
        vbox.addWidget(checkBox2)
        vbox.addWidget(tristateBox)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        r_ groupBox

    ___ createPushButtonGroup(self):
        groupBox _ QGroupBox("&Push Buttons")
        groupBox.setCheckable(True)
        groupBox.setChecked(True)

        pushButton _ ?PB..("&Normal Button")
        toggleButton _ ?PB..("&Toggle Button")
        toggleButton.setCheckable(True)
        toggleButton.setChecked(True)
        flatButton _ ?PB..("&Flat Button")
        flatButton.setFlat(True)

        popupButton _ ?PB..("Pop&up Button")
        menu _ QMenu(self)
        menu.aA..("&First Item")
        menu.aA..("&Second Item")
        menu.aA..("&Third Item")
        menu.aA..("F&ourth Item")
        popupButton.setMenu(menu)

        newAction _ menu.aA..("Submenu")
        subMenu _ QMenu("Popup Submenu", self)
        subMenu.aA..("Item 1")
        subMenu.aA..("Item 2")
        subMenu.aA..("Item 3")
        newAction.setMenu(subMenu)

        vbox _ QVBoxLayout()
        vbox.addWidget(pushButton)
        vbox.addWidget(toggleButton)
        vbox.addWidget(flatButton)
        vbox.addWidget(popupButton)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        r_ groupBox


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    clock _ Window()
    clock.s..
    sys.exit(app.exec_())
