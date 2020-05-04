# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\projectManager.ui'
#
# Created: Thu Oct 09 13:24:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ ? _____ ?C.., ?G..

c_ Ui_projectManager(object
    ___ setupUi , projectManager
        projectManager.setObjectName("projectManager")
        projectManager.r..(508, 384)
        centralwidget _ ?G...?W..(projectManager)
        centralwidget.setObjectName("centralwidget")
        verticalLayout_2 _ ?G...QVBoxLayout(centralwidget)
        verticalLayout_2.setObjectName("verticalLayout_2")
        splitter _ ?G...QSplitter(centralwidget)
        splitter.setOrientation(?C...__.Horizontal)
        splitter.setObjectName("splitter")
        verticalLayoutWidget _ ?G...?W..(splitter)
        verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        projectList_ly _ ?G...QVBoxLayout(verticalLayoutWidget)
        projectList_ly.setContentsMargins(0, 0, 0, 0)
        projectList_ly.setObjectName("projectList_ly")
        widget _ ?G...?W..(splitter)
        widget.setObjectName("widget")
        verticalLayout _ ?G...QVBoxLayout(widget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        create_btn _ ?G...?PB..(widget)
        create_btn.setObjectName("create_btn")
        verticalLayout.addWidget(create_btn)
        templateEditor_btn _ ?G...?PB..(widget)
        templateEditor_btn.setObjectName("templateEditor_btn")
        verticalLayout.addWidget(templateEditor_btn)
        groupBox _ ?G...QGroupBox(widget)
        groupBox.setObjectName("groupBox")
        verticalLayout_3 _ ?G...QVBoxLayout(groupBox)
        verticalLayout_3.setObjectName("verticalLayout_3")
        info_lb _ ?G...QLabel(groupBox)
        info_lb.setAlignment(?C...__.AlignLeading|?C...__.AlignLeft|?C...__.AlignTop)
        info_lb.setObjectName("info_lb")
        verticalLayout_3.addWidget(info_lb)
        verticalLayout.addWidget(groupBox)
        settings_btn _ ?G...?PB..(widget)
        settings_btn.setObjectName("settings_btn")
        verticalLayout.addWidget(settings_btn)
        verticalLayout_2.addWidget(splitter)
        projectManager.setCentralWidget(centralwidget)

        retranslateUi(projectManager)
        ?C...QMetaObject.connectSlotsByName(projectManager)

    ___ retranslateUi , projectManager
        projectManager.setWindowTitle(?G...?A...translate("projectManager", "Project Manager", N.., ?G...?A...UnicodeUTF8))
        create_btn.sT..(?G...?A...translate("projectManager", "Create Project", N.., ?G...?A...UnicodeUTF8))
        templateEditor_btn.sT..(?G...?A...translate("projectManager", "Template Editor", N.., ?G...?A...UnicodeUTF8))
        groupBox.setTitle(?G...?A...translate("projectManager", "Info", N.., ?G...?A...UnicodeUTF8))
        info_lb.sT..(?G...?A...translate("projectManager", "TextLabel", N.., ?G...?A...UnicodeUTF8))
        settings_btn.sT..(?G...?A...translate("projectManager", "Settings", N.., ?G...?A...UnicodeUTF8))

