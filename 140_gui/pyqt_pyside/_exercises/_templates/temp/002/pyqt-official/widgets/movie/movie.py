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


____ ?.?C.. ______ QFileInfo, QSize, __
____ ?.?G.. ______ QMovie, ?P..
____ ?.?W.. ______ (?A.., QCheckBox, ?FD.., QGridLayout,
        QHBoxLayout, QLabel, QSizePolicy, QSlider, QSpinBox, QStyle,
        QToolButton, QVBoxLayout, QWidget)


c_ MoviePlayer(QWidget):
    ___ __init__  parent_None):
        super(MoviePlayer, self).__init__(parent)

        self.movie _ QMovie(self)
        self.movie.setCacheMode(QMovie.CacheAll)

        self.movieLabel _ QLabel("No movie loaded")
        self.movieLabel.setAlignment(__.AlignCenter)
        self.movieLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.movieLabel.setBackgroundRole(?P...Dark)
        self.movieLabel.setAutoFillBackground(True)

        self.currentMovieDirectory _ ''

        self.createControls()
        self.createButtons()

        self.movie.frameChanged.c..(self.updateFrameSlider)
        self.movie.stateChanged.c..(self.updateButtons)
        self.fitCheckBox.c__.c..(self.fitToWindow)
        self.frameSlider.valueChanged.c..(self.goToFrame)
        self.speedSpinBox.valueChanged.c..(self.movie.setSpeed)

        mainLayout _ ?VBL..
        mainLayout.aW..(self.movieLabel)
        mainLayout.addLayout(self.controlsLayout)
        mainLayout.addLayout(self.buttonsLayout)
        self.sL..(mainLayout)

        self.updateFrameSlider()
        self.updateButtons()

        self.setWindowTitle("Movie Player")
        self.resize(400, 400)

    ___ o..(self):
        fileName, _ _ ?FD...gOFN..  "Open a Movie",
                self.currentMovieDirectory)

        __ fileName:
            self.openFile(fileName)

    ___ openFile  fileName):
        self.currentMovieDirectory _ QFileInfo(fileName).path()

        self.movie.stop()
        self.movieLabel.setMovie(self.movie)
        self.movie.setFileName(fileName)
        self.movie.start()

        self.updateFrameSlider();
        self.updateButtons();

    ___ goToFrame  frame):
        self.movie.jumpToFrame(frame)

    ___ fitToWindow(self):
        self.movieLabel.setScaledContents(self.fitCheckBox.isChecked())

    ___ updateFrameSlider(self):
        hasFrames _ (self.movie.currentFrameNumber() >_ 0)

        __ hasFrames:
            __ self.movie.frameCount() > 0:
                self.frameSlider.setMaximum(self.movie.frameCount() - 1)
            ____ self.movie.currentFrameNumber() > self.frameSlider.maximum
                self.frameSlider.setMaximum(self.movie.currentFrameNumber())

            self.frameSlider.setValue(self.movie.currentFrameNumber())
        ____
            self.frameSlider.setMaximum(0)

        self.frameLabel.setEnabled(hasFrames)
        self.frameSlider.setEnabled(hasFrames)

    ___ updateButtons(self):
        state _ self.movie.state()

        self.playButton.setEnabled(self.movie.isValid() and
                self.movie.frameCount() !_ 1 and state == QMovie.NotRunning)
        self.pauseButton.setEnabled(state !_ QMovie.NotRunning)
        self.pauseButton.setChecked(state == QMovie.Paused)
        self.stopButton.setEnabled(state !_ QMovie.NotRunning)

    ___ createControls(self):
        self.fitCheckBox _ QCheckBox("Fit to Window")

        self.frameLabel _ QLabel("Current frame:")

        self.frameSlider _ QSlider(__.Horizontal)
        self.frameSlider.setTickPosition(QSlider.TicksBelow)
        self.frameSlider.setTickInterval(10)

        speedLabel _ QLabel("Speed:")

        self.speedSpinBox _ QSpinBox()
        self.speedSpinBox.setRange(1, 9999)
        self.speedSpinBox.setValue(100)
        self.speedSpinBox.setSuffix("%")

        self.controlsLayout _ QGridLayout()
        self.controlsLayout.aW..(self.fitCheckBox, 0, 0, 1, 2)
        self.controlsLayout.aW..(self.frameLabel, 1, 0)
        self.controlsLayout.aW..(self.frameSlider, 1, 1, 1, 2)
        self.controlsLayout.aW..(speedLabel, 2, 0)
        self.controlsLayout.aW..(self.speedSpinBox, 2, 1)

    ___ createButtons(self):
        iconSize _ QSize(36, 36)

        openButton _ QToolButton()
        openButton.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        openButton.setIconSize(iconSize)
        openButton.setToolTip("Open File")
        openButton.c__.c..(self.o..)

        self.playButton _ QToolButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.setIconSize(iconSize)
        self.playButton.setToolTip("Play")
        self.playButton.c__.c..(self.movie.start)

        self.pauseButton _ QToolButton()
        self.pauseButton.setCheckable(True)
        self.pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.pauseButton.setIconSize(iconSize)
        self.pauseButton.setToolTip("Pause")
        self.pauseButton.c__.c..(self.movie.setPaused)

        self.stopButton _ QToolButton()
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopButton.setIconSize(iconSize)
        self.stopButton.setToolTip("Stop")
        self.stopButton.c__.c..(self.movie.stop)

        quitButton _ QToolButton()
        quitButton.setIcon(self.style().standardIcon(QStyle.SP_DialogCloseButton))
        quitButton.setIconSize(iconSize)
        quitButton.setToolTip("Quit")
        quitButton.c__.c..(self.close)

        self.buttonsLayout _ QHBoxLayout()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.aW..(openButton)
        self.buttonsLayout.aW..(self.playButton)
        self.buttonsLayout.aW..(self.pauseButton)
        self.buttonsLayout.aW..(self.stopButton)
        self.buttonsLayout.aW..(quitButton)
        self.buttonsLayout.addStretch()


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    player _ MoviePlayer()
    player.s..
    sys.exit(app.exec_())
