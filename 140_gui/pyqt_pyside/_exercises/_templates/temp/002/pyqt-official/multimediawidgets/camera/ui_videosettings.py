# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videosettings.ui'
#
# Created: Fri Jun 28 11:48:14 2013
#      by: PyQt5 UI code generator 5.0-snapshot-478d7f271b71
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_VideoSettingsUi(object):
    ___ setupUi  VideoSettingsUi):
        VideoSettingsUi.setObjectName("VideoSettingsUi")
        VideoSettingsUi.r..(561, 369)
        gridLayout_4 _ ?W...QGridLayout(VideoSettingsUi)
        gridLayout_4.setObjectName("gridLayout_4")
        scrollArea _ ?W...QScrollArea(VideoSettingsUi)
        scrollArea.setFrameShape(?W...QFrame.NoFrame)
        scrollArea.setWidgetResizable(True)
        scrollArea.setObjectName("scrollArea")
        scrollAreaWidgetContents _ ?W...?W..
        scrollAreaWidgetContents.setGeometry(?C...QRect(0, 0, 543, 250))
        scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        gridLayout_3 _ ?W...QGridLayout(scrollAreaWidgetContents)
        gridLayout_3.setObjectName("gridLayout_3")
        groupBox _ ?W...QGroupBox(scrollAreaWidgetContents)
        groupBox.setObjectName("groupBox")
        gridLayout _ ?W...QGridLayout(groupBox)
        gridLayout.setObjectName("gridLayout")
        label_2 _ ?W...QLabel(groupBox)
        label_2.setObjectName("label_2")
        gridLayout.aW..(label_2, 0, 0, 1, 2)
        audioCodecBox _ ?W...?CB(groupBox)
        audioCodecBox.setObjectName("audioCodecBox")
        gridLayout.aW..(audioCodecBox, 1, 0, 1, 2)
        label_5 _ ?W...QLabel(groupBox)
        label_5.setObjectName("label_5")
        gridLayout.aW..(label_5, 2, 0, 1, 2)
        audioSampleRateBox _ ?W...?CB(groupBox)
        audioSampleRateBox.setObjectName("audioSampleRateBox")
        gridLayout.aW..(audioSampleRateBox, 3, 0, 1, 2)
        label_3 _ ?W...QLabel(groupBox)
        label_3.setObjectName("label_3")
        gridLayout.aW..(label_3, 4, 0, 1, 1)
        audioQualitySlider _ ?W...QSlider(groupBox)
        audioQualitySlider.setMaximum(4)
        audioQualitySlider.setOrientation(?C...__.Horizontal)
        audioQualitySlider.setObjectName("audioQualitySlider")
        gridLayout.aW..(audioQualitySlider, 4, 1, 1, 1)
        gridLayout_3.aW..(groupBox, 0, 0, 1, 1)
        groupBox_2 _ ?W...QGroupBox(scrollAreaWidgetContents)
        groupBox_2.setObjectName("groupBox_2")
        gridLayout_2 _ ?W...QGridLayout(groupBox_2)
        gridLayout_2.setObjectName("gridLayout_2")
        label_8 _ ?W...QLabel(groupBox_2)
        label_8.setObjectName("label_8")
        gridLayout_2.aW..(label_8, 0, 0, 1, 2)
        videoResolutionBox _ ?W...?CB(groupBox_2)
        videoResolutionBox.setObjectName("videoResolutionBox")
        gridLayout_2.aW..(videoResolutionBox, 1, 0, 1, 2)
        label_9 _ ?W...QLabel(groupBox_2)
        label_9.setObjectName("label_9")
        gridLayout_2.aW..(label_9, 2, 0, 1, 2)
        videoFramerateBox _ ?W...?CB(groupBox_2)
        videoFramerateBox.setObjectName("videoFramerateBox")
        gridLayout_2.aW..(videoFramerateBox, 3, 0, 1, 2)
        label_6 _ ?W...QLabel(groupBox_2)
        label_6.setObjectName("label_6")
        gridLayout_2.aW..(label_6, 4, 0, 1, 2)
        videoCodecBox _ ?W...?CB(groupBox_2)
        videoCodecBox.setObjectName("videoCodecBox")
        gridLayout_2.aW..(videoCodecBox, 5, 0, 1, 2)
        label_7 _ ?W...QLabel(groupBox_2)
        label_7.setObjectName("label_7")
        gridLayout_2.aW..(label_7, 6, 0, 1, 1)
        videoQualitySlider _ ?W...QSlider(groupBox_2)
        videoQualitySlider.setMaximum(4)
        videoQualitySlider.setOrientation(?C...__.Horizontal)
        videoQualitySlider.setObjectName("videoQualitySlider")
        gridLayout_2.aW..(videoQualitySlider, 6, 1, 1, 1)
        gridLayout_3.aW..(groupBox_2, 0, 1, 3, 1)
        label_4 _ ?W...QLabel(scrollAreaWidgetContents)
        label_4.setObjectName("label_4")
        gridLayout_3.aW..(label_4, 1, 0, 1, 1)
        containerFormatBox _ ?W...?CB(scrollAreaWidgetContents)
        containerFormatBox.setObjectName("containerFormatBox")
        gridLayout_3.aW..(containerFormatBox, 2, 0, 1, 1)
        scrollArea.setWidget(scrollAreaWidgetContents)
        gridLayout_4.aW..(scrollArea, 0, 0, 1, 1)
        spacerItem _ ?W...QSpacerItem(20, 14, ?W...QSizePolicy.Minimum, ?W...QSizePolicy.E..)
        gridLayout_4.aI..(spacerItem, 1, 0, 1, 1)
        buttonBox _ ?W...QDialogButtonBox(VideoSettingsUi)
        buttonBox.setOrientation(?C...__.Horizontal)
        buttonBox.setStandardButtons(?W...QDialogButtonBox.Cancel|?W...QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        gridLayout_4.aW..(buttonBox, 2, 0, 1, 1)

        retranslateUi(VideoSettingsUi)
        buttonBox.accepted.c..(VideoSettingsUi.accept)
        buttonBox.rejected.c..(VideoSettingsUi.reject)
        ?C...QMetaObject.connectSlotsByName(VideoSettingsUi)

    ___ retranslateUi  VideoSettingsUi):
        _translate _ ?C...QCoreApplication.translate
        VideoSettingsUi.sWT..(_translate("VideoSettingsUi", "Dialog"))
        groupBox.setTitle(_translate("VideoSettingsUi", "Audio"))
        label_2.sT..(_translate("VideoSettingsUi", "Audio Codec:"))
        label_5.sT..(_translate("VideoSettingsUi", "Sample Rate:"))
        label_3.sT..(_translate("VideoSettingsUi", "Quality:"))
        groupBox_2.setTitle(_translate("VideoSettingsUi", "Video"))
        label_8.sT..(_translate("VideoSettingsUi", "Resolution:"))
        label_9.sT..(_translate("VideoSettingsUi", "Framerate:"))
        label_6.sT..(_translate("VideoSettingsUi", "Video Codec:"))
        label_7.sT..(_translate("VideoSettingsUi", "Quality:"))
        label_4.sT..(_translate("VideoSettingsUi", "Container Format:"))

