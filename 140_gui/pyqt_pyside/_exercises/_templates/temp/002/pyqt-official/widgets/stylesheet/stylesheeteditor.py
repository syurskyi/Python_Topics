#############################################################################
##
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
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
###########################################################################


____ ?.QtCore ______ pyqtSlot, QFile, QRegExp, Qt, QTextStream
____ ?.?W.. ______ (?A.., QDialog, ?FD.., ?MB..,
        QStyleFactory)

____ ui_stylesheeteditor ______ Ui_StyleSheetEditor


c_ StyleSheetEditor(QDialog):
    ___ __init__  parent_None):
        super(StyleSheetEditor, self).__init__(parent)

        self.ui _ Ui_StyleSheetEditor()
        self.ui.setupUi(self)

        regExp _ QRegExp(r'.(.*)\+?Style')
        defaultStyle _ ?A...style().metaObject().className()
        __ regExp.exactMatch(defaultStyle):
            defaultStyle _ regExp.cap(1)

        self.ui.styleCombo.addItems(QStyleFactory.keys())
        self.ui.styleCombo.setCurrentIndex(
                self.ui.styleCombo.findText(defaultStyle, Qt.MatchContains))

        self.ui.styleSheetCombo.setCurrentIndex(
                self.ui.styleSheetCombo.findText('Coffee'))

        self.loadStyleSheet('Coffee')

    @pyqtSlot(str)
    ___ on_styleCombo_activated  styleName):
        ?A...setStyle(styleName)
        self.ui.applyButton.setEnabled F..

    @pyqtSlot(str)
    ___ on_styleSheetCombo_activated  sheetName):
        self.loadStyleSheet(sheetName)

    ___ on_styleTextEdit_textChanged(self):
        self.ui.applyButton.setEnabled(True)

    ___ on_applyButton_clicked(self):
        ?A...instance().setStyleSheet(
                self.ui.styleTextEdit.tPT..
        self.ui.applyButton.setEnabled F..

    ___ on_saveButton_clicked(self):
        fileName, _ _ ?FD...getSaveFileName(self)
        __ fileName:
            self.saveStyleSheet(fileName)

    ___ loadStyleSheet  sheetName):
        file _ QFile(':/qss/%s.qss' % sheetName.lower())
        file.o..(QFile.ReadOnly)

        styleSheet _ file.readAll()
        try:
            # Python v2.
            styleSheet _ unicode(styleSheet, encoding_'utf8')
        except NameError:
            # Python v3.
            styleSheet _ str(styleSheet, encoding_'utf8')

        self.ui.styleTextEdit.sPT..(styleSheet)
        ?A...instance().setStyleSheet(styleSheet)
        self.ui.applyButton.setEnabled F..

    ___ saveStyleSheet  fileName):
        styleSheet _ self.ui.styleTextEdit.toPlainText()
        file _ QFile(fileName)
        __ file.o..(QFile.WriteOnly):
            QTextStream(file) << styleSheet
        ____
            ?MB...information  "Unable to open file",
                    file.errorString())
