#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2017 Riverbank Computing Limited.
## Copyright (C) 2017 Hans-Peter Jansen <hpj@urpla.net>
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

____ ?.?C.. ______ (QCommandLineOption, QCommandLineParser,
         ?CA.., ?D.., QT_VERSION_STR)
____ ?.?W.. ______ (?A.., QFileIconProvider, QFileSystemModel,
        QTreeView)


app _ ?A..(___.a..

 ?CA...setApplicationVersion(QT_VERSION_STR)
parser _ QCommandLineParser()
parser.setApplicationDescription("Qt Dir View Example")
parser.addHelpOption()
parser.addVersionOption()

dontUseCustomDirectoryIconsOption _ QCommandLineOption('c',
        "Set QFileIconProvider.DontUseCustomDirectoryIcons")
parser.addOption(dontUseCustomDirectoryIconsOption)
parser.addPositionalArgument('directory', "The directory to start in.")
parser.process ?)
___
    rootPath _ parser.positionalArguments().p.. 0)
_____ IE..
    rootPath _ N..

model _ QFileSystemModel()
model.setRootPath('')
__ parser.isSet(dontUseCustomDirectoryIconsOption):
    model.iconProvider().setOptions(
            QFileIconProvider.DontUseCustomDirectoryIcons)
tree _ ?TV..
tree.sM..(model)
__ rootPath __ no. N..:
    rootIndex _ model.index(?D...cleanPath(rootPath))
    __ rootIndex.isValid
        tree.setRootIndex(rootIndex)

# Demonstrating look and feel features.
tree.setAnimated F..
tree.setIndentation(20)
tree.sSE.. st.

availableSize _ ?A...desktop().availableGeometry(tree).size()
tree.r..(availableSize / 2)
tree.setColumnWidth(0, tree.width() / 3)

tree.sWT..("Dir View")
tree.s..

___.e.. ?.e..
