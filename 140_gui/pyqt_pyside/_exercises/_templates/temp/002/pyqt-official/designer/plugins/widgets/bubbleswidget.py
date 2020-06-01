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

____ ?.?C.. ______ (pyqtProperty, pyqtSignal, pyqtSlot, QPointF, QRectF,
        QSize, QSizeF, __, QTimer)
____ ?.?G.. ______ QBrush, ?C.., QPainter, QPen, QRadialGradient
____ ?.?W.. ______ ?A.., QWidget


c_ BaseClass(QWidget):
    """BaseClass(QWidget)

    Provides a base custom widget class to show that properties implemented
    in Python can be inherited and shown as belonging to distinct classes
    in Qt Designer's Property Editor.
    """

    ___ __init__  parent_None):

        super(BaseClass, self).__init__(parent)

        self.resetAuthor()

    # Define getter, setter and resetter methods for the author property.

    ___ getAuthor(self):
        r_ self._author

    ___ setAuthor  name):
        self._author _ name

    ___ resetAuthor(self):
        self._author _ "David Boddie"

    author _ pyqtProperty(str, getAuthor, setAuthor, resetAuthor)


c_ Bubble:
    """Bubble

    Provides a class to represent individual bubbles in a BubblesWidget.
    Each Bubble instance can render itself onto a paint device using a
    QPainter passed to its drawBubble() method.
    """

    ___ __init__  position, radius, speed, innerColor, outerColor):

        self.position _ position
        self.radius _ radius
        self.speed _ speed
        self.innerColor _ innerColor
        self.outerColor _ outerColor
        self.updateBrush()

    ___ updateBrush(self):

        gradient _ QRadialGradient(
                QPointF(self.radius, self.radius), self.radius,
                QPointF(self.radius*0.5, self.radius*0.5))

        gradient.setColorAt(0, ?C..(255, 255, 255, 255))
        gradient.setColorAt(0.25, self.innerColor)
        gradient.setColorAt(1, self.outerColor)
        self.brush _ QBrush(gradient)

    ___ drawBubble  painter):

        painter.save()
        painter.translate(self.position.x() - self.radius,
                          self.position.y() - self.radius)
        painter.setBrush(self.brush)
        painter.drawEllipse(0.0, 0.0, 2*self.radius, 2*self.radius)
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
    bubbleLeft _ pyqtSignal()
    bubblesRemaining _ pyqtSignal(int)

    ___ __init__  parent_None):

        super(BubblesWidget, self).__init__(parent)

        self.pen _ QPen(?C..("#cccccc"))
        self.bubbles _ []
        self.backgroundColor1 _ self.randomColor()
        self.backgroundColor2 _ self.randomColor().darker(150)
        self.newBubble _ N..

        random.seed()

        self.animation_timer _ QTimer(self)
        self.animation_timer.setSingleShot F..
        self.animation_timer.timeout.c..(self.animate)
        self.animation_timer.start(25)

        self.bubbleTimer _ ?T..
        self.bubbleTimer.setSingleShot F..
        self.bubbleTimer.timeout.c..(self.expandBubble)

        self.setMouseTracking(True)
        self.setMinimumSize(QSize(200, 200))
        self.setWindowTitle("Bubble Maker")

    ___ paintEvent  event):

        background _ QRadialGradient(QPointF(self.rect().topLeft()), 500,
                QPointF(self.rect().bottomRight()))
        background.setColorAt(0, self.backgroundColor1)
        background.setColorAt(1, self.backgroundColor2)

        painter _ QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(background))

        painter.setPen(self.pen)

        for bubble in self.bubbles:

            __ QRectF(bubble.position - QPointF(bubble.radius, bubble.radius),
                      QSizeF(2*bubble.radius, 2*bubble.radius)).intersects(QRectF(event.rect())):
                bubble.drawBubble(painter)

        __ self.newBubble:

            self.newBubble.drawBubble(painter)

        painter.end()

    ___ mousePressEvent  event):

        __ event.button() == __.LeftButton and self.newBubble __ N..:

            self.newBubble _ Bubble(QPointF(event.pos()), 4.0,
                                    1.0 + random.random() * 7,
                                    self.randomColor(), self.randomColor())
            self.bubbleTimer.start(50)
            event.accept()

    ___ mouseMoveEvent  event):

        __ self.newBubble:

            self.update(
                QRectF(self.newBubble.position - \
                       QPointF(self.newBubble.radius + 1, self.newBubble.radius + 1),
                       QSizeF(2*self.newBubble.radius + 2, 2*self.newBubble.radius + 2)).toRect()
                )
            self.newBubble.position _ QPointF(event.pos())
            self.update(
                QRectF(self.newBubble.position - \
                       QPointF(self.newBubble.radius + 1, self.newBubble.radius + 1),
                       QSizeF(2*self.newBubble.radius + 2, 2*self.newBubble.radius + 2)).toRect()
                )

        event.accept()

    ___ mouseReleaseEvent  event):

        __ self.newBubble:

            self.bubbles.append(self.newBubble)
            self.newBubble _ N..
            self.bubbleTimer.stop()
            self.bubblesRemaining.emit(len(self.bubbles))

        event.accept()

    ___ expandBubble(self):

        __ self.newBubble:

            self.newBubble.radius _ min(self.newBubble.radius + 4.0,
                                        self.width()/8.0, self.height()/8.0)
            self.update(
                QRectF(self.newBubble.position - \
                       QPointF(self.newBubble.radius + 1, self.newBubble.radius + 1),
                       QSizeF(2*self.newBubble.radius + 2, 2*self.newBubble.radius + 2)).toRect()
                )
            self.newBubble.updateBrush()

    ___ randomColor(self):

        red _ 205 + random.random() * 50
        green _ 205 + random.random() * 50
        blue _ 205 + random.random() * 50
        alpha _ 91 + random.random() * 100

        r_ ?C..(red, green, blue, alpha)

    ___ animate(self):

        bubbles _ []
        left _ False
        for bubble in self.bubbles:

            bubble.position _ bubble.position + QPointF(0, -bubble.speed)

            self.update(
                    QRectF(bubble.position - QPointF(bubble.radius + 1,
                                    bubble.radius + 1),
                            QSizeF(2*bubble.radius + 2, 2*bubble.radius + 2 + bubble.speed)).toRect())

            __ bubble.position.y() + bubble.radius > 0:
                bubbles.append(bubble)
            ____
                self.bubbleLeft.emit()
                left _ True

        __ self.newBubble:
            self.update(
                    QRectF(self.newBubble.position - QPointF(
                                    self.newBubble.radius + 1,
                                    self.newBubble.radius + 1),
                            QSizeF(2*self.newBubble.radius + 2, 2*self.newBubble.radius + 2)).toRect())

        self.bubbles _ bubbles
        __ left:
            self.bubblesRemaining.emit(len(self.bubbles))

    ___ sizeHint(self):

        r_ QSize(200, 200)

    # We provide getter and setter methods for the numberOfBubbles property.
    ___ getBubbles(self):

        r_ len(self.bubbles)

    # The setBubbles() method can also be used as a slot.
    @pyqtSlot(int)
    ___ setBubbles  value):

        value _ max(0, value)

        while len(self.bubbles) < value:

            newBubble _ Bubble(QPointF(random.random() * self.width(),
                                       random.random() * self.height()),
                               4.0 + random.random() * 20,
                               1.0 + random.random() * 7,
                               self.randomColor(), self.randomColor())
            newBubble.updateBrush()
            self.bubbles.append(newBubble)

        self.bubbles _ self.bubbles[:value]
        self.bubblesRemaining.emit(value)
        self.update()

    numberOfBubbles _ pyqtProperty(int, getBubbles, setBubbles)

    # We provide getter and setter methods for the color1 and color2
    # properties. The red, green and blue components for the QColor
    # values stored in these properties can be edited individually in
    # Qt Designer.

    ___ getColor1(self):

        r_ self.backgroundColor1

    ___ setColor1  value):

        self.backgroundColor1 _ ?C..(value)
        self.update()

    color1 _ pyqtProperty(?C.., getColor1, setColor1)

    ___ getColor2(self):

        r_ self.backgroundColor2

    ___ setColor2  value):

        self.backgroundColor2 _ ?C..(value)
        self.update()

    color2 _ pyqtProperty(?C.., getColor2, setColor2)

    # The stop() and start() slots provide simple control over the animation
    # of the bubbles in the widget.

    @pyqtSlot()
    ___ stop(self):

        self.animation_timer.stop()

    @pyqtSlot()
    ___ start(self):

        self.animation_timer.start(25)


__ __name__ == "__main__":

    ______ sys

    app _ ?A..(sys.argv)
    widget _ BubblesWidget()
    widget.s..
    sys.exit(app.exec_())
