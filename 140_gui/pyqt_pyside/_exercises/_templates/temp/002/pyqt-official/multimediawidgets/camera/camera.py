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


____ ?.?C.. ______ QByteArray, qFuzzyCompare, __, QTimer
____ ?.?G.. ______ ?P.., QPixmap
____ ?.QtMultimedia ______ (QAudioEncoderSettings, QCamera,
        QCameraImageCapture, QImageEncoderSettings, QMediaMetaData,
        QMediaRecorder, QMultimedia, QVideoEncoderSettings)
____ ?.?W.. ______ (?A.., QActionGroup, ?A.., QDialog,
        QMainWindow, ?MB..)

____ ui_camera ______ Ui_Camera
____ ui_imagesettings ______ Ui_ImageSettingsUi
____ ui_videosettings ______ Ui_VideoSettingsUi


c_ ImageSettings(QDialog):

    ___  -   imageCapture, parent_None):
        super(ImageSettings, self). - (parent)

        ui _ Ui_ImageSettingsUi()
        imagecapture _ imageCapture

        ui.setupUi

        ui.imageCodecBox.addItem("Default image format", "")
        ___ codecName __ imagecapture.supportedImageCodecs
            description _ imagecapture.imageCodecDescription(codecName)
            ui.imageCodecBox.addItem(codecName + ": " + description,
                    codecName)

        ui.imageQualitySlider.setRange(0, QMultimedia.VeryHighQuality)

        ui.imageResolutionBox.addItem("Default resolution")
        supportedResolutions, _ _ imagecapture.supportedResolutions()
        ___ resolution __ supportedResolutions:
            ui.imageResolutionBox.addItem(
                    "%dx%d" % (resolution.width(), resolution.height()),
                    resolution)

    ___ imageSettings
        settings _ imagecapture.encodingSettings()
        settings.setCodec(boxValue(ui.imageCodecBox))
        settings.setQuality(
                QMultimedia.EncodingQuality(
                        ui.imageQualitySlider.value()))
        settings.setResolution(boxValue(ui.imageResolutionBox))

        r_ settings

    ___ setImageSettings  settings):
        selectComboBoxItem(ui.imageCodecBox, settings.codec())
        selectComboBoxItem(ui.imageResolutionBox,
                settings.resolution())
        ui.imageQualitySlider.setValue(settings.quality())

    @staticmethod
    ___ boxValue(box):
        idx _ box.currentIndex()
        __ idx == -1:
            r_ N..

        r_ box.itemData(idx)

    @staticmethod
    ___ selectComboBoxItem(box, value):
        ___ i __ range(box.count()):
            __ box.itemData(i) == value:
                box.setCurrentIndex(i)
                break


c_ VideoSettings(QDialog):

    ___  -   mediaRecorder, parent_None):
        super(VideoSettings, self). - (parent)

        ui _ Ui_VideoSettingsUi()
        mediaRecorder _ mediaRecorder

        ui.setupUi

        ui.audioCodecBox.addItem("Default audio codec", "")
        ___ codecName __ mediaRecorder.supportedAudioCodecs
            description _ mediaRecorder.audioCodecDescription(codecName)
            ui.audioCodecBox.addItem(codecName + ": " + description,
                    codecName)

        supportedSampleRates, _ _ mediaRecorder.supportedAudioSampleRates()
        ___ sampleRate __ supportedSampleRates:
            ui.audioSampleRateBox.addItem(str(sampleRate), sampleRate)

        ui.audioQualitySlider.setRange(0, QMultimedia.VeryHighQuality)

        ui.videoCodecBox.addItem("Default video codec", "")
        ___ codecName __ mediaRecorder.supportedVideoCodecs
            description _ mediaRecorder.videoCodecDescription(codecName)
            ui.videoCodecBox.addItem(codecName + ": " + description,
                    codecName)

        ui.videoQualitySlider.setRange(0, QMultimedia.VeryHighQuality)

        ui.videoResolutionBox.addItem("Default")
        supportedResolutions, _ _ mediaRecorder.supportedResolutions()
        ___ resolution __ supportedResolutions:
            ui.videoResolutionBox.addItem(
                    "%dx%d" % (resolution.width(), resolution.height()),
                    resolution)

        ui.videoFramerateBox.addItem("Default")
        supportedFrameRates, _ _ mediaRecorder.supportedFrameRates()
        ___ rate __ supportedFrameRates:
            ui.videoFramerateBox.addItem("%0.2f" % rate, rate)

        ui.containerFormatBox.addItem("Default container", "")
        ___ format __ mediaRecorder.supportedContainers
            ui.containerFormatBox.addItem(
                    format + ":" + mediaRecorder.containerDescription(
                            format),
                    format)

    ___ audioSettings
        settings _ mediaRecorder.audioSettings()
        settings.setCodec(boxValue(ui.audioCodecBox))
        settings.setQuality(
                QMultimedia.EncodingQuality(
                        ui.audioQualitySlider.value()))
        settings.setSampleRate(boxValue(ui.audioSampleRateBox))

        r_ settings

    ___ setAudioSettings  settings):
        selectComboBoxItem(ui.audioCodecBox, settings.codec())
        selectComboBoxItem(ui.audioSampleRateBox,
                settings.sampleRate())
        ui.audioQualitySlider.setValue(settings.quality())

    ___ videoSettings
        settings _ mediaRecorder.videoSettings()
        settings.setCodec(boxValue(ui.videoCodecBox))
        settings.setQuality(
                QMultimedia.EncodingQuality(
                        ui.videoQualitySlider.value()))
        settings.setResolution(boxValue(ui.videoResolutionBox))
        settings.setFrameRate(boxValue(ui.videoFramerateBox))

        r_ settings

    ___ setVideoSettings  settings):
        selectComboBoxItem(ui.videoCodecBox, settings.codec())
        selectComboBoxItem(ui.videoResolutionBox,
                settings.resolution())
        ui.videoQualitySlider.setValue(settings.quality())

        ___ i __ range(1, ui.videoFramerateBox.count()):
            itemRate _ ui.videoFramerateBox.itemData(i)
            __ qFuzzyCompare(itemRate, settings.frameRate()):
                ui.videoFramerateBox.setCurrentIndex(i)
                break

    ___ format
        r_ boxValue(ui.containerFormatBox)

    ___ setFormat  format):
        selectComboBoxItem(ui.containerFormatBox, format)

    @staticmethod
    ___ boxValue(box):
        idx _ box.currentIndex()
        __ idx == -1:
            r_ N..

        r_ box.itemData(idx)

    @staticmethod
    ___ selectComboBoxItem(box, value):
        ___ i __ range(box.count()):
            __ box.itemData(i) == value:
                box.setCurrentIndex(i)
                break


c_ Camera ?MW..

    ___  -   parent_None):
        super(Camera, self). - (parent)

        ui _ Ui_Camera()
        camera _ N..
        imageCapture _ N..
        mediaRecorder _ N..
        isCapturingImage _ False
        applicationExiting _ False

        imageSettings _ QImageEncoderSettings()
        audioSettings _ QAudioEncoderSettings()
        videoSettings _ QVideoEncoderSettings()
        videoContainerFormat _ ''

        ui.setupUi

        cameraDevice _ QByteArray()

        videoDevicesGroup _ QActionGroup
        videoDevicesGroup.setExclusive(True)

        ___ deviceName __ QCamera.availableDevices
            description _ QCamera.deviceDescription(deviceName)
            videoDeviceAction _ ?A..(description, videoDevicesGroup)
            videoDeviceAction.setCheckable(True)
            videoDeviceAction.setData(deviceName)

            __ cameraDevice.isEmpty
                cameraDevice _ deviceName
                videoDeviceAction.setChecked(True)

            ui.menuDevices.aA..(videoDeviceAction)

        videoDevicesGroup.t__.c..(updateCameraDevice)
        ui.captureWidget.currentChanged.c..(updateCaptureMode)

        ui.lockButton.hide()

        setCamera(cameraDevice)

    ___ setCamera  cameraDevice):
        __ cameraDevice.isEmpty
            camera _ QCamera()
        ____
            camera _ QCamera(cameraDevice)

        camera.stateChanged.c..(updateCameraState)
        camera.error.c..(displayCameraError)

        mediaRecorder _ QMediaRecorder(camera)
        mediaRecorder.stateChanged.c..(updateRecorderState)

        imageCapture _ QCameraImageCapture(camera)

        mediaRecorder.durationChanged.c..(updateRecordTime)
        mediaRecorder.error.c..(displayRecorderError)

        mediaRecorder.setMetaData(QMediaMetaData.Title, "Test Title")

        ui.exposureCompensation.valueChanged.c..(
                setExposureCompensation)

        camera.setViewfinder(ui.viewfinder)

        updateCameraState(camera.state())
        updateLockStatus(camera.lockStatus(), QCamera.UserRequest)
        updateRecorderState(mediaRecorder.state())

        imageCapture.readyForCaptureChanged.c..(readyForCapture)
        imageCapture.imageCaptured.c..(processCapturedImage)
        imageCapture.imageSaved.c..(imageSaved)

        camera.lockStatusChanged.c..(updateLockStatus)

        ui.captureWidget.setTabEnabled(0,
                camera.isCaptureModeSupported(QCamera.CaptureStillImage))
        ui.captureWidget.setTabEnabled(1,
                camera.isCaptureModeSupported(QCamera.CaptureVideo))

        updateCaptureMode()
        camera.start()

    ___ keyPressEvent  event):
        __ event.isAutoRepeat
            r_

        __ event.key() == __.Key_CameraFocus:
            displayViewfinder()
            camera.searchAndLock()
            event.accept()
        ____ event.key() == __.Key_Camera:
            __ camera.captureMode() == QCamera.CaptureStillImage:
                takeImage()
            ____ mediaRecorder.state() == QMediaRecorder.RecordingState:
                stop()
            ____
                record()

            event.accept()
        ____
            super(Camera, self).keyPressEvent(event)

    ___ keyReleaseEvent  event):
        __ event.isAutoRepeat
            r_

        __ event.key() == __.Key_CameraFocus:
            camera.unlock()
        ____
            super(Camera, self).keyReleaseEvent(event)

    ___ updateRecordTime
        msg _ "Recorded %d sec" % (mediaRecorder.duration() // 1000)
        ui.statusbar.showMessage(msg)

    ___ processCapturedImage  requestId, img):
        scaledImage _ img.scaled(ui.viewfinder.size(), __.KeepAspectRatio,
                __.SmoothTransformation)

        ui.lastImagePreviewLabel.setPixmap(QPixmap.fromImage(scaledImage))

        displayCapturedImage()
        QTimer.singleShot(4000, displayViewfinder)

    ___ configureCaptureSettings
        __ camera.captureMode() == QCamera.CaptureStillImage:
            configureImageSettings()
        ____ camera.captureMode() == QCamera.CaptureVideo:
            configureVideoSettings()

    ___ configureVideoSettings
        settingsDialog _ VideoSettings(mediaRecorder)

        settingsDialog.setAudioSettings(audioSettings)
        settingsDialog.setVideoSettings(videoSettings)
        settingsDialog.setFormat(videoContainerFormat)

        __ settingsDialog.exec_
            audioSettings _ settingsDialog.audioSettings()
            videoSettings _ settingsDialog.videoSettings()
            videoContainerFormat _ settingsDialog.format()

            mediaRecorder.setEncodingSettings(audioSettings,
                    videoSettings, videoContainerFormat)

    ___ configureImageSettings
        settingsDialog _ ImageSettings(imageCapture)

        settingsDialog.setImageSettings(imageSettings)

        __ settingsDialog.exec_
            imageSettings _ settingsDialog.imageSettings()
            imageCapture.setEncodingSettings(imageSettings)

    ___ record
        mediaRecorder.record()
        updateRecordTime()

    ___ pause
        mediaRecorder.pause()

    ___ stop
        mediaRecorder.stop()

    ___ setMuted  muted):
        mediaRecorder.setMuted(muted)

    ___ toggleLock
        __ camera.lockStatus() __ (QCamera.Searching, QCamera.Locked):
            camera.unlock()
        ____ camera.lockStatus() == QCamera.Unlocked:
            camera.searchAndLock()

    ___ updateLockStatus  status, reason):
        indicationColor _ __.black

        __ status == QCamera.Searching:
            ui.statusbar.showMessage("Focusing...")
            ui.lockButton.sT..("Focusing...")
            indicationColor _ __.yellow
        ____ status == QCamera.Locked:
            ui.lockButton.sT..("Unlock")
            ui.statusbar.showMessage("Focused", 2000)
            indicationColor _ __.darkGreen
        ____ status == QCamera.Unlocked:
            ui.lockButton.sT..("Focus")

            __ reason == QCamera.LockFailed:
                ui.statusbar.showMessage("Focus Failed", 2000)
                indicationColor _ __.red

        palette _ ui.lockButton.palette()
        palette.sC..(?P...ButtonText, indicationColor)
        ui.lockButton.sP..(palette)

    ___ takeImage
        isCapturingImage _ True
        imageCapture.capture()

    ___ startCamera
        camera.start()

    ___ stopCamera
        camera.stop()

    ___ updateCaptureMode
        tabIndex _ ui.captureWidget.currentIndex()
        captureMode _ QCamera.CaptureStillImage __ tabIndex == 0 else QCamera.CaptureVideo

        __ camera.isCaptureModeSupported(captureMode):
            camera.setCaptureMode(captureMode)

    ___ updateCameraState  state):
        __ state == QCamera.ActiveState:
            ui.actionStartCamera.sE.. F..
            ui.actionStopCamera.sE..(True)
            ui.captureWidget.sE..(True)
            ui.actionSettings.sE..(True)
        ____ state __ (QCamera.UnloadedState, QCamera.LoadedState):
            ui.actionStartCamera.sE..(True)
            ui.actionStopCamera.sE.. F..
            ui.captureWidget.sE.. F..
            ui.actionSettings.sE.. F..

    ___ updateRecorderState  state):
        __ state == QMediaRecorder.StoppedState:
            ui.recordButton.sE..(True)
            ui.pauseButton.sE..(True)
            ui.stopButton.sE.. F..
        ____ state == QMediaRecorder.PausedState:
            ui.recordButton.sE..(True)
            ui.pauseButton.sE.. F..
            ui.stopButton.sE..(True)
        ____ state == QMediaRecorder.RecordingState:
            ui.recordButton.sE.. F..
            ui.pauseButton.sE..(True)
            ui.stopButton.sE..(True)

    ___ setExposureCompensation  index):
        camera.exposure().setExposureCompensation(index * 0.5)

    ___ displayRecorderError
        ?MB...warning  "Capture error",
                mediaRecorder.errorString())

    ___ displayCameraError
        ?MB...warning  "Camera error", camera.errorString())

    ___ updateCameraDevice  action):
        setCamera(action.data())

    ___ displayViewfinder
        ui.stackedWidget.setCurrentIndex(0)

    ___ displayCapturedImage
        ui.stackedWidget.setCurrentIndex(1)

    ___ readyForCapture  ready):
        ui.takeImageButton.sE..(ready)

    ___ imageSaved  id, fileName):
        isCapturingImage _ False

        __ applicationExiting:
            close()

    ___ closeEvent  event):
        __ isCapturingImage:
            sE.. F..
            applicationExiting _ True
            event.ignore()
        ____
            event.accept()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    camera _ Camera()
    camera.s..

    ___.e..(app.exec_())
