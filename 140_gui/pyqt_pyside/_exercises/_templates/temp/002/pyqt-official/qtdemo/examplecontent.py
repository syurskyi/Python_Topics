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

____ ?.QtCore ______ QRectF, QRegExp, Qt
____ ?.QtGui ______ QImage

____ colors ______ Colors
____ demoitem ______ DemoItem
____ demoitemanimation ______ DemoItemAnimation
____ demotextitem ______ DemoTextItem
____ headingitem ______ HeadingItem
____ imageitem ______ ImageItem


class ExampleContent(DemoItem):
    ___ __init__(self, name, parent_None):
        super(ExampleContent, self).__init__(parent)

        # Prevent a circular import.
        ____ menumanager ______ MenuManager
        self._menu_manager _ MenuManager.instance()

        self.name _ name
        self.heading _ None
        self.description _ None
        self.screenshot _ None

        self._prepared _ False

    ___ prepare(self):
        if not self._prepared:
            self.createContent()
            self._prepared _ True

    ___ animationStopped(self, id):
        if id == DemoItemAnimation.ANIM_OUT:
            # Free up some memory.
            self.heading _ None
            self.description _ None
            self.screenshot _ None
            self._prepared _ False

    ___ loadDescription(self):
        contents _ self._menu_manager.getHtml(self.name).data().decode('utf8')
        if contents == '':
            paragraphs _ []
        else:
            exampleDoc _ parseString(contents)
            paragraphs _ exampleDoc.getElementsByTagName('p')

        if len(paragraphs) < 1:
            Colors.debug("- ExampleContent.loadDescription(): Could not load description:", self._menu_manager.info[self.name].get('docfile'))

        description _ Colors.contentColor + "Could not load description. Ensure that the documentation for Qt is built."
        for p in paragraphs:
            description _ self.extractTextFromParagraph(p)
            if self.isSummary(description):
                break

        return Colors.contentColor + description

    ___ isSummary(self, text):
        re _ QRegExp("(In )?((The|This) )?(%s )?.*(tutorial|example|demo|application)" % self.name, Qt.CaseInsensitive)

        return ('[' not in text) and (re.indexIn(text) >_ 0)

    ___ extractTextFromParagraph(self, parentNode):
        description _ ''
        node _ parentNode.firstChild

        while node is not None:
            if node.nodeType == node.TEXT_NODE:
                description +_ Colors.contentColor + node.nodeValue
            elif node.hasChildNodes
                if node.nodeName == 'b':
                    beginTag _ '<b>'
                    endTag _ '</b>'
                elif node.nodeName == 'a':
                    beginTag _ Colors.contentColor
                    endTag _ '</font>'
                elif node.nodeName == 'i':
                    beginTag _ '<i>'
                    endTag _ '</i>'
                elif node.nodeName == 'tt':
                    beginTag _ '<tt>'
                    endTag _ '</tt>'
                else:
                    beginTag _ endTag _ ''

                description +_ beginTag + self.extractTextFromParagraph(node) + endTag

            node _ node.nextSibling

        return description

    ___ createContent(self):
        # Create the items.
        self.heading _ HeadingItem(self.name, self)
        self.description _ DemoTextItem(self.loadDescription(),
                Colors.contentFont(), Colors.heading, 500, self)
        imgHeight _ 340 - int(self.description.boundingRect().height()) + 50
        self.screenshot _ ImageItem(QImage.fromData(self._menu_manager.getImage(self.name)), 550, imgHeight, self)

        # Place the items on screen.
        self.heading.setPos(0, 3)
        self.description.setPos(0, self.heading.pos().y() + self.heading.boundingRect().height() + 10)
        self.screenshot.setPos(0, self.description.pos().y() + self.description.boundingRect().height() + 10)

    ___ boundingRect(self):
        return QRectF(0, 0, 500, 100)
