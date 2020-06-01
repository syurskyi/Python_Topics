# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_MainWindow(object):
    ___ setupUi  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        self.horizontalLayout _ ?W...QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calendar _ ?W...QCalendarWidget(MainWindow)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Expanding, ?W...QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy)
        self.calendar.setObjectName("calendar")
        self.horizontalLayout.addWidget(self.calendar)
        self.verticalLayout _ ?W...QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label _ ?W...QLabel(MainWindow)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.event_list _ ?W...QListWidget(MainWindow)
        self.event_list.setObjectName("event_list")
        self.verticalLayout.addWidget(self.event_list)
        self.groupBox _ ?W...QGroupBox(MainWindow)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout _ ?W...QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.event_category _ ?W...QComboBox(self.groupBox)
        self.event_category.setObjectName("event_category")
        self.event_category.addItem("")
        self.event_category.addItem("")
        self.event_category.addItem("")
        self.event_category.addItem("")
        self.event_category.addItem("")
        self.event_category.addItem("")
        self.gridLayout.addWidget(self.event_category, 1, 0, 1, 1)
        self.event_time _ ?W...QTimeEdit(self.groupBox)
        self.event_time.setObjectName("event_time")
        self.gridLayout.addWidget(self.event_time, 1, 1, 1, 1)
        self.event_detail _ ?W...QTextEdit(self.groupBox)
        self.event_detail.setObjectName("event_detail")
        self.gridLayout.addWidget(self.event_detail, 2, 0, 1, 3)
        self.event_title _ ?W...QLineEdit(self.groupBox)
        self.event_title.setObjectName("event_title")
        self.gridLayout.addWidget(self.event_title, 0, 0, 1, 3)
        self.allday_check _ ?W...QCheckBox(self.groupBox)
        self.allday_check.setObjectName("allday_check")
        self.gridLayout.addWidget(self.allday_check, 1, 2, 1, 1)
        self.add_button _ ?W...?PB..(self.groupBox)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 3, 1, 1, 1)
        self.del_button _ ?W...?PB..(self.groupBox)
        self.del_button.setObjectName("del_button")
        self.gridLayout.addWidget(self.del_button, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(MainWindow)
        self.allday_check.toggled['bool'].c..(self.event_time.setDisabled)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ ?C...QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Calendar App"))
        self.label.sT..(_translate("MainWindow", "Events on Date"))
        self.groupBox.setTitle(_translate("MainWindow", "Event"))
        self.event_category.setItemText(0, _translate("MainWindow", "Select Category…"))
        self.event_category.setItemText(1, _translate("MainWindow", "New…"))
        self.event_category.setItemText(2, _translate("MainWindow", "Work"))
        self.event_category.setItemText(3, _translate("MainWindow", "Meeting"))
        self.event_category.setItemText(4, _translate("MainWindow", "Doctor"))
        self.event_category.setItemText(5, _translate("MainWindow", "Family"))
        self.allday_check.sT..(_translate("MainWindow", "All Day"))
        self.add_button.sT..(_translate("MainWindow", "Add/Update"))
        self.del_button.sT..(_translate("MainWindow", "Delete"))

