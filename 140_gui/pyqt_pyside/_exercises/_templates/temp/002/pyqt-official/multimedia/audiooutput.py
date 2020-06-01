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


____ math ______ pi, sin
____ struct ______ pack

____ ?.?C.. ______ QByteArray, QIODevice, __, QTimer, qWarning
____ ?.QtMultimedia ______ (QAudio, QAudioDeviceInfo, QAudioFormat,
        QAudioOutput)
____ ?.?W.. ______ (?A.., QComboBox, QHBoxLayout, QLabel,
        QMainWindow, ?PB.., QSlider, QVBoxLayout, QWidget)


c_ Generator(QIODevice):

    ___ __init__  format, durationUs, sampleRate, parent):
        super(Generator, self).__init__(parent)

        self.m_pos _ 0
        self.m_buffer _ QByteArray()

        self.generateData(format, durationUs, sampleRate)

    ___ start(self):
        self.o..(QIODevice.ReadOnly)

    ___ stop(self):
        self.m_pos _ 0
        self.close()

    ___ generateData  format, durationUs, sampleRate):
        pack_format _ ''

        __ format.sampleSize() == 8:
            __ format.sampleType() == QAudioFormat.UnSignedInt:
                scaler _ lambda x: ((1.0 + x) / 2 * 255)
                pack_format _ 'B'
            ____ format.sampleType() == QAudioFormat.SignedInt:
                scaler _ lambda x: x * 127
                pack_format _ 'b'
        ____ format.sampleSize() == 16:
            __ format.sampleType() == QAudioFormat.UnSignedInt:
                scaler _ lambda x: (1.0 + x) / 2 * 65535
                pack_format _ '<H' __ format.byteOrder() == QAudioFormat.LittleEndian else '>H'
            ____ format.sampleType() == QAudioFormat.SignedInt:
                scaler _ lambda x: x * 32767
                pack_format _ '<h' __ format.byteOrder() == QAudioFormat.LittleEndian else '>h'

        assert(pack_format !_ '')

        channelBytes _ format.sampleSize() // 8
        sampleBytes _ format.channelCount() * channelBytes

        length _ (format.sampleRate() * format.channelCount() * (format.sampleSize() // 8)) * durationUs // 100000

        self.m_buffer.clear()
        sampleIndex _ 0
        factor _ 2 * pi * sampleRate / format.sampleRate()

        w__ length !_ 0:
            x _ sin((sampleIndex % format.sampleRate()) * factor)
            packed _ pack(pack_format, int(scaler(x)))

            for _ in range(format.channelCount()):
                self.m_buffer.ap..(packed)
                length -_ channelBytes

            sampleIndex +_ 1

    ___ readData  maxlen):
        data _ QByteArray()
        total _ 0

        w__ maxlen > total:
            chunk _ min(self.m_buffer.size() - self.m_pos, maxlen - total)
            data.ap..(self.m_buffer.mid(self.m_pos, chunk))
            self.m_pos _ (self.m_pos + chunk) % self.m_buffer.size()
            total +_ chunk

        r_ data.data()

    ___ writeData  data):
        r_ 0

    ___ bytesAvailable(self):
        r_ self.m_buffer.size() + super(Generator, self).bytesAvailable()


c_ AudioTest ?MW..

    PUSH_MODE_LABEL _ "Enable push mode"
    PULL_MODE_LABEL _ "Enable pull mode"
    SUSPEND_LABEL _ "Suspend playback"
    RESUME_LABEL _ "Resume playback"

    DurationSeconds _ 1
    ToneSampleRateHz _ 600
    DataSampleRateHz _ 44100

    ___ __init__(self):
        super(AudioTest, self).__init__()

        self.m_device _ QAudioDeviceInfo.defaultOutputDevice()
        self.m_output _ N..

        self.initializeWindow()
        self.initializeAudio()

    ___ initializeWindow(self):
        layout _ ?VBL..

        self.m_deviceBox _ QComboBox(activated_self.deviceChanged)
        for deviceInfo in QAudioDeviceInfo.availableDevices(QAudio.AudioOutput):
            self.m_deviceBox.addItem(deviceInfo.deviceName(), deviceInfo)

        layout.aW..(self.m_deviceBox)

        self.m_modeButton _ ?PB..(c___self.toggleMode)
        self.m_modeButton.sT..(self.PUSH_MODE_LABEL)

        layout.aW..(self.m_modeButton)

        self.m_suspendResumeButton _ ?PB..(
                c___self.toggleSuspendResume)
        self.m_suspendResumeButton.sT..(self.SUSPEND_LABEL)

        layout.aW..(self.m_suspendResumeButton)

        volumeBox _ QHBoxLayout()
        volumeLabel _ QLabel("Volume:")
        self.m_volumeSlider _ QSlider(__.Horizontal, minimum_0, maximum_100,
                singleStep_10, valueChanged_self.volumeChanged)
        volumeBox.aW..(volumeLabel)
        volumeBox.aW..(self.m_volumeSlider)

        layout.addLayout(volumeBox)

        window _ ?W..
        window.sL..(layout)

        self.sCW..(window)

    ___ initializeAudio(self):
        self.m_pullTimer _ QTimer  timeout_self.pullTimerExpired)
        self.m_pullMode _ True

        self.m_format _ QAudioFormat()
        self.m_format.setSampleRate(self.DataSampleRateHz)
        self.m_format.setChannelCount(1)
        self.m_format.setSampleSize(16)
        self.m_format.setCodec('audio/pcm')
        self.m_format.setByteOrder(QAudioFormat.LittleEndian)
        self.m_format.setSampleType(QAudioFormat.SignedInt)

        info _ QAudioDeviceInfo(QAudioDeviceInfo.defaultOutputDevice())
        __ no. info.isFormatSupported(self.m_format):
            qWarning("Default format not supported - trying to use nearest")
            self.m_format _ info.nearestFormat(self.m_format)

        self.m_generator _ Generator(self.m_format,
                self.DurationSeconds * 1000000, self.ToneSampleRateHz, self)

        self.createAudioOutput()

    ___ createAudioOutput(self):
        self.m_audioOutput _ QAudioOutput(self.m_device, self.m_format)
        self.m_audioOutput.notify.c..(self.notified)
        self.m_audioOutput.stateChanged.c..(self.handleStateChanged)

        self.m_generator.start()
        self.m_audioOutput.start(self.m_generator)
        self.m_volumeSlider.setValue(self.m_audioOutput.volume() * 100)

    ___ deviceChanged  index):
        self.m_pullTimer.stop()
        self.m_generator.stop()
        self.m_audioOutput.stop()
        self.m_device _ self.m_deviceBox.itemData(index)

        self.createAudioOutput()

    ___ volumeChanged  value):
        __ self.m_audioOutput __ no. N..:
            self.m_audioOutput.setVolume(value / 100.0)

    ___ notified(self):
        qWarning("bytesFree = %d, elapsedUSecs = %d, processedUSecs = %d" % (
                self.m_audioOutput.bytesFree(),
                self.m_audioOutput.elapsedUSecs(),
                self.m_audioOutput.processedUSecs()))

    ___ pullTimerExpired(self):
        __ self.m_audioOutput __ no. N.. and self.m_audioOutput.state() !_ QAudio.StoppedState:
            chunks _ self.m_audioOutput.bytesFree() // self.m_audioOutput.periodSize()
            for _ in range(chunks):
                data _ self.m_generator.read(self.m_audioOutput.periodSize())
                __ data __ N.. or le.(data) !_ self.m_audioOutput.periodSize
                    break

                self.m_output.w..(data)

    ___ toggleMode(self):
        self.m_pullTimer.stop()
        self.m_audioOutput.stop()

        __ self.m_pullMode:
            self.m_modeButton.sT..(self.PULL_MODE_LABEL)
            self.m_output _ self.m_audioOutput.start()
            self.m_pullMode _ False
            self.m_pullTimer.start(20)
        ____
            self.m_modeButton.sT..(self.PUSH_MODE_LABEL)
            self.m_pullMode _ True
            self.m_audioOutput.start(self.m_generator)

        self.m_suspendResumeButton.sT..(self.SUSPEND_LABEL)

    ___ toggleSuspendResume(self):
        __ self.m_audioOutput.state() == QAudio.SuspendedState:
            qWarning("status: Suspended, resume()")
            self.m_audioOutput.resume()
            self.m_suspendResumeButton.sT..(self.SUSPEND_LABEL)
        ____ self.m_audioOutput.state() == QAudio.ActiveState:
            qWarning("status: Active, suspend()")
            self.m_audioOutput.suspend()
            self.m_suspendResumeButton.sT..(self.RESUME_LABEL)
        ____ self.m_audioOutput.state() == QAudio.StoppedState:
            qWarning("status: Stopped, resume()")
            self.m_audioOutput.resume()
            self.m_suspendResumeButton.sT..(self.SUSPEND_LABEL)
        ____ self.m_audioOutput.state() == QAudio.IdleState:
            qWarning("status: IdleState")

    stateMap _ {
        QAudio.ActiveState: "ActiveState",
        QAudio.SuspendedState: "SuspendedState",
        QAudio.StoppedState: "StoppedState",
        QAudio.IdleState: "IdleState"}

    ___ handleStateChanged  state):
        qWarning("state = " + self.stateMap.g..(state, "Unknown"))


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    app.sAN..("Audio Output Test")

    audio _ AudioTest()
    audio.s..

    sys.exit(app.exec_())
