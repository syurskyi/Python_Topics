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
____ ?.QtGui ______ QPalette, QPixmap
____ ?.QtMultimedia ______ (QAudioEncoderSettings, QCamera,
        QCameraImageCapture, QImageEncoderSettings, QMediaMetaData,
        QMediaRecorder, QMultimedia, QVideoEncoderSettings)
____ ?.?W.. ______ (QAction, QActionGroup, QApplication, QDialog,
        QMainWindow, QMessageBox)

____ ui_camera ______ Ui_Camera
____ ui_imagesettings ______ Ui_ImageSettingsUi
____ ui_videosettings ______ Ui_VideoSettingsUi


class ImageSettings(QDialog):

    ___ __init__(self, imageCapture, parent_None):
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

        return settings

    ___ setImageSettings(self, settings):
        self.selectComboBoxItem(self.ui.imageCodecBox, settings.codec())
        self.selectComboBoxItem(self.ui.imageResolutionBox,
                settings.resolution())
        self.ui.imageQualitySlider.setValue(settings.quality())

    @staticmethod
    ___ boxValue(box):
        idx _ box.currentIndex()
        if idx == -1:
            return None

        return box.itemData(idx)

    @staticmethod
    ___ selectComboBoxItem(box, value):
        for i in range(box.count()):
            if box.itemData(i) == value:
                box.setCurrentIndex(i)
                break


class VideoSettings(QDialog):

    ___ __init__(self, mediaRecorder, parent_None):
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

        return settings

    ___ setAudioSettings(self, settings):
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

        return settings

    ___ setVideoSettings(self, settings):
        self.selectComboBoxItem(self.ui.videoCodecBox, settings.codec())
        self.selectComboBoxItem(self.ui.videoResolutionBox,
                settings.resolution())
        self.ui.videoQualitySlider.setValue(settings.quality())

        for i in range(1, self.ui.videoFramerateBox.count()):
            itemRate _ self.ui.videoFramerateBox.itemData(i)
            if qFuzzyCompare(itemRate, settings.frameRate()):
                self.ui.videoFramerateBox.setCurrentIndex(i)
                break

    ___ format(self):
        return self.boxValue(self.ui.containerFormatBox)

    ___ setFormat(self, format):
        self.selectComboBoxItem(self.ui.containerFormatBox, format)

    @staticmethod
    ___ boxValue(box):
        idx _ box.currentIndex()
        if idx == -1:
            return None

        return box.itemData(idx)

    @staticmethod
    ___ selectComboBoxItem(box, value):
        for i in range(box.count()):
            if box.itemData(i) == value:
                box.setCurrentIndex(i)
                break


class Camera(QMainWindow):

    ___ __init__(self, parent_None):
        super(Camera, self).__init__(parent)

        self.ui _ Ui_Camera()
        self.camera _ None
        self.imageCapture _ None
        self.mediaRecorder _ None
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
            videoDeviceAction _ QAction(description, videoDevicesGroup)
            videoDeviceAction.setCheckable(True)
            videoDeviceAction.setData(deviceName)

            if cameraDevice.isEmpty
                cameraDevice _ deviceName
                videoDeviceAction.setChecked(True)

            self.ui.menuDevices.addAction(videoDeviceAction)

        videoDevicesGroup.triggered.c..(self.updateCameraDevice)
        self.ui.captureWidget.currentChanged.c..(self.updateCaptureMode)

        self.ui.lockButton.hide()

        self.setCamera(cameraDevice)

    ___ setCamera(self, cameraDevice):
        if cameraDevice.isEmpty
            self.camera _ QCamera()
        else:
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

    ___ keyPressEvent(self, event):
        if event.isAutoRepeat
            return

        if event.key() == Qt.Key_CameraFocus:
            self.displayViewfinder()
            self.camera.searchAndLock()
            event.accept()
        elif event.key() == Qt.Key_Camera:
            if self.camera.captureMode() == QCamera.CaptureStillImage:
                self.takeImage()
            elif self.mediaRecorder.state() == QMediaRecorder.RecordingState:
                self.stop()
            else:
                self.record()

            event.accept()
        else:
            super(Camera, self).keyPressEvent(event)

    ___ keyReleaseEvent(self, event):
        if event.isAutoRepeat
            return

        if event.key() == Qt.Key_CameraFocus:
            self.camera.unlock()
        else:
            super(Camera, self).keyReleaseEvent(event)

    ___ updateRecordTime(self):
        msg _ "Recorded %d sec" % (self.mediaRecorder.duration() // 1000)
        self.ui.statusbar.showMessage(msg)

    ___ processCapturedImage(self, requestId, img):
        scaledImage _ img.scaled(self.ui.viewfinder.size(), Qt.KeepAspectRatio,
                Qt.SmoothTransformation)

        self.ui.lastImagePreviewLabel.setPixmap(QPixmap.fromImage(scaledImage))

        self.displayCapturedImage()
        QTimer.singleShot(4000, self.displayViewfinder)

    ___ configureCaptureSettings(self):
        if self.camera.captureMode() == QCamera.CaptureStillImage:
            self.configureImageSettings()
        elif self.camera.captureMode() == QCamera.CaptureVideo:
            self.configureVideoSettings()

    ___ configureVideoSettings(self):
        settingsDialog _ VideoSettings(self.mediaRecorder)

        settingsDialog.setAudioSettings(self.audioSettings)
        settingsDialog.setVideoSettings(self.videoSettings)
        settingsDialog.setFormat(self.videoContainerFormat)

        if settingsDialog.exec_
            self.audioSettings _ settingsDialog.audioSettings()
            self.videoSettings _ settingsDialog.videoSettings()
            self.videoContainerFormat _ settingsDialog.format()

            self.mediaRecorder.setEncodingSettings(self.audioSettings,
                    self.videoSettings, self.videoContainerFormat)

    ___ configureImageSettings(self):
        settingsDialog _ ImageSettings(self.imageCapture)

        settingsDialog.setImageSettings(self.imageSettings)

        if settingsDialog.exec_
            self.imageSettings _ settingsDialog.imageSettings()
            self.imageCapture.setEncodingSettings(self.imageSettings)

    ___ record(self):
        self.mediaRecorder.record()
        self.updateRecordTime()

    ___ pause(self):
        self.mediaRecorder.pause()

    ___ stop(self):
        self.mediaRecorder.stop()

    ___ setMuted(self, muted):
        self.mediaRecorder.setMuted(muted)

    ___ toggleLock(self):
        if self.camera.lockStatus() in (QCamera.Searching, QCamera.Locked):
            self.camera.unlock()
        elif self.camera.lockStatus() == QCamera.Unlocked:
            self.camera.searchAndLock()

    ___ updateLockStatus(self, status, reason):
        indicationColor _ Qt.black

        if status == QCamera.Searching:
            self.ui.statusbar.showMessage("Focusing...")
            self.ui.lockButton.sT..("Focusing...")
            indicationColor _ Qt.yellow
        elif status == QCamera.Locked:
            self.ui.lockButton.sT..("Unlock")
            self.ui.statusbar.showMessage("Focused", 2000)
            indicationColor _ Qt.darkGreen
        elif status == QCamera.Unlocked:
            self.ui.lockButton.sT..("Focus")

            if reason == QCamera.LockFailed:
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
        captureMode _ QCamera.CaptureStillImage if tabIndex == 0 else QCamera.CaptureVideo

        if self.camera.isCaptureModeSupported(captureMode):
            self.camera.setCaptureMode(captureMode)

    ___ updateCameraState(self, state):
        if state == QCamera.ActiveState:
            self.ui.actionStartCamera.setEnabled(False)
            self.ui.actionStopCamera.setEnabled(True)
            self.ui.captureWidget.setEnabled(True)
            self.ui.actionSettings.setEnabled(True)
        elif state in (QCamera.UnloadedState, QCamera.LoadedState):
            self.ui.actionStartCamera.setEnabled(True)
            self.ui.actionStopCamera.setEnabled(False)
            self.ui.captureWidget.setEnabled(False)
            self.ui.actionSettings.setEnabled(False)

    ___ updateRecorderState(self, state):
        if state == QMediaRecorder.StoppedState:
            self.ui.recordButton.setEnabled(True)
            self.ui.pauseButton.setEnabled(True)
            self.ui.stopButton.setEnabled(False)
        elif state == QMediaRecorder.PausedState:
            self.ui.recordButton.setEnabled(True)
            self.ui.pauseButton.setEnabled(False)
            self.ui.stopButton.setEnabled(True)
        elif state == QMediaRecorder.RecordingState:
            self.ui.recordButton.setEnabled(False)
            self.ui.pauseButton.setEnabled(True)
            self.ui.stopButton.setEnabled(True)

    ___ setExposureCompensation(self, index):
        self.camera.exposure().setExposureCompensation(index * 0.5)

    ___ displayRecorderError(self):
        QMessageBox.warning(self, "Capture error",
                self.mediaRecorder.errorString())

    ___ displayCameraError(self):
        QMessageBox.warning(self, "Camera error", self.camera.errorString())

    ___ updateCameraDevice(self, action):
        self.setCamera(action.data())

    ___ displayViewfinder(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    ___ displayCapturedImage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    ___ readyForCapture(self, ready):
        self.ui.takeImageButton.setEnabled(ready)

    ___ imageSaved(self, id, fileName):
        self.isCapturingImage _ False

        if self.applicationExiting:
            self.close()

    ___ closeEvent(self, event):
        if self.isCapturingImage:
            self.setEnabled(False)
            self.applicationExiting _ True
            event.ignore()
        else:
            event.accept()


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)

    camera _ Camera()
    camera.s..

    sys.exit(app.exec_())
