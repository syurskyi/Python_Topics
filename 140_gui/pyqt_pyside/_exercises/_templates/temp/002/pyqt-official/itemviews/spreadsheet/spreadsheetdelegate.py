#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2012 Hans-Peter Jansen <hpj@urpla.net>.
## Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
## Contact: Nokia Corporation (qt-info@nokia.com)
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## GNU Lesser General Public License Usage
## This file may be used under the terms of the GNU Lesser General Public
## License version 2.1 as published by the Free Software Foundation and
## appearing in the file LICENSE.LGPL included in the packaging of this
## file. Please review the following information to ensure the GNU Lesser
## General Public License version 2.1 requirements will be met:
## http:#www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights. These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU General
## Public License version 3.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of this
## file. Please review the following information to ensure the GNU General
## Public License version 3.0 requirements will be met:
## http:#www.gnu.org/copyleft/gpl.html.
##
## Other Usage
## Alternatively, this file may be used in accordance with the terms and
## conditions contained in a signed written agreement between you and Nokia.
## $QT_END_LICENSE$
##
#############################################################################


____ ?.?C.. ______ ?D.., __
____ ?.?W.. ______ QCompleter, ?DTE.., QItemDelegate, QLineEdit


c_ SpreadSheetDelegate(QItemDelegate):

    ___  -   parent _ N..):
        s__(SpreadSheetDelegate, self). - (parent)

    ___ createEditor  parent, styleOption, index):
        __ index.column() __ 1:
            editor _ ?DTE..(parent)
            editor.setDisplayFormat(parent().currentDateFormat)
            editor.setCalendarPopup( st.
            r_ editor

        editor _ QLineEdit(parent)
        # create a completer with the strings in the column as model
        allStrings _   # list
        ___ i __ ra..(1, index.model().rowCount()):
            strItem _ index.model().data(index.sibling(i, index.column()), __.ER..)
            __ strItem no. __ allStrings:
                allStrings.ap..(strItem)

        autoComplete _ QCompleter(allStrings)
        editor.setCompleter(autoComplete)
        editor.eF__.c..(commitAndCloseEditor)
        r_ editor

    ___ commitAndCloseEditor
        editor _ sender()
        commitData.e..(editor)
        closeEditor.e..(editor, QItemDelegate.NoHint)

    ___ setEditorData  editor, index):
        __ isinstance(editor, QLineEdit):
            editor.sT..(index.model().data(index, __.ER..))
        ____ isinstance(editor, ?DTE..):
            editor.setDate(?D...fromString(
                index.model().data(index, __.ER..), parent().currentDateFormat))

    ___ setModelData  editor, model, index):
        __ isinstance(editor, QLineEdit):
            model.setData(index, editor.t__())
        ____ isinstance(editor, ?DTE..):
            model.setData(index, editor.date().toString(parent().currentDateFormat))
