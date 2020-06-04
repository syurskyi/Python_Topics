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


____ ?.?C.. ______ (pS.., pyqtSlot, Q_ARG, QAbstractItemModel,
        QFileInfo, qFuzzyCompare, QMetaObject, QModelIndex, ?O.., __,
        ?T.., ?T.., ?U..)
____ ?.?G.. ______ ?C.., qGray, QImage, QPainter, ?P..
____ ?.?M.. ______ (QAbstractVideoBuffer, ?MC..,
        QMediaMetaData, ?MP.., ?MPl.., QVideoFrame, QVideoProbe)
____ ?.?MW.. ______ QVideoWidget
____ ?.?W.. ______ (?A.., ?CB, ?D.., ?FD..,
        ?FL.., ?HBL.., ?L.., ?LV.., ?MB.., ?PB..,
        ?SP.., ?S.., ?S.., QToolButton, ?VBL.., ?W..)


c_ VideoWidget(QVideoWidget):

    ___  -   parent_None):
        s__(VideoWidget, self). - (parent)

        sSP..(?SP...Ignored, ?SP...Ignored)

        p _ p..
        p.sC..(?P...Window, __.black)
        sP..(p)

        setAttribute(__.WA_OpaquePaintEvent)

    ___ keyPressEvent  event):
        __ event.key() __ __.Key_Escape and isFullScreen
            setFullScreen F..
            event.accept()
        ____ event.key() __ __.Key_Enter and event.modifiers() & __.Key_Alt:
            setFullScreen(no. isFullScreen())
            event.accept()
        ____
            s__(VideoWidget, self).keyPressEvent(event)

    ___ mouseDoubleClickEvent  event):
        setFullScreen(no. isFullScreen())
        event.accept()


c_ PlaylistModel(QAbstractItemModel):

    Title, ColumnCount _ ra..(2)

    ___  -   parent_None):
        s__(PlaylistModel, self). - (parent)

        m_playlist _ N..

    ___ rowCount  parent_QModelIndex()):
        r_ m_playlist.mediaCount() __ m_playlist __ no. N.. and no. parent.iV.. ____ 0

    ___ columnCount  parent_QModelIndex()):
        r_ ColumnCount __ no. parent.iV.. ____ 0

    ___ index  row, column, parent_QModelIndex()):
        r_ createIndex(row, column) __ m_playlist __ no. N.. and no. parent.iV.. and row >_ 0 and row < m_playlist.mediaCount() and column >_ 0 and column < ColumnCount ____ QModelIndex()

    ___ parent  child):
        r_ QModelIndex()

    ___ data  index, role_Qt.DR..):
        __ i...iV.. and role __ __.DR..:
            __ i...column() __ Title:
                location _ m_playlist.media(i...row()).canonicalUrl()
                r_ QFileInfo(location.pa__()).fN..

            r_ m_data[index]

        r_ N..

    ___ playlist
        r_ m_playlist

    ___ sPl..  playlist):
        __ m_playlist __ no. N..:
            m_playlist.mediaAboutToBeInserted.disconnect(
                    beginInsertItems)
            m_playlist.mediaInserted.disconnect(endInsertItems)
            m_playlist.mediaAboutToBeRemoved.disconnect(
                    beginRemoveItems)
            m_playlist.mediaRemoved.disconnect(endRemoveItems)
            m_playlist.mediaChanged.disconnect(changeItems)

        beginResetModel()
        m_playlist _ playlist

        __ m_playlist __ no. N..:
            m_playlist.mediaAboutToBeInserted.c..(
                    beginInsertItems)
            m_playlist.mediaInserted.c..(endInsertItems)
            m_playlist.mediaAboutToBeRemoved.c..(
                    beginRemoveItems)
            m_playlist.mediaRemoved.c..(endRemoveItems)
            m_playlist.mediaChanged.c..(changeItems)

        endResetModel()

    ___ beginInsertItems  start, end):
        beginInsertRows(QModelIndex(), start, end)

    ___ endInsertItems
        endInsertRows()

    ___ beginRemoveItems  start, end):
        beginRemoveRows(QModelIndex(), start, end)

    ___ endRemoveItems
        endRemoveRows()

    ___ changeItems  start, end):
        dataChanged.e..(index(start, 0),
                index(end, ColumnCount))


c_ PlayerControls(?W..):

    play _ pS..()
    pause _ pS..()
    stop _ pS..()
    next _ pS..()
    previous _ pS..()
    changeVolume _ pS..(in.)
    changeMuting _ pS..(bool)
    changeRate _ pS..(fl..)

    ___  -   parent_None):
        s__(PlayerControls, self). - (parent)

        playerState _ ?MP...StoppedState
        playerMuted _ F..

        playButton _ QToolButton(c___self.playClicked)
        playButton.sI..(style().standardIcon(?S...SP_MediaPlay))

        stopButton _ QToolButton(c___self.stop)
        stopButton.sI..(style().standardIcon(?S...SP_MediaStop))
        stopButton.sE.. F..

        nextButton _ QToolButton(c___self.n__)
        nextButton.sI..(
                style().standardIcon(?S...SP_MediaSkipForward))

        previousButton _ QToolButton(c___self.previous)
        previousButton.sI..(
                style().standardIcon(?S...SP_MediaSkipBackward))

        muteButton _ QToolButton(c___self.muteClicked)
        muteButton.sI..(
                style().standardIcon(?S...SP_MediaVolume))

        volumeSlider _ ?S..(__.H..,
                sliderMoved_self.changeVolume)
        volumeSlider.setRange(0, 100)

        rateBox _ ?CB(activated_self.updateRate)
        rateBox.aI..("0.5x", 0.5)
        rateBox.aI..("1.0x", 1.0)
        rateBox.aI..("2.0x", 2.0)
        rateBox.sCI..(1)

        layout _ ?HBL..
        layout.sCM..(0, 0, 0, 0)
        layout.aW..(stopButton)
        layout.aW..(previousButton)
        layout.aW..(playButton)
        layout.aW..(nextButton)
        layout.aW..(muteButton)
        layout.aW..(volumeSlider)
        layout.aW..(rateBox)
        sL..(layout)

    ___ state
        r_ playerState

    ___ setState state):
        __ state !_ playerState:
            playerState _ state

            __ state __ ?MP...StoppedState:
                stopButton.sE.. F..
                playButton.sI..(
                        style().standardIcon(?S...SP_MediaPlay))
            ____ state __ ?MP...PlayingState:
                stopButton.sE..( st.
                playButton.sI..(
                        style().standardIcon(?S...SP_MediaPause))
            ____ state __ ?MP...PausedState:
                stopButton.sE..( st.
                playButton.sI..(
                        style().standardIcon(?S...SP_MediaPlay))

    ___ volume
        r_ volumeSlider.v..

    ___ setVolume  volume):
        volumeSlider.sV..(volume)

    ___ isMuted
        r_ playerMuted

    ___ setMuted  muted):
        __ muted !_ playerMuted:
            playerMuted _ muted

            muteButton.sI..(
                    style().standardIcon(
                            ?S...SP_MediaVolumeMuted __ muted ____ ?S...SP_MediaVolume))

    ___ playClicked
        __ playerState __ (?MP...StoppedState, ?MP...PausedState):
            play.e..()
        ____ playerState __ ?MP...PlayingState:
            pause.e..()

    ___ muteClicked
        changeMuting.e..(no. playerMuted)

    ___ playbackRate
        r_ rateBox.itemData(rateBox.cI..

    ___ setPlaybackRate  rate):
        ___ i __ ra..(rateBox.count()):
            __ qFuzzyCompare(rate, rateBox.itemData(i)):
                rateBox.sCI..(i)
                r_

        rateBox.aI..("%dx" % rate, rate)
        rateBox.sCI..(rateBox.count() - 1)

    ___ updateRate
        changeRate.e..(playbackRate())


c_ FrameProcessor(?O..):

    histogramReady _ pS..(li..)

    @pyqtSlot(QVideoFrame, in.)
    ___ processFrame  frame, levels):
        histogram _ [0.0] * levels

        __ levels and frame.map(QAbstractVideoBuffer.ReadOnly):
            pixelFormat _ frame.pixelFormat()

            __ pixelFormat __ QVideoFrame.Format_YUV420P or pixelFormat __ QVideoFrame.Format_NV12:
                # Process YUV data.
                bits _ frame.bits()
                ___ idx __ ra..(frame.height() * frame.width()):
                    histogram[(bits[idx] * levels) >> 8] +_ 1.0
            ____
                imageFormat _ QVideoFrame.imageFormatFromPixelFormat(pixelFormat)
                __ imageFormat !_ QImage.Format_Invalid:
                    # Process RGB data.
                    image _ QImage(frame.bits(), frame.width(), frame.height(), imageFormat)

                    ___ y __ ra..(image.height()):
                        ___ x __ ra..(image.width()):
                            pixel _ image.pixel(x, y)
                            histogram[(qGray(pixel) * levels) >> 8] +_ 1.0

            # Find the maximum value.
            maxValue _ 0.0
            ___ value __ histogram:
                __ value > maxValue:
                    maxValue _ value

            # Normalise the values between 0 and 1.
            __ maxValue > 0.0:
                ___ i __ ra..(le.(histogram)):
                    histogram[i] /_ maxValue

            frame.unmap()

        histogramReady.e..(histogram)


c_ HistogramWidget(?W..):

    ___  -   parent_None):
        s__(HistogramWidget, self). - (parent)

        m_levels _ 128
        m_isBusy _ F..
        m_histogram _   # list
        m_processor _ FrameProcessor()
        m_processorThread _ ?T..()

        m_processor.moveToThread(m_processorThread)
        m_processor.histogramReady.c..(setHistogram)

    ___ __del__
        m_processorThread.quit()
        m_processorThread.wait(10000)

    ___ setLevels  levels):
        m_levels _ levels

    ___ processFrame  frame):
        __ m_isBusy:
            r_

        m_isBusy _ T..
        QMetaObject.invokeMethod(m_processor, 'processFrame',
                __.QueuedConnection, Q_ARG(QVideoFrame, frame),
                Q_ARG(in., m_levels))

    @pyqtSlot(li..)
    ___ setHistogram  histogram):
        m_isBusy _ F..
        m_histogram _ li..(histogram)
        update()

    ___ paintEvent  event):
        painter _ QPainter

        __ le.(m_histogram) __ 0:
            painter.fillRect(0, 0, width(), height(),
                    ?C...fromRgb(0, 0, 0))
            r_

        barWidth _ width() / fl..(le.(m_histogram))

        ___ i, value __ en..(m_histogram):
            h _ value * height()
            # Draw the level.
            painter.fillRect(barWidth * i, height() - h,
                    barWidth * (i + 1), height(), __.red)
            # Clear the rest of the control.
            painter.fillRect(barWidth * i, 0, barWidth * (i + 1),
                    height() - h, __.black)


c_ Player(?W..):

    fullScreenChanged _ pS..(bool)

    ___  -   playlist, parent_None):
        s__(Player, self). - (parent)

        colorDialog _ N..
        trackInfo _ ""
        statusInfo _ ""
        duration _ 0

        player _ ?MP..
        playlist _ ?MPl..()
        player.sPl..(playlist)

        player.dC...c..(dC..)
        player.pC...c..(pC..)
        player.metaDataChanged.c..(metaDataChanged)
        playlist.currentIndexChanged.c..(playlistPositionChanged)
        player.mediaStatusChanged.c..(statusChanged)
        player.bufferStatusChanged.c..(bufferingProgress)
        player.videoAvailableChanged.c..(videoAvailableChanged)
        player.error.c..(displayErrorMessage)

        videoWidget _ VideoWidget()
        player.setVideoOutput(videoWidget)

        playlistModel _ PlaylistModel()
        playlistModel.sPl..(playlist)

        playlistView _ ?LV..
        playlistView.sM..(playlistModel)
        playlistView.sCI..(
                playlistModel.index(playlist.currentIndex(), 0))

        playlistView.activated.c..(jump)

        slider _ ?S..(__.H..)
        slider.setRange(0, player.duration() / 1000)

        labelDuration _ ?L..
        slider.sliderMoved.c..(seek)

        labelHistogram _ ?L..
        labelHistogram.sT..("Histogram:")
        histogram _ HistogramWidget()
        histogramLayout _ ?HBL..
        histogramLayout.aW..(labelHistogram)
        histogramLayout.aW..(histogram, 1)

        probe _ QVideoProbe()
        probe.videoFrameProbed.c..(histogram.processFrame)
        probe.setSource(player)

        openButton _ ?PB..("Open", c___self.o..)

        controls _ PlayerControls()
        controls.setState(player.state())
        controls.setVolume(player.volume())
        controls.setMuted(controls.isMuted())

        controls.play.c..(player.play)
        controls.pause.c..(player.pause)
        controls.stop.c..(player.stop)
        controls.next.c..(playlist.next)
        controls.previous.c..(previousClicked)
        controls.changeVolume.c..(player.setVolume)
        controls.changeMuting.c..(player.setMuted)
        controls.changeRate.c..(player.setPlaybackRate)
        controls.stop.c..(videoWidget.update)

        player.stateChanged.c..(controls.setState)
        player.volumeChanged.c..(controls.setVolume)
        player.mutedChanged.c..(controls.setMuted)

        fullScreenButton _ ?PB..("FullScreen")
        fullScreenButton.setCheckable( st.

        colorButton _ ?PB..("Color Options...")
        colorButton.sE.. F..
        colorButton.c__.c..(showColorDialog)

        displayLayout _ ?HBL..
        displayLayout.aW..(videoWidget, 2)
        displayLayout.aW..(playlistView)

        controlLayout _ ?HBL..
        controlLayout.sCM..(0, 0, 0, 0)
        controlLayout.aW..(openButton)
        controlLayout.addStretch(1)
        controlLayout.aW..(controls)
        controlLayout.addStretch(1)
        controlLayout.aW..(fullScreenButton)
        controlLayout.aW..(colorButton)

        layout _ ?VBL..
        layout.aL..(displayLayout)
        hLayout _ ?HBL..
        hLayout.aW..(slider)
        hLayout.aW..(labelDuration)
        layout.aL..(hLayout)
        layout.aL..(controlLayout)
        layout.aL..(histogramLayout)

        sL..(layout)

        __ no. player.isAvailable
            ?MB...w..  "Service not available",
                    "The QMediaPlayer object does not have a valid service.\n"
                    "Please check the media service plugins are installed.")

            controls.sE.. F..
            playlistView.sE.. F..
            openButton.sE.. F..
            colorButton.sE.. F..
            fullScreenButton.sE.. F..

        metaDataChanged()

        addToPlaylist(playlist)

    ___ o..
        fileNames, _ _ ?FD...getOpenFileNames  "Open Files")
        addToPlaylist(fileNames)

    ___ addToPlaylist  fileNames):
        ___ name __ fileNames:
            fileInfo _ QFileInfo(name)
            __ fileInfo.e..
                url _ ?U...fLF..(fileInfo.absoluteFilePath())
                __ fileInfo.suffix().lower() __ 'm3u':
                    playlist.load(url)
                ____
                    playlist.aM..(?MC..(url))
            ____
                url _ ?U..(name)
                __ url.isValid
                    playlist.aM..(?MC..(url))

    ___ dC..  duration):
        duration /_ 1000

        duration _ duration
        slider.sM..(duration)

    ___ pC..  progress):
        progress /_ 1000

        __ no. slider.isSliderDown
            slider.sV..(progress)

        updateDurationInfo(progress)

    ___ metaDataChanged
        __ player.isMetaDataAvailable
            setTrackInfo("%s - %s" % (
                    player.metaData(QMediaMetaData.AlbumArtist),
                    player.metaData(QMediaMetaData.Title)))

    ___ previousClicked
        # Go to the previous track if we are within the first 5 seconds of
        # playback.  Otherwise, seek to the beginning.
        __ player.position() <_ 5000:
            playlist.previous()
        ____
            player.setPosition(0)

    ___ jump  index):
        __ i...isValid
            playlist.sCI..(i...row())
            player.play()

    ___ playlistPositionChanged  position):
        playlistView.sCI..(
                playlistModel.i..(position, 0))

    ___ seek  seconds):
        player.setPosition(seconds * 1000)

    ___ statusChanged  status):
        handleCursor(status)

        __ status __ ?MP...LoadingMedia:
            setStatusInfo("Loading...")
        ____ status __ ?MP...StalledMedia:
            setStatusInfo("Media Stalled")
        ____ status __ ?MP...EndOfMedia:
            ?A...alert
        ____ status __ ?MP...InvalidMedia:
            displayErrorMessage()
        ____
            setStatusInfo("")

    ___ handleCursor  status):
        __ status __ (?MP...LoadingMedia, ?MP...BufferingMedia, ?MP...StalledMedia):
            setCursor(__.BusyCursor)
        ____
            unsetCursor()

    ___ bufferingProgress  progress):
        setStatusInfo("Buffering %d%" % progress)

    ___ videoAvailableChanged  available):
        __ available:
            fullScreenButton.c__.c..(
                    videoWidget.setFullScreen)
            videoWidget.fullScreenChanged.c..(
                    fullScreenButton.sC__)

            __ fullScreenButton.isChecked
                videoWidget.setFullScreen( st.
        ____
            fullScreenButton.c__.disconnect(
                    videoWidget.setFullScreen)
            videoWidget.fullScreenChanged.disconnect(
                    fullScreenButton.sC__)

            videoWidget.setFullScreen F..

        colorButton.sE..(available)

    ___ setTrackInfo  info):
        trackInfo _ info

        __ statusInfo !_ "":
            sWT..("%s | %s" % (trackInfo, statusInfo))
        ____
            sWT..(trackInfo)

    ___ setStatusInfo  info):
        statusInfo _ info

        __ statusInfo !_ "":
            sWT..("%s | %s" % (trackInfo, statusInfo))
        ____
            sWT..(trackInfo)

    ___ displayErrorMessage
        setStatusInfo(player.errorString())

    ___ updateDurationInfo  currentInfo):
        duration _ duration
        __ currentInfo or duration:
            currentTime _ ?T..((currentInfo/3600)%60, (currentInfo/60)%60,
                    currentInfo%60, (currentInfo*1000)%1000)
            totalTime _ ?T..((duration/3600)%60, (duration/60)%60,
                    duration%60, (duration*1000)%1000);

            f.. _ 'hh:mm:ss' __ duration > 3600 ____ 'mm:ss'
            tStr _ currentTime.toString(f..) + " / " + totalTime.toString(f..)
        ____
            tStr _ ""

        labelDuration.sT..(tStr)

    ___ showColorDialog
        __ colorDialog __ N..:
            brightnessSlider _ ?S..(__.H..)
            brightnessSlider.setRange(-100, 100)
            brightnessSlider.sV..(videoWidget.brightness())
            brightnessSlider.sliderMoved.c..(
                    videoWidget.setBrightness)
            videoWidget.brightnessChanged.c..(
                    brightnessSlider.sV..)

            contrastSlider _ ?S..(__.H..)
            contrastSlider.setRange(-100, 100)
            contrastSlider.sV..(videoWidget.contrast())
            contrastSlider.sliderMoved.c..(videoWidget.setContrast)
            videoWidget.contrastChanged.c..(contrastSlider.sV..)

            hueSlider _ ?S..(__.H..)
            hueSlider.setRange(-100, 100)
            hueSlider.sV..(videoWidget.hue())
            hueSlider.sliderMoved.c..(videoWidget.setHue)
            videoWidget.hueChanged.c..(hueSlider.sV..)

            saturationSlider _ ?S..(__.H..)
            saturationSlider.setRange(-100, 100)
            saturationSlider.sV..(videoWidget.saturation())
            saturationSlider.sliderMoved.c..(
                    videoWidget.setSaturation)
            videoWidget.saturationChanged.c..(
                    saturationSlider.sV..)

            layout _ ?FL..
            layout.aR..("Brightness", brightnessSlider)
            layout.aR..("Contrast", contrastSlider)
            layout.aR..("Hue", hueSlider)
            layout.aR..("Saturation", saturationSlider)

            button _ ?PB..("Close")
            layout.aR..(button)

            colorDialog _ ?D..
            colorDialog.sWT..("Color Options")
            colorDialog.sL..(layout)

            button.c__.c..(colorDialog.close)

        colorDialog.s..


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    player _ Player(___.argv[1:])
    player.s..

    ___.e.. ?.e..
