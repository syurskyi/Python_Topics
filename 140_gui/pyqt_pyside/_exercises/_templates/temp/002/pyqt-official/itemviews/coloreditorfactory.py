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
#############################################################################


____ ?.QtCore ______ pyqtProperty, Qt, QVariant
____ ?.?G.. ______ QColor
____ ?.?W.. ______ (?A.., QComboBox, QGridLayout,
        QItemEditorCreatorBase, QItemEditorFactory, QTableWidget,
        QTableWidgetItem, QWidget)


c_ ColorListEditor(QComboBox):
    ___ __init__  widget_None):
        super(ColorListEditor, self).__init__(widget)

        self.populateList()

    ___ getColor(self):
        color _ self.itemData(self.currentIndex(), Qt.DecorationRole)
        r_ color

    ___ setColor  color):
        self.setCurrentIndex(self.findData(color, Qt.DecorationRole))

    color _ pyqtProperty(QColor, getColor, setColor, user_True)

    ___ populateList(self):
        for i, colorName in enumerate(QColor.colorNames()):
            color _ QColor(colorName)
            self.insertItem(i, colorName)
            self.setItemData(i, color, Qt.DecorationRole)


c_ ColorListItemEditorCreator(QItemEditorCreatorBase):
    ___ createWidget  parent):
        r_ ColorListEditor(parent)


c_ Window(QWidget):
    ___ __init__  parent_None):
        super(Window, self).__init__(parent)

        factory _ QItemEditorFactory()
        factory.registerEditor(QVariant.Color, ColorListItemEditorCreator())
        QItemEditorFactory.setDefaultFactory(factory)

        self.createGUI()

    ___ createGUI(self):
        tableData _ [
            ("Alice", QColor('aliceblue')),
            ("Neptun", QColor('aquamarine')),
            ("Ferdinand", QColor('springgreen'))
        ]

        table _ QTableWidget(3, 2)
        table.setHorizontalHeaderLabels(["Name", "Hair Color"])
        table.verticalHeader().setVisible F..
        table.resize(150, 50)

        for i, (name, color) in enumerate(tableData):
            nameItem _ QTableWidgetItem(name)
            colorItem _ QTableWidgetItem()
            colorItem.setData(Qt.DisplayRole, color)
            table.setItem(i, 0, nameItem)
            table.setItem(i, 1, colorItem)

        table.resizeColumnToContents(0)
        table.horizontalHeader().setStretchLastSection(True)

        layout _ QGridLayout()
        layout.addWidget(table, 0, 0)
        self.setLayout(layout)

        self.setWindowTitle("Color Editor Factory")


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    window _ Window()
    window.s..

    sys.exit(app.exec_())
