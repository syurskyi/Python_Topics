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


____ ?.?C.. ______ QRect, ?S.., __
____ ?.?W.. ______ (?A.., QFrame, ?L.., QLayout,
        QTextBrowser, ?W.., QWidgetItem)


c_ ItemWrapper o..
    ___  -   i, p):
        item _ i
        position _ p


c_ BorderLayout(QLayout):
    West, North, South, East, Center _ ra..(5)
    MinimumSize, SizeHint _ ra..(2)

    ___  -   parent_None, margin_None, spacing_-1):
        s__(BorderLayout, self). - (parent)

        __ margin __ no. N..:
            sCM..(margin, margin, margin, margin)

        setSpacing(spacing)
        li.. _   # list

    ___ __del__
        l _ takeAt(0)
        w__ l __ no. N..:
            l _ takeAt(0)

    ___ aI..  item):
        add(item, West)

    ___ aW..  widget, position):
        add(QWidgetItem(widget), position)

    ___ expandingDirections
        r_ __.H.. | __.Vertical

    ___ hasHeightForWidth
        r_ F..

    ___ count
        r_ le.(li..)

    ___ itemAt  index):
        __ index < le.(li..):
            r_ li..[index].item

        r_ N..

    ___ minimumSize
        r_ calculateSize(MinimumSize)

    ___ setGeometry  rect):
        center _ N..
        eastWidth _ 0
        westWidth _ 0
        northHeight _ 0
        southHeight _ 0
        centerHeight _ 0

        s__(BorderLayout, self).setGeometry(rect)

        ___ wrapper __ li..:
            item _ wrapper.item
            position _ wrapper.position

            __ position __ North:
                item.setGeometry(QRect(rect.x(), northHeight,
                        rect.width(), item.sH..().height()))

                northHeight +_ item.geometry().height() + spacing()

            ____ position __ South:
                item.setGeometry(QRect(item.geometry().x(),
                        item.geometry().y(), rect.width(),
                        item.sH..().height()))

                southHeight +_ item.geometry().height() + spacing()

                item.setGeometry(QRect(rect.x(),
                        rect.y() + rect.height() - southHeight + spacing(),
                        item.geometry().width(), item.geometry().height()))

            ____ position __ Center:
                center _ wrapper

        centerHeight _ rect.height() - northHeight - southHeight

        ___ wrapper __ li..:
            item _ wrapper.item
            position _ wrapper.position

            __ position __ West:
                item.setGeometry(QRect(rect.x() + westWidth,
                        northHeight, item.sH..().width(), centerHeight))

                westWidth +_ item.geometry().width() + spacing()

            ____ position __ East:
                item.setGeometry(QRect(item.geometry().x(),
                        item.geometry().y(), item.sH..().width(),
                        centerHeight))

                eastWidth +_ item.geometry().width() + spacing()

                item.setGeometry(QRect(rect.x() + rect.width() - eastWidth + spacing(),
                        northHeight, item.geometry().width(),
                        item.geometry().height()))

        __ center:
            center.item.setGeometry(QRect(westWidth, northHeight,
                    rect.width() - eastWidth - westWidth, centerHeight))

    ___ sH..
        r_ calculateSize(SizeHint)

    ___ takeAt  index):
        __ index >_ 0 and index < le.(li..):
            layoutStruct _ li...p.. index)
            r_ layoutStruct.item

        r_ N..

    ___ add  item, position):
        li...ap..(ItemWrapper(item, position))

    ___ calculateSize  sizeType):
        totalSize _ ?S..()

        ___ wrapper __ li..:
            position _ wrapper.position
            itemSize _ ?S..()

            __ sizeType __ MinimumSize:
                itemSize _ wrapper.item.minimumSize()
            ____ # sizeType == self.SizeHint
                itemSize _ wrapper.item.sH..()

            __ position __ (North, South, Center):
                totalSize.setHeight(totalSize.height() + itemSize.height())

            __ position __ (West, East, Center):
                totalSize.sW..(totalSize.width() + itemSize.width())

        r_ totalSize


c_ Window(?W..):
    ___  -
        s__(Window, self). - ()

        centralWidget _ QTextBrowser()
        centralWidget.sPT..("Central widget")

        layout _ BorderLayout()
        layout.aW..(centralWidget, BorderLayout.Center)

        # Because BorderLayout doesn't call its super-class addWidget() it
        # doesn't take ownership of the widgets until setLayout() is called.
        # Therefore we keep a local reference to each label to prevent it being
        # garbage collected too soon.
        label_n _ createLabel("North")
        layout.aW..(label_n, BorderLayout.North)

        label_w _ createLabel("West")
        layout.aW..(label_w, BorderLayout.West)

        label_e1 _ createLabel("East 1")
        layout.aW..(label_e1, BorderLayout.East)

        label_e2 _ createLabel("East 2")
        layout.aW..(label_e2, BorderLayout.East)

        label_s _ createLabel("South")
        layout.aW..(label_s, BorderLayout.South)

        sL..(layout)

        sWT..("Border Layout")

    ___ createLabel  t__):
        label _ ?L..(t__)
        label.setFrameStyle(QFrame.Box | QFrame.Raised)

        r_ label


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ Window()
    window.s..
    ___.e.. ?.e..
