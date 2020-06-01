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
____ ?.?G.. ______ QDoubleValidator, QIntValidator
____ ?.?W.. ______ (?A.., QComboBox, QGridLayout, QGroupBox,
        QLabel, QLineEdit, QWidget)


c_ Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        echoGroup _ QGroupBox("Echo")

        echoLabel _ QLabel("Mode:")
        echoComboBox _ QComboBox()
        echoComboBox.addItem("Normal")
        echoComboBox.addItem("Password")
        echoComboBox.addItem("PasswordEchoOnEdit")
        echoComboBox.addItem("No Echo")

        self.echoLineEdit _ ?LE..
        self.echoLineEdit.setFocus()

        validatorGroup _ QGroupBox("Validator")

        validatorLabel _ QLabel("Type:")
        validatorComboBox _ QComboBox()
        validatorComboBox.addItem("No validator")
        validatorComboBox.addItem("Integer validator")
        validatorComboBox.addItem("Double validator")

        self.validatorLineEdit _ ?LE..

        alignmentGroup _ QGroupBox("Alignment")

        alignmentLabel _ QLabel("Type:")
        alignmentComboBox _ QComboBox()
        alignmentComboBox.addItem("Left")
        alignmentComboBox.addItem("Centered")
        alignmentComboBox.addItem("Right")

        self.alignmentLineEdit _ ?LE..

        inputMaskGroup _ QGroupBox("Input mask")

        inputMaskLabel _ QLabel("Type:")
        inputMaskComboBox _ QComboBox()
        inputMaskComboBox.addItem("No mask")
        inputMaskComboBox.addItem("Phone number")
        inputMaskComboBox.addItem("ISO date")
        inputMaskComboBox.addItem("License key")

        self.inputMaskLineEdit _ ?LE..

        accessGroup _ QGroupBox("Access")

        accessLabel _ QLabel("Read-only:")
        accessComboBox _ QComboBox()
        accessComboBox.addItem("False")
        accessComboBox.addItem("True")

        self.accessLineEdit _ ?LE..

        echoComboBox.activated.c..(self.echoChanged)
        validatorComboBox.activated.c..(self.validatorChanged)
        alignmentComboBox.activated.c..(self.alignmentChanged)
        inputMaskComboBox.activated.c..(self.inputMaskChanged)
        accessComboBox.activated.c..(self.accessChanged)

        echoLayout _ QGridLayout()
        echoLayout.aW..(echoLabel, 0, 0)
        echoLayout.aW..(echoComboBox, 0, 1)
        echoLayout.aW..(self.echoLineEdit, 1, 0, 1, 2)
        echoGroup.sL..(echoLayout)

        validatorLayout _ QGridLayout()
        validatorLayout.aW..(validatorLabel, 0, 0)
        validatorLayout.aW..(validatorComboBox, 0, 1)
        validatorLayout.aW..(self.validatorLineEdit, 1, 0, 1, 2)
        validatorGroup.sL..(validatorLayout)

        alignmentLayout _ QGridLayout()
        alignmentLayout.aW..(alignmentLabel, 0, 0)
        alignmentLayout.aW..(alignmentComboBox, 0, 1)
        alignmentLayout.aW..(self.alignmentLineEdit, 1, 0, 1, 2)
        alignmentGroup. sL..(alignmentLayout)

        inputMaskLayout _ QGridLayout()
        inputMaskLayout.aW..(inputMaskLabel, 0, 0)
        inputMaskLayout.aW..(inputMaskComboBox, 0, 1)
        inputMaskLayout.aW..(self.inputMaskLineEdit, 1, 0, 1, 2)
        inputMaskGroup.sL..(inputMaskLayout)

        accessLayout _ QGridLayout()
        accessLayout.aW..(accessLabel, 0, 0)
        accessLayout.aW..(accessComboBox, 0, 1)
        accessLayout.aW..(self.accessLineEdit, 1, 0, 1, 2)
        accessGroup.sL..(accessLayout)

        layout _ QGridLayout()
        layout.aW..(echoGroup, 0, 0)
        layout.aW..(validatorGroup, 1, 0)
        layout.aW..(alignmentGroup, 2, 0)
        layout.aW..(inputMaskGroup, 0, 1)
        layout.aW..(accessGroup, 1, 1)
        self.sL..(layout)

        self.setWindowTitle("Line Edits")

    ___ echoChanged  index):
        __ index == 0:
            self.echoLineEdit.setEchoMode(QLineEdit.Normal)
        ____ index == 1:
            self.echoLineEdit.setEchoMode(QLineEdit.Password)
        ____ index == 2:
            self.echoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        ____ index == 3:
    	    self.echoLineEdit.setEchoMode(QLineEdit.NoEcho)

    ___ validatorChanged  index):
        __ index == 0:
            self.validatorLineEdit.setValidator(0)
        ____ index == 1:
            self.validatorLineEdit.setValidator(QIntValidator(self.validatorLineEdit))
        ____ index == 2:
            self.validatorLineEdit.setValidator(QDoubleValidator(-999.0, 999.0, 2, self.validatorLineEdit))

        self.validatorLineEdit.clear()

    ___ alignmentChanged  index):
        __ index == 0:
            self.alignmentLineEdit.setAlignment(__.AlignLeft)
        ____ index == 1:
            self.alignmentLineEdit.setAlignment(__.AlignCenter)
        ____ index == 2:
    	    self.alignmentLineEdit.setAlignment(__.AlignRight)

    ___ inputMaskChanged  index):
        __ index == 0:
            self.inputMaskLineEdit.setInputMask('')
        ____ index == 1:
            self.inputMaskLineEdit.setInputMask('+99 99 99 99 99;_')
        ____ index == 2:
            self.inputMaskLineEdit.setInputMask('0000-00-00')
            self.inputMaskLineEdit.sT..('00000000')
            self.inputMaskLineEdit.setCursorPosition(0)
        ____ index == 3:
            self.inputMaskLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

    ___ accessChanged  index):
        __ index == 0:
            self.accessLineEdit.setReadOnly F..
        ____ index == 1:
            self.accessLineEdit.setReadOnly(True)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ Window()
    window.s..
    sys.exit(app.exec_())
