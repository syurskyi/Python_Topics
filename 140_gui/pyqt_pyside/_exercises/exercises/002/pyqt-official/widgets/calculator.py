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


______ m__

____ ?.?C.. ______ __
____ ?.?W.. ______ (?A.., QGridLayout, QLayout, QLineEdit,
        ?SP.., QToolButton, ?W..)


c_ Button(QToolButton):
    ___  -   t__, parent_None):
        s__(Button, self). - (parent)

        sSP..(?SP...E.., ?SP...Preferred)
        sT..(t__)

    ___ sH..
        size _ s__(Button, self).sH..()
        size.setHeight(size.height() + 20)
        size.sW..(max(size.width(), size.height()))
        r_ size


c_ Calculator(?W..):
    NumDigitButtons _ 10
    
    ___  -   parent_None):
        s__(Calculator, self). - (parent)

        pendingAdditiveOperator _ ''
        pendingMultiplicativeOperator _ ''

        sumInMemory _ 0.0
        sumSoFar _ 0.0
        factorSoFar _ 0.0
        waitingForOperand _ T..

        display _ QLineEdit('0')
        display.sRO..( st.
        display.setAlignment(__.AlignRight)
        display.setMaxLength(15)

        font _ display.font()
        font.sPS..(font.pointSize() + 8)
        display.sF..(font)

        digitButtons _   # list
        
        ___ i __ ra..(Calculator.NumDigitButtons):
            digitButtons.ap..(createButton(st.(i),
                    digitClicked))

        pointButton _ createButton(".", pointClicked)
        changeSignButton _ createButton(u"\N{PLUS-MINUS SIGN}",
                changeSignClicked)

        backspaceButton _ createButton("Backspace",
                backspaceClicked)
        clearButton _ createButton("Clear", clear)
        clearAllButton _ createButton("Clear All", clearAll)

        clearMemoryButton _ createButton("MC", clearMemory)
        readMemoryButton _ createButton("MR", readMemory)
        setMemoryButton _ createButton("MS", setMemory)
        addToMemoryButton _ createButton("M+", addToMemory)

        divisionButton _ createButton(u"\N{DIVISION SIGN}",
                multiplicativeOperatorClicked)
        timesButton _ createButton(u"\N{MULTIPLICATION SIGN}",
                multiplicativeOperatorClicked)
        minusButton _ createButton("-", additiveOperatorClicked)
        plusButton _ createButton("+", additiveOperatorClicked)

        squareRootButton _ createButton("Sqrt",
                unaryOperatorClicked)
        powerButton _ createButton(u"x\N{SUPERSCRIPT TWO}",
                unaryOperatorClicked)
        reciprocalButton _ createButton("1/x",
                unaryOperatorClicked)
        equalButton _ createButton("=", equalClicked)

        mainLayout _ QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.aW..(display, 0, 0, 1, 6)
        mainLayout.aW..(backspaceButton, 1, 0, 1, 2)
        mainLayout.aW..(clearButton, 1, 2, 1, 2)
        mainLayout.aW..(clearAllButton, 1, 4, 1, 2)

        mainLayout.aW..(clearMemoryButton, 2, 0)
        mainLayout.aW..(readMemoryButton, 3, 0)
        mainLayout.aW..(setMemoryButton, 4, 0)
        mainLayout.aW..(addToMemoryButton, 5, 0)

        ___ i __ ra..(1, Calculator.NumDigitButtons):
            row _ ((9 - i) / 3) + 2
            column _ ((i - 1) % 3) + 1
            mainLayout.aW..(digitButtons[i], row, column)

        mainLayout.aW..(digitButtons[0], 5, 1)
        mainLayout.aW..(pointButton, 5, 2)
        mainLayout.aW..(changeSignButton, 5, 3)

        mainLayout.aW..(divisionButton, 2, 4)
        mainLayout.aW..(timesButton, 3, 4)
        mainLayout.aW..(minusButton, 4, 4)
        mainLayout.aW..(plusButton, 5, 4)

        mainLayout.aW..(squareRootButton, 2, 5)
        mainLayout.aW..(powerButton, 3, 5)
        mainLayout.aW..(reciprocalButton, 4, 5)
        mainLayout.aW..(equalButton, 5, 5)
        sL..(mainLayout)

        sWT..("Calculator")

    ___ digitClicked
        clickedButton _ sender()
        digitValue _ in.(clickedButton.t__())

        __ display.t__() __ '0' and digitValue __ 0.0:
            r_

        __ waitingForOperand:
            display.c..
            waitingForOperand _ F..

        display.sT..(display.t__() + st.(digitValue))

    ___ unaryOperatorClicked
        clickedButton _ sender()
        clickedOperator _ clickedButton.t__()
        operand _ fl..(display.t__())

        __ clickedOperator __ "Sqrt":
            __ operand < 0.0:
                abortOperation()
                r_

            result _ m__.sqrt(operand)
        ____ clickedOperator __ u"x\N{SUPERSCRIPT TWO}":
            result _ m__.pow(operand, 2.0)
        ____ clickedOperator __ "1/x":
            __ operand __ 0.0:
                abortOperation()
                r_

            result _ 1.0 / operand

        display.sT..(st.(result))
        waitingForOperand _ T..

    ___ additiveOperatorClicked
        clickedButton _ sender()
        clickedOperator _ clickedButton.t__()
        operand _ fl..(display.t__())

        __ pendingMultiplicativeOperator:
            __ no. calculate(operand, pendingMultiplicativeOperator):
                abortOperation()
                r_

            display.sT..(st.(factorSoFar))
            operand _ factorSoFar
            factorSoFar _ 0.0
            pendingMultiplicativeOperator _ ''

        __ pendingAdditiveOperator:
            __ no. calculate(operand, pendingAdditiveOperator):
                abortOperation()
                r_

            display.sT..(st.(sumSoFar))
        ____
            sumSoFar _ operand

        pendingAdditiveOperator _ clickedOperator
        waitingForOperand _ T..

    ___ multiplicativeOperatorClicked
        clickedButton _ sender()
        clickedOperator _ clickedButton.t__()
        operand _ fl..(display.t__())

        __ pendingMultiplicativeOperator:
            __ no. calculate(operand, pendingMultiplicativeOperator):
                abortOperation()
                r_

            display.sT..(st.(factorSoFar))
        ____
            factorSoFar _ operand

        pendingMultiplicativeOperator _ clickedOperator
        waitingForOperand _ T..

    ___ equalClicked
        operand _ fl..(display.t__())

        __ pendingMultiplicativeOperator:
            __ no. calculate(operand, pendingMultiplicativeOperator):
                abortOperation()
                r_

            operand _ factorSoFar
            factorSoFar _ 0.0
            pendingMultiplicativeOperator _ ''

        __ pendingAdditiveOperator:
            __ no. calculate(operand, pendingAdditiveOperator):
                abortOperation()
                r_

            pendingAdditiveOperator _ ''
        ____
            sumSoFar _ operand

        display.sT..(st.(sumSoFar))
        sumSoFar _ 0.0
        waitingForOperand _ T..

    ___ pointClicked
        __ waitingForOperand:
            display.sT..('0')

        __ "." no. __ display.t__
            display.sT..(display.t__() + ".")

        waitingForOperand _ F..

    ___ changeSignClicked
        t__ _ display.t__()
        value _ fl..(t__)

        __ value > 0.0:
            t__ _ "-" + t__
        ____ value < 0.0:
            t__ _ t__[1:]

        display.sT..(t__)

    ___ backspaceClicked
        __ waitingForOperand:
            r_

        t__ _ display.t__()[:-1]
        __ no. t__:
            t__ _ '0'
            waitingForOperand _ T..

        display.sT..(t__)

    ___ clear
        __ waitingForOperand:
            r_

        display.sT..('0')
        waitingForOperand _ T..

    ___ clearAll
        sumSoFar _ 0.0
        factorSoFar _ 0.0
        pendingAdditiveOperator _ ''
        pendingMultiplicativeOperator _ ''
        display.sT..('0')
        waitingForOperand _ T..

    ___ clearMemory
        sumInMemory _ 0.0

    ___ readMemory
        display.sT..(st.(sumInMemory))
        waitingForOperand _ T..

    ___ setMemory
        equalClicked()
        sumInMemory _ fl..(display.t__())

    ___ addToMemory
        equalClicked()
        sumInMemory +_ fl..(display.t__())

    ___ createButton  t__, member):
        button _ Button(t__)
        button.c__.c..(member)
        r_ button

    ___ abortOperation
        clearAll()
        display.sT..("####")

    ___ calculate  rightOperand, pendingOperator):
        __ pendingOperator __ "+":
            sumSoFar +_ rightOperand
        ____ pendingOperator __ "-":
            sumSoFar -_ rightOperand
        ____ pendingOperator __ u"\N{MULTIPLICATION SIGN}":
            factorSoFar *_ rightOperand
        ____ pendingOperator __ u"\N{DIVISION SIGN}":
            __ rightOperand __ 0.0:
                r_ F..

            factorSoFar /_ rightOperand

        r_ T..


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    calc _ Calculator()
    calc.s..
    ___.e.. ?.e..
