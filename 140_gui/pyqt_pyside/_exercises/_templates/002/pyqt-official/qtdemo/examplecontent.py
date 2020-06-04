#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################


____ xml.dom.minidom ______ parseString

____ ?.?C.. ______ QRectF, QRegExp, __
____ ?.?G.. ______ QImage

____ colors ______ Colors
____ demoitem ______ DemoItem
____ demoitemanimation ______ DemoItemAnimation
____ demotextitem ______ DemoTextItem
____ headingitem ______ HeadingItem
____ imageitem ______ ImageItem


c_ ExampleContent(DemoItem):
    ___  -   name, parent_None):
        s__(ExampleContent, self). - (parent)

        # Prevent a circular import.
        ____ menumanager ______ MenuManager
        _menu_manager _ MenuManager.i.. 

        name _ name
        heading _ N..
        description _ N..
        screenshot _ N..

        _prepared _ F..

    ___ prepare 
        __ no. _prepared:
            createContent()
            _prepared _ T..

    ___ animationStopped  id):
        __ id __ DemoItemAnimation.ANIM_OUT:
            # Free up some memory.
            heading _ N..
            description _ N..
            screenshot _ N..
            _prepared _ F..

    ___ loadDescription 
        contents _ _menu_manager.getHtml(name).data().d..('utf8')
        __ contents __ '':
            paragraphs _   # list
        ____
            exampleDoc _ parseString(contents)
            paragraphs _ exampleDoc.getElementsByTagName('p')

        __ le.(paragraphs) < 1:
            Colors.debug("- ExampleContent.loadDescription(): Could not load description:", _menu_manager.info[name].g..('docfile'))

        description _ Colors.contentColor + "Could not load description. Ensure that the documentation for Qt is built."
        ___ p __ paragraphs:
            description _ extractTextFromParagraph(p)
            __ isSummary(description):
                break

        r_ Colors.contentColor + description

    ___ isSummary  t__):
        __ _ QRegExp("(In )?((The|This) )?(%s )?.*(tutorial|example|demo|application)" % name, __.CaseInsensitive)

        r_ ('[' no. __ t__) and (__.indexIn(t__) >_ 0)

    ___ extractTextFromParagraph  parentNode):
        description _ ''
        node _ parentNode.firstChild

        w__ node __ no. N..:
            __ node.nodeType __ node.TEXT_NODE:
                description +_ Colors.contentColor + node.nodeValue
            ____ node.hasChildNodes
                __ node.nodeName __ 'b':
                    beginTag _ '<b>'
                    endTag _ '</b>'
                ____ node.nodeName __ 'a':
                    beginTag _ Colors.contentColor
                    endTag _ '</font>'
                ____ node.nodeName __ 'i':
                    beginTag _ '<i>'
                    endTag _ '</i>'
                ____ node.nodeName __ 'tt':
                    beginTag _ '<tt>'
                    endTag _ '</tt>'
                ____
                    beginTag _ endTag _ ''

                description +_ beginTag + extractTextFromParagraph(node) + endTag

            node _ node.nextSibling

        r_ description

    ___ createContent 
        # Create the items.
        heading _ HeadingItem(name, self)
        description _ DemoTextItem(loadDescription(),
                Colors.contentFont(), Colors.heading, 500, self)
        imgHeight _ 340 - in.(description.boundingRect().height()) + 50
        screenshot _ ImageItem(QImage.fromData(_menu_manager.getImage(name)), 550, imgHeight, self)

        # Place the items on screen.
        heading.setPos(0, 3)
        description.setPos(0, heading.pos().y() + heading.boundingRect().height() + 10)
        screenshot.setPos(0, description.pos().y() + description.boundingRect().height() + 10)

    ___ boundingRect 
        r_ QRectF(0, 0, 500, 100)
