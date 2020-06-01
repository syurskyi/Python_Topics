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
____ ?.QtGui ______ QColor, qGray, QImage, QPainter, QPalette
____ ?.QtMultimedia ______ (QAbstractVideoBuffer, QMediaContent,
        QMediaMetaData, QMediaPlayer, QMediaPlaylist, QVideoFrame, QVideoProbe)
____ ?.QtMultimediaWidgets ______ QVideoWidget
____ ?.?W.. ______ (?A.., QComboBox, QDialog, QFileDialog,
        QFormLayout, QHBoxLayout, QLabel, QListView, QMessageBox, ?PB..,
        QSizePolicy, QSlider, QStyle, QToolButton, QVBoxLayout, QWidget)


class VideoWidget(QVideoWidget):

    ___ __init__(self, parent_None):
        super(VideoWidget, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        p _ self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.setAttribute(Qt.WA_OpaquePaintEvent)

    ___ keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape and self.isFullScreen
            self.setFullScreen(False)
            event.accept()
        elif event.key() == Qt.Key_Enter and event.modifiers() & Qt.Key_Alt:
            self.setFullScreen(not self.isFullScreen())
            event.accept()
        else:
            super(VideoWidget, self).keyPressEvent(event)

    ___ mouseDoubleClickEvent(self, event):
        self.setFullScreen(not self.isFullScreen())
        event.accept()


class PlaylistModel(QAbstractItemModel):

    Title, ColumnCount _ range(2)

    ___ __init__(self, parent_None):
        super(PlaylistModel, self).__init__(parent)

        self.m_playlist _ None

    ___ rowCount(self, parent_QModelIndex()):
        return self.m_playlist.mediaCount() if self.m_playlist is not None and not parent.isValid() else 0

    ___ columnCount(self, parent_QModelIndex()):
        return self.ColumnCount if not parent.isValid() else 0

    ___ index(self, row, column, parent_QModelIndex()):
        return self.createIndex(row, column) if self.m_playlist is not None and not parent.isValid() and row >_ 0 and row < self.m_playlist.mediaCount() and column >_ 0 and column < self.ColumnCount else QModelIndex()

    ___ parent(self, child):
        return QModelIndex()

    ___ data(self, index, role_Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            if index.column() == self.Title:
                location _ self.m_playlist.media(index.row()).canonicalUrl()
                return QFileInfo(location.path()).fileName()

            return self.m_data[index]

        return None

    ___ playlist(self):
        return self.m_playlist

    ___ setPlaylist(self, playlist):
        if self.m_playlist is not None:
            self.m_playlist.mediaAboutToBeInserted.disconnect(
                    self.beginInsertItems)
            self.m_playlist.mediaInserted.disconnect(self.endInsertItems)
            self.m_playlist.mediaAboutToBeRemoved.disconnect(
                    self.beginRemoveItems)
            self.m_playlist.mediaRemoved.disconnect(self.endRemoveItems)
            self.m_playlist.mediaChanged.disconnect(self.changeItems)

        self.beginResetModel()
        self.m_playlist _ playlist

        if self.m_playlist is not None:
            self.m_playlist.mediaAboutToBeInserted.c..(
                    self.beginInsertItems)
            self.m_playlist.mediaInserted.c..(self.endInsertItems)
            self.m_playlist.mediaAboutToBeRemoved.c..(
                    self.beginRemoveItems)
            self.m_playlist.mediaRemoved.c..(self.endRemoveItems)
            self.m_playlist.mediaChanged.c..(self.changeItems)

        self.endResetModel()

    ___ beginInsertItems(self, start, end):
        self.beginInsertRows(QModelIndex(), start, end)

    ___ endInsertItems(self):
        self.endInsertRows()

    ___ beginRemoveItems(self, start, end):
        self.beginRemoveRows(QModelIndex(), start, end)

    ___ endRemoveItems(self):
        self.endRemoveRows()

    ___ changeItems(self, start, end):
        self.dataChanged.emit(self.index(start, 0),
                self.index(end, self.ColumnCount))


class PlayerControls(QWidget):

    play _ pyqtSignal()
    pause _ pyqtSignal()
    stop _ pyqtSignal()
    next _ pyqtSignal()
    previous _ pyqtSignal()
    changeVolume _ pyqtSignal(int)
    changeMuting _ pyqtSignal(bool)
    changeRate _ pyqtSignal(float)

    ___ __init__(self, parent_None):
        super(PlayerControls, self).__init__(parent)

        self.playerState _ QMediaPlayer.StoppedState
        self.playerMuted _ False

        self.playButton _ QToolButton(c___self.playClicked)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        self.stopButton _ QToolButton(c___self.stop)
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopButton.setEnabled(False)

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
        return self.playerState

    ___ setState(self,state):
        if state !_ self.playerState:
            self.playerState _ state

            if state == QMediaPlayer.StoppedState:
                self.stopButton.setEnabled(False)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))
            elif state == QMediaPlayer.PlayingState:
                self.stopButton.setEnabled(True)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPause))
            elif state == QMediaPlayer.PausedState:
                self.stopButton.setEnabled(True)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))

    ___ volume(self):
        return self.volumeSlider.value()

    ___ setVolume(self, volume):
        self.volumeSlider.setValue(volume)

    ___ isMuted(self):
        return self.playerMuted

    ___ setMuted(self, muted):
        if muted !_ self.playerMuted:
            self.playerMuted _ muted

            self.muteButton.setIcon(
                    self.style().standardIcon(
                            QStyle.SP_MediaVolumeMuted if muted else QStyle.SP_MediaVolume))

    ___ playClicked(self):
        if self.playerState in (QMediaPlayer.StoppedState, QMediaPlayer.PausedState):
            self.play.emit()
        elif self.playerState == QMediaPlayer.PlayingState:
            self.pause.emit()

    ___ muteClicked(self):
        self.changeMuting.emit(not self.playerMuted)

    ___ playbackRate(self):
        return self.rateBox.itemData(self.rateBox.currentIndex())

    ___ setPlaybackRate(self, rate):
        for i in range(self.rateBox.count()):
            if qFuzzyCompare(rate, self.rateBox.itemData(i)):
                self.rateBox.setCurrentIndex(i)
                return

        self.rateBox.addItem("%dx" % rate, rate)
        self.rateBox.setCurrentIndex(self.rateBox.count() - 1)

    ___ updateRate(self):
        self.changeRate.emit(self.playbackRate())


class FrameProcessor(QObject):

    histogramReady _ pyqtSignal(list)

    @pyqtSlot(QVideoFrame, int)
    ___ processFrame(self, frame, levels):
        histogram _ [0.0] * levels

        if levels and frame.map(QAbstractVideoBuffer.ReadOnly):
            pixelFormat _ frame.pixelFormat()

            if pixelFormat == QVideoFrame.Format_YUV420P or pixelFormat == QVideoFrame.Format_NV12:
                # Process YUV data.
                bits _ frame.bits()
                for idx in range(frame.height() * frame.width()):
                    histogram[(bits[idx] * levels) >> 8] +_ 1.0
            else:
                imageFormat _ QVideoFrame.imageFormatFromPixelFormat(pixelFormat)
                if imageFormat !_ QImage.Format_Invalid:
                    # Process RGB data.
                    image _ QImage(frame.bits(), frame.width(), frame.height(), imageFormat)

                    for y in range(image.height()):
                        for x in range(image.width()):
                            pixel _ image.pixel(x, y)
                            histogram[(qGray(pixel) * levels) >> 8] +_ 1.0

            # Find the maximum value.
            maxValue _ 0.0
            for value in histogram:
                if value > maxValue:
                    maxValue _ value

            # Normalise the values between 0 and 1.
            if maxValue > 0.0:
                for i in range(len(histogram)):
                    histogram[i] /_ maxValue

            frame.unmap()

        self.histogramReady.emit(histogram)


class HistogramWidget(QWidget):

    ___ __init__(self, parent_None):
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

    ___ setLevels(self, levels):
        self.m_levels _ levels

    ___ processFrame(self, frame):
        if self.m_isBusy:
            return

        self.m_isBusy _ True
        QMetaObject.invokeMethod(self.m_processor, 'processFrame',
                Qt.QueuedConnection, Q_ARG(QVideoFrame, frame),
                Q_ARG(int, self.m_levels))

    @pyqtSlot(list)
    ___ setHistogram(self, histogram):
        self.m_isBusy _ False
        self.m_histogram _ list(histogram)
        self.update()

    ___ paintEvent(self, event):
        painter _ QPainter(self)

        if len(self.m_histogram) == 0:
            painter.fillRect(0, 0, self.width(), self.height(),
                    QColor.fromRgb(0, 0, 0))
            return

        barWidth _ self.width() / float(len(self.m_histogram))

        for i, value in enumerate(self.m_histogram):
            h _ value * self.height()
            # Draw the level.
            painter.fillRect(barWidth * i, self.height() - h,
                    barWidth * (i + 1), self.height(), Qt.red)
            # Clear the rest of the control.
            painter.fillRect(barWidth * i, 0, barWidth * (i + 1),
                    self.height() - h, Qt.black)


class Player(QWidget):

    fullScreenChanged _ pyqtSignal(bool)

    ___ __init__(self, playlist, parent_None):
        super(Player, self).__init__(parent)

        self.colorDialog _ None
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

        openButton _ ?PB..("Open", c___self.open)

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
        self.colorButton.setEnabled(False)
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

        if not self.player.isAvailable
            QMessageBox.warning(self, "Service not available",
                    "The QMediaPlayer object does not have a valid service.\n"
                    "Please check the media service plugins are installed.")

            controls.setEnabled(False)
            self.playlistView.setEnabled(False)
            openButton.setEnabled(False)
            self.colorButton.setEnabled(False)
            self.fullScreenButton.setEnabled(False)

        self.metaDataChanged()

        self.addToPlaylist(playlist)

    ___ open(self):
        fileNames, _ _ QFileDialog.getOpenFileNames(self, "Open Files")
        self.addToPlaylist(fileNames)

    ___ addToPlaylist(self, fileNames):
        for name in fileNames:
            fileInfo _ QFileInfo(name)
            if fileInfo.exists
                url _ QUrl.fromLocalFile(fileInfo.absoluteFilePath())
                if fileInfo.suffix().lower() == 'm3u':
                    self.playlist.load(url)
                else:
                    self.playlist.addMedia(QMediaContent(url))
            else:
                url _ QUrl(name)
                if url.isValid
                    self.playlist.addMedia(QMediaContent(url))

    ___ durationChanged(self, duration):
        duration /_ 1000

        self.duration _ duration
        self.slider.setMaximum(duration)

    ___ positionChanged(self, progress):
        progress /_ 1000

        if not self.slider.isSliderDown
            self.slider.setValue(progress)

        self.updateDurationInfo(progress)

    ___ metaDataChanged(self):
        if self.player.isMetaDataAvailable
            self.setTrackInfo("%s - %s" % (
                    self.player.metaData(QMediaMetaData.AlbumArtist),
                    self.player.metaData(QMediaMetaData.Title)))

    ___ previousClicked(self):
        # Go to the previous track if we are within the first 5 seconds of
        # playback.  Otherwise, seek to the beginning.
        if self.player.position() <_ 5000:
            self.playlist.previous()
        else:
            self.player.setPosition(0)

    ___ jump(self, index):
        if index.isValid
            self.playlist.setCurrentIndex(index.row())
            self.player.play()

    ___ playlistPositionChanged(self, position):
        self.playlistView.setCurrentIndex(
                self.playlistModel.index(position, 0))

    ___ seek(self, seconds):
        self.player.setPosition(seconds * 1000)

    ___ statusChanged(self, status):
        self.handleCursor(status)

        if status == QMediaPlayer.LoadingMedia:
            self.setStatusInfo("Loading...")
        elif status == QMediaPlayer.StalledMedia:
            self.setStatusInfo("Media Stalled")
        elif status == QMediaPlayer.EndOfMedia:
            ?A...alert(self)
        elif status == QMediaPlayer.InvalidMedia:
            self.displayErrorMessage()
        else:
            self.setStatusInfo("")

    ___ handleCursor(self, status):
        if status in (QMediaPlayer.LoadingMedia, QMediaPlayer.BufferingMedia, QMediaPlayer.StalledMedia):
            self.setCursor(Qt.BusyCursor)
        else:
            self.unsetCursor()

    ___ bufferingProgress(self, progress):
        self.setStatusInfo("Buffering %d%" % progress)

    ___ videoAvailableChanged(self, available):
        if available:
            self.fullScreenButton.c__.c..(
                    self.videoWidget.setFullScreen)
            self.videoWidget.fullScreenChanged.c..(
                    self.fullScreenButton.setChecked)

            if self.fullScreenButton.isChecked
                self.videoWidget.setFullScreen(True)
        else:
            self.fullScreenButton.c__.disconnect(
                    self.videoWidget.setFullScreen)
            self.videoWidget.fullScreenChanged.disconnect(
                    self.fullScreenButton.setChecked)

            self.videoWidget.setFullScreen(False)

        self.colorButton.setEnabled(available)

    ___ setTrackInfo(self, info):
        self.trackInfo _ info

        if self.statusInfo !_ "":
            self.setWindowTitle("%s | %s" % (self.trackInfo, self.statusInfo))
        else:
            self.setWindowTitle(self.trackInfo)

    ___ setStatusInfo(self, info):
        self.statusInfo _ info

        if self.statusInfo !_ "":
            self.setWindowTitle("%s | %s" % (self.trackInfo, self.statusInfo))
        else:
            self.setWindowTitle(self.trackInfo)

    ___ displayErrorMessage(self):
        self.setStatusInfo(self.player.errorString())

    ___ updateDurationInfo(self, currentInfo):
        duration _ self.duration
        if currentInfo or duration:
            currentTime _ QTime((currentInfo/3600)%60, (currentInfo/60)%60,
                    currentInfo%60, (currentInfo*1000)%1000)
            totalTime _ QTime((duration/3600)%60, (duration/60)%60,
                    duration%60, (duration*1000)%1000);

            format _ 'hh:mm:ss' if duration > 3600 else 'mm:ss'
            tStr _ currentTime.toString(format) + " / " + totalTime.toString(format)
        else:
            tStr _ ""

        self.labelDuration.sT..(tStr)

    ___ showColorDialog(self):
        if self.colorDialog is None:
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


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    player _ Player(sys.argv[1:])
    player.s..

    sys.exit(app.exec_())
