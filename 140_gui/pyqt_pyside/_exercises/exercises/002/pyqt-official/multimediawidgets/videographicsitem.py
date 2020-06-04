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


____ ?.?C.. ______ ?D.., ?S.., QSizeF, __, ?U..
____ ?.?G.. ______ QTransform
____ ?.?M.. ______ ?MC.., ?MP..
____ ?.?MW.. ______ QGraphicsVideoItem
____ ?.?W.. ______ (?A.., ?FD.., QGraphicsScene,
        QGraphicsView, ?HBL.., ?PB.., ?S.., ?S.., ?VBL..,
        ?W..)


c_ VideoPlayer(?W..):

    ___  -   parent_None):
        s__(VideoPlayer, self). - (parent)

        mediaPlayer _ ?MP..(N.., ?MP...VideoSurface)

        videoItem _ QGraphicsVideoItem()
        videoItem.setSize(QSizeF(640, 480))

        scene _ QGraphicsScene
        graphicsView _ QGraphicsView(scene)

        scene.aI..(videoItem)

        rotateSlider _ ?S..(__.H..)
        rotateSlider.setRange(-180,  180)
        rotateSlider.sV..(0)
        rotateSlider.valueChanged.c..(rotateVideo)

        openButton _ ?PB..("Open...")
        openButton.c__.c..(openFile)

        playButton _ ?PB..()
        playButton.sE.. F..
        playButton.sI..(style().standardIcon(?S...SP_MediaPlay))
        playButton.c__.c..(play)

        positionSlider _ ?S..(__.H..)
        positionSlider.setRange(0, 0)
        positionSlider.sliderMoved.c..(setPosition)

        controlLayout _ ?HBL..
        controlLayout.sCM..(0, 0, 0, 0)
        controlLayout.aW..(openButton)
        controlLayout.aW..(playButton)
        controlLayout.aW..(positionSlider)

        layout _ ?VBL..
        layout.aW..(graphicsView)
        layout.aW..(rotateSlider)
        layout.aL..(controlLayout)

        sL..(layout)

        mediaPlayer.setVideoOutput(videoItem)
        mediaPlayer.stateChanged.c..(mediaStateChanged)
        mediaPlayer.pC...c..(pC..)
        mediaPlayer.dC...c..(dC..)

    ___ sH..
        r_ ?S..(800, 600)

    ___ openFile
        fileName, _ _ ?FD...gOFN..  "Open Movie",
                ?D...homePath())

        __ fileName !_ '':
            mediaPlayer.sM..(
                    ?MC..(?U...fLF..(fileName)))
            playButton.sE..( st.

    ___ play
        __ mediaPlayer.s.. __ ?MP...PlayingState:
            mediaPlayer.pause()
        ____
            mediaPlayer.play()

    ___ mediaStateChanged  state):
        __ mediaPlayer.s.. __ ?MP...PlayingState:
            playButton.sI..(
                    style().standardIcon(?S...SP_MediaPause))
        ____
            playButton.sI..(
                    style().standardIcon(?S...SP_MediaPlay))

    ___ pC..  position):
        positionSlider.sV..(position)

    ___ dC..  duration):
        positionSlider.setRange(0, duration)

    ___ setPosition  position):
        mediaPlayer.setPosition(position)

    ___ rotateVideo  angle):
        x _ videoItem.boundingRect().width() / 2.0
        y _ videoItem.boundingRect().height() / 2.0

        videoItem.setTransform(
                QTransform().translate(x, y).rotate(angle).translate(-x, -y))


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    player _ VideoPlayer()
    player.s..

    ___.e.. ?.e..
