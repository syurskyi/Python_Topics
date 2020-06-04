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


____ ?.?C.. ______ QFile, QFileInfo, QRectF, QTextStream

____ colors ______ Colors
____ demoitem ______ DemoItem
____ demoitemanimation ______ DemoItemAnimation
____ demotextitem ______ DemoTextItem
____ headingitem ______ HeadingItem


c_ MenuContentItem(DemoItem):
    ___  -   el, parent_None):
        s__(MenuContentItem, self). - (parent)

        name _ el.getAttribute('name')
        heading _ N..
        description1 _ N..
        description2 _ N..

        readme_dir _ QFileInfo(__file__).dir()
        readme_dir.cdUp()
        readme_dir.cd(el.getAttribute('dirname'))

        readmePath _ readme_dir.absoluteFilePath('README')

        _prepared _ F..

    ___ prepare 
        __ no. _prepared:
            createContent()
            _prepared_ T..

    ___ animationStopped  id):
        __ name __ Colors.rootMenuName:
            # Optimization hack.
            r_

        __ id __ DemoItemAnimation.ANIM_OUT:
            # Free up some memory
            heading _ N..
            description1 _ N..
            description2 _ N..
            _prepared _ F..

    ___ loadDescription  startPara, nrPara):
        readme _ QFile(readmePath)
        __ no. readme.o..(QFile.ReadOnly):
            Colors.debug("- MenuContentItem.loadDescription: Could not load:", readmePath)
            r_ ""

        in_str _ QTextStream(readme)
        # Skip a certain number of paragraphs.
        w__ startPara:
            __ no. in_str.readLine
                startPara -_ 1

        # Read in the number of wanted paragraphs.
        result _ ''
        line _ in_str.readLine()
        w__ T..
            result +_ line + " "
            line _ in_str.readLine()
            __ no. line:
                nrPara -_ 1
                line _ "<br><br>" + in_str.readLine()

            __ nrPara __ 0 or in_str.atEnd
                break

        r_ Colors.contentColor + result

    ___ createContent 
        # Create the items.
        heading _ HeadingItem(name, self)
        para1 _ loadDescription(0, 1)
        __ no. para1:
            para1 _ Colors.contentColor + "Could not load description. Ensure that the documentation for Qt is built."
        bgcolor _ Colors.sceneBg1.darker(200)
        bgcolor.setAlpha(100)
        description1 _ DemoTextItem(para1, Colors.contentFont(),
                Colors.heading, 500, self, DemoTextItem.STATIC_TEXT)
        description2 _ DemoTextItem(loadDescription(1, 2),
                Colors.contentFont(), Colors.heading, 250, self,
                DemoTextItem.STATIC_TEXT)

        # Place the items on screen.
        heading.setPos(0, 3)
        description1.setPos(0, heading.pos().y() + heading.boundingRect().height() + 10)
        description2.setPos(0, description1.pos().y() + description1.boundingRect().height() + 15)

    ___ boundingRect 
        r_ QRectF(0, 0, 500, 350)
