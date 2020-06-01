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
____ ?.?W.. ______ (?A.., QCheckBox, QDialog,
        QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
        ?PB.., QVBoxLayout, QWidget)


class FindDialog(QDialog):
    ___ __init__(self, parent_None):
        super(FindDialog, self).__init__(parent)

        label _ QLabel("Find &what:")
        lineEdit _ QLineEdit()
        label.setBuddy(lineEdit)

        caseCheckBox _ QCheckBox("Match &case")
        fromStartCheckBox _ QCheckBox("Search from &start")
        fromStartCheckBox.setChecked(True)

        findButton _ ?PB..("&Find")
        findButton.setDefault(True)

        moreButton _ ?PB..("&More")
        moreButton.setCheckable(True)
        moreButton.setAutoDefault(False)

        extension _ QWidget()

        wholeWordsCheckBox _ QCheckBox("&Whole words")
        backwardCheckBox _ QCheckBox("Search &backward")
        searchSelectionCheckBox _ QCheckBox("Search se&lection")

        buttonBox _ QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(findButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(moreButton, QDialogButtonBox.ActionRole)

        moreButton.toggled.c..(extension.setVisible)

        extensionLayout _ QVBoxLayout()
        extensionLayout.setContentsMargins(0, 0, 0, 0)
        extensionLayout.addWidget(wholeWordsCheckBox)
        extensionLayout.addWidget(backwardCheckBox)
        extensionLayout.addWidget(searchSelectionCheckBox)
        extension.setLayout(extensionLayout)

        topLeftLayout _ QHBoxLayout()
        topLeftLayout.addWidget(label)
        topLeftLayout.addWidget(lineEdit)

        leftLayout _ QVBoxLayout()
        leftLayout.addLayout(topLeftLayout)
        leftLayout.addWidget(caseCheckBox)
        leftLayout.addWidget(fromStartCheckBox)

        mainLayout _ QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(leftLayout, 0, 0)
        mainLayout.addWidget(buttonBox, 0, 1)
        mainLayout.addWidget(extension, 1, 0, 1, 2)
        mainLayout.setRowStretch(2, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Extension")
        extension.hide()


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    dialog _ FindDialog()
    dialog.s..
    sys.exit(app.exec_())
