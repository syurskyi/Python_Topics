#!/usr/bin/env python

"""
pythonconsolewidget.py

A Python console custom widget for Qt Designer.

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

____ ?.?C.. ______ pS.., QEvent, __
____ ?.?W.. ______ ?A.., QLineEdit


c_ PythonConsoleWidget(QLineEdit):
    """PythonConsoleWidget(QLineEdit)
    
    Provides a custom widget to accept Python expressions and emit output
    to other components via a custom signal.
    """
    
    pythonOutput _ pS.. st.
    
    ___  -   parent_None):
    
        s__(PythonConsoleWidget, self). - (parent)
        
        history _   # list
        current _ -1
        
        rP__.c..(e..)
    
    ___ keyReleaseEvent  event):
    
        __ event.type() __ QEvent.KeyRelease:
        
            __ event.key() __ __.Key_Up:
                current _ max(0, current - 1)
                __ 0 <_ current < le.(history):
                    sT..(history[current])
                    current _ current
                
                event.accept()
            
            ____ event.key() __ __.Key_Down:
                current _ min(le.(history), current + 1)
                __ 0 <_ current < le.(history):
                    sT..(history[current])
                ____
                    c..
                current _ current
                
                event.accept()
    
    ___ e..
    
        # Define this here to give users something to look at.
        qApp _ ?A...i.. 
        
        expression _ t__()
        ___
            result _ st.(eval(st.(expression)))
            
            # Emit the result of the evaluated expression.
            pythonOutput.e..(result)

            # Clear the line edit, append the successful expression to the
            # history, and update the current command index.
            c..
            history.ap..(expression)
            current _ le.(history)
        _____:
            p..


__ __name__ __ "__main__":

    ______ ___

    app _ ?A..(___.a..
    widget _ PythonConsoleWidget()
    widget.s..
    ___.e.. ?.e..
