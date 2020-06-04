#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
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
#############################################################################


____ ?.?C.. ______ QFileInfo, ?S.., __
____ ?.?G.. ______ QMovie, ?P..
____ ?.?W.. ______ (?A.., QCheckBox, ?FD.., QGridLayout,
        ?HBL.., ?L.., ?SP.., ?S.., SB.., ?S..,
        QToolButton, ?VBL.., ?W..)


c_ MoviePlayer(?W..):
    ___  -   parent_None):
        s__(MoviePlayer, self). - (parent)

        movie _ QMovie
        movie.setCacheMode(QMovie.CacheAll)

        movieLabel _ ?L..("No movie loaded")
        movieLabel.setAlignment(__.AlignCenter)
        movieLabel.sSP..(?SP...Ignored, ?SP...Ignored)
        movieLabel.setBackgroundRole(?P...Dark)
        movieLabel.setAutoFillBackground( st.

        currentMovieDirectory _ ''

        createControls()
        createButtons()

        movie.frameChanged.c..(updateFrameSlider)
        movie.stateChanged.c..(updateButtons)
        fitCheckBox.c__.c..(fitToWindow)
        frameSlider.valueChanged.c..(goToFrame)
        speedSpinBox.valueChanged.c..(movie.setSpeed)

        mainLayout _ ?VBL..
        mainLayout.aW..(movieLabel)
        mainLayout.aL..(controlsLayout)
        mainLayout.aL..(buttonsLayout)
        sL..(mainLayout)

        updateFrameSlider()
        updateButtons()

        sWT..("Movie Player")
        r..(400, 400)

    ___ o..
        fileName, _ _ ?FD...gOFN..  "Open a Movie",
                currentMovieDirectory)

        __ fileName:
            openFile(fileName)

    ___ openFile  fileName):
        currentMovieDirectory _ QFileInfo(fileName).pa__()

        movie.s..
        movieLabel.setMovie(movie)
        movie.setFileName(fileName)
        movie.start()

        updateFrameSlider();
        updateButtons();

    ___ goToFrame  frame):
        movie.jumpToFrame(frame)

    ___ fitToWindow
        movieLabel.setScaledContents(fitCheckBox.isChecked())

    ___ updateFrameSlider
        hasFrames _ (movie.currentFrameNumber() >_ 0)

        __ hasFrames:
            __ movie.frameCount() > 0:
                frameSlider.sM..(movie.frameCount() - 1)
            ____ movie.currentFrameNumber() > frameSlider.maximum
                frameSlider.sM..(movie.currentFrameNumber())

            frameSlider.sV..(movie.currentFrameNumber())
        ____
            frameSlider.sM..(0)

        frameLabel.sE..(hasFrames)
        frameSlider.sE..(hasFrames)

    ___ updateButtons
        state _ movie.s..

        playButton.sE..(movie.iV.. and
                movie.frameCount() !_ 1 and state __ QMovie.NotRunning)
        pauseButton.sE..(state !_ QMovie.NotRunning)
        pauseButton.sC__(state __ QMovie.Paused)
        stopButton.sE..(state !_ QMovie.NotRunning)

    ___ createControls
        fitCheckBox _ QCheckBox("Fit to Window")

        frameLabel _ ?L..("Current frame:")

        frameSlider _ ?S..(__.H..)
        frameSlider.setTickPosition(?S...TicksBelow)
        frameSlider.setTickInterval(10)

        speedLabel _ ?L..("Speed:")

        speedSpinBox _ SB..()
        speedSpinBox.setRange(1, 9999)
        speedSpinBox.sV..(100)
        speedSpinBox.setSuffix("%")

        controlsLayout _ QGridLayout()
        controlsLayout.aW..(fitCheckBox, 0, 0, 1, 2)
        controlsLayout.aW..(frameLabel, 1, 0)
        controlsLayout.aW..(frameSlider, 1, 1, 1, 2)
        controlsLayout.aW..(speedLabel, 2, 0)
        controlsLayout.aW..(speedSpinBox, 2, 1)

    ___ createButtons
        iconSize _ ?S..(36, 36)

        openButton _ QToolButton()
        openButton.sI..(style().standardIcon(?S...SP_DialogOpenButton))
        openButton.setIconSize(iconSize)
        openButton.sTT..("Open File")
        openButton.c__.c..(o..)

        playButton _ QToolButton()
        playButton.sI..(style().standardIcon(?S...SP_MediaPlay))
        playButton.setIconSize(iconSize)
        playButton.sTT..("Play")
        playButton.c__.c..(movie.start)

        pauseButton _ QToolButton()
        pauseButton.setCheckable( st.
        pauseButton.sI..(style().standardIcon(?S...SP_MediaPause))
        pauseButton.setIconSize(iconSize)
        pauseButton.sTT..("Pause")
        pauseButton.c__.c..(movie.setPaused)

        stopButton _ QToolButton()
        stopButton.sI..(style().standardIcon(?S...SP_MediaStop))
        stopButton.setIconSize(iconSize)
        stopButton.sTT..("Stop")
        stopButton.c__.c..(movie.stop)

        quitButton _ QToolButton()
        quitButton.sI..(style().standardIcon(?S...SP_DialogCloseButton))
        quitButton.setIconSize(iconSize)
        quitButton.sTT..("Quit")
        quitButton.c__.c..(close)

        buttonsLayout _ ?HBL..
        buttonsLayout.addStretch()
        buttonsLayout.aW..(openButton)
        buttonsLayout.aW..(playButton)
        buttonsLayout.aW..(pauseButton)
        buttonsLayout.aW..(stopButton)
        buttonsLayout.aW..(quitButton)
        buttonsLayout.addStretch()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    player _ MoviePlayer()
    player.s..
    ___.e.. ?.e..
