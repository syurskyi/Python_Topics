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


____ ?.?W.. ______ (?A.., QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, ?PB.., QSpinBox, QTextEdit,
        QVBoxLayout)


c_ Dialog(QDialog):
    NumGridRows _ 3
    NumButtons _ 4

    ___ __init__(self):
        super(Dialog, self).__init__()

        self.createMenu()
        self.createHorizontalGroupBox()
        self.createGridGroupBox()
        self.createFormGroupBox()

        bigEditor _ QTextEdit()
        bigEditor.sPT..("This widget takes up all the remaining space "
                "in the top-level layout.")

        buttonBox _ QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonBox.accepted.c..(self.accept)
        buttonBox.rejected.c..(self.reject)

        mainLayout _ QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(bigEditor)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Basic Layouts")

    ___ createMenu(self):
        self.menuBar _ QMenuBar()

        self.fileMenu _ QMenu("&File", self)
        self.exitAction _ self.fileMenu.aA..("E&xit")
        self.menuBar.aM..(self.fileMenu)

        self.exitAction.t__.c..(self.accept)

    ___ createHorizontalGroupBox(self):
        self.horizontalGroupBox _ QGroupBox("Horizontal layout")
        layout _ QHBoxLayout()

        for i in range(Dialog.NumButtons):
            button _ ?PB..("Button %d" % (i + 1))
            layout.addWidget(button)

        self.horizontalGroupBox.setLayout(layout)

    ___ createGridGroupBox(self):
        self.gridGroupBox _ QGroupBox("Grid layout")
        layout _ QGridLayout()

        for i in range(Dialog.NumGridRows):
            label _ QLabel("Line %d:" % (i + 1))
            lineEdit _ QLineEdit()
            layout.addWidget(label, i + 1, 0)
            layout.addWidget(lineEdit, i + 1, 1)

        self.smallEditor _ QTextEdit()
        self.smallEditor.sPT..("This widget takes up about two thirds "
                "of the grid layout.")

        layout.addWidget(self.smallEditor, 0, 2, 4, 1)

        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)
        self.gridGroupBox.setLayout(layout)

    ___ createFormGroupBox(self):
        self.formGroupBox _ QGroupBox("Form layout")
        layout _ QFormLayout()
        layout.addRow(QLabel("Line 1:"), QLineEdit())
        layout.addRow(QLabel("Line 2, long text:"), QComboBox())
        layout.addRow(QLabel("Line 3:"), QSpinBox())
        self.formGroupBox.setLayout(layout)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    dialog _ Dialog()
    sys.exit(dialog.exec_())
