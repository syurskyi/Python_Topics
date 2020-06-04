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


____ ?.?C.. ______ QByteArray, qFuzzyCompare, __, ?T..
____ ?.?G.. ______ ?P.., ?P..
____ ?.?M.. ______ (QAudioEncoderSettings, QCamera,
        QCameraImageCapture, QImageEncoderSettings, QMediaMetaData,
        ?MR.., QMultimedia, QVideoEncoderSettings)
____ ?.?W.. ______ (?A.., QActionGroup, ?A.., ?D..,
        ?MW.., ?MB..)

____ ui_camera ______ Ui_Camera
____ ui_imagesettings ______ Ui_ImageSettingsUi
____ ui_videosettings ______ Ui_VideoSettingsUi


c_ ImageSettings(?D..):

    ___  -   imageCapture, parent_None):
        s__(ImageSettings, self). - (parent)

        ui _ Ui_ImageSettingsUi()
        imagecapture _ imageCapture

        ui.setupUi

        ui.imageCodecBox.aI..("Default image format", "")
        ___ codecName __ imagecapture.supportedImageCodecs
            description _ imagecapture.imageCodecDescription(codecName)
            ui.imageCodecBox.aI..(codecName + ": " + description,
                    codecName)

        ui.imageQualitySlider.setRange(0, QMultimedia.VeryHighQuality)

        ui.imageResolutionBox.aI..("Default resolution")
        supportedResolutions, _ _ imagecapture.supportedResolutions()
        ___ resolution __ supportedResolutions:
            ui.imageResolutionBox.aI..(
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
        ui.imageQualitySlider.sV..(settings.quality())

    @staticmethod
    ___ boxValue(box):
        idx _ box.currentIndex()
        __ idx __ -1:
            r_ N..

        r_ box.itemData(idx)

    @staticmethod
    ___ selectComboBoxItem(box, value):
        ___ i __ ra..(box.count()):
            __ box.itemData(i) __ value:
                box.sCI..(i)
                break


c_ VideoSettings(?D..):

    ___  -   mediaRecorder, parent_None):
        s__(VideoSettings, self). - (parent)

        ui _ Ui_VideoSettingsUi()
        mediaRecorder _ mediaRecorder

        ui.setupUi

        ui.audioCodecBox.aI..("Default audio codec", "")
        ___ codecName __ mediaRecorder.sAC..
            description _ mediaRecorder.audioCodecDescription(codecName)
            ui.audioCodecBox.aI..(codecName + ": " + description,
                    codecName)

        supportedSampleRates, _ _ mediaRecorder.supportedAudioSampleRates()
        ___ sampleRate __ supportedSampleRates:
            ui.audioSampleRateBox.aI..(st.(sampleRate), sampleRate)

        ui.audioQualitySlider.setRange(0, QMultimedia.VeryHighQuality)

        ui.videoCodecBox.aI..("Default video codec", "")
        ___ codecName __ mediaRecorder.sVC..
            description _ mediaRecorder.videoCodecDescription(codecName)
            ui.videoCodecBox.aI..(codecName + ": " + description,
                    codecName)

        ui.videoQualitySlider.setRange(0, QMultimedia.VeryHighQuality)

        ui.videoResolutionBox.aI..("Default")
        supportedResolutions, _ _ mediaRecorder.supportedResolutions()
        ___ resolution __ supportedResolutions:
            ui.videoResolutionBox.aI..(
                    "%dx%d" % (resolution.width(), resolution.height()),
                    resolution)

        ui.videoFramerateBox.aI..("Default")
        supportedFrameRates, _ _ mediaRecorder.supportedFrameRates()
        ___ rate __ supportedFrameRates:
            ui.videoFramerateBox.aI..("%0.2f" % rate, rate)

        ui.containerFormatBox.aI..("Default container", "")
        ___ f.. __ mediaRecorder.supportedContainers
            ui.containerFormatBox.aI..(
                    f.. + ":" + mediaRecorder.containerDescription(
                            f..),
                    f..)

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
        ui.audioQualitySlider.sV..(settings.quality())

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
        ui.videoQualitySlider.sV..(settings.quality())

        ___ i __ ra..(1, ui.videoFramerateBox.count()):
            itemRate _ ui.videoFramerateBox.itemData(i)
            __ qFuzzyCompare(itemRate, settings.frameRate()):
                ui.videoFramerateBox.sCI..(i)
                break

    ___ f..
        r_ boxValue(ui.containerFormatBox)

    ___ setFormat  f..):
        selectComboBoxItem(ui.containerFormatBox, f..)

    @staticmethod
    ___ boxValue(box):
        idx _ box.currentIndex()
        __ idx __ -1:
            r_ N..

        r_ box.itemData(idx)

    @staticmethod
    ___ selectComboBoxItem(box, value):
        ___ i __ ra..(box.count()):
            __ box.itemData(i) __ value:
                box.sCI..(i)
                break


c_ Camera ?MW..

    ___  -   parent_None):
        s__(Camera, self). - (parent)

        ui _ Ui_Camera()
        camera _ N..
        imageCapture _ N..
        mediaRecorder _ N..
        isCapturingImage _ F..
        applicationExiting _ F..

        imageSettings _ QImageEncoderSettings()
        audioSettings _ QAudioEncoderSettings()
        videoSettings _ QVideoEncoderSettings()
        videoContainerFormat _ ''

        ui.setupUi

        cameraDevice _ QByteArray()

        videoDevicesGroup _ QActionGroup
        videoDevicesGroup.setExclusive( st.

        ___ deviceName __ QCamera.availableDevices
            description _ QCamera.deviceDescription(deviceName)
            videoDeviceAction _ ?A..(description, videoDevicesGroup)
            videoDeviceAction.setCheckable( st.
            videoDeviceAction.setData(deviceName)

            __ cameraDevice.isEmpty
                cameraDevice _ deviceName
                videoDeviceAction.sC__( st.

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

        mediaRecorder _ ?MR..(camera)
        mediaRecorder.stateChanged.c..(updateRecorderState)

        imageCapture _ QCameraImageCapture(camera)

        mediaRecorder.dC...c..(updateRecordTime)
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

        __ event.key() __ __.Key_CameraFocus:
            displayViewfinder()
            camera.searchAndLock()
            event.accept()
        ____ event.key() __ __.Key_Camera:
            __ camera.captureMode() __ QCamera.CaptureStillImage:
                takeImage()
            ____ mediaRecorder.s.. __ ?MR...RS..:
                s..
            ____
                r..

            event.accept()
        ____
            s__(Camera, self).keyPressEvent(event)

    ___ keyReleaseEvent  event):
        __ event.isAutoRepeat
            r_

        __ event.key() __ __.Key_CameraFocus:
            camera.unlock()
        ____
            s__(Camera, self).keyReleaseEvent(event)

    ___ updateRecordTime
        msg _ "Recorded %d sec" % (mediaRecorder.duration() // 1000)
        ui.statusbar.sM..(msg)

    ___ processCapturedImage  requestId, img):
        scaledImage _ img.scaled(ui.viewfinder.size(), __.KeepAspectRatio,
                __.SmoothTransformation)

        ui.lastImagePreviewLabel.sP..(?P...fromImage(scaledImage))

        displayCapturedImage()
        ?T...sS..(4000, displayViewfinder)

    ___ configureCaptureSettings
        __ camera.captureMode() __ QCamera.CaptureStillImage:
            configureImageSettings()
        ____ camera.captureMode() __ QCamera.CaptureVideo:
            configureVideoSettings()

    ___ configureVideoSettings
        settingsDialog _ VideoSettings(mediaRecorder)

        settingsDialog.setAudioSettings(audioSettings)
        settingsDialog.setVideoSettings(videoSettings)
        settingsDialog.setFormat(videoContainerFormat)

        __ settingsDialog.e..
            audioSettings _ settingsDialog.audioSettings()
            videoSettings _ settingsDialog.videoSettings()
            videoContainerFormat _ settingsDialog.f..()

            mediaRecorder.setEncodingSettings(audioSettings,
                    videoSettings, videoContainerFormat)

    ___ configureImageSettings
        settingsDialog _ ImageSettings(imageCapture)

        settingsDialog.setImageSettings(imageSettings)

        __ settingsDialog.e..
            imageSettings _ settingsDialog.imageSettings()
            imageCapture.setEncodingSettings(imageSettings)

    ___ record
        mediaRecorder.r..
        updateRecordTime()

    ___ pause
        mediaRecorder.pause()

    ___ stop
        mediaRecorder.s..

    ___ setMuted  muted):
        mediaRecorder.setMuted(muted)

    ___ toggleLock
        __ camera.lockStatus() __ (QCamera.Searching, QCamera.Locked):
            camera.unlock()
        ____ camera.lockStatus() __ QCamera.Unlocked:
            camera.searchAndLock()

    ___ updateLockStatus  status, reason):
        indicationColor _ __.black

        __ status __ QCamera.Searching:
            ui.statusbar.sM..("Focusing...")
            ui.lockButton.sT..("Focusing...")
            indicationColor _ __.yellow
        ____ status __ QCamera.Locked:
            ui.lockButton.sT..("Unlock")
            ui.statusbar.sM..("Focused", 2000)
            indicationColor _ __.darkGreen
        ____ status __ QCamera.Unlocked:
            ui.lockButton.sT..("Focus")

            __ reason __ QCamera.LockFailed:
                ui.statusbar.sM..("Focus Failed", 2000)
                indicationColor _ __.red

        palette _ ui.lockButton.p..
        palette.sC..(?P...ButtonText, indicationColor)
        ui.lockButton.sP..(palette)

    ___ takeImage
        isCapturingImage _ T..
        imageCapture.capture()

    ___ startCamera
        camera.start()

    ___ stopCamera
        camera.s..

    ___ updateCaptureMode
        tabIndex _ ui.captureWidget.currentIndex()
        captureMode _ QCamera.CaptureStillImage __ tabIndex __ 0 ____ QCamera.CaptureVideo

        __ camera.isCaptureModeSupported(captureMode):
            camera.sCM..(captureMode)

    ___ updateCameraState  state):
        __ state __ QCamera.ActiveState:
            ui.actionStartCamera.sE.. F..
            ui.actionStopCamera.sE..( st.
            ui.captureWidget.sE..( st.
            ui.actionSettings.sE..( st.
        ____ state __ (QCamera.UnloadedState, QCamera.LoadedState):
            ui.actionStartCamera.sE..( st.
            ui.actionStopCamera.sE.. F..
            ui.captureWidget.sE.. F..
            ui.actionSettings.sE.. F..

    ___ updateRecorderState  state):
        __ state __ ?MR...StoppedState:
            ui.recordButton.sE..( st.
            ui.pauseButton.sE..( st.
            ui.stopButton.sE.. F..
        ____ state __ ?MR...PausedState:
            ui.recordButton.sE..( st.
            ui.pauseButton.sE.. F..
            ui.stopButton.sE..( st.
        ____ state __ ?MR...RS..:
            ui.recordButton.sE.. F..
            ui.pauseButton.sE..( st.
            ui.stopButton.sE..( st.

    ___ setExposureCompensation  index):
        camera.exposure().setExposureCompensation(index * 0.5)

    ___ displayRecorderError
        ?MB...w..  "Capture error",
                mediaRecorder.errorString())

    ___ displayCameraError
        ?MB...w..  "Camera error", camera.errorString())

    ___ updateCameraDevice  action):
        setCamera(action.data())

    ___ displayViewfinder
        ui.stackedWidget.sCI..(0)

    ___ displayCapturedImage
        ui.stackedWidget.sCI..(1)

    ___ readyForCapture  ready):
        ui.takeImageButton.sE..(ready)

    ___ imageSaved  id, fileName):
        isCapturingImage _ F..

        __ applicationExiting:
            c..

    ___ closeEvent  event):
        __ isCapturingImage:
            sE.. F..
            applicationExiting _ T..
            event.ignore()
        ____
            event.accept()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    camera _ Camera()
    camera.s..

    ___.e.. ?.e..
