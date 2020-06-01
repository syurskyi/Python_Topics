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


____ ?.QtCore ______ QByteArray, qFuzzyCompare, Qt, QTimer
____ ?.?G.. ______ QPalette, QPixmap
____ ?.QtMultimedia ______ (QAudioEncoderSettings, QCamera,
        QCameraImageCapture, QImageEncoderSettings, QMediaMetaData,
        QMediaRecorder, QMultimedia, QVideoEncoderSettings)
____ ?.?W.. ______ (?A.., QActionGroup, ?A.., QDialog,
        QMainWindow, ?MB..)

____ ui_camera ______ Ui_Camera
____ ui_imagesettings ______ Ui_ImageSettingsUi
____ ui_videosettings ______ Ui_VideoSettingsUi


c_ ImageSettings(QDialog):

    ___ __init__  imageCapture, parent_None):
        super(ImageSettings, self).__init__(parent)

        self.ui _ Ui_ImageSettingsUi()
        self.imagecapture _ imageCapture

        self.ui.setupUi(self)

        self.ui.imageCodecBox.addItem("Default image format", "")
        for codecName in self.imagecapture.supportedImageCodecs
            description _ self.imagecapture.imageCodecDescription(codecName)
            self.ui.imageCodecBox.addItem(codecName + ": " + description,
                    codecName)

        self.ui.imageQualitySlider.setRange(0, QMultimedia.VeryHighQuality)

        self.ui.imageResolutionBox.addItem("Default resolution")
        supportedResolutions, _ _ self.imagecapture.supportedResolutions()
        for resolution in supportedResolutions:
            self.ui.imageResolutionBox.addItem(
                    "%dx%d" % (resolution.width(), resolution.height()),
                    resolution)

    ___ imageSettings(self):
        settings _ self.imagecapture.encodingSettings()
        settings.setCodec(self.boxValue(self.ui.imageCodecBox))
        settings.setQuality(
                QMultimedia.EncodingQuality(
                        self.ui.imageQualitySlider.value()))
        settings.setResolution(self.boxValue(self.ui.imageResolutionBox))

        r_ settings

    ___ setImageSettings  settings):
        self.selectComboBoxItem(self.ui.imageCodecBox, settings.codec())
        self.selectComboBoxItem(self.ui.imageResolutionBox,
                settings.resolution())
        self.ui.imageQualitySlider.setValue(settings.quality())

    @staticmethod
    ___ boxValue(box):
        idx _ box.currentIndex()
        __ idx == -1:
            r_ N..

        r_ box.itemData(idx)

    @staticmethod
    ___ selectComboBoxItem(box, value):
        for i in range(box.count()):
            __ box.itemData(i) == value:
                box.setCurrentIndex(i)
                break


c_ VideoSettings(QDialog):

    ___ __init__  mediaRecorder, parent_None):
        super(VideoSettings, self).__init__(parent)

        self.ui _ Ui_VideoSettingsUi()
        self.mediaRecorder _ mediaRecorder

        self.ui.setupUi(self)

        self.ui.audioCodecBox.addItem("Default audio codec", "")
        for codecName in self.mediaRecorder.supportedAudioCodecs
            description _ self.mediaRecorder.audioCodecDescription(codecName)
            self.ui.audioCodecBox.addItem(codecName + ": " + description,
                    codecName)

        supportedSampleRates, _ _ self.mediaRecorder.supportedAudioSampleRates()
        for sampleRate in supportedSampleRates:
            self.ui.audioSampleRateBox.addItem(str(sampleRate), sampleRate)

        self.ui.audioQualitySlider.setRange(0, QMultimedia.VeryHighQuality)

        self.ui.videoCodecBox.addItem("Default video codec", "")
        for codecName in self.mediaRecorder.supportedVideoCodecs
            description _ self.mediaRecorder.videoCodecDescription(codecName)
            self.ui.videoCodecBox.addItem(codecName + ": " + description,
                    codecName)

        self.ui.videoQualitySlider.setRange(0, QMultimedia.VeryHighQuality)

        self.ui.videoResolutionBox.addItem("Default")
        supportedResolutions, _ _ self.mediaRecorder.supportedResolutions()
        for resolution in supportedResolutions:
            self.ui.videoResolutionBox.addItem(
                    "%dx%d" % (resolution.width(), resolution.height()),
                    resolution)

        self.ui.videoFramerateBox.addItem("Default")
        supportedFrameRates, _ _ self.mediaRecorder.supportedFrameRates()
        for rate in supportedFrameRates:
            self.ui.videoFramerateBox.addItem("%0.2f" % rate, rate)

        self.ui.containerFormatBox.addItem("Default container", "")
        for format in self.mediaRecorder.supportedContainers
            self.ui.containerFormatBox.addItem(
                    format + ":" + self.mediaRecorder.containerDescription(
                            format),
                    format)

    ___ audioSettings(self):
        settings _ self.mediaRecorder.audioSettings()
        settings.setCodec(self.boxValue(self.ui.audioCodecBox))
        settings.setQuality(
                QMultimedia.EncodingQuality(
                        self.ui.audioQualitySlider.value()))
        settings.setSampleRate(self.boxValue(self.ui.audioSampleRateBox))

        r_ settings

    ___ setAudioSettings  settings):
        self.selectComboBoxItem(self.ui.audioCodecBox, settings.codec())
        self.selectComboBoxItem(self.ui.audioSampleRateBox,
                settings.sampleRate())
        self.ui.audioQualitySlider.setValue(settings.quality())

    ___ videoSettings(self):
        settings _ self.mediaRecorder.videoSettings()
        settings.setCodec(self.boxValue(self.ui.videoCodecBox))
        settings.setQuality(
                QMultimedia.EncodingQuality(
                        self.ui.videoQualitySlider.value()))
        settings.setResolution(self.boxValue(self.ui.videoResolutionBox))
        settings.setFrameRate(self.boxValue(self.ui.videoFramerateBox))

        r_ settings

    ___ setVideoSettings  settings):
        self.selectComboBoxItem(self.ui.videoCodecBox, settings.codec())
        self.selectComboBoxItem(self.ui.videoResolutionBox,
                settings.resolution())
        self.ui.videoQualitySlider.setValue(settings.quality())

        for i in range(1, self.ui.videoFramerateBox.count()):
            itemRate _ self.ui.videoFramerateBox.itemData(i)
            __ qFuzzyCompare(itemRate, settings.frameRate()):
                self.ui.videoFramerateBox.setCurrentIndex(i)
                break

    ___ format(self):
        r_ self.boxValue(self.ui.containerFormatBox)

    ___ setFormat  format):
        self.selectComboBoxItem(self.ui.containerFormatBox, format)

    @staticmethod
    ___ boxValue(box):
        idx _ box.currentIndex()
        __ idx == -1:
            r_ N..

        r_ box.itemData(idx)

    @staticmethod
    ___ selectComboBoxItem(box, value):
        for i in range(box.count()):
            __ box.itemData(i) == value:
                box.setCurrentIndex(i)
                break


c_ Camera ?MW..

    ___ __init__  parent_None):
        super(Camera, self).__init__(parent)

        self.ui _ Ui_Camera()
        self.camera _ N..
        self.imageCapture _ N..
        self.mediaRecorder _ N..
        self.isCapturingImage _ False
        self.applicationExiting _ False

        self.imageSettings _ QImageEncoderSettings()
        self.audioSettings _ QAudioEncoderSettings()
        self.videoSettings _ QVideoEncoderSettings()
        self.videoContainerFormat _ ''

        self.ui.setupUi(self)

        cameraDevice _ QByteArray()

        videoDevicesGroup _ QActionGroup(self)
        videoDevicesGroup.setExclusive(True)

        for deviceName in QCamera.availableDevices
            description _ QCamera.deviceDescription(deviceName)
            videoDeviceAction _ ?A..(description, videoDevicesGroup)
            videoDeviceAction.setCheckable(True)
            videoDeviceAction.setData(deviceName)

            __ cameraDevice.isEmpty
                cameraDevice _ deviceName
                videoDeviceAction.setChecked(True)

            self.ui.menuDevices.aA..(videoDeviceAction)

        videoDevicesGroup.t__.c..(self.updateCameraDevice)
        self.ui.captureWidget.currentChanged.c..(self.updateCaptureMode)

        self.ui.lockButton.hide()

        self.setCamera(cameraDevice)

    ___ setCamera  cameraDevice):
        __ cameraDevice.isEmpty
            self.camera _ QCamera()
        ____
            self.camera _ QCamera(cameraDevice)

        self.camera.stateChanged.c..(self.updateCameraState)
        self.camera.error.c..(self.displayCameraError)

        self.mediaRecorder _ QMediaRecorder(self.camera)
        self.mediaRecorder.stateChanged.c..(self.updateRecorderState)

        self.imageCapture _ QCameraImageCapture(self.camera)

        self.mediaRecorder.durationChanged.c..(self.updateRecordTime)
        self.mediaRecorder.error.c..(self.displayRecorderError)

        self.mediaRecorder.setMetaData(QMediaMetaData.Title, "Test Title")

        self.ui.exposureCompensation.valueChanged.c..(
                self.setExposureCompensation)

        self.camera.setViewfinder(self.ui.viewfinder)

        self.updateCameraState(self.camera.state())
        self.updateLockStatus(self.camera.lockStatus(), QCamera.UserRequest)
        self.updateRecorderState(self.mediaRecorder.state())

        self.imageCapture.readyForCaptureChanged.c..(self.readyForCapture)
        self.imageCapture.imageCaptured.c..(self.processCapturedImage)
        self.imageCapture.imageSaved.c..(self.imageSaved)

        self.camera.lockStatusChanged.c..(self.updateLockStatus)

        self.ui.captureWidget.setTabEnabled(0,
                self.camera.isCaptureModeSupported(QCamera.CaptureStillImage))
        self.ui.captureWidget.setTabEnabled(1,
                self.camera.isCaptureModeSupported(QCamera.CaptureVideo))

        self.updateCaptureMode()
        self.camera.start()

    ___ keyPressEvent  event):
        __ event.isAutoRepeat
            r_

        __ event.key() == Qt.Key_CameraFocus:
            self.displayViewfinder()
            self.camera.searchAndLock()
            event.accept()
        ____ event.key() == Qt.Key_Camera:
            __ self.camera.captureMode() == QCamera.CaptureStillImage:
                self.takeImage()
            ____ self.mediaRecorder.state() == QMediaRecorder.RecordingState:
                self.stop()
            ____
                self.record()

            event.accept()
        ____
            super(Camera, self).keyPressEvent(event)

    ___ keyReleaseEvent  event):
        __ event.isAutoRepeat
            r_

        __ event.key() == Qt.Key_CameraFocus:
            self.camera.unlock()
        ____
            super(Camera, self).keyReleaseEvent(event)

    ___ updateRecordTime(self):
        msg _ "Recorded %d sec" % (self.mediaRecorder.duration() // 1000)
        self.ui.statusbar.showMessage(msg)

    ___ processCapturedImage  requestId, img):
        scaledImage _ img.scaled(self.ui.viewfinder.size(), Qt.KeepAspectRatio,
                Qt.SmoothTransformation)

        self.ui.lastImagePreviewLabel.setPixmap(QPixmap.fromImage(scaledImage))

        self.displayCapturedImage()
        QTimer.singleShot(4000, self.displayViewfinder)

    ___ configureCaptureSettings(self):
        __ self.camera.captureMode() == QCamera.CaptureStillImage:
            self.configureImageSettings()
        ____ self.camera.captureMode() == QCamera.CaptureVideo:
            self.configureVideoSettings()

    ___ configureVideoSettings(self):
        settingsDialog _ VideoSettings(self.mediaRecorder)

        settingsDialog.setAudioSettings(self.audioSettings)
        settingsDialog.setVideoSettings(self.videoSettings)
        settingsDialog.setFormat(self.videoContainerFormat)

        __ settingsDialog.exec_
            self.audioSettings _ settingsDialog.audioSettings()
            self.videoSettings _ settingsDialog.videoSettings()
            self.videoContainerFormat _ settingsDialog.format()

            self.mediaRecorder.setEncodingSettings(self.audioSettings,
                    self.videoSettings, self.videoContainerFormat)

    ___ configureImageSettings(self):
        settingsDialog _ ImageSettings(self.imageCapture)

        settingsDialog.setImageSettings(self.imageSettings)

        __ settingsDialog.exec_
            self.imageSettings _ settingsDialog.imageSettings()
            self.imageCapture.setEncodingSettings(self.imageSettings)

    ___ record(self):
        self.mediaRecorder.record()
        self.updateRecordTime()

    ___ pause(self):
        self.mediaRecorder.pause()

    ___ stop(self):
        self.mediaRecorder.stop()

    ___ setMuted  muted):
        self.mediaRecorder.setMuted(muted)

    ___ toggleLock(self):
        __ self.camera.lockStatus() in (QCamera.Searching, QCamera.Locked):
            self.camera.unlock()
        ____ self.camera.lockStatus() == QCamera.Unlocked:
            self.camera.searchAndLock()

    ___ updateLockStatus  status, reason):
        indicationColor _ Qt.black

        __ status == QCamera.Searching:
            self.ui.statusbar.showMessage("Focusing...")
            self.ui.lockButton.sT..("Focusing...")
            indicationColor _ Qt.yellow
        ____ status == QCamera.Locked:
            self.ui.lockButton.sT..("Unlock")
            self.ui.statusbar.showMessage("Focused", 2000)
            indicationColor _ Qt.darkGreen
        ____ status == QCamera.Unlocked:
            self.ui.lockButton.sT..("Focus")

            __ reason == QCamera.LockFailed:
                self.ui.statusbar.showMessage("Focus Failed", 2000)
                indicationColor _ Qt.red

        palette _ self.ui.lockButton.palette()
        palette.setColor(QPalette.ButtonText, indicationColor)
        self.ui.lockButton.setPalette(palette)

    ___ takeImage(self):
        self.isCapturingImage _ True
        self.imageCapture.capture()

    ___ startCamera(self):
        self.camera.start()

    ___ stopCamera(self):
        self.camera.stop()

    ___ updateCaptureMode(self):
        tabIndex _ self.ui.captureWidget.currentIndex()
        captureMode _ QCamera.CaptureStillImage __ tabIndex == 0 else QCamera.CaptureVideo

        __ self.camera.isCaptureModeSupported(captureMode):
            self.camera.setCaptureMode(captureMode)

    ___ updateCameraState  state):
        __ state == QCamera.ActiveState:
            self.ui.actionStartCamera.setEnabled F..
            self.ui.actionStopCamera.setEnabled(True)
            self.ui.captureWidget.setEnabled(True)
            self.ui.actionSettings.setEnabled(True)
        ____ state in (QCamera.UnloadedState, QCamera.LoadedState):
            self.ui.actionStartCamera.setEnabled(True)
            self.ui.actionStopCamera.setEnabled F..
            self.ui.captureWidget.setEnabled F..
            self.ui.actionSettings.setEnabled F..

    ___ updateRecorderState  state):
        __ state == QMediaRecorder.StoppedState:
            self.ui.recordButton.setEnabled(True)
            self.ui.pauseButton.setEnabled(True)
            self.ui.stopButton.setEnabled F..
        ____ state == QMediaRecorder.PausedState:
            self.ui.recordButton.setEnabled(True)
            self.ui.pauseButton.setEnabled F..
            self.ui.stopButton.setEnabled(True)
        ____ state == QMediaRecorder.RecordingState:
            self.ui.recordButton.setEnabled F..
            self.ui.pauseButton.setEnabled(True)
            self.ui.stopButton.setEnabled(True)

    ___ setExposureCompensation  index):
        self.camera.exposure().setExposureCompensation(index * 0.5)

    ___ displayRecorderError(self):
        ?MB...warning  "Capture error",
                self.mediaRecorder.errorString())

    ___ displayCameraError(self):
        ?MB...warning  "Camera error", self.camera.errorString())

    ___ updateCameraDevice  action):
        self.setCamera(action.data())

    ___ displayViewfinder(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    ___ displayCapturedImage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    ___ readyForCapture  ready):
        self.ui.takeImageButton.setEnabled(ready)

    ___ imageSaved  id, fileName):
        self.isCapturingImage _ False

        __ self.applicationExiting:
            self.close()

    ___ closeEvent  event):
        __ self.isCapturingImage:
            self.setEnabled F..
            self.applicationExiting _ True
            event.ignore()
        ____
            event.accept()


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    camera _ Camera()
    camera.s..

    sys.exit(app.exec_())
