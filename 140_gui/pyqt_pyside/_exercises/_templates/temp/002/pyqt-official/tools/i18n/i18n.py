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


____ ?.?C.. ______ ?D.., QEvent, __, QT_TRANSLATE_NOOP, QTranslator
____ ?.?G.. ______ ?C.., ?P..
____ ?.?W.. ______ (?A.., ?A.., QCheckBox, ?D..,
        ?DBB..., QGridLayout, ?GB.., QListWidget, ?MW..,
        QRadioButton, ?VBL.., ?W..)

______ i18n_rc


c_ LanguageChooser(?D..):
    ___  -   parent_None):
        s__(LanguageChooser, self). - (parent, __.WindowStaysOnTopHint)

        qmFileForCheckBoxMap _   # dict
        mainWindowForCheckBoxMap _   # dict

        groupBox _ ?GB..("Languages")

        groupBoxLayout _ QGridLayout()

        qmFiles _ findQmFiles()

        ___ i, qmf __ en..(qmFiles):
            checkBox _ QCheckBox(languageName(qmf))
            qmFileForCheckBoxMap[checkBox] _ qmf
            checkBox.t__.c..(checkBoxToggled)
            groupBoxLayout.aW..(checkBox, i / 2, i % 2)

        groupBox.sL..(groupBoxLayout)

        buttonBox _ ?DBB...()

        showAllButton _ buttonBox.addButton("Show All",
                ?DBB....ActionRole)
        hideAllButton _ buttonBox.addButton("Hide All",
                ?DBB....ActionRole)

        showAllButton.c__.c..(showAll)
        hideAllButton.c__.c..(hideAll)

        mainLayout _ ?VBL..
        mainLayout.aW..(groupBox)
        mainLayout.aW..(buttonBox)
        sL..(mainLayout)

        sWT..("I18N")

    ___ eventFilter  object, event):
        __ event.type() __ QEvent.Close:
            __ isinstance(object, MainWindow):
                window _ object

                ___ checkBox, w __ mainWindowForCheckBoxMap.i..
                    __ w __ window:
                        break
                ____
                    checkBox _ N..

                __ checkBox:
                    checkBox.sC__ F..

        r_ ?W...eventFilter  object, event)

    ___ closeEvent  event):
        ?A...i.. .quit()

    ___ checkBoxToggled 
        checkBox _ sender()
        window _ mainWindowForCheckBoxMap.g..(checkBox)

        __ no. window:
            translator _ QTranslator()
            translator.load(qmFileForCheckBoxMap[checkBox])
            ?A...installTranslator(translator)

            # Because we will be installing an event filter for the main window
            # it is important that this instance isn't garbage collected before
            # the main window when the program terminates.  We ensure this by
            # making the main window a child of this one.
            window _ MainWindow
            window.sP..(?P..(colorForLanguage(checkBox.t__())))

            window.installEventFilter
            mainWindowForCheckBoxMap[checkBox] _ window

        window.setVisible(checkBox.isChecked())

    ___ showAll 
        ___ checkBox __ qmFileForCheckBoxMap.keys
            checkBox.sC__( st.

    ___ hideAll 
        ___ checkBox __ qmFileForCheckBoxMap.keys
            checkBox.sC__ F..

    ___ findQmFiles 
        trans_dir _ ?D..(':/translations')
        fileNames _ trans_dir.entryList(['*.qm'], ?D...Files, ?D...Name)

        r_ [trans_dir.fP..(fn) ___ fn __ fileNames]

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

    ___  -   parent_None):
        s__(MainWindow, self). - (parent)

        centralWidget _ ?W..
        sCW..(centralWidget)

        createGroupBox()

        listWidget _ QListWidget()

        ___ le __ MainWindow.listEntries:
            listWidget.aI..(tr(le))

        mainLayout _ ?VBL..
        mainLayout.aW..(groupBox)
        mainLayout.aW..(listWidget)
        centralWidget.sL..(mainLayout)

        exitAction _ ?A..(tr("E&xit"), self,
                triggered_QApplication.i.. .quit)

        fileMenu _ mB.. .aM..(tr("&File"))
        fileMenu.sP..(?P..(__.red))
        fileMenu.aA..(exitAction)

        sWT..(tr("Language: %s") % tr("English"))
        sB.. .sM..(tr("Internationalization Example"))

        __ tr("LTR") __ "RTL":
            setLayoutDirection(__.RightToLeft)

    ___ createGroupBox 
        groupBox _ ?GB..(tr("View"))
        perspectiveRadioButton _ QRadioButton(tr("Perspective"))
        isometricRadioButton _ QRadioButton(tr("Isometric"))
        obliqueRadioButton _ QRadioButton(tr("Oblique"))
        perspectiveRadioButton.sC__( st.

        groupBoxLayout _ ?VBL..
        groupBoxLayout.aW..(perspectiveRadioButton)
        groupBoxLayout.aW..(isometricRadioButton)
        groupBoxLayout.aW..(obliqueRadioButton)
        groupBox.sL..(groupBoxLayout)


__ __name__ __ "__main__":

    ______ ___

    app _ ?A..(___.a..
    chooser _ LanguageChooser()
    chooser.s..
    ___.e.. ?.e..
