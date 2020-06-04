#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
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
##   * Neither the name of Riverbank Computing Limited nor the names of
##     its contributors may be used to endorse or promote products
##     derived from this software without specific prior written
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
##
#############################################################################


____ ?.?C.. ______ pP.., pS.., pyqtSlot
____ ?.?W.. ______ ?A.., ?TE..


# The purpose of this class is to show that Designer's property editor shows
# all Python classes in the hierarchy that define properties.
c_ PyTextViewer(?TE..):

    # Initialise the instance.
    ___  -   parent_None):
        s__(PyTextViewer, self). - (parent)

        sRO..( st.

        # Initialise the author property by calling it's reset function.
        resetAuthor()

    # The getter for the author property.  Note that we cannot follow the Qt
    # naming convention (ie. by using the naming the getter "author") because
    # it would conflict with the property name.
    ___ getAuthor
        r_ _author

    # The setter for the author property.
    ___ setAuthor  name):
        _author _ name

    # The resetter for the author property.  Only Qt Designer uses this.  Qt
    # Designer does not use the deleter function of the property.
    ___ resetAuthor
        _author _ "David Boddie"

    # Define the author property.  This will look like a C++ property to Qt
    # Designer and a Python property to Python.
    author _ pP..(st., getAuthor, setAuthor, resetAuthor)


# This is the class that implements the custom widget.
c_ PyDemo(PyTextViewer):

    # Define the Qt signals as a sequence of C++ function signatures excluding
    # the return type.  These may be connected to other signals or slots in Qt
    # Designer.
    zoomChanged _ pS..(in.)

    # Initialise the instance.
    ___  -   parent_None):
        s__(PyDemo, self). - (parent)

        sWT..("PyQt Demonstration Widget")
        sT..(_demo_text)

        # Initialise the zoom property.  We don't just call the resetter
        # because it assumes that this has already been initialised.
        _zoom _ 0

    # The getter for the zoom property.
    ___ getZoom
        r_ _zoom

    # The setter for the zoom property.  We also make define this as a Qt slot
    # which can be connected to Qt signals in Qt Designer.
    @pyqtSlot(in.)
    ___ setZoom  zoom):
        # Don't do anything if nothing has changed.
        __ _zoom __ zoom:
            r_

        # Zoom in or out according to the relative zoom levels.
        __ _zoom < zoom:
            zoomIn(zoom - _zoom)
        ____ _zoom > zoom:
            zoomOut(_zoom - zoom)

        # Remember the new zoom level.
        _zoom _ zoom

        # Emit the Qt signal to say that the zoom level has changed.
        zoomChanged.e..(zoom)

    # The resetter for the zoom property.
    ___ resetZoom
        setZoom(0)

    # Define the zoom property.  Changing the value of this in Qt Designer's
    # property editor causes the zoom level to change dynamically.
    zoom _ pP..(in., getZoom, setZoom, resetZoom)


# The text displayed in the custom widget.
_demo_text _ """<h3>PyQt Demonstration Widget</h3>
<p>This simple example demonstrates the following features.</p>
<ul>
 <li>The definition of properties that behave as C++ properties to Qt and
     Python properties to Python.</li>
 <li>The definition of new Qt signals that can be connected to other signals
     and Qt slots in Designer.</li>
 <li>The definition of new Qt slots that can be connected to signals in
     Designer.</li>
</ul>
"""


# Display the custom widget if the script is being run directly from the
# command line.
__ __name__ __ "__main__":

    ______ ___

    app _ ?A..(___.a..

    demo _ PyDemo()
    demo.s..

    ___.e.. ?.e..