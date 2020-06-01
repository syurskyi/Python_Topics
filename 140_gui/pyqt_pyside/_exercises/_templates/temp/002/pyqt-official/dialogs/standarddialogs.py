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

____ ?.QtCore ______ QDir, Qt
____ ?.QtGui ______ QFont, QPalette
____ ?.?W.. ______ (QApplication, QCheckBox, QColorDialog, QDialog,
        QErrorMessage, QFileDialog, QFontDialog, QFrame, QGridLayout,
        QInputDialog, QLabel, QLineEdit, QMessageBox, ?PB..)


class Dialog(QDialog):
    MESSAGE _ "<p>Message boxes have a caption, a text, and up to three " \
            "buttons, each with standard or custom texts.</p>" \
            "<p>Click a button to close the message box. Pressing the Esc " \
            "button will activate the detected escape button (if any).</p>"

    ___ __init__(self, parent_None):
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
        self.colorButton.c__.c..(self.setColor)
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
        if sys.platform not in ("win32", "darwin"):
            self.native.hide()

        layout _ QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
        layout.addWidget(self.integerButton, 0, 0)
        layout.addWidget(self.integerLabel, 0, 1)
        layout.addWidget(self.doubleButton, 1, 0)
        layout.addWidget(self.doubleLabel, 1, 1)
        layout.addWidget(self.itemButton, 2, 0)
        layout.addWidget(self.itemLabel, 2, 1)
        layout.addWidget(self.textButton, 3, 0)
        layout.addWidget(self.textLabel, 3, 1)
        layout.addWidget(self.colorButton, 4, 0)
        layout.addWidget(self.colorLabel, 4, 1)
        layout.addWidget(self.fontButton, 5, 0)
        layout.addWidget(self.fontLabel, 5, 1)
        layout.addWidget(self.directoryButton, 6, 0)
        layout.addWidget(self.directoryLabel, 6, 1)
        layout.addWidget(self.openFileNameButton, 7, 0)
        layout.addWidget(self.openFileNameLabel, 7, 1)
        layout.addWidget(self.openFileNamesButton, 8, 0)
        layout.addWidget(self.openFileNamesLabel, 8, 1)
        layout.addWidget(self.saveFileNameButton, 9, 0)
        layout.addWidget(self.saveFileNameLabel, 9, 1)
        layout.addWidget(self.criticalButton, 10, 0)
        layout.addWidget(self.criticalLabel, 10, 1)
        layout.addWidget(self.informationButton, 11, 0)
        layout.addWidget(self.informationLabel, 11, 1)
        layout.addWidget(self.questionButton, 12, 0)
        layout.addWidget(self.questionLabel, 12, 1)
        layout.addWidget(self.warningButton, 13, 0)
        layout.addWidget(self.warningLabel, 13, 1)
        layout.addWidget(self.errorButton, 14, 0)
        layout.addWidget(self.errorLabel, 14, 1)
        layout.addWidget(self.native, 15, 0)
        self.setLayout(layout)

        self.setWindowTitle("Standard Dialogs")

    ___ setInteger(self):
        i, ok _ QInputDialog.getInt(self, "QInputDialog.getInt()",
                "Percentage:", 25, 0, 100, 1)
        if ok:
            self.integerLabel.sT..("%d%%" % i)

    ___ setDouble(self):
        d, ok _ QInputDialog.getDouble(self, "QInputDialog.getDouble()",
                "Amount:", 37.56, -10000, 10000, 2)
        if ok:
            self.doubleLabel.sT..("$%g" % d)

    ___ setItem(self):
        items _ ("Spring", "Summer", "Fall", "Winter")

        item, ok _ QInputDialog.getItem(self, "QInputDialog.getItem()",
                "Season:", items, 0, False)
        if ok and item:
            self.itemLabel.sT..(item)

    ___ sT..(self):
        text, ok _ QInputDialog.getText(self, "QInputDialog.getText()",
                "User name:", QLineEdit.Normal, QDir.home().dirName())
        if ok and text !_ '':
            self.textLabel.sT..(text)

    ___ setColor(self):
        color _ QColorDialog.getColor(Qt.green, self)
        if color.isValid
            self.colorLabel.sT..(color.name())
            self.colorLabel.setPalette(QPalette(color))
            self.colorLabel.setAutoFillBackground(True)

    ___ setFont(self):
        font, ok _ QFontDialog.getFont(QFont(self.fontLabel.text()), self)
        if ok:
            self.fontLabel.sT..(font.key())
            self.fontLabel.setFont(font)

    ___ setExistingDirectory(self):
        options _ QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory _ QFileDialog.getExistingDirectory(self,
                "QFileDialog.getExistingDirectory()",
                self.directoryLabel.text(), options_options)
        if directory:
            self.directoryLabel.sT..(directory)

    ___ setOpenFileName(self):
        options _ QFileDialog.Options()
        if not self.native.isChecked
            options |_ QFileDialog.DontUseNativeDialog
        fileName, _ _ QFileDialog.getOpenFileName(self,
                "QFileDialog.getOpenFileName()", self.openFileNameLabel.text(),
                "All Files (*);;Text Files (*.txt)", options_options)
        if fileName:
            self.openFileNameLabel.sT..(fileName)

    ___ setOpenFileNames(self):
        options _ QFileDialog.Options()
        if not self.native.isChecked
            options |_ QFileDialog.DontUseNativeDialog
        files, _ _ QFileDialog.getOpenFileNames(self,
                "QFileDialog.getOpenFileNames()", self.openFilesPath,
                "All Files (*);;Text Files (*.txt)", options_options)
        if files:
            self.openFilesPath _ files[0]
            self.openFileNamesLabel.sT..("[%s]" % ', '.join(files))

    ___ setSaveFileName(self):
        options _ QFileDialog.Options()
        if not self.native.isChecked
            options |_ QFileDialog.DontUseNativeDialog
        fileName, _ _ QFileDialog.getSaveFileName(self,
                "QFileDialog.getSaveFileName()",
                self.saveFileNameLabel.text(),
                "All Files (*);;Text Files (*.txt)", options_options)
        if fileName:
            self.saveFileNameLabel.sT..(fileName)

    ___ criticalMessage(self):
        reply _ QMessageBox.critical(self, "QMessageBox.critical()",
                Dialog.MESSAGE,
                QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore)
        if reply == QMessageBox.Abort:
            self.criticalLabel.sT..("Abort")
        elif reply == QMessageBox.Retry:
            self.criticalLabel.sT..("Retry")
        else:
            self.criticalLabel.sT..("Ignore")

    ___ informationMessage(self):
        reply _ QMessageBox.information(self,
                "QMessageBox.information()", Dialog.MESSAGE)
        if reply == QMessageBox.Ok:
            self.informationLabel.sT..("OK")
        else:
            self.informationLabel.sT..("Escape")

    ___ questionMessage(self):
        reply _ QMessageBox.question(self, "QMessageBox.question()",
                Dialog.MESSAGE,
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.questionLabel.sT..("Yes")
        elif reply == QMessageBox.No:
            self.questionLabel.sT..("No")
        else:
            self.questionLabel.sT..("Cancel")

    ___ warningMessage(self):
        msgBox _ QMessageBox(QMessageBox.Warning, "QMessageBox.warning()",
                Dialog.MESSAGE, QMessageBox.NoButton, self)
        msgBox.addButton("Save &Again", QMessageBox.AcceptRole)
        msgBox.addButton("&Continue", QMessageBox.RejectRole)
        if msgBox.e.. == QMessageBox.AcceptRole:
            self.warningLabel.sT..("Save Again")
        else:
            self.warningLabel.sT..("Continue")

    ___ errorMessage(self):
        self.errorMessageDialog.showMessage("This dialog shows and remembers "
                "error messages. If the checkbox is checked (as it is by "
                "default), the shown message will be shown again, but if the "
                "user unchecks the box the message will not appear again if "
                "QErrorMessage.showMessage() is called with the same message.")
        self.errorLabel.sT..("If the box is unchecked, the message won't "
                "appear again.")


if __name__ == '__main__':
    app _ QApplication(sys.argv)
    dialog _ Dialog()
    dialog.s..
    sys.exit(app.exec_())
