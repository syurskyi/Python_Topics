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


______ ___
______ __

____ ?.?C.. ______ QLibraryInfo, QProcess, QProcessEnvironment
____ ?.?W.. ______ ?A.., ?MB..


app _ ?A..(___.a..

?MB...i..(N.., "PyQt Designer Plugins",
        "<p>This example will start Qt Designer when you click the <b>OK</b> "
        "button.</p>"
        "<p>Before doing so it sets the <tt>PYQTDESIGNERPATH</tt> environment "
        "variable to the <tt>python</tt> directory that is part of this "
        "example.  This directory contains all the example Python plugin "
        "modules.</p>"
        "<p>It also sets the <tt>PYTHONPATH</tt> environment variable to the "
        "<tt>widgets</tt> directory that is also part of this example.  This "
        "directory contains the Python modules that implement the example "
        "custom widgets.</p>"
        "<p>All of the example custom widgets should then appear in "
        "Designer's widget box in the <b>PyQt Examples</b> group.</p>")

# Tell Qt Designer where it can find the directory containing the plugins and
# Python where it can find the widgets.
base _ __.p__ .dirname(__file__)
env _ QProcessEnvironment.systemEnvironment()
env.insert('PYQTDESIGNERPATH', __.p__ .join(base, 'python'))
env.insert('PYTHONPATH', __.p__ .join(base, 'widgets'))

# Start Designer.
designer _ QProcess()
designer.setProcessEnvironment(env)

designer_bin _ QLibraryInfo.location(QLibraryInfo.BinariesPath)

__ ___.platform __ 'darwin':
    designer_bin +_ '/Designer.app/Contents/MacOS/Designer'
____
    designer_bin +_ '/designer'

designer.start(designer_bin)
designer.waitForFinished(-1)

___.e..(designer.exitCode())
