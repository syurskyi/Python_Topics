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


______ math

____ ?.?C.. ______ __
____ ?.?W.. ______ (?A.., QGridLayout, QLayout, QLineEdit,
        QSizePolicy, QToolButton, QWidget)


c_ Button(QToolButton):
    ___ __init__  t__, parent_None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.sT..(t__)

    ___ sizeHint(self):
        size _ super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        r_ size


c_ Calculator(QWidget):
    NumDigitButtons _ 10
    
    ___ __init__  parent_None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator _ ''
        self.pendingMultiplicativeOperator _ ''

        self.sumInMemory _ 0.0
        self.sumSoFar _ 0.0
        self.factorSoFar _ 0.0
        self.waitingForOperand _ True

        self.display _ QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(__.AlignRight)
        self.display.setMaxLength(15)

        font _ self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons _   # list
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.ap..(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton _ self.createButton(".", self.pointClicked)
        self.changeSignButton _ self.createButton(u"\N{PLUS-MINUS SIGN}",
                self.changeSignClicked)

        self.backspaceButton _ self.createButton("Backspace",
                self.backspaceClicked)
        self.clearButton _ self.createButton("Clear", self.clear)
        self.clearAllButton _ self.createButton("Clear All", self.clearAll)

        self.clearMemoryButton _ self.createButton("MC", self.clearMemory)
        self.readMemoryButton _ self.createButton("MR", self.readMemory)
        self.setMemoryButton _ self.createButton("MS", self.setMemory)
        self.addToMemoryButton _ self.createButton("M+", self.addToMemory)

        self.divisionButton _ self.createButton(u"\N{DIVISION SIGN}",
                self.multiplicativeOperatorClicked)
        self.timesButton _ self.createButton(u"\N{MULTIPLICATION SIGN}",
                self.multiplicativeOperatorClicked)
        self.minusButton _ self.createButton("-", self.additiveOperatorClicked)
        self.plusButton _ self.createButton("+", self.additiveOperatorClicked)

        self.squareRootButton _ self.createButton("Sqrt",
                self.unaryOperatorClicked)
        self.powerButton _ self.createButton(u"x\N{SUPERSCRIPT TWO}",
                self.unaryOperatorClicked)
        self.reciprocalButton _ self.createButton("1/x",
                self.unaryOperatorClicked)
        self.equalButton _ self.createButton("=", self.equalClicked)

        mainLayout _ QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.aW..(self.display, 0, 0, 1, 6)
        mainLayout.aW..(self.backspaceButton, 1, 0, 1, 2)
        mainLayout.aW..(self.clearButton, 1, 2, 1, 2)
        mainLayout.aW..(self.clearAllButton, 1, 4, 1, 2)

        mainLayout.aW..(self.clearMemoryButton, 2, 0)
        mainLayout.aW..(self.readMemoryButton, 3, 0)
        mainLayout.aW..(self.setMemoryButton, 4, 0)
        mainLayout.aW..(self.addToMemoryButton, 5, 0)

        for i in range(1, Calculator.NumDigitButtons):
            row _ ((9 - i) / 3) + 2
            column _ ((i - 1) % 3) + 1
            mainLayout.aW..(self.digitButtons[i], row, column)

        mainLayout.aW..(self.digitButtons[0], 5, 1)
        mainLayout.aW..(self.pointButton, 5, 2)
        mainLayout.aW..(self.changeSignButton, 5, 3)

        mainLayout.aW..(self.divisionButton, 2, 4)
        mainLayout.aW..(self.timesButton, 3, 4)
        mainLayout.aW..(self.minusButton, 4, 4)
        mainLayout.aW..(self.plusButton, 5, 4)

        mainLayout.aW..(self.squareRootButton, 2, 5)
        mainLayout.aW..(self.powerButton, 3, 5)
        mainLayout.aW..(self.reciprocalButton, 4, 5)
        mainLayout.aW..(self.equalButton, 5, 5)
        self.sL..(mainLayout)

        self.setWindowTitle("Calculator")

    ___ digitClicked(self):
        clickedButton _ self.sender()
        digitValue _ int(clickedButton.t__())

        __ self.display.t__() == '0' and digitValue == 0.0:
            r_

        __ self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand _ False

        self.display.sT..(self.display.t__() + str(digitValue))

    ___ unaryOperatorClicked(self):
        clickedButton _ self.sender()
        clickedOperator _ clickedButton.t__()
        operand _ float(self.display.t__())

        __ clickedOperator == "Sqrt":
            __ operand < 0.0:
                self.abortOperation()
                r_

            result _ math.sqrt(operand)
        ____ clickedOperator == u"x\N{SUPERSCRIPT TWO}":
            result _ math.pow(operand, 2.0)
        ____ clickedOperator == "1/x":
            __ operand == 0.0:
                self.abortOperation()
                r_

            result _ 1.0 / operand

        self.display.sT..(str(result))
        self.waitingForOperand _ True

    ___ additiveOperatorClicked(self):
        clickedButton _ self.sender()
        clickedOperator _ clickedButton.t__()
        operand _ float(self.display.t__())

        __ self.pendingMultiplicativeOperator:
            __ no. self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                r_

            self.display.sT..(str(self.factorSoFar))
            operand _ self.factorSoFar
            self.factorSoFar _ 0.0
            self.pendingMultiplicativeOperator _ ''

        __ self.pendingAdditiveOperator:
            __ no. self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                r_

            self.display.sT..(str(self.sumSoFar))
        ____
            self.sumSoFar _ operand

        self.pendingAdditiveOperator _ clickedOperator
        self.waitingForOperand _ True

    ___ multiplicativeOperatorClicked(self):
        clickedButton _ self.sender()
        clickedOperator _ clickedButton.t__()
        operand _ float(self.display.t__())

        __ self.pendingMultiplicativeOperator:
            __ no. self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                r_

            self.display.sT..(str(self.factorSoFar))
        ____
            self.factorSoFar _ operand

        self.pendingMultiplicativeOperator _ clickedOperator
        self.waitingForOperand _ True

    ___ equalClicked(self):
        operand _ float(self.display.t__())

        __ self.pendingMultiplicativeOperator:
            __ no. self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                r_

            operand _ self.factorSoFar
            self.factorSoFar _ 0.0
            self.pendingMultiplicativeOperator _ ''

        __ self.pendingAdditiveOperator:
            __ no. self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                r_

            self.pendingAdditiveOperator _ ''
        ____
            self.sumSoFar _ operand

        self.display.sT..(str(self.sumSoFar))
        self.sumSoFar _ 0.0
        self.waitingForOperand _ True

    ___ pointClicked(self):
        __ self.waitingForOperand:
            self.display.sT..('0')

        __ "." no. in self.display.t__
            self.display.sT..(self.display.t__() + ".")

        self.waitingForOperand _ False

    ___ changeSignClicked(self):
        t__ _ self.display.t__()
        value _ float(t__)

        __ value > 0.0:
            t__ _ "-" + t__
        ____ value < 0.0:
            t__ _ t__[1:]

        self.display.sT..(t__)

    ___ backspaceClicked(self):
        __ self.waitingForOperand:
            r_

        t__ _ self.display.t__()[:-1]
        __ no. t__:
            t__ _ '0'
            self.waitingForOperand _ True

        self.display.sT..(t__)

    ___ clear(self):
        __ self.waitingForOperand:
            r_

        self.display.sT..('0')
        self.waitingForOperand _ True

    ___ clearAll(self):
        self.sumSoFar _ 0.0
        self.factorSoFar _ 0.0
        self.pendingAdditiveOperator _ ''
        self.pendingMultiplicativeOperator _ ''
        self.display.sT..('0')
        self.waitingForOperand _ True

    ___ clearMemory(self):
        self.sumInMemory _ 0.0

    ___ readMemory(self):
        self.display.sT..(str(self.sumInMemory))
        self.waitingForOperand _ True

    ___ setMemory(self):
        self.equalClicked()
        self.sumInMemory _ float(self.display.t__())

    ___ addToMemory(self):
        self.equalClicked()
        self.sumInMemory +_ float(self.display.t__())

    ___ createButton  t__, member):
        button _ Button(t__)
        button.c__.c..(member)
        r_ button

    ___ abortOperation(self):
        self.clearAll()
        self.display.sT..("####")

    ___ calculate  rightOperand, pendingOperator):
        __ pendingOperator == "+":
            self.sumSoFar +_ rightOperand
        ____ pendingOperator == "-":
            self.sumSoFar -_ rightOperand
        ____ pendingOperator == u"\N{MULTIPLICATION SIGN}":
            self.factorSoFar *_ rightOperand
        ____ pendingOperator == u"\N{DIVISION SIGN}":
            __ rightOperand == 0.0:
                r_ False

            self.factorSoFar /_ rightOperand

        r_ True


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    calc _ Calculator()
    calc.s..
    ___.exit(app.exec_())
