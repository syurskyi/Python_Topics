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


____ ?.?C.. ______ (pyqtSignal, pyqtSlot, Q_ARG, QAbstractItemModel,
        QFileInfo, qFuzzyCompare, QMetaObject, QModelIndex, QObject, __,
        QThread, QTime, QUrl)
____ ?.?G.. ______ ?C.., qGray, QImage, QPainter, ?P..
____ ?.QtMultimedia ______ (QAbstractVideoBuffer, QMediaContent,
        QMediaMetaData, QMediaPlayer, QMediaPlaylist, QVideoFrame, QVideoProbe)
____ ?.QtMultimediaWidgets ______ QVideoWidget
____ ?.?W.. ______ (?A.., QComboBox, QDialog, ?FD..,
        QFormLayout, QHBoxLayout, QLabel, QListView, ?MB.., ?PB..,
        QSizePolicy, QSlider, QStyle, QToolButton, QVBoxLayout, QWidget)


c_ VideoWidget(QVideoWidget):

    ___  -   parent_None):
        super(VideoWidget, self). - (parent)

        sSP..(QSizePolicy.Ignored, QSizePolicy.Ignored)

        p _ palette()
        p.sC..(?P...Window, __.black)
        sP..(p)

        setAttribute(__.WA_OpaquePaintEvent)

    ___ keyPressEvent  event):
        __ event.key() == __.Key_Escape and isFullScreen
            setFullScreen F..
            event.accept()
        ____ event.key() == __.Key_Enter and event.modifiers() & __.Key_Alt:
            setFullScreen(no. isFullScreen())
            event.accept()
        ____
            super(VideoWidget, self).keyPressEvent(event)

    ___ mouseDoubleClickEvent  event):
        setFullScreen(no. isFullScreen())
        event.accept()


c_ PlaylistModel(QAbstractItemModel):

    Title, ColumnCount _ range(2)

    ___  -   parent_None):
        super(PlaylistModel, self). - (parent)

        m_playlist _ N..

    ___ rowCount  parent_QModelIndex()):
        r_ m_playlist.mediaCount() __ m_playlist __ no. N.. and no. parent.isValid() else 0

    ___ columnCount  parent_QModelIndex()):
        r_ ColumnCount __ no. parent.isValid() else 0

    ___ index  row, column, parent_QModelIndex()):
        r_ createIndex(row, column) __ m_playlist __ no. N.. and no. parent.isValid() and row >_ 0 and row < m_playlist.mediaCount() and column >_ 0 and column < ColumnCount else QModelIndex()

    ___ parent  child):
        r_ QModelIndex()

    ___ data  index, role_Qt.DisplayRole):
        __ index.isValid() and role == __.DisplayRole:
            __ index.column() == Title:
                location _ m_playlist.media(index.row()).canonicalUrl()
                r_ QFileInfo(location.path()).fileName()

            r_ m_data[index]

        r_ N..

    ___ playlist
        r_ m_playlist

    ___ setPlaylist  playlist):
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
        dataChanged.emit(index(start, 0),
                index(end, ColumnCount))


c_ PlayerControls(QWidget):

    play _ pyqtSignal()
    pause _ pyqtSignal()
    stop _ pyqtSignal()
    next _ pyqtSignal()
    previous _ pyqtSignal()
    changeVolume _ pyqtSignal(int)
    changeMuting _ pyqtSignal(bool)
    changeRate _ pyqtSignal(float)

    ___  -   parent_None):
        super(PlayerControls, self). - (parent)

        playerState _ QMediaPlayer.StoppedState
        playerMuted _ False

        playButton _ QToolButton(c___self.playClicked)
        playButton.setIcon(style().standardIcon(QStyle.SP_MediaPlay))

        stopButton _ QToolButton(c___self.stop)
        stopButton.setIcon(style().standardIcon(QStyle.SP_MediaStop))
        stopButton.sE.. F..

        nextButton _ QToolButton(c___self.next)
        nextButton.setIcon(
                style().standardIcon(QStyle.SP_MediaSkipForward))

        previousButton _ QToolButton(c___self.previous)
        previousButton.setIcon(
                style().standardIcon(QStyle.SP_MediaSkipBackward))

        muteButton _ QToolButton(c___self.muteClicked)
        muteButton.setIcon(
                style().standardIcon(QStyle.SP_MediaVolume))

        volumeSlider _ QSlider(__.Horizontal,
                sliderMoved_self.changeVolume)
        volumeSlider.setRange(0, 100)

        rateBox _ QComboBox(activated_self.updateRate)
        rateBox.addItem("0.5x", 0.5)
        rateBox.addItem("1.0x", 1.0)
        rateBox.addItem("2.0x", 2.0)
        rateBox.setCurrentIndex(1)

        layout _ QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
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

            __ state == QMediaPlayer.StoppedState:
                stopButton.sE.. F..
                playButton.setIcon(
                        style().standardIcon(QStyle.SP_MediaPlay))
            ____ state == QMediaPlayer.PlayingState:
                stopButton.sE..(True)
                playButton.setIcon(
                        style().standardIcon(QStyle.SP_MediaPause))
            ____ state == QMediaPlayer.PausedState:
                stopButton.sE..(True)
                playButton.setIcon(
                        style().standardIcon(QStyle.SP_MediaPlay))

    ___ volume
        r_ volumeSlider.value()

    ___ setVolume  volume):
        volumeSlider.setValue(volume)

    ___ isMuted
        r_ playerMuted

    ___ setMuted  muted):
        __ muted !_ playerMuted:
            playerMuted _ muted

            muteButton.setIcon(
                    style().standardIcon(
                            QStyle.SP_MediaVolumeMuted __ muted else QStyle.SP_MediaVolume))

    ___ playClicked
        __ playerState __ (QMediaPlayer.StoppedState, QMediaPlayer.PausedState):
            play.emit()
        ____ playerState == QMediaPlayer.PlayingState:
            pause.emit()

    ___ muteClicked
        changeMuting.emit(no. playerMuted)

    ___ playbackRate
        r_ rateBox.itemData(rateBox.currentIndex())

    ___ setPlaybackRate  rate):
        ___ i __ range(rateBox.count()):
            __ qFuzzyCompare(rate, rateBox.itemData(i)):
                rateBox.setCurrentIndex(i)
                r_

        rateBox.addItem("%dx" % rate, rate)
        rateBox.setCurrentIndex(rateBox.count() - 1)

    ___ updateRate
        changeRate.emit(playbackRate())


c_ FrameProcessor(QObject):

    histogramReady _ pyqtSignal(list)

    @pyqtSlot(QVideoFrame, int)
    ___ processFrame  frame, levels):
        histogram _ [0.0] * levels

        __ levels and frame.map(QAbstractVideoBuffer.ReadOnly):
            pixelFormat _ frame.pixelFormat()

            __ pixelFormat == QVideoFrame.Format_YUV420P or pixelFormat == QVideoFrame.Format_NV12:
                # Process YUV data.
                bits _ frame.bits()
                ___ idx __ range(frame.height() * frame.width()):
                    histogram[(bits[idx] * levels) >> 8] +_ 1.0
            ____
                imageFormat _ QVideoFrame.imageFormatFromPixelFormat(pixelFormat)
                __ imageFormat !_ QImage.Format_Invalid:
                    # Process RGB data.
                    image _ QImage(frame.bits(), frame.width(), frame.height(), imageFormat)

                    ___ y __ range(image.height()):
                        ___ x __ range(image.width()):
                            pixel _ image.pixel(x, y)
                            histogram[(qGray(pixel) * levels) >> 8] +_ 1.0

            # Find the maximum value.
            maxValue _ 0.0
            ___ value __ histogram:
                __ value > maxValue:
                    maxValue _ value

            # Normalise the values between 0 and 1.
            __ maxValue > 0.0:
                ___ i __ range(le.(histogram)):
                    histogram[i] /_ maxValue

            frame.unmap()

        histogramReady.emit(histogram)


c_ HistogramWidget(QWidget):

    ___  -   parent_None):
        super(HistogramWidget, self). - (parent)

        m_levels _ 128
        m_isBusy _ False
        m_histogram _   # list
        m_processor _ FrameProcessor()
        m_processorThread _ QThread()

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

        m_isBusy _ True
        QMetaObject.invokeMethod(m_processor, 'processFrame',
                __.QueuedConnection, Q_ARG(QVideoFrame, frame),
                Q_ARG(int, m_levels))

    @pyqtSlot(list)
    ___ setHistogram  histogram):
        m_isBusy _ False
        m_histogram _ list(histogram)
        update()

    ___ paintEvent  event):
        painter _ QPainter

        __ le.(m_histogram) == 0:
            painter.fillRect(0, 0, width(), height(),
                    ?C...fromRgb(0, 0, 0))
            r_

        barWidth _ width() / float(le.(m_histogram))

        ___ i, value __ en..(m_histogram):
            h _ value * height()
            # Draw the level.
            painter.fillRect(barWidth * i, height() - h,
                    barWidth * (i + 1), height(), __.red)
            # Clear the rest of the control.
            painter.fillRect(barWidth * i, 0, barWidth * (i + 1),
                    height() - h, __.black)


c_ Player(QWidget):

    fullScreenChanged _ pyqtSignal(bool)

    ___  -   playlist, parent_None):
        super(Player, self). - (parent)

        colorDialog _ N..
        trackInfo _ ""
        statusInfo _ ""
        duration _ 0

        player _ QMediaPlayer()
        playlist _ QMediaPlaylist()
        player.setPlaylist(playlist)

        player.durationChanged.c..(durationChanged)
        player.positionChanged.c..(positionChanged)
        player.metaDataChanged.c..(metaDataChanged)
        playlist.currentIndexChanged.c..(playlistPositionChanged)
        player.mediaStatusChanged.c..(statusChanged)
        player.bufferStatusChanged.c..(bufferingProgress)
        player.videoAvailableChanged.c..(videoAvailableChanged)
        player.error.c..(displayErrorMessage)

        videoWidget _ VideoWidget()
        player.setVideoOutput(videoWidget)

        playlistModel _ PlaylistModel()
        playlistModel.setPlaylist(playlist)

        playlistView _ QListView()
        playlistView.sM..(playlistModel)
        playlistView.setCurrentIndex(
                playlistModel.index(playlist.currentIndex(), 0))

        playlistView.activated.c..(jump)

        slider _ QSlider(__.Horizontal)
        slider.setRange(0, player.duration() / 1000)

        labelDuration _ QLabel()
        slider.sliderMoved.c..(seek)

        labelHistogram _ QLabel()
        labelHistogram.sT..("Histogram:")
        histogram _ HistogramWidget()
        histogramLayout _ QHBoxLayout()
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
        fullScreenButton.setCheckable(True)

        colorButton _ ?PB..("Color Options...")
        colorButton.sE.. F..
        colorButton.c__.c..(showColorDialog)

        displayLayout _ QHBoxLayout()
        displayLayout.aW..(videoWidget, 2)
        displayLayout.aW..(playlistView)

        controlLayout _ QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.aW..(openButton)
        controlLayout.addStretch(1)
        controlLayout.aW..(controls)
        controlLayout.addStretch(1)
        controlLayout.aW..(fullScreenButton)
        controlLayout.aW..(colorButton)

        layout _ ?VBL..
        layout.aL..(displayLayout)
        hLayout _ QHBoxLayout()
        hLayout.aW..(slider)
        hLayout.aW..(labelDuration)
        layout.aL..(hLayout)
        layout.aL..(controlLayout)
        layout.aL..(histogramLayout)

        sL..(layout)

        __ no. player.isAvailable
            ?MB...warning  "Service not available",
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
            __ fileInfo.exists
                url _ QUrl.fromLocalFile(fileInfo.absoluteFilePath())
                __ fileInfo.suffix().lower() == 'm3u':
                    playlist.load(url)
                ____
                    playlist.addMedia(QMediaContent(url))
            ____
                url _ QUrl(name)
                __ url.isValid
                    playlist.addMedia(QMediaContent(url))

    ___ durationChanged  duration):
        duration /_ 1000

        duration _ duration
        slider.setMaximum(duration)

    ___ positionChanged  progress):
        progress /_ 1000

        __ no. slider.isSliderDown
            slider.setValue(progress)

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
        __ index.isValid
            playlist.setCurrentIndex(index.row())
            player.play()

    ___ playlistPositionChanged  position):
        playlistView.setCurrentIndex(
                playlistModel.index(position, 0))

    ___ seek  seconds):
        player.setPosition(seconds * 1000)

    ___ statusChanged  status):
        handleCursor(status)

        __ status == QMediaPlayer.LoadingMedia:
            setStatusInfo("Loading...")
        ____ status == QMediaPlayer.StalledMedia:
            setStatusInfo("Media Stalled")
        ____ status == QMediaPlayer.EndOfMedia:
            ?A...alert
        ____ status == QMediaPlayer.InvalidMedia:
            displayErrorMessage()
        ____
            setStatusInfo("")

    ___ handleCursor  status):
        __ status __ (QMediaPlayer.LoadingMedia, QMediaPlayer.BufferingMedia, QMediaPlayer.StalledMedia):
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
                    fullScreenButton.setChecked)

            __ fullScreenButton.isChecked
                videoWidget.setFullScreen(True)
        ____
            fullScreenButton.c__.disconnect(
                    videoWidget.setFullScreen)
            videoWidget.fullScreenChanged.disconnect(
                    fullScreenButton.setChecked)

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
            currentTime _ QTime((currentInfo/3600)%60, (currentInfo/60)%60,
                    currentInfo%60, (currentInfo*1000)%1000)
            totalTime _ QTime((duration/3600)%60, (duration/60)%60,
                    duration%60, (duration*1000)%1000);

            format _ 'hh:mm:ss' __ duration > 3600 else 'mm:ss'
            tStr _ currentTime.toString(format) + " / " + totalTime.toString(format)
        ____
            tStr _ ""

        labelDuration.sT..(tStr)

    ___ showColorDialog
        __ colorDialog __ N..:
            brightnessSlider _ QSlider(__.Horizontal)
            brightnessSlider.setRange(-100, 100)
            brightnessSlider.setValue(videoWidget.brightness())
            brightnessSlider.sliderMoved.c..(
                    videoWidget.setBrightness)
            videoWidget.brightnessChanged.c..(
                    brightnessSlider.setValue)

            contrastSlider _ QSlider(__.Horizontal)
            contrastSlider.setRange(-100, 100)
            contrastSlider.setValue(videoWidget.contrast())
            contrastSlider.sliderMoved.c..(videoWidget.setContrast)
            videoWidget.contrastChanged.c..(contrastSlider.setValue)

            hueSlider _ QSlider(__.Horizontal)
            hueSlider.setRange(-100, 100)
            hueSlider.setValue(videoWidget.hue())
            hueSlider.sliderMoved.c..(videoWidget.setHue)
            videoWidget.hueChanged.c..(hueSlider.setValue)

            saturationSlider _ QSlider(__.Horizontal)
            saturationSlider.setRange(-100, 100)
            saturationSlider.setValue(videoWidget.saturation())
            saturationSlider.sliderMoved.c..(
                    videoWidget.setSaturation)
            videoWidget.saturationChanged.c..(
                    saturationSlider.setValue)

            layout _ QFormLayout()
            layout.addRow("Brightness", brightnessSlider)
            layout.addRow("Contrast", contrastSlider)
            layout.addRow("Hue", hueSlider)
            layout.addRow("Saturation", saturationSlider)

            button _ ?PB..("Close")
            layout.addRow(button)

            colorDialog _ QDialog
            colorDialog.sWT..("Color Options")
            colorDialog.sL..(layout)

            button.c__.c..(colorDialog.close)

        colorDialog.s..


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    player _ Player(___.argv[1:])
    player.s..

    ___.e..(app.exec_())
