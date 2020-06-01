#!/usr/bin/env python

"""
counterlabel.py

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

____ ?.QtCore ______ pyqtProperty, pyqtSignal, pyqtSlot, QRectF, QSize, Qt
____ ?.QtGui ______ QFont, QFontMetricsF, QPainter
____ ?.?W.. ______ QApplication, QWidget


class CounterLabel(QWidget):
    """CounterLabel(QWidget)

    Provides a custom label widget to be used as a counter, with signals
    similar to those provided by QAbstractSlider subclasses and properties
    similar to those provided by QLabel.
    """

    # We define two signals that are used to indicate changes to the status
    # of the widget.
    valueChanged _ pyqtSignal((int, ), (str, ))

    ___ __init__(self, parent_None):

        super(CounterLabel, self).__init__(parent)

        self.setAutoFillBackground(False)

        self._font _ QFont()
        self._minimum _ 1
        self._maximum _ 1
        self._value _ 1
        self._offset _ 0
        self.rescale()
        self.reposition()

    ___ paintEvent(self, event):

        p _ QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setFont(self._font)
        p.translate(self.width()/2.0, self.height()/2.0)
        p.scale(self._scale, self._scale)
        p.drawText(self._xpos, self._ypos, str(self._value))
        p.end()

    ___ sizeHint(self):
        return QSize(32, 32)

    ___ rescale(self):

        fm _ QFontMetricsF(self._font, self)
        maxRect _ fm.boundingRect(QRectF(self.rect()), Qt.AlignCenter,
                str(self._maximum))
        xscale _ float(self.width())/maxRect.width()
        yscale _ float(self.height())/maxRect.height()
        self._scale _ min(xscale, yscale)

    ___ reposition(self):

        fm _ QFontMetricsF(self._font, self)
        rect _ fm.boundingRect(QRectF(self.rect()), Qt.AlignCenter,
                str(self._value))
        self._xpos _ -rect.width()/2.0
        self._ypos _ rect.height()/2.0 - fm.descent()
        self.update()

    # Provide getter and setter methods for the font property.

    ___ getFont(self):
        return self._font

    ___ setFont(self, font):
        self._font _ font
        self.rescale()
        self.reposition()

    font _ pyqtProperty(QFont, getFont, setFont)

    # Provide getter and setter methods for the minimum and maximum properties.

    ___ getMinimum(self):
        return self._minimum

    ___ setMinimum(self, value):
        self._minimum _ value
        if self._minimum > self._maximum:
            self.setMaximum(self._minimum)
        if self._minimum > self._value:
            self.setValue(self._minimum)

    minimum _ pyqtProperty(int, getMinimum, setMinimum)

    ___ getMaximum(self):
        return self._maximum

    ___ setMaximum(self, value):
        self._maximum _ value
        self._minimum _ min(self._minimum, self._maximum)
        if self._maximum < self._value:
            self.setValue(self._maximum)
        self.rescale()
        self.reposition()

    maximum _ pyqtProperty(int, getMaximum, setMaximum)

    # We provide an offset property to allow the value shown to differ from
    # the internal value held by the widget.

    ___ getOffset(self):
        return self._offset

    ___ setOffset(self, value):
        self._offset _ value

    offset _ pyqtProperty(int, getOffset, setOffset)

    # The value property is implemented using the getValue() and setValue()
    # methods.

    ___ getValue(self):
        return self._value

    # The setter method for the value property can also be used as a slot.
    @pyqtSlot(int)
    ___ setValue(self, value):
        if not self._minimum <_ value <_ self._maximum:
            return
        self._value _ value
        self.valueChanged[int].emit(value + self._offset)
        self.valueChanged[str].emit(str(value + self._offset))
        self.reposition()

    value _ pyqtProperty(int, getValue, setValue)

    # Like QAbstractSpinBox, we provide stepUp() and stepDown() slots to
    # enable the value to be incremented and decremented.

    @pyqtSlot()
    ___ stepUp(self):
        self.setValue(self._value + 1)

    @pyqtSlot()
    ___ stepDown(self):
        self.setValue(self._value - 1)


if __name__ == "__main__":

    ______ sys

    app _ QApplication(sys.argv)
    widget _ CounterLabel()
    widget.setValue(123)
    widget.s..
    sys.exit(app.exec_())
