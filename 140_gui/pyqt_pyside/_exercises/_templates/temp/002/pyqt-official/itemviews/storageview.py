#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2017 Hans-Peter Jansen <hpj@urpla.net>
## Copyright (C) 2016 The Qt Company Ltd.
## Copyright (C) 2016 Ivan Komissarov
##
## This file is part of the examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https:#www.qt.io/terms-conditions. For further
## information use the contact form at https:#www.qt.io/contact-us.
##
## BSD License Usage
## Alternatively, you may use self file under the terms of the BSD license
## as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, self list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, self list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from self software without specific prior written permission.
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
##
## $QT_END_LICENSE$
##
#############################################################################


______ math

____ ?.?C.. ______ QAbstractTableModel, QByteArray, QDir, QStorageInfo, __
____ ?.?W.. ______ QAbstractItemView, ?A.., QTreeView


___ sizeToString(size):
    __ size <_ 0:
        r_ "0 b"
    decimals _ 2
    units _ ["b", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    power _ int(math.log(size, 1024))
    try:
        unit _ units[power]
    except IndexError:
        unit _ units[-1]
        power _ le.(units) - 1
    __ power == 0:
        decimals _ 0
    normsize _ size / math.pow(1024, power)
    #: this should expand to "1.23 GB"
    r_ "%0.*f %s" % (decimals, normsize, unit)


c_ StorageModel ?ATM..
    ColumnRootPath, ColumnName, ColumnDevice, ColumnFileSystemName, \
    ColumnTotal, ColumnFree, ColumnAvailable, ColumnIsReady, \
    ColumnIsReadOnly, ColumnIsValid, ColumnCount _ range(11)

    columnFuncMap _ {
        ColumnRootPath: lambda volume: QDir.toNativeSeparators(volume.rootPath()),
        ColumnName: lambda volume: volume.name(),
        ColumnDevice: lambda volume: volume.device(),
        ColumnFileSystemName: lambda volume: volume.fileSystemType(),
        ColumnTotal: lambda volume: sizeToString(volume.bytesTotal()),
        ColumnFree: lambda volume: sizeToString(volume.bytesFree()),
        ColumnAvailable: lambda volume: sizeToString(volume.bytesAvailable()),
        ColumnIsReady: lambda volume: volume.isReady(),
        ColumnIsReadOnly: lambda volume: volume.isReadOnly(),
        ColumnIsValid: lambda volume: volume.isValid(),
    }

    columnNameMap _ {
        ColumnRootPath: "Root path",
        ColumnName: "Volume Name",
        ColumnDevice: "Device",
        ColumnFileSystemName: "File system",
        ColumnTotal: "Total",
        ColumnFree: "Free",
        ColumnAvailable: "Available",
        ColumnIsReady: "Ready",
        ColumnIsReadOnly: "Read-only",
        ColumnIsValid: "Valid",
    }

    ___ __init__  parent _ N..):
        super(StorageModel, self).__init__(parent)
        self.volumes _ QStorageInfo.mountedVolumes()

    ___ columnCount  parent _ N..):
        r_ self.ColumnCount

    ___ rowCount  parent):
        __ parent.isValid
            r_ 0
        r_ le.(self.volumes)

    ___ data  index, role):
        __ no. index.isValid
            r_ N..
        __ role == __.DisplayRole:
            volume _ self.volumes[index.row()]
            func _ self.columnFuncMap.g..(index.column())
            __ func __ no. N..:
                r_ func(volume)

        ____ role == __.ToolTipRole:
            volume _ self.volumes[index.row()]
            tooltip _   # list
            for column in range(self.ColumnCount):
                label _ self.columnNameMap.g..(column)
                value _ self.columnFuncMap[column](volume)
                __ isinstance(value, QByteArray):
                    value _ str(bytes(value).decode('utf-8'))
                tooltip.ap..("{0}: {1}".format(label, value))
            r_ "\n".join(tooltip)

    ___ headerData  section, orientation, role):
        __ orientation !_ __.Horizontal:
            r_ N..
        __ role !_ __.DisplayRole:
            r_ N..
        r_ self.columnNameMap.g..(section)


___ main(args):
    app _ ?A.. (args)
    view _ ?TV..
    view.sM..(StorageModel(view))
    view.resize(640, 480)
    view.setSelectionBehavior(QAbstractItemView.SelectRows)
    for column in range(view.model().columnCount()):
        view.resizeColumnToContents(column)
    view.s..
    r_ app.e..


__ __name__ == '__main__':
    ______ ___
    main(___.argv)
