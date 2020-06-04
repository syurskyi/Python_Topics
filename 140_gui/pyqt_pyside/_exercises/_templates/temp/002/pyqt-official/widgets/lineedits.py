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
____ ?.?W.. ______ (?A.., ?CB, QGridLayout, ?GB..,
        ?L.., QLineEdit, ?W..)


c_ Window(?W..):
    ___  -
        s__(Window, self). - ()

        echoGroup _ ?GB..("Echo")

        echoLabel _ ?L..("Mode:")
        echoComboBox _ ?CB()
        echoComboBox.aI..("Normal")
        echoComboBox.aI..("Password")
        echoComboBox.aI..("PasswordEchoOnEdit")
        echoComboBox.aI..("No Echo")

        echoLineEdit _ ?LE..
        echoLineEdit.setFocus()

        validatorGroup _ ?GB..("Validator")

        validatorLabel _ ?L..("Type:")
        validatorComboBox _ ?CB()
        validatorComboBox.aI..("No validator")
        validatorComboBox.aI..("Integer validator")
        validatorComboBox.aI..("Double validator")

        validatorLineEdit _ ?LE..

        alignmentGroup _ ?GB..("Alignment")

        alignmentLabel _ ?L..("Type:")
        alignmentComboBox _ ?CB()
        alignmentComboBox.aI..("Left")
        alignmentComboBox.aI..("Centered")
        alignmentComboBox.aI..("Right")

        alignmentLineEdit _ ?LE..

        inputMaskGroup _ ?GB..("Input mask")

        inputMaskLabel _ ?L..("Type:")
        inputMaskComboBox _ ?CB()
        inputMaskComboBox.aI..("No mask")
        inputMaskComboBox.aI..("Phone number")
        inputMaskComboBox.aI..("ISO date")
        inputMaskComboBox.aI..("License key")

        inputMaskLineEdit _ ?LE..

        accessGroup _ ?GB..("Access")

        accessLabel _ ?L..("Read-only:")
        accessComboBox _ ?CB()
        accessComboBox.aI..("False")
        accessComboBox.aI..("True")

        accessLineEdit _ ?LE..

        echoComboBox.activated.c..(echoChanged)
        validatorComboBox.activated.c..(validatorChanged)
        alignmentComboBox.activated.c..(alignmentChanged)
        inputMaskComboBox.activated.c..(inputMaskChanged)
        accessComboBox.activated.c..(accessChanged)

        echoLayout _ QGridLayout()
        echoLayout.aW..(echoLabel, 0, 0)
        echoLayout.aW..(echoComboBox, 0, 1)
        echoLayout.aW..(echoLineEdit, 1, 0, 1, 2)
        echoGroup.sL..(echoLayout)

        validatorLayout _ QGridLayout()
        validatorLayout.aW..(validatorLabel, 0, 0)
        validatorLayout.aW..(validatorComboBox, 0, 1)
        validatorLayout.aW..(validatorLineEdit, 1, 0, 1, 2)
        validatorGroup.sL..(validatorLayout)

        alignmentLayout _ QGridLayout()
        alignmentLayout.aW..(alignmentLabel, 0, 0)
        alignmentLayout.aW..(alignmentComboBox, 0, 1)
        alignmentLayout.aW..(alignmentLineEdit, 1, 0, 1, 2)
        alignmentGroup. sL..(alignmentLayout)

        inputMaskLayout _ QGridLayout()
        inputMaskLayout.aW..(inputMaskLabel, 0, 0)
        inputMaskLayout.aW..(inputMaskComboBox, 0, 1)
        inputMaskLayout.aW..(inputMaskLineEdit, 1, 0, 1, 2)
        inputMaskGroup.sL..(inputMaskLayout)

        accessLayout _ QGridLayout()
        accessLayout.aW..(accessLabel, 0, 0)
        accessLayout.aW..(accessComboBox, 0, 1)
        accessLayout.aW..(accessLineEdit, 1, 0, 1, 2)
        accessGroup.sL..(accessLayout)

        layout _ QGridLayout()
        layout.aW..(echoGroup, 0, 0)
        layout.aW..(validatorGroup, 1, 0)
        layout.aW..(alignmentGroup, 2, 0)
        layout.aW..(inputMaskGroup, 0, 1)
        layout.aW..(accessGroup, 1, 1)
        sL..(layout)

        sWT..("Line Edits")

    ___ echoChanged  index):
        __ index __ 0:
            echoLineEdit.setEchoMode(QLineEdit.Normal)
        ____ index __ 1:
            echoLineEdit.setEchoMode(QLineEdit.Password)
        ____ index __ 2:
            echoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        ____ index __ 3:
    	    echoLineEdit.setEchoMode(QLineEdit.NoEcho)

    ___ validatorChanged  index):
        __ index __ 0:
            validatorLineEdit.sV..(0)
        ____ index __ 1:
            validatorLineEdit.sV..(QIntValidator(validatorLineEdit))
        ____ index __ 2:
            validatorLineEdit.sV..(QDoubleValidator(-999.0, 999.0, 2, validatorLineEdit))

        validatorLineEdit.c..

    ___ alignmentChanged  index):
        __ index __ 0:
            alignmentLineEdit.setAlignment(__.AlignLeft)
        ____ index __ 1:
            alignmentLineEdit.setAlignment(__.AlignCenter)
        ____ index __ 2:
    	    alignmentLineEdit.setAlignment(__.AlignRight)

    ___ inputMaskChanged  index):
        __ index __ 0:
            inputMaskLineEdit.setInputMask('')
        ____ index __ 1:
            inputMaskLineEdit.setInputMask('+99 99 99 99 99;_')
        ____ index __ 2:
            inputMaskLineEdit.setInputMask('0000-00-00')
            inputMaskLineEdit.sT..('00000000')
            inputMaskLineEdit.setCursorPosition(0)
        ____ index __ 3:
            inputMaskLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

    ___ accessChanged  index):
        __ index __ 0:
            accessLineEdit.sRO.. F..
        ____ index __ 1:
            accessLineEdit.sRO..( st.


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ Window()
    window.s..
    ___.e.. ?.e..
