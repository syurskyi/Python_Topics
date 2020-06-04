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


____ ?.?M.. ______ QAudio, QAudioDeviceInfo, QAudioFormat
____ ?.?W.. ______ ?A.., ?TWI.., ?MW..

____ ui_audiodevicesbase ______ Ui_AudioDevicesBase


c_ AudioDevicesBase(?MW.., Ui_AudioDevicesBase):

    ___  -   parent_None):
        s__(AudioDevicesBase, self). - (parent)

        setupUi


c_ AudioTest(AudioDevicesBase):

    ___  -   parent_None):
        s__(AudioTest, self). - (parent)

        deviceInfo _ QAudioDeviceInfo()
        settings _ QAudioFormat()
        mode _ QAudio.AudioOutput

        testButton.c__.c..(test)
        modeBox.activated.c..(modeChanged)
        deviceBox.activated.c..(deviceChanged)
        sampleRateBox.activated.c..(sampleRateChanged)
        channelsBox.activated.c..(channelChanged)
        codecsBox.activated.c..(codecChanged)
        sampleSizesBox.activated.c..(sampleSizeChanged)
        sampleTypesBox.activated.c..(sampleTypeChanged)
        endianBox.activated.c..(endianChanged)
        populateTableButton.c__.c..(populateTable)

        modeBox.sCI..(0)
        modeChanged(0)
        deviceBox.sCI..(0)
        deviceChanged(0)

    ___ test
        testResult.c..

        __ no. deviceInfo.isNull
            __ deviceInfo.isFormatSupported(settings):
                testResult.sT..("Success")
                nearestSampleRate.sT..("")
                nearestChannel.sT..("")
                nearestCodec.sT..("")
                nearestSampleSize.sT..("")
                nearestSampleType.sT..("")
                nearestEndian.sT..("")
            ____
                nearest _ deviceInfo.nearestFormat(settings)
                testResult.sT..("Failed")
                nearestSampleRate.sT..(st.(nearest.sampleRate()))
                nearestChannel.sT..(st.(nearest.channelCount()))
                nearestCodec.sT..(nearest.codec())
                nearestSampleSize.sT..(st.(nearest.sampleSize()))
                nearestSampleType.sT..(
                        sampleTypeToString(nearest.sampleType()))
                nearestEndian.sT..(
                        endianToString(nearest.byteOrder()))
        ____
            testResult.sT..("No Device")

    sampleTypeMap _ {
        QAudioFormat.SignedInt: "SignedInt",
        QAudioFormat.UnSignedInt: "UnSignedInt",
        QAudioFormat.Float: "Float"
    }

    @classmethod
    ___ sampleTypeToString(cls, sampleType):
        r_ cls.sampleTypeMap.g..(sampleType, "Unknown")

    endianMap _ {
        QAudioFormat.LittleEndian: "LittleEndian",
        QAudioFormat.BigEndian: "BigEndian"
    }

    @classmethod
    ___ endianToString(cls, endian):
        r_ cls.endianMap.g..(endian, "Unknown")

    ___ modeChanged  idx):
        testResult.c..

        __ idx __ 0:
            mode _ QAudio.AudioInput
        ____
            mode _ QAudio.AudioOutput

        deviceBox.c..
        ___ deviceInfo __ QAudioDeviceInfo.availableDevices(mode):
            deviceBox.aI..(deviceInfo.deviceName(), deviceInfo)

        deviceBox.sCI..(0)
        deviceChanged(0)

    ___ deviceChanged  idx):
        testResult.c..

        __ deviceBox.count() __ 0:
            r_

        deviceInfo _ deviceBox.itemData(idx)

        sampleRateBox.c..
        sampleRatez _ deviceInfo.supportedSampleRates()
        sampleRateBox.aI..([st.(sr) ___ sr __ sampleRatez])
        __ le.(sampleRatez) !_ 0:
            settings.setSampleRate(sampleRatez[0])

        channelsBox.c..
        chz _ deviceInfo.supportedChannelCounts()
        channelsBox.aI..([st.(ch) ___ ch __ chz])
        __ le.(chz) !_ 0:
            settings.setChannelCount(chz[0])

        codecsBox.c..
        codecs _ deviceInfo.supportedCodecs()
        codecsBox.aI..([st.(c) ___ c __ codecs])
        __ le.(codecs) !_ 0:
            settings.setCodec(codecs[0])

        # Create a failed condition.
        codecsBox.aI..("audio/test")

        sampleSizesBox.c..
        sampleSizez _ deviceInfo.supportedSampleSizes()
        sampleSizesBox.aI..([st.(ss) ___ ss __ sampleSizez])
        __ le.(sampleSizez) !_ 0:
            settings.setSampleSize(sampleSizez[0])

        sampleTypesBox.c..
        sampleTypez _ deviceInfo.supportedSampleTypes()
        sampleTypesBox.aI..(
                [sampleTypeToString(st) ___ st __ sampleTypez])
        __ le.(sampleTypez) !_ 0:
            settings.setSampleType(sampleTypez[0])

        endianBox.c..
        endianz _ deviceInfo.supportedByteOrders()
        endianBox.aI..([endianToString(e) ___ e __ endianz])
        __ le.(endianz) !_ 0:
            settings.setByteOrder(endianz[0])

        allFormatsTable.clearContents()

    ___ populateTable
        row _ 0
        f.. _ QAudioFormat()

        ___ codec __ deviceInfo.supportedCodecs
            f...setCodec(codec)

            ___ sampleRate __ deviceInfo.supportedSampleRates
                f...setSampleRate(sampleRate)

                ___ channels __ deviceInfo.supportedChannelCounts
                    f...setChannelCount(channels)

                    ___ sampleType __ deviceInfo.supportedSampleTypes
                        f...setSampleType(sampleType)

                        ___ sampleSize __ deviceInfo.supportedSampleSizes
                            f...setSampleSize(sampleSize)

                            ___ endian __ deviceInfo.supportedByteOrders
                                f...setByteOrder(endian)

                                __ deviceInfo.isFormatSupported(f..):
                                    allFormatsTable.sRC..(row + 1)

                                    setFormatValue(row, 0, f...codec())
                                    setFormatValue(row, 1,
                                            st.(f...sampleRate()))
                                    setFormatValue(row, 2,
                                            st.(f...channelCount()))
                                    setFormatValue(row, 3,
                                            sampleTypeToString(
                                                    f...sampleType()))
                                    setFormatValue(row, 4,
                                            st.(f...sampleSize()))
                                    setFormatValue(row, 5,
                                            endianToString(
                                                    f...byteOrder()))

                                    row +_ 1

    ___ setFormatValue  row, column, value):
        allFormatsTable.setItem(row, column, ?TWI..(value))

    ___ sampleRateChanged  idx):
        settings.setSampleRate(in.(sampleRateBox.iT..(idx)))

    ___ channelChanged  idx):
        settings.setChannelCount(in.(channelsBox.iT..(idx)))

    ___ codecChanged  idx):
        settings.setCodec(codecsBox.iT..(idx))

    ___ sampleSizeChanged  idx):
        settings.setSampleSize(in.(sampleSizesBox.iT..(idx)))

    ___ sampleTypeChanged  idx):
        sampleType _ in.(sampleTypesBox.iT..(idx))

        __ sampleType __ QAudioFormat.SignedInt:
            settings.setSampleType(QAudioFormat.SignedInt)
        ____ sampleType __ QAudioFormat.UnSignedInt:
            settings.setSampleType(QAudioFormat.UnSignedInt)
        ____ sampleType __ QAudioFormat.Float:
            settings.setSampleType(QAudioFormat.Float)

    ___ endianChanged  idx):
        endian _ in.(endianBox.iT..(idx))

        __ endian __ QAudioFormat.LittleEndian:
            settings.setByteOrder(QAudioFormat.LittleEndian)
        ____ endian __ QAudioFormat.BigEndian:
            settings.setByteOrder(QAudioFormat.BigEndian)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    app.sAN..("Audio Device Test")

    audio _ AudioTest()
    audio.s..

    ___.e.. ?.e..
