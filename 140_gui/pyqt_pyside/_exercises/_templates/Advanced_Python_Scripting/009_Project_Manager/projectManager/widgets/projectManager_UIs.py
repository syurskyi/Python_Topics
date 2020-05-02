# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\projectManager.ui'
#
# Created: Thu Oct 09 13:24:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., QtGui

c_ Ui_projectManager(object
    ___ setupUi , projectManager
        projectManager.setObjectName("projectManager")
        projectManager.resize(508, 384)
        centralwidget = QtGui.?W..(projectManager)
        centralwidget.setObjectName("centralwidget")
        verticalLayout_2 = QtGui.QVBoxLayout(centralwidget)
        verticalLayout_2.setObjectName("verticalLayout_2")
        splitter = QtGui.QSplitter(centralwidget)
        splitter.setOrientation(?C...Qt.Horizontal)
        splitter.setObjectName("splitter")
        verticalLayoutWidget = QtGui.?W..(splitter)
        verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        projectList_ly = QtGui.QVBoxLayout(verticalLayoutWidget)
        projectList_ly.setContentsMargins(0, 0, 0, 0)
        projectList_ly.setObjectName("projectList_ly")
        widget = QtGui.?W..(splitter)
        widget.setObjectName("widget")
        verticalLayout = QtGui.QVBoxLayout(widget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        create_btn = QtGui.?PB..(widget)
        create_btn.setObjectName("create_btn")
        verticalLayout.addWidget(create_btn)
        templateEditor_btn = QtGui.?PB..(widget)
        templateEditor_btn.setObjectName("templateEditor_btn")
        verticalLayout.addWidget(templateEditor_btn)
        groupBox = QtGui.QGroupBox(widget)
        groupBox.setObjectName("groupBox")
        verticalLayout_3 = QtGui.QVBoxLayout(groupBox)
        verticalLayout_3.setObjectName("verticalLayout_3")
        info_lb = QtGui.QLabel(groupBox)
        info_lb.setAlignment(?C...Qt.AlignLeading|?C...Qt.AlignLeft|?C...Qt.AlignTop)
        info_lb.setObjectName("info_lb")
        verticalLayout_3.addWidget(info_lb)
        verticalLayout.addWidget(groupBox)
        settings_btn = QtGui.?PB..(widget)
        settings_btn.setObjectName("settings_btn")
        verticalLayout.addWidget(settings_btn)
        verticalLayout_2.addWidget(splitter)
        projectManager.setCentralWidget(centralwidget)

        retranslateUi(projectManager)
        ?C...QMetaObject.connectSlotsByName(projectManager)

    ___ retranslateUi , projectManager
        projectManager.setWindowTitle(QtGui.?A...translate("projectManager", "Project Manager", None, QtGui.?A...UnicodeUTF8))
        create_btn.sT..(QtGui.?A...translate("projectManager", "Create Project", None, QtGui.?A...UnicodeUTF8))
        templateEditor_btn.sT..(QtGui.?A...translate("projectManager", "Template Editor", None, QtGui.?A...UnicodeUTF8))
        groupBox.setTitle(QtGui.?A...translate("projectManager", "Info", None, QtGui.?A...UnicodeUTF8))
        info_lb.sT..(QtGui.?A...translate("projectManager", "TextLabel", None, QtGui.?A...UnicodeUTF8))
        settings_btn.sT..(QtGui.?A...translate("projectManager", "Settings", None, QtGui.?A...UnicodeUTF8))

