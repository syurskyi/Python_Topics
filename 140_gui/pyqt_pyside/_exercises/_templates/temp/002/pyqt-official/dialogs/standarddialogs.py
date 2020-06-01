#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
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


______ sys

____ ?.?C.. ______ QDir, __
____ ?.?G.. ______ QFont, ?P..
____ ?.?W.. ______ (?A.., QCheckBox, QColorDialog, QDialog,
        QErrorMessage, ?FD.., QFontDialog, QFrame, QGridLayout,
        QInputDialog, QLabel, QLineEdit, ?MB.., ?PB..)


c_ Dialog(QDialog):
    MESSAGE _ "<p>Message boxes have a caption, a text, and up to three " \
            "buttons, each with standard or custom texts.</p>" \
            "<p>Click a button to close the message box. Pressing the Esc " \
            "button will activate the detected escape button (if any).</p>"

    ___ __init__  parent_None):
        super(Dialog, self).__init__(parent)

        self.openFilesPath _ ''

        self.errorMessageDialog _ QErrorMessage(self)

        frameStyle _ QFrame.Sunken | QFrame.Panel

        self.integerLabel _ QLabel()
        self.integerLabel.setFrameStyle(frameStyle)
        self.integerButton _ ?PB..("QInputDialog.get&Int()")

        self.doubleLabel _ QLabel()
        self.doubleLabel.setFrameStyle(frameStyle)
        self.doubleButton _ ?PB..("QInputDialog.get&Double()")

        self.itemLabel _ QLabel()
        self.itemLabel.setFrameStyle(frameStyle)
        self.itemButton _ ?PB..("QInputDialog.getIte&m()")

        self.textLabel _ QLabel()
        self.textLabel.setFrameStyle(frameStyle)
        self.textButton _ ?PB..("QInputDialog.get&Text()")

        self.colorLabel _ QLabel()
        self.colorLabel.setFrameStyle(frameStyle)
        self.colorButton _ ?PB..("QColorDialog.get&Color()")

        self.fontLabel _ QLabel()
        self.fontLabel.setFrameStyle(frameStyle)
        self.fontButton _ ?PB..("QFontDialog.get&Font()")

        self.directoryLabel _ QLabel()
        self.directoryLabel.setFrameStyle(frameStyle)
        self.directoryButton _ ?PB..("QFileDialog.getE&xistingDirectory()")

        self.openFileNameLabel _ QLabel()
        self.openFileNameLabel.setFrameStyle(frameStyle)
        self.openFileNameButton _ ?PB..("QFileDialog.get&OpenFileName()")

        self.openFileNamesLabel _ QLabel()
        self.openFileNamesLabel.setFrameStyle(frameStyle)
        self.openFileNamesButton _ ?PB..("QFileDialog.&getOpenFileNames()")

        self.saveFileNameLabel _ QLabel()
        self.saveFileNameLabel.setFrameStyle(frameStyle)
        self.saveFileNameButton _ ?PB..("QFileDialog.get&SaveFileName()")

        self.criticalLabel _ QLabel()
        self.criticalLabel.setFrameStyle(frameStyle)
        self.criticalButton _ ?PB..("QMessageBox.critica&l()")

        self.informationLabel _ QLabel()
        self.informationLabel.setFrameStyle(frameStyle)
        self.informationButton _ ?PB..("QMessageBox.i&nformation()")

        self.questionLabel _ QLabel()
        self.questionLabel.setFrameStyle(frameStyle)
        self.questionButton _ ?PB..("QMessageBox.&question()")

        self.warningLabel _ QLabel()
        self.warningLabel.setFrameStyle(frameStyle)
        self.warningButton _ ?PB..("QMessageBox.&warning()")

        self.errorLabel _ QLabel()
        self.errorLabel.setFrameStyle(frameStyle)
        self.errorButton _ ?PB..("QErrorMessage.show&M&essage()")

        self.integerButton.c__.c..(self.setInteger)
        self.doubleButton.c__.c..(self.setDouble)
        self.itemButton.c__.c..(self.setItem)
        self.textButton.c__.c..(self.sT..)
        self.colorButton.c__.c..(self.sC..)
        self.fontButton.c__.c..(self.setFont)
        self.directoryButton.c__.c..(self.setExistingDirectory)
        self.openFileNameButton.c__.c..(self.setOpenFileName)
        self.openFileNamesButton.c__.c..(self.setOpenFileNames)
        self.saveFileNameButton.c__.c..(self.setSaveFileName)
        self.criticalButton.c__.c..(self.criticalMessage)
        self.informationButton.c__.c..(self.informationMessage)
        self.questionButton.c__.c..(self.questionMessage)
        self.warningButton.c__.c..(self.warningMessage)
        self.errorButton.c__.c..(self.errorMessage)

        self.native _ QCheckBox()
        self.native.sT..("Use native file dialog.")
        self.native.setChecked(True)
        __ sys.platform no. in ("win32", "darwin"):
            self.native.hide()

        layout _ QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
        layout.aW..(self.integerButton, 0, 0)
        layout.aW..(self.integerLabel, 0, 1)
        layout.aW..(self.doubleButton, 1, 0)
        layout.aW..(self.doubleLabel, 1, 1)
        layout.aW..(self.itemButton, 2, 0)
        layout.aW..(self.itemLabel, 2, 1)
        layout.aW..(self.textButton, 3, 0)
        layout.aW..(self.textLabel, 3, 1)
        layout.aW..(self.colorButton, 4, 0)
        layout.aW..(self.colorLabel, 4, 1)
        layout.aW..(self.fontButton, 5, 0)
        layout.aW..(self.fontLabel, 5, 1)
        layout.aW..(self.directoryButton, 6, 0)
        layout.aW..(self.directoryLabel, 6, 1)
        layout.aW..(self.openFileNameButton, 7, 0)
        layout.aW..(self.openFileNameLabel, 7, 1)
        layout.aW..(self.openFileNamesButton, 8, 0)
        layout.aW..(self.openFileNamesLabel, 8, 1)
        layout.aW..(self.saveFileNameButton, 9, 0)
        layout.aW..(self.saveFileNameLabel, 9, 1)
        layout.aW..(self.criticalButton, 10, 0)
        layout.aW..(self.criticalLabel, 10, 1)
        layout.aW..(self.informationButton, 11, 0)
        layout.aW..(self.informationLabel, 11, 1)
        layout.aW..(self.questionButton, 12, 0)
        layout.aW..(self.questionLabel, 12, 1)
        layout.aW..(self.warningButton, 13, 0)
        layout.aW..(self.warningLabel, 13, 1)
        layout.aW..(self.errorButton, 14, 0)
        layout.aW..(self.errorLabel, 14, 1)
        layout.aW..(self.native, 15, 0)
        self.sL..(layout)

        self.setWindowTitle("Standard Dialogs")

    ___ setInteger(self):
        i, ok _ QInputDialog.getInt  "QInputDialog.getInt()",
                "Percentage:", 25, 0, 100, 1)
        __ ok:
            self.integerLabel.sT..("%d%%" % i)

    ___ setDouble(self):
        d, ok _ QInputDialog.getDouble  "QInputDialog.getDouble()",
                "Amount:", 37.56, -10000, 10000, 2)
        __ ok:
            self.doubleLabel.sT..("$%g" % d)

    ___ setItem(self):
        items _ ("Spring", "Summer", "Fall", "Winter")

        item, ok _ QInputDialog.getItem  "QInputDialog.getItem()",
                "Season:", items, 0, False)
        __ ok and item:
            self.itemLabel.sT..(item)

    ___ sT..(self):
        t__, ok _ QInputDialog.getText  "QInputDialog.getText()",
                "User name:", QLineEdit.Normal, QDir.home().dirName())
        __ ok and t__ !_ '':
            self.textLabel.sT..(t__)

    ___ sC..(self):
        color _ QColorDialog.getColor(__.green, self)
        __ color.isValid
            self.colorLabel.sT..(color.name())
            self.colorLabel.sP..(?P..(color))
            self.colorLabel.setAutoFillBackground(True)

    ___ setFont(self):
        font, ok _ QFontDialog.getFont(QFont(self.fontLabel.t__()), self)
        __ ok:
            self.fontLabel.sT..(font.key())
            self.fontLabel.setFont(font)

    ___ setExistingDirectory(self):
        options _ ?FD...DontResolveSymlinks | ?FD...ShowDirsOnly
        directory _ ?FD...getExistingDirectory
                "QFileDialog.getExistingDirectory()",
                self.directoryLabel.t__(), options_options)
        __ directory:
            self.directoryLabel.sT..(directory)

    ___ setOpenFileName(self):
        options _ ?FD...Options()
        __ no. self.native.isChecked
            options |_ ?FD...DontUseNativeDialog
        fileName, _ _ ?FD...gOFN..
                "QFileDialog.getOpenFileName()", self.openFileNameLabel.t__(),
                "All Files (*);;Text Files (*.txt)", options_options)
        __ fileName:
            self.openFileNameLabel.sT..(fileName)

    ___ setOpenFileNames(self):
        options _ ?FD...Options()
        __ no. self.native.isChecked
            options |_ ?FD...DontUseNativeDialog
        files, _ _ ?FD...getOpenFileNames
                "QFileDialog.getOpenFileNames()", self.openFilesPath,
                "All Files (*);;Text Files (*.txt)", options_options)
        __ files:
            self.openFilesPath _ files[0]
            self.openFileNamesLabel.sT..("[%s]" % ', '.join(files))

    ___ setSaveFileName(self):
        options _ ?FD...Options()
        __ no. self.native.isChecked
            options |_ ?FD...DontUseNativeDialog
        fileName, _ _ ?FD...getSaveFileName
                "QFileDialog.getSaveFileName()",
                self.saveFileNameLabel.t__(),
                "All Files (*);;Text Files (*.txt)", options_options)
        __ fileName:
            self.saveFileNameLabel.sT..(fileName)

    ___ criticalMessage(self):
        reply _ ?MB...critical  "QMessageBox.critical()",
                Dialog.MESSAGE,
                ?MB...Abort | ?MB...Retry | ?MB...Ignore)
        __ reply == ?MB...Abort:
            self.criticalLabel.sT..("Abort")
        ____ reply == ?MB...Retry:
            self.criticalLabel.sT..("Retry")
        ____
            self.criticalLabel.sT..("Ignore")

    ___ informationMessage(self):
        reply _ ?MB...information
                "QMessageBox.information()", Dialog.MESSAGE)
        __ reply == ?MB...Ok:
            self.informationLabel.sT..("OK")
        ____
            self.informationLabel.sT..("Escape")

    ___ questionMessage(self):
        reply _ ?MB...q..  "QMessageBox.question()",
                Dialog.MESSAGE,
                ?MB...Yes | ?MB...No | ?MB...Cancel)
        __ reply == ?MB...Yes:
            self.questionLabel.sT..("Yes")
        ____ reply == ?MB...No:
            self.questionLabel.sT..("No")
        ____
            self.questionLabel.sT..("Cancel")

    ___ warningMessage(self):
        msgBox _ ?MB..(?MB...Warning, "QMessageBox.warning()",
                Dialog.MESSAGE, ?MB...NoButton, self)
        msgBox.addButton("Save &Again", ?MB...AcceptRole)
        msgBox.addButton("&Continue", ?MB...RejectRole)
        __ msgBox.e.. == ?MB...AcceptRole:
            self.warningLabel.sT..("Save Again")
        ____
            self.warningLabel.sT..("Continue")

    ___ errorMessage(self):
        self.errorMessageDialog.showMessage("This dialog shows and remembers "
                "error messages. If the checkbox is checked (as it is by "
                "default), the shown message will be shown again, but if the "
                "user unchecks the box the message will not appear again if "
                "QErrorMessage.showMessage() is called with the same message.")
        self.errorLabel.sT..("If the box is unchecked, the message won't "
                "appear again.")


__ __name__ == '__main__':
    app _ ?A..(sys.argv)
    dialog _ Dialog()
    dialog.s..
    sys.exit(app.exec_())
