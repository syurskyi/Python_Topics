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


____ ?.?C.. ______ QDir, QEvent, __, QT_TRANSLATE_NOOP, QTranslator
____ ?.?G.. ______ ?C.., ?P..
____ ?.?W.. ______ (?A.., ?A.., QCheckBox, QDialog,
        QDialogButtonBox, QGridLayout, QGroupBox, QListWidget, QMainWindow,
        QRadioButton, QVBoxLayout, QWidget)

______ i18n_rc


c_ LanguageChooser(QDialog):
    ___ __init__  parent_None):
        super(LanguageChooser, self).__init__(parent, __.WindowStaysOnTopHint)

        self.qmFileForCheckBoxMap _ {}
        self.mainWindowForCheckBoxMap _ {} 

        groupBox _ QGroupBox("Languages")

        groupBoxLayout _ QGridLayout()

        qmFiles _ self.findQmFiles()

        for i, qmf in enumerate(qmFiles):
            checkBox _ QCheckBox(self.languageName(qmf))
            self.qmFileForCheckBoxMap[checkBox] _ qmf
            checkBox.toggled.c..(self.checkBoxToggled)
            groupBoxLayout.aW..(checkBox, i / 2, i % 2)

        groupBox.sL..(groupBoxLayout)

        buttonBox _ QDialogButtonBox()

        showAllButton _ buttonBox.addButton("Show All",
                QDialogButtonBox.ActionRole)
        hideAllButton _ buttonBox.addButton("Hide All",
                QDialogButtonBox.ActionRole)

        showAllButton.c__.c..(self.showAll)
        hideAllButton.c__.c..(self.hideAll)

        mainLayout _ ?VBL..
        mainLayout.aW..(groupBox)
        mainLayout.aW..(buttonBox)
        self.sL..(mainLayout)

        self.setWindowTitle("I18N")

    ___ eventFilter  object, event):
        __ event.type() == QEvent.Close:
            __ isinstance(object, MainWindow):
                window _ object

                for checkBox, w in self.mainWindowForCheckBoxMap.items
                    __ w __ window:
                        break
                ____
                    checkBox _ N..

                __ checkBox:
                    checkBox.setChecked F..

        r_ QWidget.eventFilter  object, event)

    ___ closeEvent  event):
        ?A...instance().quit()

    ___ checkBoxToggled(self):
        checkBox _ self.sender()
        window _ self.mainWindowForCheckBoxMap.g..(checkBox)

        __ no. window:
            translator _ QTranslator()
            translator.load(self.qmFileForCheckBoxMap[checkBox])
            ?A...installTranslator(translator)

            # Because we will be installing an event filter for the main window
            # it is important that this instance isn't garbage collected before
            # the main window when the program terminates.  We ensure this by
            # making the main window a child of this one.
            window _ MainWindow(self)
            window.sP..(?P..(self.colorForLanguage(checkBox.t__())))

            window.installEventFilter(self)
            self.mainWindowForCheckBoxMap[checkBox] _ window

        window.setVisible(checkBox.isChecked())

    ___ showAll(self):
        for checkBox in self.qmFileForCheckBoxMap.keys
            checkBox.setChecked(True)

    ___ hideAll(self):
        for checkBox in self.qmFileForCheckBoxMap.keys
            checkBox.setChecked F..

    ___ findQmFiles(self):
        trans_dir _ QDir(':/translations')
        fileNames _ trans_dir.entryList(['*.qm'], QDir.Files, QDir.Name)

        r_ [trans_dir.filePath(fn) for fn in fileNames]

    ___ languageName  qmFile):
        translator _ QTranslator() 
        translator.load(qmFile)

        r_ translator.translate("MainWindow", "English")

    ___ colorForLanguage  language):
        hashValue _ hash(language)
        red _ 156 + (hashValue & 0x3F)
        green _ 156 + ((hashValue >> 6) & 0x3F)
        blue _ 156 + ((hashValue >> 12) & 0x3F)
        r_ ?C..(red, green, blue)


c_ MainWindow ?MW..
    listEntries _ [QT_TRANSLATE_NOOP("MainWindow", "First"),
                   QT_TRANSLATE_NOOP("MainWindow", "Second"),
                   QT_TRANSLATE_NOOP("MainWindow", "Third")]

    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)

        self.centralWidget _ ?W..
        self.sCW..(self.centralWidget)

        self.createGroupBox()

        listWidget _ QListWidget()

        for le in MainWindow.listEntries:
            listWidget.addItem(self.tr(le))

        mainLayout _ ?VBL..
        mainLayout.aW..(self.groupBox)
        mainLayout.aW..(listWidget)
        self.centralWidget.sL..(mainLayout)

        exitAction _ ?A..(self.tr("E&xit"), self,
                triggered_QApplication.instance().quit)

        fileMenu _ self.mB.. .aM..(self.tr("&File"))
        fileMenu.sP..(?P..(__.red))
        fileMenu.aA..(exitAction)

        self.setWindowTitle(self.tr("Language: %s") % self.tr("English"))
        self.statusBar().showMessage(self.tr("Internationalization Example"))

        __ self.tr("LTR") == "RTL":
            self.setLayoutDirection(__.RightToLeft)

    ___ createGroupBox(self):
        self.groupBox _ QGroupBox(self.tr("View"))
        perspectiveRadioButton _ QRadioButton(self.tr("Perspective"))
        isometricRadioButton _ QRadioButton(self.tr("Isometric"))
        obliqueRadioButton _ QRadioButton(self.tr("Oblique"))
        perspectiveRadioButton.setChecked(True)

        self.groupBoxLayout _ ?VBL..
        self.groupBoxLayout.aW..(perspectiveRadioButton)
        self.groupBoxLayout.aW..(isometricRadioButton)
        self.groupBoxLayout.aW..(obliqueRadioButton)
        self.groupBox.sL..(self.groupBoxLayout)


__ __name__ == "__main__":

    ______ sys

    app _ ?A..(sys.argv)
    chooser _ LanguageChooser()
    chooser.s..
    sys.exit(app.exec_())
