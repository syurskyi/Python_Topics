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


____ ?.?C.. ______ QFile, QRegExp, QTextCodec, QTextStream
____ ?.?W.. ______ (?A.., ?A.., ?CB, ?D..,
        ?DBB..., ?FD.., QGridLayout, ?L.., ?MW.., ?M..,
        ?MB.., ?TE..)


___ codec_name(codec):
    ___
        # Python v3.
        name _ st.(codec.name(), encoding_'ascii')
    _____ TypeError:
        # Python v2.
        name _ st.(codec.name())

    r_ name


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        textEdit _ ?TE..()
        textEdit.setLineWrapMode(?TE...NoWrap)
        sCW..(textEdit)

        codecs _   # list
        findCodecs()

        previewForm _ PreviewForm
        previewForm.setCodecList(codecs)

        saveAsActs _   # list
        createActions()
        createMenus()

        sWT..("Codecs")
        r..(500, 400)

    ___ o..
        fileName, _ _ ?FD...gOFN..
        __ fileName:
            inFile _ QFile(fileName)
            __ no. inFile.o..(QFile.ReadOnly):
                ?MB...w..  "Codecs",
                        "Cannot read file %s:\n%s" % (fileName, inFile.errorString()))
                r_

            data _ inFile.rA..

            previewForm.setEncodedData(data)
            __ previewForm.e..
                textEdit.sPT..(previewForm.decodedString())

    ___ save
        fileName, _ _ ?FD...getSaveFileName
        __ fileName:
            outFile _ QFile(fileName)
            __ no. outFile.o..(QFile.WriteOnly|QFile.Text):
                ?MB...w..  "Codecs",
                        "Cannot write file %s:\n%s" % (fileName, outFile.errorString()))
                r_

            action _ sender()
            codecName _ action.data()

            out _ QTextStream(outFile)
            out.setCodec(codecName)
            out << textEdit.toPlainText()

    ___ about
        ?MB...about  "About Codecs",
                "The <b>Codecs</b> example demonstrates how to read and "
                "write files using various encodings.")

    ___ aboutToShowSaveAsMenu
        currentText _ textEdit.toPlainText()

        ___ action __ saveAsActs:
            codecName _ action.data()
            codec _ QTextCodec.codecForName(codecName)
            action.setVisible(codec and codec.canEncode(currentText))

    ___ findCodecs
        codecMap _   # list
        iso8859RegExp _ QRegExp('ISO[- ]8859-([0-9]+).*')

        ___ mib __ QTextCodec.availableMibs
            codec _ QTextCodec.codecForMib(mib)
            sortKey _ codec_name(codec).upper()
            rank _ 0

            __ sortKey.s_w_('UTF-8'):
                rank _ 1
            ____ sortKey.s_w_('UTF-16'):
                rank _ 2
            ____ iso8859RegExp.exactMatch(sortKey):
                __ le.(iso8859RegExp.cap(1)) __ 1:
                    rank _ 3
                ____
                    rank _ 4
            ____
                rank _ 5

            codecMap.ap..((st.(rank) + sortKey, codec))

        codecMap.s..()
        codecs _ [item[-1] ___ item __ codecMap]

    ___ createActions
        openAct _ ?A..("&Open...", self, shortcut_"Ctrl+O",
                triggered_self.o..)

        ___ codec __ codecs:
            name _ codec_name(codec)

            action _ ?A..(name + '...', self, triggered_self.save)
            action.setData(name)
            saveAsActs.ap..(action)

        exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        aboutAct _ ?A..("&About", self, triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.i.. .aboutQt)

    ___ createMenus
        saveAsMenu _ ?M..("&Save As", self)
        ___ action __ saveAsActs:
            saveAsMenu.aA..(action)

        saveAsMenu.aboutToShow.c..(aboutToShowSaveAsMenu)

        fileMenu _ ?M..("&File", self)
        fileMenu.aA..(openAct)
        fileMenu.aM..(saveAsMenu)
        fileMenu.aS..)
        fileMenu.aA..(exitAct)

        helpMenu _ ?M..("&Help", self)
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

        mB.. .aM..(fileMenu)
        mB.. .aS..)
        mB.. .aM..(helpMenu)


c_ PreviewForm(?D..):
    ___  -   parent):
        s__(PreviewForm, self). - (parent)

        encodingComboBox _ ?CB()
        encodingLabel _ ?L..("&Encoding:")
        encodingLabel.setBuddy(encodingComboBox)

        textEdit _ ?TE..()
        textEdit.setLineWrapMode(?TE...NoWrap)
        textEdit.sRO..( st.

        buttonBox _ ?DBB...(?DBB....Ok | ?DBB....Cancel)

        encodingComboBox.activated.c..(updateTextEdit)
        buttonBox.a___.c..(accept)
        buttonBox.r___.c..(reject)

        mainLayout _ QGridLayout()
        mainLayout.aW..(encodingLabel, 0, 0)
        mainLayout.aW..(encodingComboBox, 0, 1)
        mainLayout.aW..(textEdit, 1, 0, 1, 2)
        mainLayout.aW..(buttonBox, 2, 0, 1, 2)
        sL..(mainLayout)

        sWT..("Choose Encoding")
        r..(400, 300)

    ___ setCodecList  codecs):
        encodingComboBox.c..
        ___ codec __ codecs:
            encodingComboBox.aI..(codec_name(codec), codec.mibEnum())

    ___ setEncodedData  data):
        encodedData _ data
        updateTextEdit()

    ___ decodedString
        r_ decodedStr

    ___ updateTextEdit
        mib _ encodingComboBox.itemData(encodingComboBox.cI..
        codec _ QTextCodec.codecForMib(mib)

        data _ QTextStream(encodedData)
        data.setAutoDetectUnicode F..
        data.setCodec(codec)

        decodedStr _ data.rA..
        textEdit.sPT..(decodedStr)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    mainWin _ MainWindow()
    mainWin.s..
    ___.e.. ?.e..
