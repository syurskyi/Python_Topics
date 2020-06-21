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


______ ___

____ ?.?C.. ______ ?D.., __
____ ?.?G.. ______ ?F.., ?P..
____ ?.?W.. ______ (?A.., QCheckBox, QColorDialog, ?D..,
        QErrorMessage, ?FD.., QFontDialog, QFrame, QGridLayout,
        QInputDialog, ?L.., QLineEdit, ?MB.., ?PB..)


c_ Dialog(?D..):
    MESSAGE _ "<p>Message boxes have a caption, a text, and up to three " \
            "buttons, each with standard or custom texts.</p>" \
            "<p>Click a button to close the message box. Pressing the Esc " \
            "button will activate the detected escape button (if any).</p>"

    ___  -   parent_None):
        s__(Dialog, self). - (parent)

        openFilesPath _ ''

        errorMessageDialog _ QErrorMessage

        frameStyle _ QFrame.Sunken | QFrame.Panel

        integerLabel _ ?L..
        integerLabel.setFrameStyle(frameStyle)
        integerButton _ ?PB..("QInputDialog.get&Int()")

        doubleLabel _ ?L..
        doubleLabel.setFrameStyle(frameStyle)
        doubleButton _ ?PB..("QInputDialog.get&Double()")

        itemLabel _ ?L..
        itemLabel.setFrameStyle(frameStyle)
        itemButton _ ?PB..("QInputDialog.getIte&m()")

        textLabel _ ?L..
        textLabel.setFrameStyle(frameStyle)
        textButton _ ?PB..("QInputDialog.get&Text()")

        colorLabel _ ?L..
        colorLabel.setFrameStyle(frameStyle)
        colorButton _ ?PB..("QColorDialog.get&Color()")

        fontLabel _ ?L..
        fontLabel.setFrameStyle(frameStyle)
        fontButton _ ?PB..("QFontDialog.get&Font()")

        directoryLabel _ ?L..
        directoryLabel.setFrameStyle(frameStyle)
        directoryButton _ ?PB..("QFileDialog.getE&xistingDirectory()")

        openFileNameLabel _ ?L..
        openFileNameLabel.setFrameStyle(frameStyle)
        openFileNameButton _ ?PB..("QFileDialog.get&OpenFileName()")

        openFileNamesLabel _ ?L..
        openFileNamesLabel.setFrameStyle(frameStyle)
        openFileNamesButton _ ?PB..("QFileDialog.&getOpenFileNames()")

        saveFileNameLabel _ ?L..
        saveFileNameLabel.setFrameStyle(frameStyle)
        saveFileNameButton _ ?PB..("QFileDialog.get&SaveFileName()")

        criticalLabel _ ?L..
        criticalLabel.setFrameStyle(frameStyle)
        criticalButton _ ?PB..("QMessageBox.critica&l()")

        informationLabel _ ?L..
        informationLabel.setFrameStyle(frameStyle)
        informationButton _ ?PB..("QMessageBox.i&nformation()")

        questionLabel _ ?L..
        questionLabel.setFrameStyle(frameStyle)
        questionButton _ ?PB..("QMessageBox.&question()")

        warningLabel _ ?L..
        warningLabel.setFrameStyle(frameStyle)
        warningButton _ ?PB..("QMessageBox.&warning()")

        errorLabel _ ?L..
        errorLabel.setFrameStyle(frameStyle)
        errorButton _ ?PB..("QErrorMessage.show&M&essage()")

        integerButton.c__.c..(setInteger)
        doubleButton.c__.c..(setDouble)
        itemButton.c__.c..(setItem)
        textButton.c__.c..(sT..)
        colorButton.c__.c..(sC..)
        fontButton.c__.c..(sF..)
        directoryButton.c__.c..(setExistingDirectory)
        openFileNameButton.c__.c..(setOpenFileName)
        openFileNamesButton.c__.c..(setOpenFileNames)
        saveFileNameButton.c__.c..(setSaveFileName)
        criticalButton.c__.c..(criticalMessage)
        informationButton.c__.c..(informationMessage)
        questionButton.c__.c..(questionMessage)
        warningButton.c__.c..(warningMessage)
        errorButton.c__.c..(errorMessage)

        native _ QCheckBox()
        native.sT..("Use native file dialog.")
        native.sC__( st.
        __ ___.platform no. __ ("win32", "darwin"):
            native.hide()

        layout _ QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
        layout.aW..(integerButton, 0, 0)
        layout.aW..(integerLabel, 0, 1)
        layout.aW..(doubleButton, 1, 0)
        layout.aW..(doubleLabel, 1, 1)
        layout.aW..(itemButton, 2, 0)
        layout.aW..(itemLabel, 2, 1)
        layout.aW..(textButton, 3, 0)
        layout.aW..(textLabel, 3, 1)
        layout.aW..(colorButton, 4, 0)
        layout.aW..(colorLabel, 4, 1)
        layout.aW..(fontButton, 5, 0)
        layout.aW..(fontLabel, 5, 1)
        layout.aW..(directoryButton, 6, 0)
        layout.aW..(directoryLabel, 6, 1)
        layout.aW..(openFileNameButton, 7, 0)
        layout.aW..(openFileNameLabel, 7, 1)
        layout.aW..(openFileNamesButton, 8, 0)
        layout.aW..(openFileNamesLabel, 8, 1)
        layout.aW..(saveFileNameButton, 9, 0)
        layout.aW..(saveFileNameLabel, 9, 1)
        layout.aW..(criticalButton, 10, 0)
        layout.aW..(criticalLabel, 10, 1)
        layout.aW..(informationButton, 11, 0)
        layout.aW..(informationLabel, 11, 1)
        layout.aW..(questionButton, 12, 0)
        layout.aW..(questionLabel, 12, 1)
        layout.aW..(warningButton, 13, 0)
        layout.aW..(warningLabel, 13, 1)
        layout.aW..(errorButton, 14, 0)
        layout.aW..(errorLabel, 14, 1)
        layout.aW..(native, 15, 0)
        sL..(layout)

        sWT..("Standard Dialogs")

    ___ setInteger 
        i, ok _ QInputDialog.getInt  "QInputDialog.getInt()",
                "Percentage:", 25, 0, 100, 1)
        __ ok:
            integerLabel.sT..("%d%%" % i)

    ___ setDouble 
        d, ok _ QInputDialog.getDouble  "QInputDialog.getDouble()",
                "Amount:", 37.56, -10000, 10000, 2)
        __ ok:
            doubleLabel.sT..("$%g" % d)

    ___ setItem 
        i.. _ ("Spring", "Summer", "Fall", "Winter")

        item, ok _ QInputDialog.getItem  "QInputDialog.getItem()",
                "Season:", i.., 0, F..)
        __ ok and item:
            itemLabel.sT..(item)

    ___ sT.. 
        t__, ok _ QInputDialog.getText  "QInputDialog.getText()",
                "User name:", QLineEdit.Normal, ?D...h.. .dirName())
        __ ok and t__ !_ '':
            textLabel.sT..(t__)

    ___ sC.. 
        color _ QColorDialog.getColor(__.green, self)
        __ color.isValid
            colorLabel.sT..(color.name())
            colorLabel.sP..(?P..(color))
            colorLabel.setAutoFillBackground( st.

    ___ sF.. 
        font, ok _ QFontDialog.getFont(?F..(fontLabel.t__()), self)
        __ ok:
            fontLabel.sT..(font.key())
            fontLabel.sF..(font)

    ___ setExistingDirectory 
        options _ ?FD...DontResolveSymlinks | ?FD...ShowDirsOnly
        directory _ ?FD...getExistingDirectory
                "QFileDialog.getExistingDirectory()",
                directoryLabel.t__(), options_options)
        __ directory:
            directoryLabel.sT..(directory)

    ___ setOpenFileName 
        options _ ?FD...Options()
        __ no. native.isChecked
            options |_ ?FD...DontUseNativeDialog
        fileName, _ _ ?FD...gOFN..
                "QFileDialog.getOpenFileName()", openFileNameLabel.t__(),
                "All Files (*);;Text Files (*.txt)", options_options)
        __ fileName:
            openFileNameLabel.sT..(fileName)

    ___ setOpenFileNames 
        options _ ?FD...Options()
        __ no. native.isChecked
            options |_ ?FD...DontUseNativeDialog
        files, _ _ ?FD...getOpenFileNames
                "QFileDialog.getOpenFileNames()", openFilesPath,
                "All Files (*);;Text Files (*.txt)", options_options)
        __ files:
            openFilesPath _ files[0]
            openFileNamesLabel.sT..("[%s]" % ', '.join(files))

    ___ setSaveFileName 
        options _ ?FD...Options()
        __ no. native.isChecked
            options |_ ?FD...DontUseNativeDialog
        fileName, _ _ ?FD...getSaveFileName
                "QFileDialog.getSaveFileName()",
                saveFileNameLabel.t__(),
                "All Files (*);;Text Files (*.txt)", options_options)
        __ fileName:
            saveFileNameLabel.sT..(fileName)

    ___ criticalMessage 
        reply _ ?MB...c..  "QMessageBox.critical()",
                Dialog.MESSAGE,
                ?MB...Abort | ?MB...Retry | ?MB...Ignore)
        __ reply __ ?MB...Abort:
            criticalLabel.sT..("Abort")
        ____ reply __ ?MB...Retry:
            criticalLabel.sT..("Retry")
        ____
            criticalLabel.sT..("Ignore")

    ___ informationMessage 
        reply _ ?MB...i..
                "QMessageBox.information()", Dialog.MESSAGE)
        __ reply __ ?MB...Ok:
            informationLabel.sT..("OK")
        ____
            informationLabel.sT..("Escape")

    ___ questionMessage 
        reply _ ?MB...q..  "QMessageBox.question()",
                Dialog.MESSAGE,
                ?MB...Yes | ?MB...No | ?MB...Cancel)
        __ reply __ ?MB...Yes:
            questionLabel.sT..("Yes")
        ____ reply __ ?MB...No:
            questionLabel.sT..("No")
        ____
            questionLabel.sT..("Cancel")

    ___ warningMessage 
        msgBox _ ?MB..(?MB...Warning, "QMessageBox.warning()",
                Dialog.MESSAGE, ?MB...NoButton, self)
        msgBox.addButton("Save &Again", ?MB...AcceptRole)
        msgBox.addButton("&Continue", ?MB...RejectRole)
        __ msgBox.e.. __ ?MB...AcceptRole:
            warningLabel.sT..("Save Again")
        ____
            warningLabel.sT..("Continue")

    ___ errorMessage 
        errorMessageDialog.sM..("This dialog shows and remembers "
                "error messages. If the checkbox is checked (as it is by "
                "default), the shown message will be shown again, but if the "
                "user unchecks the box the message will not appear again if "
                "QErrorMessage.showMessage() is called with the same message.")
        errorLabel.sT..("If the box is unchecked, the message won't "
                "appear again.")


__ ______ __ ______
    app _ ?A..(___.a..
    dialog _ Dialog()
    dialog.s..
    ___.e.. ?.e..
