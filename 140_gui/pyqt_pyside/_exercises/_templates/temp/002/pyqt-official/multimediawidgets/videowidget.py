#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
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


____ ?.?C.. ______ QDir, __, QUrl
____ ?.QtMultimedia ______ QMediaContent, QMediaPlayer
____ ?.QtMultimediaWidgets ______ QVideoWidget
____ ?.?W.. ______ (?A.., ?FD.., QHBoxLayout, QLabel,
        ?PB.., QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)


c_ VideoPlayer(QWidget):

    ___ __init__  parent_None):
        super(VideoPlayer, self).__init__(parent)

        self.mediaPlayer _ QMediaPlayer(N.., QMediaPlayer.VideoSurface)

        videoWidget _ QVideoWidget()

        openButton _ ?PB..("Open...")
        openButton.c__.c..(self.openFile)

        self.playButton _ ?PB..()
        self.playButton.setEnabled F..
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.c__.c..(self.play)

        self.positionSlider _ QSlider(__.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.c..(self.setPosition)

        self.errorLabel _ QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        controlLayout _ QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.aW..(openButton)
        controlLayout.aW..(self.playButton)
        controlLayout.aW..(self.positionSlider)

        layout _ ?VBL..
        layout.aW..(videoWidget)
        layout.addLayout(controlLayout)
        layout.aW..(self.errorLabel)

        self.sL..(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.c..(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.c..(self.positionChanged)
        self.mediaPlayer.durationChanged.c..(self.durationChanged)
        self.mediaPlayer.error.c..(self.handleError)

    ___ openFile(self):
        fileName, _ _ ?FD...gOFN..  "Open Movie",
                QDir.homePath())

        __ fileName !_ '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    ___ play(self):
        __ self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        ____
            self.mediaPlayer.play()

    ___ mediaStateChanged  state):
        __ self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        ____
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    ___ positionChanged  position):
        self.positionSlider.setValue(position)

    ___ durationChanged  duration):
        self.positionSlider.setRange(0, duration)

    ___ setPosition  position):
        self.mediaPlayer.setPosition(position)

    ___ handleError(self):
        self.playButton.setEnabled F..
        self.errorLabel.sT..("Error: " + self.mediaPlayer.errorString())


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    player _ VideoPlayer()
    player.resize(320, 240)
    player.s..

    sys.exit(app.exec_())
