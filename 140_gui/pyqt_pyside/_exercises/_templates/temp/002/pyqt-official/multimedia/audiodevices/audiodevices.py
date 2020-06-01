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


____ ?.QtMultimedia ______ QAudio, QAudioDeviceInfo, QAudioFormat
____ ?.?W.. ______ ?A.., QTableWidgetItem, QMainWindow

____ ui_audiodevicesbase ______ Ui_AudioDevicesBase


c_ AudioDevicesBase(QMainWindow, Ui_AudioDevicesBase):

    ___ __init__  parent_None):
        super(AudioDevicesBase, self).__init__(parent)

        self.setupUi(self)


c_ AudioTest(AudioDevicesBase):

    ___ __init__  parent_None):
        super(AudioTest, self).__init__(parent)

        self.deviceInfo _ QAudioDeviceInfo()
        self.settings _ QAudioFormat()
        self.mode _ QAudio.AudioOutput

        self.testButton.c__.c..(self.test)
        self.modeBox.activated.c..(self.modeChanged)
        self.deviceBox.activated.c..(self.deviceChanged)
        self.sampleRateBox.activated.c..(self.sampleRateChanged)
        self.channelsBox.activated.c..(self.channelChanged)
        self.codecsBox.activated.c..(self.codecChanged)
        self.sampleSizesBox.activated.c..(self.sampleSizeChanged)
        self.sampleTypesBox.activated.c..(self.sampleTypeChanged)
        self.endianBox.activated.c..(self.endianChanged)
        self.populateTableButton.c__.c..(self.populateTable)

        self.modeBox.setCurrentIndex(0)
        self.modeChanged(0)
        self.deviceBox.setCurrentIndex(0)
        self.deviceChanged(0)

    ___ test(self):
        self.testResult.clear()

        __ no. self.deviceInfo.isNull
            __ self.deviceInfo.isFormatSupported(self.settings):
                self.testResult.sT..("Success")
                self.nearestSampleRate.sT..("")
                self.nearestChannel.sT..("")
                self.nearestCodec.sT..("")
                self.nearestSampleSize.sT..("")
                self.nearestSampleType.sT..("")
                self.nearestEndian.sT..("")
            ____
                nearest _ self.deviceInfo.nearestFormat(self.settings)
                self.testResult.sT..("Failed")
                self.nearestSampleRate.sT..(str(nearest.sampleRate()))
                self.nearestChannel.sT..(str(nearest.channelCount()))
                self.nearestCodec.sT..(nearest.codec())
                self.nearestSampleSize.sT..(str(nearest.sampleSize()))
                self.nearestSampleType.sT..(
                        self.sampleTypeToString(nearest.sampleType()))
                self.nearestEndian.sT..(
                        self.endianToString(nearest.byteOrder()))
        ____
            self.testResult.sT..("No Device")

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
        self.testResult.clear()

        __ idx == 0:
            self.mode _ QAudio.AudioInput
        ____
            self.mode _ QAudio.AudioOutput

        self.deviceBox.clear()
        for deviceInfo in QAudioDeviceInfo.availableDevices(self.mode):
            self.deviceBox.addItem(deviceInfo.deviceName(), deviceInfo)

        self.deviceBox.setCurrentIndex(0)
        self.deviceChanged(0)

    ___ deviceChanged  idx):
        self.testResult.clear()

        __ self.deviceBox.count() == 0:
            r_

        self.deviceInfo _ self.deviceBox.itemData(idx)

        self.sampleRateBox.clear()
        sampleRatez _ self.deviceInfo.supportedSampleRates()
        self.sampleRateBox.addItems([str(sr) for sr in sampleRatez])
        __ len(sampleRatez) !_ 0:
            self.settings.setSampleRate(sampleRatez[0])

        self.channelsBox.clear()
        chz _ self.deviceInfo.supportedChannelCounts()
        self.channelsBox.addItems([str(ch) for ch in chz])
        __ len(chz) !_ 0:
            self.settings.setChannelCount(chz[0])

        self.codecsBox.clear()
        codecs _ self.deviceInfo.supportedCodecs()
        self.codecsBox.addItems([str(c) for c in codecs])
        __ len(codecs) !_ 0:
            self.settings.setCodec(codecs[0])

        # Create a failed condition.
        self.codecsBox.addItem("audio/test")

        self.sampleSizesBox.clear()
        sampleSizez _ self.deviceInfo.supportedSampleSizes()
        self.sampleSizesBox.addItems([str(ss) for ss in sampleSizez])
        __ len(sampleSizez) !_ 0:
            self.settings.setSampleSize(sampleSizez[0])

        self.sampleTypesBox.clear()
        sampleTypez _ self.deviceInfo.supportedSampleTypes()
        self.sampleTypesBox.addItems(
                [self.sampleTypeToString(st) for st in sampleTypez])
        __ len(sampleTypez) !_ 0:
            self.settings.setSampleType(sampleTypez[0])

        self.endianBox.clear()
        endianz _ self.deviceInfo.supportedByteOrders()
        self.endianBox.addItems([self.endianToString(e) for e in endianz])
        __ len(endianz) !_ 0:
            self.settings.setByteOrder(endianz[0])

        self.allFormatsTable.clearContents()

    ___ populateTable(self):
        row _ 0
        format _ QAudioFormat()

        for codec in self.deviceInfo.supportedCodecs
            format.setCodec(codec)

            for sampleRate in self.deviceInfo.supportedSampleRates
                format.setSampleRate(sampleRate)

                for channels in self.deviceInfo.supportedChannelCounts
                    format.setChannelCount(channels)

                    for sampleType in self.deviceInfo.supportedSampleTypes
                        format.setSampleType(sampleType)

                        for sampleSize in self.deviceInfo.supportedSampleSizes
                            format.setSampleSize(sampleSize)

                            for endian in self.deviceInfo.supportedByteOrders
                                format.setByteOrder(endian)

                                __ self.deviceInfo.isFormatSupported(format):
                                    self.allFormatsTable.setRowCount(row + 1)

                                    self.setFormatValue(row, 0, format.codec())
                                    self.setFormatValue(row, 1,
                                            str(format.sampleRate()))
                                    self.setFormatValue(row, 2,
                                            str(format.channelCount()))
                                    self.setFormatValue(row, 3,
                                            self.sampleTypeToString(
                                                    format.sampleType()))
                                    self.setFormatValue(row, 4,
                                            str(format.sampleSize()))
                                    self.setFormatValue(row, 5,
                                            self.endianToString(
                                                    format.byteOrder()))

                                    row +_ 1

    ___ setFormatValue  row, column, value):
        self.allFormatsTable.setItem(row, column, QTableWidgetItem(value))

    ___ sampleRateChanged  idx):
        self.settings.setSampleRate(int(self.sampleRateBox.itemText(idx)))

    ___ channelChanged  idx):
        self.settings.setChannelCount(int(self.channelsBox.itemText(idx)))

    ___ codecChanged  idx):
        self.settings.setCodec(self.codecsBox.itemText(idx))

    ___ sampleSizeChanged  idx):
        self.settings.setSampleSize(int(self.sampleSizesBox.itemText(idx)))

    ___ sampleTypeChanged  idx):
        sampleType _ int(self.sampleTypesBox.itemText(idx))

        __ sampleType == QAudioFormat.SignedInt:
            self.settings.setSampleType(QAudioFormat.SignedInt)
        ____ sampleType == QAudioFormat.UnSignedInt:
            self.settings.setSampleType(QAudioFormat.UnSignedInt)
        ____ sampleType == QAudioFormat.Float:
            self.settings.setSampleType(QAudioFormat.Float)

    ___ endianChanged  idx):
        endian _ int(self.endianBox.itemText(idx))

        __ endian == QAudioFormat.LittleEndian:
            self.settings.setByteOrder(QAudioFormat.LittleEndian)
        ____ endian == QAudioFormat.BigEndian:
            self.settings.setByteOrder(QAudioFormat.BigEndian)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    app.sAN..("Audio Device Test")

    audio _ AudioTest()
    audio.s..

    sys.exit(app.exec_())
