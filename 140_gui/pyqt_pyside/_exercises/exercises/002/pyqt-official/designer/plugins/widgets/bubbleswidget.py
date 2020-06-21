#!/usr/bin/env python

"""
bubbleswidget.py

A PyQt custom widget example for Qt Designer.

Copyright (C) 2006 David Boddie <david@boddie.org.uk>
Copyright (C) 2005-2006 Trolltech ASA. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

______ random

____ ?.?C.. ______ (pP.., pS.., pyqtSlot, QPointF, QRectF,
        ?S.., QSizeF, __, ?T..)
____ ?.?G.. ______ ?B.., ?C.., QPainter, ?P.., QRadialGradient
____ ?.?W.. ______ ?A.., ?W..


c_ BaseClass(?W..):
    """BaseClass(QWidget)

    Provides a base custom widget class to show that properties implemented
    in Python can be inherited and shown as belonging to distinct classes
    in Qt Designer's Property Editor.
    """

    ___  -   parent_None):

        s__(BaseClass, self). - (parent)

        resetAuthor()

    # Define getter, setter and resetter methods for the author property.

    ___ getAuthor
        r_ _author

    ___ setAuthor  name):
        _author _ name

    ___ resetAuthor
        _author _ "David Boddie"

    author _ pP..(st., getAuthor, setAuthor, resetAuthor)


c_ Bubble:
    """Bubble

    Provides a class to represent individual bubbles in a BubblesWidget.
    Each Bubble instance can render itself onto a paint device using a
    QPainter passed to its drawBubble() method.
    """

    ___  -   position, radius, speed, innerColor, outerColor):

        position _ position
        radius _ radius
        speed _ speed
        innerColor _ innerColor
        outerColor _ outerColor
        updateBrush()

    ___ updateBrush

        gradient _ QRadialGradient(
                QPointF(radius, radius), radius,
                QPointF(radius*0.5, radius*0.5))

        gradient.setColorAt(0, ?C..(255, 255, 255, 255))
        gradient.setColorAt(0.25, innerColor)
        gradient.setColorAt(1, outerColor)
        brush _ ?B..(gradient)

    ___ drawBubble  painter):

        painter.save()
        painter.translate(position.x() - radius,
                          position.y() - radius)
        painter.sB..(brush)
        painter.drawEllipse(0.0, 0.0, 2*radius, 2*radius)
        painter.restore()


c_ BubblesWidget(BaseClass):
    """BubblesWidget(BaseClass)

    Provides a custom widget that shows a number of rising bubbles.
    Various properties are defined so that the user can customize the
    appearance of the widget, and change the number and behaviour of the
    bubbles shown.
    """

    # We define two signals that are used to indicate changes to the status
    # of the widget.
    bubbleLeft _ pS..()
    bubblesRemaining _ pS..(in.)

    ___  -   parent_None):

        s__(BubblesWidget, self). - (parent)

        pen _ ?P..(?C..("#cccccc"))
        bubbles _   # list
        backgroundColor1 _ randomColor()
        backgroundColor2 _ randomColor().darker(150)
        newBubble _ N..

        random.seed()

        animation_timer _ ?T..
        animation_timer.setSingleShot F..
        animation_timer.timeout.c..(animate)
        animation_timer.start(25)

        bubbleTimer _ ?T..
        bubbleTimer.setSingleShot F..
        bubbleTimer.timeout.c..(expandBubble)

        setMouseTracking( st.
        sMS..(?S..(200, 200))
        sWT..("Bubble Maker")

    ___ paintEvent  event):

        background _ QRadialGradient(QPointF(rect().topLeft()), 500,
                QPointF(rect().bottomRight()))
        background.setColorAt(0, backgroundColor1)
        background.setColorAt(1, backgroundColor2)

        painter _ QPainter()
        painter.begin
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), ?B..(background))

        painter.sP..(pen)

        ___ bubble __ bubbles:

            __ QRectF(bubble.position - QPointF(bubble.radius, bubble.radius),
                      QSizeF(2*bubble.radius, 2*bubble.radius)).intersects(QRectF(event.rect())):
                bubble.drawBubble(painter)

        __ newBubble:

            newBubble.drawBubble(painter)

        painter.end()

    ___ mousePressEvent  event):

        __ event.button() __ __.LeftButton and newBubble __ N..:

            newBubble _ Bubble(QPointF(event.pos()), 4.0,
                                    1.0 + random.random() * 7,
                                    randomColor(), randomColor())
            bubbleTimer.start(50)
            event.accept()

    ___ mouseMoveEvent  event):

        __ newBubble:

            update(
                QRectF(newBubble.position - \
                       QPointF(newBubble.radius + 1, newBubble.radius + 1),
                       QSizeF(2*newBubble.radius + 2, 2*newBubble.radius + 2)).toRect()
                )
            newBubble.position _ QPointF(event.pos())
            update(
                QRectF(newBubble.position - \
                       QPointF(newBubble.radius + 1, newBubble.radius + 1),
                       QSizeF(2*newBubble.radius + 2, 2*newBubble.radius + 2)).toRect()
                )

        event.accept()

    ___ mouseReleaseEvent  event):

        __ newBubble:

            bubbles.ap..(newBubble)
            newBubble _ N..
            bubbleTimer.s..
            bubblesRemaining.e..(le.(bubbles))

        event.accept()

    ___ expandBubble

        __ newBubble:

            newBubble.radius _ min(newBubble.radius + 4.0,
                                        width()/8.0, height()/8.0)
            update(
                QRectF(newBubble.position - \
                       QPointF(newBubble.radius + 1, newBubble.radius + 1),
                       QSizeF(2*newBubble.radius + 2, 2*newBubble.radius + 2)).toRect()
                )
            newBubble.updateBrush()

    ___ randomColor

        red _ 205 + random.random() * 50
        green _ 205 + random.random() * 50
        blue _ 205 + random.random() * 50
        alpha _ 91 + random.random() * 100

        r_ ?C..(red, green, blue, alpha)

    ___ animate

        bubbles _   # list
        left _ F..
        ___ bubble __ bubbles:

            bubble.position _ bubble.position + QPointF(0, -bubble.speed)

            update(
                    QRectF(bubble.position - QPointF(bubble.radius + 1,
                                    bubble.radius + 1),
                            QSizeF(2*bubble.radius + 2, 2*bubble.radius + 2 + bubble.speed)).toRect())

            __ bubble.position.y() + bubble.radius > 0:
                bubbles.ap..(bubble)
            ____
                bubbleLeft.e..()
                left _ T..

        __ newBubble:
            update(
                    QRectF(newBubble.position - QPointF(
                                    newBubble.radius + 1,
                                    newBubble.radius + 1),
                            QSizeF(2*newBubble.radius + 2, 2*newBubble.radius + 2)).toRect())

        bubbles _ bubbles
        __ left:
            bubblesRemaining.e..(le.(bubbles))

    ___ sH..

        r_ ?S..(200, 200)

    # We provide getter and setter methods for the numberOfBubbles property.
    ___ getBubbles

        r_ le.(bubbles)

    # The setBubbles() method can also be used as a slot.
    @pyqtSlot(in.)
    ___ setBubbles  value):

        value _ max(0, value)

        w__ le.(bubbles) < value:

            newBubble _ Bubble(QPointF(random.random() * width(),
                                       random.random() * height()),
                               4.0 + random.random() * 20,
                               1.0 + random.random() * 7,
                               randomColor(), randomColor())
            newBubble.updateBrush()
            bubbles.ap..(newBubble)

        bubbles _ bubbles[:value]
        bubblesRemaining.e..(value)
        update()

    numberOfBubbles _ pP..(in., getBubbles, setBubbles)

    # We provide getter and setter methods for the color1 and color2
    # properties. The red, green and blue components for the QColor
    # values stored in these properties can be edited individually in
    # Qt Designer.

    ___ getColor1

        r_ backgroundColor1

    ___ setColor1  value):

        backgroundColor1 _ ?C..(value)
        update()

    color1 _ pP..(?C.., getColor1, setColor1)

    ___ getColor2

        r_ backgroundColor2

    ___ setColor2  value):

        backgroundColor2 _ ?C..(value)
        update()

    color2 _ pP..(?C.., getColor2, setColor2)

    # The stop() and start() slots provide simple control over the animation
    # of the bubbles in the widget.

    @pyqtSlot()
    ___ stop

        animation_timer.s..

    @pyqtSlot()
    ___ start

        animation_timer.start(25)


__ __name__ __ "__main__":

    ______ ___

    app _ ?A..(___.a..
    widget _ BubblesWidget()
    widget.s..
    ___.e.. ?.e..
