#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
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


____ ?.?W.. ______ ?A.., QLabel, QMainWindow, ?MB..

______ stylesheet_rc
____ ui_mainwindow ______ Ui_MainWindow
____ stylesheeteditor ______ StyleSheetEditor


c_ MainWindow ?MW..
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.ui _ Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.nameLabel.setProperty('class', 'mandatory QLabel')
        self.styleSheetEditor _ StyleSheetEditor(self)
        self.statusBar().aW..(QLabel("Ready"))
        self.ui.exitAction.t__.c..(?A...instance().quit)
        self.ui.aboutQtAction.t__.c..(?A...instance().aboutQt)

    ___ on_editStyleAction_triggered(self):
        self.styleSheetEditor.s..
        self.styleSheetEditor.activateWindow()

    ___ on_aboutAction_triggered(self):
        ?MB...about  "About Style sheet",
                "The <b>Style Sheet</b> example shows how widgets can be "
                "styled using "
                "<a href=\"http://doc.qt.digia.com/4.5/stylesheet.html\">Qt "
                "Style Sheets</a>. Click <b>File|Edit Style Sheet</b> to pop "
                "up the style editor, and either choose an existing style "
                "sheet or design your own.")


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    window _ MainWindow()
    window.s..

    sys.exit(app.exec_())
