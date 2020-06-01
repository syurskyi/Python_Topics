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


____ ?.QtCore ______ QDate, Qt
____ ?.?W.. ______ QCompleter, QDateTimeEdit, QItemDelegate, QLineEdit


c_ SpreadSheetDelegate(QItemDelegate):

    ___ __init__  parent _ N..):
        super(SpreadSheetDelegate, self).__init__(parent)

    ___ createEditor  parent, styleOption, index):
        __ index.column() == 1:
            editor _ QDateTimeEdit(parent)
            editor.setDisplayFormat(self.parent().currentDateFormat)
            editor.setCalendarPopup(True)
            r_ editor

        editor _ QLineEdit(parent)
        # create a completer with the strings in the column as model
        allStrings _ []
        for i in range(1, index.model().rowCount()):
            strItem _ index.model().data(index.sibling(i, index.column()), Qt.EditRole)
            __ strItem no. in allStrings:
                allStrings.append(strItem)

        autoComplete _ QCompleter(allStrings)
        editor.setCompleter(autoComplete)
        editor.editingFinished.c..(self.commitAndCloseEditor)
        r_ editor

    ___ commitAndCloseEditor(self):
        editor _ self.sender()
        self.commitData.emit(editor)
        self.closeEditor.emit(editor, QItemDelegate.NoHint)

    ___ setEditorData  editor, index):
        __ isinstance(editor, QLineEdit):
            editor.sT..(index.model().data(index, Qt.EditRole))
        ____ isinstance(editor, QDateTimeEdit):
            editor.setDate(QDate.fromString(
                index.model().data(index, Qt.EditRole), self.parent().currentDateFormat))

    ___ setModelData  editor, model, index):
        __ isinstance(editor, QLineEdit):
            model.setData(index, editor.text())
        ____ isinstance(editor, QDateTimeEdit):
            model.setData(index, editor.date().toString(self.parent().currentDateFormat))
