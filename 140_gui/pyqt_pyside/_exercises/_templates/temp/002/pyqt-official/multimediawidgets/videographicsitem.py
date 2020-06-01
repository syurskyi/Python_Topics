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


____ ?.QtCore ______ QDir, QSize, QSizeF, Qt, QUrl
____ ?.QtGui ______ QTransform
____ ?.QtMultimedia ______ QMediaContent, QMediaPlayer
____ ?.QtMultimediaWidgets ______ QGraphicsVideoItem
____ ?.?W.. ______ (QApplication, QFileDialog, QGraphicsScene,
        QGraphicsView, QHBoxLayout, ?PB.., QSlider, QStyle, QVBoxLayout,
        QWidget)


class VideoPlayer(QWidget):

    ___ __init__(self, parent_None):
        super(VideoPlayer, self).__init__(parent)

        self.mediaPlayer _ QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.videoItem _ QGraphicsVideoItem()
        self.videoItem.setSize(QSizeF(640, 480))

        scene _ QGraphicsScene(self)
        graphicsView _ QGraphicsView(scene)

        scene.addItem(self.videoItem)

        rotateSlider _ QSlider(Qt.Horizontal)
        rotateSlider.setRange(-180,  180)
        rotateSlider.setValue(0)
        rotateSlider.valueChanged.c..(self.rotateVideo)

        openButton _ ?PB..("Open...")
        openButton.c__.c..(self.openFile)

        self.playButton _ ?PB..()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.c__.c..(self.play)

        self.positionSlider _ QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.c..(self.setPosition)

        controlLayout _ QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout _ QVBoxLayout()
        layout.addWidget(graphicsView)
        layout.addWidget(rotateSlider)
        layout.addLayout(controlLayout)

        self.setLayout(layout)

        self.mediaPlayer.setVideoOutput(self.videoItem)
        self.mediaPlayer.stateChanged.c..(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.c..(self.positionChanged)
        self.mediaPlayer.durationChanged.c..(self.durationChanged)

    ___ sizeHint(self):
        return QSize(800, 600)

    ___ openFile(self):
        fileName, _ _ QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())

        if fileName !_ '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    ___ play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    ___ mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    ___ positionChanged(self, position):
        self.positionSlider.setValue(position)

    ___ durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    ___ setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    ___ rotateVideo(self, angle):
        x _ self.videoItem.boundingRect().width() / 2.0
        y _ self.videoItem.boundingRect().height() / 2.0

        self.videoItem.setTransform(
                QTransform().translate(x, y).rotate(angle).translate(-x, -y))


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)

    player _ VideoPlayer()
    player.s..

    sys.exit(app.exec_())
