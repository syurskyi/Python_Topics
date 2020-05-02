# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\projectManager.ui'
#
# Created: Thu Oct 09 13:24:16 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

____ PyQt4 _____ ?C.., QtGui

try:
    _fromUtf8 = ?C...QString.fromUtf8
except AttributeError:
    ___ _fromUtf8(s
        return s

try:
    _encoding = QtGui.?A...UnicodeUTF8
    ___ _translate(context, text, disambig
        return QtGui.?A...translate(context, text, disambig, _encoding)
except AttributeError:
    ___ _translate(context, text, disambig
        return QtGui.?A...translate(context, text, disambig)

c_ Ui_projectManager(object
    ___ setupUi , projectManager
        projectManager.setObjectName(_fromUtf8("projectManager"))
        projectManager.resize(508, 384)
        centralwidget = QtGui.?W..(projectManager)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        verticalLayout_2 = QtGui.QVBoxLayout(centralwidget)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        splitter = QtGui.QSplitter(centralwidget)
        splitter.setOrientation(?C...Qt.Horizontal)
        splitter.setObjectName(_fromUtf8("splitter"))
        verticalLayoutWidget = QtGui.?W..(splitter)
        verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        projectList_ly = QtGui.QVBoxLayout(verticalLayoutWidget)
        projectList_ly.setMargin(0)
        projectList_ly.setObjectName(_fromUtf8("projectList_ly"))
        widget = QtGui.?W..(splitter)
        widget.setObjectName(_fromUtf8("widget"))
        verticalLayout = QtGui.QVBoxLayout(widget)
        verticalLayout.setMargin(0)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        create_btn = QtGui.?PB..(widget)
        create_btn.setObjectName(_fromUtf8("create_btn"))
        verticalLayout.addWidget(create_btn)
        templateEditor_btn = QtGui.?PB..(widget)
        templateEditor_btn.setObjectName(_fromUtf8("templateEditor_btn"))
        verticalLayout.addWidget(templateEditor_btn)
        groupBox = QtGui.QGroupBox(widget)
        groupBox.setObjectName(_fromUtf8("groupBox"))
        verticalLayout_3 = QtGui.QVBoxLayout(groupBox)
        verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        info_lb = QtGui.QLabel(groupBox)
        info_lb.setAlignment(?C...Qt.AlignLeading|?C...Qt.AlignLeft|?C...Qt.AlignTop)
        info_lb.setObjectName(_fromUtf8("info_lb"))
        verticalLayout_3.addWidget(info_lb)
        verticalLayout.addWidget(groupBox)
        settings_btn = QtGui.?PB..(widget)
        settings_btn.setObjectName(_fromUtf8("settings_btn"))
        verticalLayout.addWidget(settings_btn)
        verticalLayout_2.addWidget(splitter)
        projectManager.setCentralWidget(centralwidget)

        retranslateUi(projectManager)
        ?C...QMetaObject.connectSlotsByName(projectManager)

    ___ retranslateUi , projectManager
        projectManager.setWindowTitle(_translate("projectManager", "Project Manager", None))
        create_btn.sT..(_translate("projectManager", "Create Project", None))
        templateEditor_btn.sT..(_translate("projectManager", "Template Editor", None))
        groupBox.setTitle(_translate("projectManager", "Info", None))
        info_lb.sT..(_translate("projectManager", "TextLabel", None))
        settings_btn.sT..(_translate("projectManager", "Settings", None))

