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


____ ?.QtCore ______ (pyqtSignal, pyqtSlot, Q_ARG, QAbstractItemModel,
        QFileInfo, qFuzzyCompare, QMetaObject, QModelIndex, QObject, Qt,
        QThread, QTime, QUrl)
____ ?.?G.. ______ QColor, qGray, QImage, QPainter, QPalette
____ ?.QtMultimedia ______ (QAbstractVideoBuffer, QMediaContent,
        QMediaMetaData, QMediaPlayer, QMediaPlaylist, QVideoFrame, QVideoProbe)
____ ?.QtMultimediaWidgets ______ QVideoWidget
____ ?.?W.. ______ (?A.., QComboBox, QDialog, ?FD..,
        QFormLayout, QHBoxLayout, QLabel, QListView, ?MB.., ?PB..,
        QSizePolicy, QSlider, QStyle, QToolButton, QVBoxLayout, QWidget)


c_ VideoWidget(QVideoWidget):

    ___ __init__  parent_None):
        super(VideoWidget, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        p _ self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.setAttribute(Qt.WA_OpaquePaintEvent)

    ___ keyPressEvent  event):
        __ event.key() == Qt.Key_Escape and self.isFullScreen
            self.setFullScreen F..
            event.accept()
        ____ event.key() == Qt.Key_Enter and event.modifiers() & Qt.Key_Alt:
            self.setFullScreen(no. self.isFullScreen())
            event.accept()
        ____
            super(VideoWidget, self).keyPressEvent(event)

    ___ mouseDoubleClickEvent  event):
        self.setFullScreen(no. self.isFullScreen())
        event.accept()


c_ PlaylistModel(QAbstractItemModel):

    Title, ColumnCount _ range(2)

    ___ __init__  parent_None):
        super(PlaylistModel, self).__init__(parent)

        self.m_playlist _ N..

    ___ rowCount  parent_QModelIndex()):
        r_ self.m_playlist.mediaCount() __ self.m_playlist __ no. N.. and no. parent.isValid() else 0

    ___ columnCount  parent_QModelIndex()):
        r_ self.ColumnCount __ no. parent.isValid() else 0

    ___ index  row, column, parent_QModelIndex()):
        r_ self.createIndex(row, column) __ self.m_playlist __ no. N.. and no. parent.isValid() and row >_ 0 and row < self.m_playlist.mediaCount() and column >_ 0 and column < self.ColumnCount else QModelIndex()

    ___ parent  child):
        r_ QModelIndex()

    ___ data  index, role_Qt.DisplayRole):
        __ index.isValid() and role == Qt.DisplayRole:
            __ index.column() == self.Title:
                location _ self.m_playlist.media(index.row()).canonicalUrl()
                r_ QFileInfo(location.path()).fileName()

            r_ self.m_data[index]

        r_ N..

    ___ playlist(self):
        r_ self.m_playlist

    ___ setPlaylist  playlist):
        __ self.m_playlist __ no. N..:
            self.m_playlist.mediaAboutToBeInserted.disconnect(
                    self.beginInsertItems)
            self.m_playlist.mediaInserted.disconnect(self.endInsertItems)
            self.m_playlist.mediaAboutToBeRemoved.disconnect(
                    self.beginRemoveItems)
            self.m_playlist.mediaRemoved.disconnect(self.endRemoveItems)
            self.m_playlist.mediaChanged.disconnect(self.changeItems)

        self.beginResetModel()
        self.m_playlist _ playlist

        __ self.m_playlist __ no. N..:
            self.m_playlist.mediaAboutToBeInserted.c..(
                    self.beginInsertItems)
            self.m_playlist.mediaInserted.c..(self.endInsertItems)
            self.m_playlist.mediaAboutToBeRemoved.c..(
                    self.beginRemoveItems)
            self.m_playlist.mediaRemoved.c..(self.endRemoveItems)
            self.m_playlist.mediaChanged.c..(self.changeItems)

        self.endResetModel()

    ___ beginInsertItems  start, end):
        self.beginInsertRows(QModelIndex(), start, end)

    ___ endInsertItems(self):
        self.endInsertRows()

    ___ beginRemoveItems  start, end):
        self.beginRemoveRows(QModelIndex(), start, end)

    ___ endRemoveItems(self):
        self.endRemoveRows()

    ___ changeItems  start, end):
        self.dataChanged.emit(self.index(start, 0),
                self.index(end, self.ColumnCount))


c_ PlayerControls(QWidget):

    play _ pyqtSignal()
    pause _ pyqtSignal()
    stop _ pyqtSignal()
    next _ pyqtSignal()
    previous _ pyqtSignal()
    changeVolume _ pyqtSignal(int)
    changeMuting _ pyqtSignal(bool)
    changeRate _ pyqtSignal(float)

    ___ __init__  parent_None):
        super(PlayerControls, self).__init__(parent)

        self.playerState _ QMediaPlayer.StoppedState
        self.playerMuted _ False

        self.playButton _ QToolButton(c___self.playClicked)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        self.stopButton _ QToolButton(c___self.stop)
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopButton.setEnabled F..

        self.nextButton _ QToolButton(c___self.next)
        self.nextButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaSkipForward))

        self.previousButton _ QToolButton(c___self.previous)
        self.previousButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaSkipBackward))

        self.muteButton _ QToolButton(c___self.muteClicked)
        self.muteButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaVolume))

        self.volumeSlider _ QSlider(Qt.Horizontal,
                sliderMoved_self.changeVolume)
        self.volumeSlider.setRange(0, 100)

        self.rateBox _ QComboBox(activated_self.updateRate)
        self.rateBox.addItem("0.5x", 0.5)
        self.rateBox.addItem("1.0x", 1.0)
        self.rateBox.addItem("2.0x", 2.0)
        self.rateBox.setCurrentIndex(1)

        layout _ QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.stopButton)
        layout.addWidget(self.previousButton)
        layout.addWidget(self.playButton)
        layout.addWidget(self.nextButton)
        layout.addWidget(self.muteButton)
        layout.addWidget(self.volumeSlider)
        layout.addWidget(self.rateBox)
        self.setLayout(layout)

    ___ state(self):
        r_ self.playerState

    ___ setState state):
        __ state !_ self.playerState:
            self.playerState _ state

            __ state == QMediaPlayer.StoppedState:
                self.stopButton.setEnabled F..
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))
            ____ state == QMediaPlayer.PlayingState:
                self.stopButton.setEnabled(True)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPause))
            ____ state == QMediaPlayer.PausedState:
                self.stopButton.setEnabled(True)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))

    ___ volume(self):
        r_ self.volumeSlider.value()

    ___ setVolume  volume):
        self.volumeSlider.setValue(volume)

    ___ isMuted(self):
        r_ self.playerMuted

    ___ setMuted  muted):
        __ muted !_ self.playerMuted:
            self.playerMuted _ muted

            self.muteButton.setIcon(
                    self.style().standardIcon(
                            QStyle.SP_MediaVolumeMuted __ muted else QStyle.SP_MediaVolume))

    ___ playClicked(self):
        __ self.playerState in (QMediaPlayer.StoppedState, QMediaPlayer.PausedState):
            self.play.emit()
        ____ self.playerState == QMediaPlayer.PlayingState:
            self.pause.emit()

    ___ muteClicked(self):
        self.changeMuting.emit(no. self.playerMuted)

    ___ playbackRate(self):
        r_ self.rateBox.itemData(self.rateBox.currentIndex())

    ___ setPlaybackRate  rate):
        for i in range(self.rateBox.count()):
            __ qFuzzyCompare(rate, self.rateBox.itemData(i)):
                self.rateBox.setCurrentIndex(i)
                r_

        self.rateBox.addItem("%dx" % rate, rate)
        self.rateBox.setCurrentIndex(self.rateBox.count() - 1)

    ___ updateRate(self):
        self.changeRate.emit(self.playbackRate())


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
                for idx in range(frame.height() * frame.width()):
                    histogram[(bits[idx] * levels) >> 8] +_ 1.0
            ____
                imageFormat _ QVideoFrame.imageFormatFromPixelFormat(pixelFormat)
                __ imageFormat !_ QImage.Format_Invalid:
                    # Process RGB data.
                    image _ QImage(frame.bits(), frame.width(), frame.height(), imageFormat)

                    for y in range(image.height()):
                        for x in range(image.width()):
                            pixel _ image.pixel(x, y)
                            histogram[(qGray(pixel) * levels) >> 8] +_ 1.0

            # Find the maximum value.
            maxValue _ 0.0
            for value in histogram:
                __ value > maxValue:
                    maxValue _ value

            # Normalise the values between 0 and 1.
            __ maxValue > 0.0:
                for i in range(len(histogram)):
                    histogram[i] /_ maxValue

            frame.unmap()

        self.histogramReady.emit(histogram)


c_ HistogramWidget(QWidget):

    ___ __init__  parent_None):
        super(HistogramWidget, self).__init__(parent)

        self.m_levels _ 128
        self.m_isBusy _ False
        self.m_histogram _ []
        self.m_processor _ FrameProcessor()
        self.m_processorThread _ QThread()

        self.m_processor.moveToThread(self.m_processorThread)
        self.m_processor.histogramReady.c..(self.setHistogram)

    ___ __del__(self):
        self.m_processorThread.quit()
        self.m_processorThread.wait(10000)

    ___ setLevels  levels):
        self.m_levels _ levels

    ___ processFrame  frame):
        __ self.m_isBusy:
            r_

        self.m_isBusy _ True
        QMetaObject.invokeMethod(self.m_processor, 'processFrame',
                Qt.QueuedConnection, Q_ARG(QVideoFrame, frame),
                Q_ARG(int, self.m_levels))

    @pyqtSlot(list)
    ___ setHistogram  histogram):
        self.m_isBusy _ False
        self.m_histogram _ list(histogram)
        self.update()

    ___ paintEvent  event):
        painter _ QPainter(self)

        __ len(self.m_histogram) == 0:
            painter.fillRect(0, 0, self.width(), self.height(),
                    QColor.fromRgb(0, 0, 0))
            r_

        barWidth _ self.width() / float(len(self.m_histogram))

        for i, value in enumerate(self.m_histogram):
            h _ value * self.height()
            # Draw the level.
            painter.fillRect(barWidth * i, self.height() - h,
                    barWidth * (i + 1), self.height(), Qt.red)
            # Clear the rest of the control.
            painter.fillRect(barWidth * i, 0, barWidth * (i + 1),
                    self.height() - h, Qt.black)


c_ Player(QWidget):

    fullScreenChanged _ pyqtSignal(bool)

    ___ __init__  playlist, parent_None):
        super(Player, self).__init__(parent)

        self.colorDialog _ N..
        self.trackInfo _ ""
        self.statusInfo _ ""
        self.duration _ 0

        self.player _ QMediaPlayer()
        self.playlist _ QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        self.player.durationChanged.c..(self.durationChanged)
        self.player.positionChanged.c..(self.positionChanged)
        self.player.metaDataChanged.c..(self.metaDataChanged)
        self.playlist.currentIndexChanged.c..(self.playlistPositionChanged)
        self.player.mediaStatusChanged.c..(self.statusChanged)
        self.player.bufferStatusChanged.c..(self.bufferingProgress)
        self.player.videoAvailableChanged.c..(self.videoAvailableChanged)
        self.player.error.c..(self.displayErrorMessage)

        self.videoWidget _ VideoWidget()
        self.player.setVideoOutput(self.videoWidget)

        self.playlistModel _ PlaylistModel()
        self.playlistModel.setPlaylist(self.playlist)

        self.playlistView _ QListView()
        self.playlistView.setModel(self.playlistModel)
        self.playlistView.setCurrentIndex(
                self.playlistModel.index(self.playlist.currentIndex(), 0))

        self.playlistView.activated.c..(self.jump)

        self.slider _ QSlider(Qt.Horizontal)
        self.slider.setRange(0, self.player.duration() / 1000)

        self.labelDuration _ QLabel()
        self.slider.sliderMoved.c..(self.seek)

        self.labelHistogram _ QLabel()
        self.labelHistogram.sT..("Histogram:")
        self.histogram _ HistogramWidget()
        histogramLayout _ QHBoxLayout()
        histogramLayout.addWidget(self.labelHistogram)
        histogramLayout.addWidget(self.histogram, 1)

        self.probe _ QVideoProbe()
        self.probe.videoFrameProbed.c..(self.histogram.processFrame)
        self.probe.setSource(self.player)

        openButton _ ?PB..("Open", c___self.o..)

        controls _ PlayerControls()
        controls.setState(self.player.state())
        controls.setVolume(self.player.volume())
        controls.setMuted(controls.isMuted())

        controls.play.c..(self.player.play)
        controls.pause.c..(self.player.pause)
        controls.stop.c..(self.player.stop)
        controls.next.c..(self.playlist.next)
        controls.previous.c..(self.previousClicked)
        controls.changeVolume.c..(self.player.setVolume)
        controls.changeMuting.c..(self.player.setMuted)
        controls.changeRate.c..(self.player.setPlaybackRate)
        controls.stop.c..(self.videoWidget.update)

        self.player.stateChanged.c..(controls.setState)
        self.player.volumeChanged.c..(controls.setVolume)
        self.player.mutedChanged.c..(controls.setMuted)

        self.fullScreenButton _ ?PB..("FullScreen")
        self.fullScreenButton.setCheckable(True)

        self.colorButton _ ?PB..("Color Options...")
        self.colorButton.setEnabled F..
        self.colorButton.c__.c..(self.showColorDialog)

        displayLayout _ QHBoxLayout()
        displayLayout.addWidget(self.videoWidget, 2)
        displayLayout.addWidget(self.playlistView)

        controlLayout _ QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addStretch(1)
        controlLayout.addWidget(controls)
        controlLayout.addStretch(1)
        controlLayout.addWidget(self.fullScreenButton)
        controlLayout.addWidget(self.colorButton)

        layout _ QVBoxLayout()
        layout.addLayout(displayLayout)
        hLayout _ QHBoxLayout()
        hLayout.addWidget(self.slider)
        hLayout.addWidget(self.labelDuration)
        layout.addLayout(hLayout)
        layout.addLayout(controlLayout)
        layout.addLayout(histogramLayout)

        self.setLayout(layout)

        __ no. self.player.isAvailable
            ?MB...warning  "Service not available",
                    "The QMediaPlayer object does not have a valid service.\n"
                    "Please check the media service plugins are installed.")

            controls.setEnabled F..
            self.playlistView.setEnabled F..
            openButton.setEnabled F..
            self.colorButton.setEnabled F..
            self.fullScreenButton.setEnabled F..

        self.metaDataChanged()

        self.addToPlaylist(playlist)

    ___ o..(self):
        fileNames, _ _ ?FD...getOpenFileNames  "Open Files")
        self.addToPlaylist(fileNames)

    ___ addToPlaylist  fileNames):
        for name in fileNames:
            fileInfo _ QFileInfo(name)
            __ fileInfo.exists
                url _ QUrl.fromLocalFile(fileInfo.absoluteFilePath())
                __ fileInfo.suffix().lower() == 'm3u':
                    self.playlist.load(url)
                ____
                    self.playlist.addMedia(QMediaContent(url))
            ____
                url _ QUrl(name)
                __ url.isValid
                    self.playlist.addMedia(QMediaContent(url))

    ___ durationChanged  duration):
        duration /_ 1000

        self.duration _ duration
        self.slider.setMaximum(duration)

    ___ positionChanged  progress):
        progress /_ 1000

        __ no. self.slider.isSliderDown
            self.slider.setValue(progress)

        self.updateDurationInfo(progress)

    ___ metaDataChanged(self):
        __ self.player.isMetaDataAvailable
            self.setTrackInfo("%s - %s" % (
                    self.player.metaData(QMediaMetaData.AlbumArtist),
                    self.player.metaData(QMediaMetaData.Title)))

    ___ previousClicked(self):
        # Go to the previous track if we are within the first 5 seconds of
        # playback.  Otherwise, seek to the beginning.
        __ self.player.position() <_ 5000:
            self.playlist.previous()
        ____
            self.player.setPosition(0)

    ___ jump  index):
        __ index.isValid
            self.playlist.setCurrentIndex(index.row())
            self.player.play()

    ___ playlistPositionChanged  position):
        self.playlistView.setCurrentIndex(
                self.playlistModel.index(position, 0))

    ___ seek  seconds):
        self.player.setPosition(seconds * 1000)

    ___ statusChanged  status):
        self.handleCursor(status)

        __ status == QMediaPlayer.LoadingMedia:
            self.setStatusInfo("Loading...")
        ____ status == QMediaPlayer.StalledMedia:
            self.setStatusInfo("Media Stalled")
        ____ status == QMediaPlayer.EndOfMedia:
            ?A...alert(self)
        ____ status == QMediaPlayer.InvalidMedia:
            self.displayErrorMessage()
        ____
            self.setStatusInfo("")

    ___ handleCursor  status):
        __ status in (QMediaPlayer.LoadingMedia, QMediaPlayer.BufferingMedia, QMediaPlayer.StalledMedia):
            self.setCursor(Qt.BusyCursor)
        ____
            self.unsetCursor()

    ___ bufferingProgress  progress):
        self.setStatusInfo("Buffering %d%" % progress)

    ___ videoAvailableChanged  available):
        __ available:
            self.fullScreenButton.c__.c..(
                    self.videoWidget.setFullScreen)
            self.videoWidget.fullScreenChanged.c..(
                    self.fullScreenButton.setChecked)

            __ self.fullScreenButton.isChecked
                self.videoWidget.setFullScreen(True)
        ____
            self.fullScreenButton.c__.disconnect(
                    self.videoWidget.setFullScreen)
            self.videoWidget.fullScreenChanged.disconnect(
                    self.fullScreenButton.setChecked)

            self.videoWidget.setFullScreen F..

        self.colorButton.setEnabled(available)

    ___ setTrackInfo  info):
        self.trackInfo _ info

        __ self.statusInfo !_ "":
            self.setWindowTitle("%s | %s" % (self.trackInfo, self.statusInfo))
        ____
            self.setWindowTitle(self.trackInfo)

    ___ setStatusInfo  info):
        self.statusInfo _ info

        __ self.statusInfo !_ "":
            self.setWindowTitle("%s | %s" % (self.trackInfo, self.statusInfo))
        ____
            self.setWindowTitle(self.trackInfo)

    ___ displayErrorMessage(self):
        self.setStatusInfo(self.player.errorString())

    ___ updateDurationInfo  currentInfo):
        duration _ self.duration
        __ currentInfo or duration:
            currentTime _ QTime((currentInfo/3600)%60, (currentInfo/60)%60,
                    currentInfo%60, (currentInfo*1000)%1000)
            totalTime _ QTime((duration/3600)%60, (duration/60)%60,
                    duration%60, (duration*1000)%1000);

            format _ 'hh:mm:ss' __ duration > 3600 else 'mm:ss'
            tStr _ currentTime.toString(format) + " / " + totalTime.toString(format)
        ____
            tStr _ ""

        self.labelDuration.sT..(tStr)

    ___ showColorDialog(self):
        __ self.colorDialog __ N..:
            brightnessSlider _ QSlider(Qt.Horizontal)
            brightnessSlider.setRange(-100, 100)
            brightnessSlider.setValue(self.videoWidget.brightness())
            brightnessSlider.sliderMoved.c..(
                    self.videoWidget.setBrightness)
            self.videoWidget.brightnessChanged.c..(
                    brightnessSlider.setValue)

            contrastSlider _ QSlider(Qt.Horizontal)
            contrastSlider.setRange(-100, 100)
            contrastSlider.setValue(self.videoWidget.contrast())
            contrastSlider.sliderMoved.c..(self.videoWidget.setContrast)
            self.videoWidget.contrastChanged.c..(contrastSlider.setValue)

            hueSlider _ QSlider(Qt.Horizontal)
            hueSlider.setRange(-100, 100)
            hueSlider.setValue(self.videoWidget.hue())
            hueSlider.sliderMoved.c..(self.videoWidget.setHue)
            self.videoWidget.hueChanged.c..(hueSlider.setValue)

            saturationSlider _ QSlider(Qt.Horizontal)
            saturationSlider.setRange(-100, 100)
            saturationSlider.setValue(self.videoWidget.saturation())
            saturationSlider.sliderMoved.c..(
                    self.videoWidget.setSaturation)
            self.videoWidget.saturationChanged.c..(
                    saturationSlider.setValue)

            layout _ QFormLayout()
            layout.addRow("Brightness", brightnessSlider)
            layout.addRow("Contrast", contrastSlider)
            layout.addRow("Hue", hueSlider)
            layout.addRow("Saturation", saturationSlider)

            button _ ?PB..("Close")
            layout.addRow(button)

            self.colorDialog _ QDialog(self)
            self.colorDialog.setWindowTitle("Color Options")
            self.colorDialog.setLayout(layout)

            button.c__.c..(self.colorDialog.close)

        self.colorDialog.s..


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    player _ Player(sys.argv[1:])
    player.s..

    sys.exit(app.exec_())
