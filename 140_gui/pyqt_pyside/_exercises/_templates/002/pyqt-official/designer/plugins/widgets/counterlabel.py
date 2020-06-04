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

____ ?.?C.. ______ pP.., pS.., pyqtSlot, QRectF, ?S.., __
____ ?.?G.. ______ ?F.., QFontMetricsF, QPainter
____ ?.?W.. ______ ?A.., ?W..


c_ CounterLabel(?W..):
    """CounterLabel(QWidget)

    Provides a custom label widget to be used as a counter, with signals
    similar to those provided by QAbstractSlider subclasses and properties
    similar to those provided by QLabel.
    """

    # We define two signals that are used to indicate changes to the status
    # of the widget.
    valueChanged _ pS..((in., ), (st., ))

    ___  -   parent_None):

        s__(CounterLabel, self). - (parent)

        setAutoFillBackground F..

        _font _ ?F..()
        _minimum _ 1
        _maximum _ 1
        _value _ 1
        _offset _ 0
        rescale()
        reposition()

    ___ paintEvent  event):

        p _ QPainter()
        p.begin
        p.setRenderHint(QPainter.Antialiasing)
        p.sF..(_font)
        p.translate(width()/2.0, height()/2.0)
        p.scale(_scale, _scale)
        p.drawText(_xpos, _ypos, st.(_value))
        p.end()

    ___ sH..
        r_ ?S..(32, 32)

    ___ rescale 

        fm _ QFontMetricsF(_font, self)
        maxRect _ fm.boundingRect(QRectF(rect()), __.AlignCenter,
                st.(_maximum))
        xscale _ fl..(width())/maxRect.width()
        yscale _ fl..(height())/maxRect.height()
        _scale _ min(xscale, yscale)

    ___ reposition 

        fm _ QFontMetricsF(_font, self)
        rect _ fm.boundingRect(QRectF(rect()), __.AlignCenter,
                st.(_value))
        _xpos _ -rect.width()/2.0
        _ypos _ rect.height()/2.0 - fm.descent()
        update()

    # Provide getter and setter methods for the font property.

    ___ getFont 
        r_ _font

    ___ sF..  font):
        _font _ font
        rescale()
        reposition()

    font _ pP..(?F.., getFont, sF..)

    # Provide getter and setter methods for the minimum and maximum properties.

    ___ getMinimum 
        r_ _minimum

    ___ setMinimum  value):
        _minimum _ value
        __ _minimum > _maximum:
            sM..(_minimum)
        __ _minimum > _value:
            sV..(_minimum)

    minimum _ pP..(in., getMinimum, setMinimum)

    ___ getMaximum 
        r_ _maximum

    ___ sM..  value):
        _maximum _ value
        _minimum _ min(_minimum, _maximum)
        __ _maximum < _value:
            sV..(_maximum)
        rescale()
        reposition()

    maximum _ pP..(in., getMaximum, sM..)

    # We provide an offset property to allow the value shown to differ from
    # the internal value held by the widget.

    ___ getOffset 
        r_ _offset

    ___ setOffset  value):
        _offset _ value

    offset _ pP..(in., getOffset, setOffset)

    # The value property is implemented using the getValue() and setValue()
    # methods.

    ___ getValue 
        r_ _value

    # The setter method for the value property can also be used as a slot.
    @pyqtSlot(in.)
    ___ sV..  value):
        __ no. _minimum <_ value <_ _maximum:
            r_
        _value _ value
        valueChanged[in.].e..(value + _offset)
        valueChanged[st.].e..(st.(value + _offset))
        reposition()

    value _ pP..(in., getValue, sV..)

    # Like QAbstractSpinBox, we provide stepUp() and stepDown() slots to
    # enable the value to be incremented and decremented.

    @pyqtSlot()
    ___ stepUp 
        sV..(_value + 1)

    @pyqtSlot()
    ___ stepDown 
        sV..(_value - 1)


__ __name__ __ "__main__":

    ______ ___

    app _ ?A..(___.a..
    widget _ CounterLabel()
    widget.sV..(123)
    widget.s..
    ___.e.. ?.e..
