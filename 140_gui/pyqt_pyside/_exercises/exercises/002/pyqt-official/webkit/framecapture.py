#!/usr/bin/env python
"""        
Capture a web page and save its internal frames in different images

  framecapture.py <url> <outputfile>

Notes:
  'url' is the URL of the web page to be captured
  'outputfile' is the prefix of the image files to be generated

Example:
  framecapture qt.nokia.com trolltech.png

Result:
  trolltech.png (full page)
  trolltech_frame1.png (...) trolltech_frameN.png ('N' number of internal frames)
"""


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
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
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
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
## $QT_END_LICENSE$
##
###########################################################################

______ ___

____ ?.?C.. ______ pS.., ?O.., ?S.., __, ?U..
____ ?.?G.. ______ QImage, QPainter
____ ?.?W.. ______ ?A..
____ ?.QtWebKitWidgets ______ QWebPage


___ cout(s):
    ___.stdout.w..(s)
    ___.stdout.flush()


___ cerr(s):
    ___.stderr.w..(s)
    ___.stderr.flush()


c_ FrameCapture(?O..):

    finished _ pS..()

    ___  -
        s__(FrameCapture, self). - ()

        _percent _ 0
        _page _ QWebPage()
        _page.mainFrame().setScrollBarPolicy(__.Vertical,
                __.ScrollBarAlwaysOff)
        _page.mainFrame().setScrollBarPolicy(__.H..,
                __.ScrollBarAlwaysOff)
        _page.loadProgress.c..(printProgress)
        _page.loadFinished.c..(saveResult)
 
    ___ load  url, outputFileName):
        cout("Loading %s\n" % url.toString())
        _percent _ 0
        index _ outputFileName.rfind('.')
        _fileName _ index __ -1 and outputFileName + ".png" or outputFileName
        _page.mainFrame().load(url)
        _page.setViewportSize(?S..(1024, 768))
 
    ___ printProgress  percent):
        __ _percent >_ percent:
            r_
        _percent +_ 1
        w__ _percent < percent:
            _percent +_ 1
            cout("#")
 
    ___ saveResult  ok):
        cout("\n")
        # Crude error-checking.
        __ no. ok:
            cerr("Failed loading %s\n" % _page.mainFrame().u.. .toString())
            finished.e..()
            r_

        # Save each frame in different image files.
        _frameCounter _ 0
        saveFrame(_page.mainFrame())
        finished.e..()
 
    ___ saveFrame  frame):
        fileName _ _fileName
        __ _frameCounter:
            index _ fileName.rfind('.')
            fileName _ "%s_frame%s%s" % (fileName[:index], _frameCounter, fileName[index:])
        image _ QImage(frame.contentsSize(), QImage.Format_ARGB32_Premultiplied)
        image.fill(__.transparent)
        painter _ QPainter(image)
        painter.setRenderHint(QPainter.Antialiasing,  st.
        painter.setRenderHint(QPainter.TextAntialiasing,  st.
        painter.setRenderHint(QPainter.SmoothPixmapTransform,  st.
        frame.documentElement().render(painter)
        painter.end()
        image.save(fileName)
        _frameCounter +_ 1
        ___ childFrame __ frame.childFrames
            saveFrame(childFrame)


__ ______ __ ______
    __ le.(___.a.. !_ 3:
        cerr(__doc__)
        ___.e..(1)

    url _ ?U...fromUserInput(___.argv[1])
    fileName _ ___.argv[2]

    app _ ?A..(___.a..

    capture _ FrameCapture()
    capture.finished.c.. ?.quit)
    capture.load(url, fileName)

    app.e..
