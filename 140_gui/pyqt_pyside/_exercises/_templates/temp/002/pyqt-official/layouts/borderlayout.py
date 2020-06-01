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


____ ?.QtCore ______ QRect, QSize, Qt
____ ?.?W.. ______ (?A.., QFrame, QLabel, QLayout,
        QTextBrowser, QWidget, QWidgetItem)


class ItemWrapper(object):
    ___ __init__(self, i, p):
        self.item _ i
        self.position _ p


class BorderLayout(QLayout):
    West, North, South, East, Center _ range(5)
    MinimumSize, SizeHint _ range(2)

    ___ __init__(self, parent_None, margin_None, spacing_-1):
        super(BorderLayout, self).__init__(parent)

        if margin is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)
        self.list _ []

    ___ __del__(self):
        l _ self.takeAt(0)
        while l is not None:
            l _ self.takeAt(0)

    ___ addItem(self, item):
        self.add(item, self.West)

    ___ addWidget(self, widget, position):
        self.add(QWidgetItem(widget), position)

    ___ expandingDirections(self):
        return Qt.Horizontal | Qt.Vertical

    ___ hasHeightForWidth(self):
        return False

    ___ count(self):
        return len(self.list)

    ___ itemAt(self, index):
        if index < len(self.list):
            return self.list[index].item

        return None

    ___ minimumSize(self):
        return self.calculateSize(self.MinimumSize)

    ___ setGeometry(self, rect):
        center _ None
        eastWidth _ 0
        westWidth _ 0
        northHeight _ 0
        southHeight _ 0
        centerHeight _ 0

        super(BorderLayout, self).setGeometry(rect)

        for wrapper in self.list:
            item _ wrapper.item
            position _ wrapper.position

            if position == self.North:
                item.setGeometry(QRect(rect.x(), northHeight,
                        rect.width(), item.sizeHint().height()))    

                northHeight +_ item.geometry().height() + self.spacing()

            elif position == self.South:
                item.setGeometry(QRect(item.geometry().x(),
                        item.geometry().y(), rect.width(),
                        item.sizeHint().height()))

                southHeight +_ item.geometry().height() + self.spacing()

                item.setGeometry(QRect(rect.x(),
                        rect.y() + rect.height() - southHeight + self.spacing(),
                        item.geometry().width(), item.geometry().height()))

            elif position == self.Center:
                center _ wrapper

        centerHeight _ rect.height() - northHeight - southHeight

        for wrapper in self.list:
            item _ wrapper.item
            position _ wrapper.position

            if position == self.West:
                item.setGeometry(QRect(rect.x() + westWidth,
                        northHeight, item.sizeHint().width(), centerHeight))    

                westWidth +_ item.geometry().width() + self.spacing()

            elif position == self.East:
                item.setGeometry(QRect(item.geometry().x(),
                        item.geometry().y(), item.sizeHint().width(),
                        centerHeight))

                eastWidth +_ item.geometry().width() + self.spacing()

                item.setGeometry(QRect(rect.x() + rect.width() - eastWidth + self.spacing(),
                        northHeight, item.geometry().width(),
                        item.geometry().height()))

        if center:
            center.item.setGeometry(QRect(westWidth, northHeight,
                    rect.width() - eastWidth - westWidth, centerHeight))

    ___ sizeHint(self):
        return self.calculateSize(self.SizeHint)

    ___ takeAt(self, index):
        if index >_ 0 and index < len(self.list):
            layoutStruct _ self.list.pop(index)
            return layoutStruct.item

        return None

    ___ add(self, item, position):
        self.list.append(ItemWrapper(item, position))

    ___ calculateSize(self, sizeType):
        totalSize _ QSize()

        for wrapper in self.list:
            position _ wrapper.position
            itemSize _ QSize()

            if sizeType == self.MinimumSize:
                itemSize _ wrapper.item.minimumSize()
            else: # sizeType == self.SizeHint
                itemSize _ wrapper.item.sizeHint()

            if position in (self.North, self.South, self.Center):
                totalSize.setHeight(totalSize.height() + itemSize.height())

            if position in (self.West, self.East, self.Center):
                totalSize.setWidth(totalSize.width() + itemSize.width())

        return totalSize


class Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        centralWidget _ QTextBrowser()
        centralWidget.setPlainText("Central widget")

        layout _ BorderLayout()
        layout.addWidget(centralWidget, BorderLayout.Center)

        # Because BorderLayout doesn't call its super-class addWidget() it
        # doesn't take ownership of the widgets until setLayout() is called.
        # Therefore we keep a local reference to each label to prevent it being
        # garbage collected too soon.
        label_n _ self.createLabel("North")
        layout.addWidget(label_n, BorderLayout.North)

        label_w _ self.createLabel("West")
        layout.addWidget(label_w, BorderLayout.West)

        label_e1 _ self.createLabel("East 1")
        layout.addWidget(label_e1, BorderLayout.East)

        label_e2 _ self.createLabel("East 2")
        layout.addWidget(label_e2, BorderLayout.East)

        label_s _ self.createLabel("South")
        layout.addWidget(label_s, BorderLayout.South)

        self.setLayout(layout)

        self.setWindowTitle("Border Layout")

    ___ createLabel(self, text):
        label _ QLabel(text)
        label.setFrameStyle(QFrame.Box | QFrame.Raised)

        return label


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ Window()
    window.s..
    sys.exit(app.exec_())    
