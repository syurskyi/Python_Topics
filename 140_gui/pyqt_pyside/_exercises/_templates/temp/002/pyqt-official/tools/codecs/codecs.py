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


____ ?.QtCore ______ QFile, QRegExp, QTextCodec, QTextStream
____ ?.?W.. ______ (QAction, ?A.., QComboBox, QDialog,
        QDialogButtonBox, QFileDialog, QGridLayout, QLabel, QMainWindow, QMenu,
        QMessageBox, QTextEdit)


___ codec_name(codec):
    try:
        # Python v3.
        name _ str(codec.name(), encoding_'ascii')
    except TypeError:
        # Python v2.
        name _ str(codec.name())

    return name


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.textEdit _ QTextEdit()
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.setCentralWidget(self.textEdit)

        self.codecs _ []
        self.findCodecs()

        self.previewForm _ PreviewForm(self)
        self.previewForm.setCodecList(self.codecs)

        self.saveAsActs _ []
        self.createActions()
        self.createMenus()

        self.setWindowTitle("Codecs")
        self.resize(500, 400)

    ___ open(self):
        fileName, _ _ QFileDialog.getOpenFileName(self)
        if fileName:
            inFile _ QFile(fileName)
            if not inFile.open(QFile.ReadOnly):
                QMessageBox.warning(self, "Codecs",
                        "Cannot read file %s:\n%s" % (fileName, inFile.errorString()))
                return

            data _ inFile.readAll()

            self.previewForm.setEncodedData(data)
            if self.previewForm.exec_
                self.textEdit.setPlainText(self.previewForm.decodedString())

    ___ save(self):
        fileName, _ _ QFileDialog.getSaveFileName(self)
        if fileName:
            outFile _ QFile(fileName)
            if not outFile.open(QFile.WriteOnly|QFile.Text):
                QMessageBox.warning(self, "Codecs",
                        "Cannot write file %s:\n%s" % (fileName, outFile.errorString()))
                return

            action _ self.sender()
            codecName _ action.data()

            out _ QTextStream(outFile)
            out.setCodec(codecName)
            out << self.textEdit.toPlainText()

    ___ about(self):
        QMessageBox.about(self, "About Codecs",
                "The <b>Codecs</b> example demonstrates how to read and "
                "write files using various encodings.")

    ___ aboutToShowSaveAsMenu(self):
        currentText _ self.textEdit.toPlainText()

        for action in self.saveAsActs:
            codecName _ action.data()
            codec _ QTextCodec.codecForName(codecName)
            action.setVisible(codec and codec.canEncode(currentText))

    ___ findCodecs(self):
        codecMap _ []
        iso8859RegExp _ QRegExp('ISO[- ]8859-([0-9]+).*')

        for mib in QTextCodec.availableMibs
            codec _ QTextCodec.codecForMib(mib)
            sortKey _ codec_name(codec).upper()
            rank _ 0

            if sortKey.startswith('UTF-8'):
                rank _ 1
            elif sortKey.startswith('UTF-16'):
                rank _ 2
            elif iso8859RegExp.exactMatch(sortKey):
                if len(iso8859RegExp.cap(1)) == 1:
                    rank _ 3
                else:
                    rank _ 4
            else:
                rank _ 5

            codecMap.append((str(rank) + sortKey, codec))

        codecMap.sort()
        self.codecs _ [item[-1] for item in codecMap]

    ___ createActions(self):
        self.openAct _ QAction("&Open...", self, shortcut_"Ctrl+O",
                triggered_self.open)

        for codec in self.codecs:
            name _ codec_name(codec)

            action _ QAction(name + '...', self, triggered_self.save)
            action.setData(name)
            self.saveAsActs.append(action)

        self.exitAct _ QAction("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        self.aboutAct _ QAction("&About", self, triggered_self.about)

        self.aboutQtAct _ QAction("About &Qt", self,
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.saveAsMenu _ QMenu("&Save As", self)
        for action in self.saveAsActs:
            self.saveAsMenu.addAction(action)

        self.saveAsMenu.aboutToShow.c..(self.aboutToShowSaveAsMenu)

        self.fileMenu _ QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addMenu(self.saveAsMenu)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.helpMenu _ QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.helpMenu)


class PreviewForm(QDialog):
    ___ __init__(self, parent):
        super(PreviewForm, self).__init__(parent)

        self.encodingComboBox _ QComboBox()
        encodingLabel _ QLabel("&Encoding:")
        encodingLabel.setBuddy(self.encodingComboBox)

        self.textEdit _ QTextEdit()
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)

        buttonBox _ QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.encodingComboBox.activated.c..(self.updateTextEdit)
        buttonBox.accepted.c..(self.accept)
        buttonBox.rejected.c..(self.reject)

        mainLayout _ QGridLayout()
        mainLayout.addWidget(encodingLabel, 0, 0)
        mainLayout.addWidget(self.encodingComboBox, 0, 1)
        mainLayout.addWidget(self.textEdit, 1, 0, 1, 2)
        mainLayout.addWidget(buttonBox, 2, 0, 1, 2)
        self.setLayout(mainLayout)

        self.setWindowTitle("Choose Encoding")
        self.resize(400, 300)

    ___ setCodecList(self, codecs):
        self.encodingComboBox.clear()
        for codec in codecs:
            self.encodingComboBox.addItem(codec_name(codec), codec.mibEnum())

    ___ setEncodedData(self, data):
        self.encodedData _ data
        self.updateTextEdit()

    ___ decodedString(self):
        return self.decodedStr

    ___ updateTextEdit(self):
        mib _ self.encodingComboBox.itemData(self.encodingComboBox.currentIndex())
        codec _ QTextCodec.codecForMib(mib)

        data _ QTextStream(self.encodedData)
        data.setAutoDetectUnicode(False)
        data.setCodec(codec)

        self.decodedStr _ data.readAll()
        self.textEdit.setPlainText(self.decodedStr)


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
