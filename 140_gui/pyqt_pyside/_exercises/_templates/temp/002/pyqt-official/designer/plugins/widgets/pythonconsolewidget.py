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

____ ?.?C.. ______ pyqtSignal, QEvent, __
____ ?.?W.. ______ ?A.., QLineEdit


c_ PythonConsoleWidget(QLineEdit):
    """PythonConsoleWidget(QLineEdit)
    
    Provides a custom widget to accept Python expressions and emit output
    to other components via a custom signal.
    """
    
    pythonOutput _ pyqtSignal(str)
    
    ___ __init__  parent_None):
    
        super(PythonConsoleWidget, self).__init__(parent)
        
        self.history _ []
        self.current _ -1
        
        self.returnPressed.c..(self.execute)
    
    ___ keyReleaseEvent  event):
    
        __ event.type() == QEvent.KeyRelease:
        
            __ event.key() == __.Key_Up:
                current _ max(0, self.current - 1)
                __ 0 <_ current < len(self.history):
                    self.sT..(self.history[current])
                    self.current _ current
                
                event.accept()
            
            ____ event.key() == __.Key_Down:
                current _ min(len(self.history), self.current + 1)
                __ 0 <_ current < len(self.history):
                    self.sT..(self.history[current])
                ____
                    self.clear()
                self.current _ current
                
                event.accept()
    
    ___ execute(self):
    
        # Define this here to give users something to look at.
        qApp _ ?A...instance()
        
        self.expression _ self.text()
        try:
            result _ str(eval(str(self.expression)))
            
            # Emit the result of the evaluated expression.
            self.pythonOutput.emit(result)

            # Clear the line edit, append the successful expression to the
            # history, and update the current command index.
            self.clear()
            self.history.append(self.expression)
            self.current _ len(self.history)
        except:
            pass


__ __name__ == "__main__":

    ______ sys

    app _ ?A..(sys.argv)
    widget _ PythonConsoleWidget()
    widget.s..
    sys.exit(app.exec_())
