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


____ ?.?C.. ______ QRect, QSize, __
____ ?.?W.. ______ (?A.., QFrame, QLabel, QLayout,
        QTextBrowser, QWidget, QWidgetItem)


c_ ItemWrapper(object):
    ___ __init__  i, p):
        self.item _ i
        self.position _ p


c_ BorderLayout(QLayout):
    West, North, South, East, Center _ range(5)
    MinimumSize, SizeHint _ range(2)

    ___ __init__  parent_None, margin_None, spacing_-1):
        super(BorderLayout, self).__init__(parent)

        __ margin __ no. N..:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)
        self.list _   # list

    ___ __del__(self):
        l _ self.takeAt(0)
        w__ l __ no. N..:
            l _ self.takeAt(0)

    ___ addItem  item):
        self.add(item, self.West)

    ___ aW..  widget, position):
        self.add(QWidgetItem(widget), position)

    ___ expandingDirections(self):
        r_ __.Horizontal | __.Vertical

    ___ hasHeightForWidth(self):
        r_ False

    ___ count(self):
        r_ le.(self.list)

    ___ itemAt  index):
        __ index < le.(self.list):
            r_ self.list[index].item

        r_ N..

    ___ minimumSize(self):
        r_ self.calculateSize(self.MinimumSize)

    ___ setGeometry  rect):
        center _ N..
        eastWidth _ 0
        westWidth _ 0
        northHeight _ 0
        southHeight _ 0
        centerHeight _ 0

        super(BorderLayout, self).setGeometry(rect)

        for wrapper in self.list:
            item _ wrapper.item
            position _ wrapper.position

            __ position == self.North:
                item.setGeometry(QRect(rect.x(), northHeight,
                        rect.width(), item.sizeHint().height()))    

                northHeight +_ item.geometry().height() + self.spacing()

            ____ position == self.South:
                item.setGeometry(QRect(item.geometry().x(),
                        item.geometry().y(), rect.width(),
                        item.sizeHint().height()))

                southHeight +_ item.geometry().height() + self.spacing()

                item.setGeometry(QRect(rect.x(),
                        rect.y() + rect.height() - southHeight + self.spacing(),
                        item.geometry().width(), item.geometry().height()))

            ____ position == self.Center:
                center _ wrapper

        centerHeight _ rect.height() - northHeight - southHeight

        for wrapper in self.list:
            item _ wrapper.item
            position _ wrapper.position

            __ position == self.West:
                item.setGeometry(QRect(rect.x() + westWidth,
                        northHeight, item.sizeHint().width(), centerHeight))    

                westWidth +_ item.geometry().width() + self.spacing()

            ____ position == self.East:
                item.setGeometry(QRect(item.geometry().x(),
                        item.geometry().y(), item.sizeHint().width(),
                        centerHeight))

                eastWidth +_ item.geometry().width() + self.spacing()

                item.setGeometry(QRect(rect.x() + rect.width() - eastWidth + self.spacing(),
                        northHeight, item.geometry().width(),
                        item.geometry().height()))

        __ center:
            center.item.setGeometry(QRect(westWidth, northHeight,
                    rect.width() - eastWidth - westWidth, centerHeight))

    ___ sizeHint(self):
        r_ self.calculateSize(self.SizeHint)

    ___ takeAt  index):
        __ index >_ 0 and index < le.(self.list):
            layoutStruct _ self.list.p.. index)
            r_ layoutStruct.item

        r_ N..

    ___ add  item, position):
        self.list.ap..(ItemWrapper(item, position))

    ___ calculateSize  sizeType):
        totalSize _ QSize()

        for wrapper in self.list:
            position _ wrapper.position
            itemSize _ QSize()

            __ sizeType == self.MinimumSize:
                itemSize _ wrapper.item.minimumSize()
            ____ # sizeType == self.SizeHint
                itemSize _ wrapper.item.sizeHint()

            __ position in (self.North, self.South, self.Center):
                totalSize.setHeight(totalSize.height() + itemSize.height())

            __ position in (self.West, self.East, self.Center):
                totalSize.setWidth(totalSize.width() + itemSize.width())

        r_ totalSize


c_ Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        centralWidget _ QTextBrowser()
        centralWidget.sPT..("Central widget")

        layout _ BorderLayout()
        layout.aW..(centralWidget, BorderLayout.Center)

        # Because BorderLayout doesn't call its super-class addWidget() it
        # doesn't take ownership of the widgets until setLayout() is called.
        # Therefore we keep a local reference to each label to prevent it being
        # garbage collected too soon.
        label_n _ self.createLabel("North")
        layout.aW..(label_n, BorderLayout.North)

        label_w _ self.createLabel("West")
        layout.aW..(label_w, BorderLayout.West)

        label_e1 _ self.createLabel("East 1")
        layout.aW..(label_e1, BorderLayout.East)

        label_e2 _ self.createLabel("East 2")
        layout.aW..(label_e2, BorderLayout.East)

        label_s _ self.createLabel("South")
        layout.aW..(label_s, BorderLayout.South)

        self.sL..(layout)

        self.setWindowTitle("Border Layout")

    ___ createLabel  t__):
        label _ QLabel(t__)
        label.setFrameStyle(QFrame.Box | QFrame.Raised)

        r_ label


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ Window()
    window.s..
    sys.exit(app.exec_())    
