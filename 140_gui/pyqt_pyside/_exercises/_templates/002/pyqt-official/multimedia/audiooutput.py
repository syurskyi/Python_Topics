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


____ m__ ______ pi, sin
____ struct ______ pack

____ ?.?C.. ______ QByteArray, QIODevice, __, ?T.., qWarning
____ ?.?M.. ______ (QAudio, QAudioDeviceInfo, QAudioFormat,
        QAudioOutput)
____ ?.?W.. ______ (?A.., ?CB, ?HBL.., ?L..,
        ?MW.., ?PB.., ?S.., ?VBL.., ?W..)


c_ Generator(QIODevice):

    ___  -   f.., durationUs, sampleRate, parent):
        s__(Generator, self). - (parent)

        m_pos _ 0
        m_buffer _ QByteArray()

        generateData(f.., durationUs, sampleRate)

    ___ start
        o..(QIODevice.ReadOnly)

    ___ stop
        m_pos _ 0
        c..

    ___ generateData  f.., durationUs, sampleRate):
        pack_format _ ''

        __ f...sampleSize() __ 8:
            __ f...sampleType() __ QAudioFormat.UnSignedInt:
                scaler _ l___ x: ((1.0 + x) / 2 * 255)
                pack_format _ 'B'
            ____ f...sampleType() __ QAudioFormat.SignedInt:
                scaler _ l___ x: x * 127
                pack_format _ 'b'
        ____ f...sampleSize() __ 16:
            __ f...sampleType() __ QAudioFormat.UnSignedInt:
                scaler _ l___ x: (1.0 + x) / 2 * 65535
                pack_format _ '<H' __ f...byteOrder() __ QAudioFormat.LittleEndian ____ '>H'
            ____ f...sampleType() __ QAudioFormat.SignedInt:
                scaler _ l___ x: x * 32767
                pack_format _ '<h' __ f...byteOrder() __ QAudioFormat.LittleEndian ____ '>h'

        assert(pack_format !_ '')

        channelBytes _ f...sampleSize() // 8
        sampleBytes _ f...channelCount() * channelBytes

        length _ (f...sampleRate() * f...channelCount() * (f...sampleSize() // 8)) * durationUs // 100000

        m_buffer.c..
        sampleIndex _ 0
        factor _ 2 * pi * sampleRate / f...sampleRate()

        w__ length !_ 0:
            x _ sin((sampleIndex % f...sampleRate()) * factor)
            packed _ pack(pack_format, in.(scaler(x)))

            ___ _ __ ra..(f...channelCount()):
                m_buffer.ap..(packed)
                length -_ channelBytes

            sampleIndex +_ 1

    ___ readData  maxlen):
        data _ QByteArray()
        total _ 0

        w__ maxlen > total:
            chunk _ min(m_buffer.size() - m_pos, maxlen - total)
            data.ap..(m_buffer.mid(m_pos, chunk))
            m_pos _ (m_pos + chunk) % m_buffer.size()
            total +_ chunk

        r_ data.data()

    ___ writeData  data):
        r_ 0

    ___ bA..
        r_ m_buffer.size() + s__(Generator, self).bA..()


c_ AudioTest ?MW..

    PUSH_MODE_LABEL _ "Enable push mode"
    PULL_MODE_LABEL _ "Enable pull mode"
    SUSPEND_LABEL _ "Suspend playback"
    RESUME_LABEL _ "Resume playback"

    DurationSeconds _ 1
    ToneSampleRateHz _ 600
    DataSampleRateHz _ 44100

    ___  - 
        s__(AudioTest, self). - ()

        m_device _ QAudioDeviceInfo.defaultOutputDevice()
        m_output _ N..

        initializeWindow()
        initializeAudio()

    ___ initializeWindow
        layout _ ?VBL..

        m_deviceBox _ ?CB(activated_self.deviceChanged)
        ___ deviceInfo __ QAudioDeviceInfo.availableDevices(QAudio.AudioOutput):
            m_deviceBox.aI..(deviceInfo.deviceName(), deviceInfo)

        layout.aW..(m_deviceBox)

        m_modeButton _ ?PB..(c___self.toggleMode)
        m_modeButton.sT..(PUSH_MODE_LABEL)

        layout.aW..(m_modeButton)

        m_suspendResumeButton _ ?PB..(
                c___self.toggleSuspendResume)
        m_suspendResumeButton.sT..(SUSPEND_LABEL)

        layout.aW..(m_suspendResumeButton)

        volumeBox _ ?HBL..
        volumeLabel _ ?L..("Volume:")
        m_volumeSlider _ ?S..(__.H.., minimum_0, maximum_100,
                singleStep_10, valueChanged_self.volumeChanged)
        volumeBox.aW..(volumeLabel)
        volumeBox.aW..(m_volumeSlider)

        layout.aL..(volumeBox)

        window _ ?W..
        window.sL..(layout)

        sCW..(window)

    ___ initializeAudio
        m_pullTimer _ ?T..  timeout_self.pullTimerExpired)
        m_pullMode _ T..

        m_format _ QAudioFormat()
        m_format.setSampleRate(DataSampleRateHz)
        m_format.setChannelCount(1)
        m_format.setSampleSize(16)
        m_format.setCodec('audio/pcm')
        m_format.setByteOrder(QAudioFormat.LittleEndian)
        m_format.setSampleType(QAudioFormat.SignedInt)

        info _ QAudioDeviceInfo(QAudioDeviceInfo.defaultOutputDevice())
        __ no. info.isFormatSupported(m_format):
            qWarning("Default format not supported - trying to use nearest")
            m_format _ i...nearestFormat(m_format)

        m_generator _ Generator(m_format,
                DurationSeconds * 1000000, ToneSampleRateHz, self)

        createAudioOutput()

    ___ createAudioOutput
        m_audioOutput _ QAudioOutput(m_device, m_format)
        m_audioOutput.notify.c..(notified)
        m_audioOutput.stateChanged.c..(handleStateChanged)

        m_generator.start()
        m_audioOutput.start(m_generator)
        m_volumeSlider.sV..(m_audioOutput.volume() * 100)

    ___ deviceChanged  index):
        m_pullTimer.s..
        m_generator.s..
        m_audioOutput.s..
        m_device _ m_deviceBox.itemData(index)

        createAudioOutput()

    ___ volumeChanged  value):
        __ m_audioOutput __ no. N..:
            m_audioOutput.setVolume(value / 100.0)

    ___ notified
        qWarning("bytesFree = %d, elapsedUSecs = %d, processedUSecs = %d" % (
                m_audioOutput.bytesFree(),
                m_audioOutput.elapsedUSecs(),
                m_audioOutput.processedUSecs()))

    ___ pullTimerExpired
        __ m_audioOutput __ no. N.. and m_audioOutput.s.. !_ QAudio.StoppedState:
            chunks _ m_audioOutput.bytesFree() // m_audioOutput.periodSize()
            ___ _ __ ra..(chunks):
                data _ m_generator.read(m_audioOutput.periodSize())
                __ data __ N.. or le.(data) !_ m_audioOutput.periodSize
                    break

                m_output.w..(data)

    ___ toggleMode
        m_pullTimer.s..
        m_audioOutput.s..

        __ m_pullMode:
            m_modeButton.sT..(PULL_MODE_LABEL)
            m_output _ m_audioOutput.start()
            m_pullMode _ F..
            m_pullTimer.start(20)
        ____
            m_modeButton.sT..(PUSH_MODE_LABEL)
            m_pullMode _ T..
            m_audioOutput.start(m_generator)

        m_suspendResumeButton.sT..(SUSPEND_LABEL)

    ___ toggleSuspendResume
        __ m_audioOutput.s.. __ QAudio.SuspendedState:
            qWarning("status: Suspended, resume()")
            m_audioOutput.resume()
            m_suspendResumeButton.sT..(SUSPEND_LABEL)
        ____ m_audioOutput.s.. __ QAudio.ActiveState:
            qWarning("status: Active, suspend()")
            m_audioOutput.suspend()
            m_suspendResumeButton.sT..(RESUME_LABEL)
        ____ m_audioOutput.s.. __ QAudio.StoppedState:
            qWarning("status: Stopped, resume()")
            m_audioOutput.resume()
            m_suspendResumeButton.sT..(SUSPEND_LABEL)
        ____ m_audioOutput.s.. __ QAudio.IdleState:
            qWarning("status: IdleState")

    stateMap _ {
        QAudio.ActiveState: "ActiveState",
        QAudio.SuspendedState: "SuspendedState",
        QAudio.StoppedState: "StoppedState",
        QAudio.IdleState: "IdleState"}

    ___ handleStateChanged  state):
        qWarning("state = " + stateMap.g..(state, "Unknown"))


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    app.sAN..("Audio Output Test")

    audio _ AudioTest()
    audio.s..

    ___.e.. ?.e..
