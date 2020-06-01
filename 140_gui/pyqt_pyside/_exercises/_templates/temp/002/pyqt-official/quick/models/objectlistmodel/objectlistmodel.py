#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2018 Riverbank Computing Limited.
## Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
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
##   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
##     of its contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
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


____ ?.?C.. ______ pyqtProperty, pyqtSignal, QObject, QUrl
____ ?.?G.. ______ QGuiApplication
____ ?.QtQuick ______ QQuickView

______ objectlistmodel_rc


c_ DataObject(QObject):

    nameChanged _ pyqtSignal()

    @pyqtProperty(str, notify_nameChanged)
    ___ name(self):
        r_ self._name

    @name.setter
    ___ name  name):
        __ self._name !_ name:
            self._name _ name
            self.nameChanged.emit()

    colorChanged _ pyqtSignal()

    @pyqtProperty(str, notify_colorChanged)
    ___ color(self):
        r_ self._color

    @color.setter
    ___ color  color):
        __ self._color !_ color:
            self._color _ color
            self.colorChanged.emit()

    ___ __init__  name_'', color_'', parent_None):
        super(DataObject, self).__init__(parent)

        self._name _ name
        self._color _ color


__ __name__ == '__main__':
    ______ os
    ______ sys

    # This is necessary to avoid a possible crash when running from another
    # directory by ensuring the compiled version of the embedded QML file
    # doesn't get mixed up with another of the same name.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    app _ QGuiApplication(sys.argv)

    dataList _ [DataObject("Item 1", 'red'),
                DataObject("Item 2", 'green'),
                DataObject("Item 3", 'blue'),
                DataObject("Item 4", 'yellow')]

    view _ QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    ctxt _ view.rootContext()
    ctxt.setContextProperty('myModel', dataList)

    view.setSource(QUrl('qrc:view.qml'))
    view.s..

    sys.exit(app.exec_())
