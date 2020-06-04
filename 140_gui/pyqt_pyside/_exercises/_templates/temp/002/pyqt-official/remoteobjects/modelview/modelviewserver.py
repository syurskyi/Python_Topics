#!/usr/bin/python


#############################################################################
##
## Copyright (C) 2018 Riverbank Computing Limited
## Copyright (C) 2017 Ford Motor Company
##
## This file is part of the PyQt examples.
##
## $QT_BEGIN_LICENSE:BSD$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## BSD License Usage
## Alternatively, you may use this file under the terms of the BSD license
## as follows:
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
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
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


______ ___

____ ?.?C.. ______ (pyqtSlot, QLoggingCategory, QModelIndex, ?O.., __,
        ?T.., ?U..)
____ ?.?G.. ______ ?C.., ?SI.., ?SIM..
____ ?.QtRemoteObjects ______ QRemoteObjectHost, QRemoteObjectRegistryHost
____ ?.?W.. ______ ?A.., QTreeView


c_ TimerHandler(?O..):

    ___  -   model, parent_None):
        s_. - (parent)

        _model _ model

    @pyqtSlot()
    ___ changeData 
        ___ i __ ra..(10, 50):
            _model.setData(_model.index(i, 1), ?C..(__.blue),
                    __.BackgroundRole)

    @pyqtSlot()
    ___ insertData 
        _model.insertRows(2, 9)

        ___ i __ ra..(2, 11):
            _model.setData(_model.i..(i, 1), ?C..(__.green),
                    __.BackgroundRole)
            _model.setData(_model.i..(i, 1), "InsertedRow",
                    __.DR..)

    @pyqtSlot()
    ___ removeData 
        _model.removeRows(2, 4)

    @pyqtSlot()
    ___ changeFlags 
        item _ _model.item(0, 0)
        item.sE.. F..

        item _ item.child(0, 0)
        item.setFlags(item.flags() & __.ItemIsSelectable)

    @pyqtSlot()
    ___ moveData 
        _model.moveRows(QModelIndex(), 2, 4, QModelIndex(), 10)


___ addChild(numChildren, nestingLevel):
    result _   # list

    __ nestingLevel __ 0:
        r_ result

    ___ i __ ra..(numChildren):
        child _ ?SI..(
                "Child num {}, nesting level {}".f..(i + 1, nestingLevel))

        __ i __ 0:
            child.aR..(addChild(numChildren, nestingLevel - 1))

        result.ap..(child)

    r_ result


__ ______ __ ______

    QLoggingCategory.setFilterRules('qt.remoteobjects.debug=false\n'
                                    'qt.remoteobjects.warning=false')

    app _ ?A..(___.a..

    sourceModel _ ?SIM..()
    sourceModel.sHHL..(
            ["First Column with spacing", "Second Column with spacing"])

    ___ i __ ra..(10000):
        firstItem _ ?SI..("FancyTextNumber {}".f..(i))
        __ i __ 0:
            firstItem.aR..(addChild(2, 2))

        secondItem _ ?SI..("FancyRow2TextNumber {}".f..(i))
        __ i % 2 __ 0:
            firstItem.setBackground(__.red)

        sourceModel.invisibleRootItem().aR..([firstItem, secondItem])

    # Needed by QMLModelViewClient.
    roleNames _ {
        __.DR..: b'_text',
        __.BackgroundRole: b'_color'
    }
    sourceModel.setItemRoleNames(roleNames)

    roles _ [__.DR.., __.BackgroundRole]

    node _ QRemoteObjectRegistryHost(?U..('local:registry'))

    node2 _ QRemoteObjectHost(?U..('local:replica'), ?U..('local:registry'))
    node2.enableRemoting(sourceModel, 'RemoteModel', roles)

    view _ ?TV..
    view.sWT..("SourceView")
    view.sM..(sourceModel)
    view.s..

    handler _ TimerHandler(sourceModel)
    ?T...sS..(5000, handler.changeData)
    ?T...sS..(10000, handler.insertData)
    ?T...sS..(11000, handler.changeFlags)
    ?T...sS..(12000, handler.removeData)
    ?T...sS..(13000, handler.moveData)

    ___.e.. ?.e..
