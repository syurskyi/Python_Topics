# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_MainWindow o..
    ___ setupUi  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.r..(799, 600)
        horizontalLayout _ ?W...?HBL..(MainWindow)
        horizontalLayout.setObjectName("horizontalLayout")
        calendar _ ?W...QCalendarWidget(MainWindow)
        sizePolicy _ ?W...?SP..(?W...?SP...E.., ?W...?SP...E..)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(calendar.sizePolicy().hasHeightForWidth())
        calendar.sSP..(sizePolicy)
        calendar.setObjectName("calendar")
        horizontalLayout.aW..(calendar)
        verticalLayout _ ?W...?VBL..
        verticalLayout.setObjectName("verticalLayout")
        label _ ?W...?L..(MainWindow)
        label.setObjectName("label")
        verticalLayout.aW..(label)
        event_list _ ?W...QListWidget(MainWindow)
        event_list.setObjectName("event_list")
        verticalLayout.aW..(event_list)
        groupBox _ ?W...?GB..(MainWindow)
        groupBox.setObjectName("groupBox")
        gridLayout _ ?W...QGridLayout(groupBox)
        gridLayout.setObjectName("gridLayout")
        event_category _ ?W...?CB(groupBox)
        event_category.setObjectName("event_category")
        event_category.aI..("")
        event_category.aI..("")
        event_category.aI..("")
        event_category.aI..("")
        event_category.aI..("")
        event_category.aI..("")
        gridLayout.aW..(event_category, 1, 0, 1, 1)
        event_time _ ?W...?TE..(groupBox)
        event_time.setObjectName("event_time")
        gridLayout.aW..(event_time, 1, 1, 1, 1)
        event_detail _ ?W...?TE..(groupBox)
        event_detail.setObjectName("event_detail")
        gridLayout.aW..(event_detail, 2, 0, 1, 3)
        event_title _ ?W...QLineEdit(groupBox)
        event_title.setObjectName("event_title")
        gridLayout.aW..(event_title, 0, 0, 1, 3)
        allday_check _ ?W...QCheckBox(groupBox)
        allday_check.setObjectName("allday_check")
        gridLayout.aW..(allday_check, 1, 2, 1, 1)
        add_button _ ?W...?PB..(groupBox)
        add_button.setObjectName("add_button")
        gridLayout.aW..(add_button, 3, 1, 1, 1)
        del_button _ ?W...?PB..(groupBox)
        del_button.setObjectName("del_button")
        gridLayout.aW..(del_button, 3, 2, 1, 1)
        verticalLayout.aW..(groupBox)
        horizontalLayout.aL..(verticalLayout)

        retranslateUi(MainWindow)
        allday_check.t__['bool'].c..(event_time.sD..)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ ?C... ?CA...translate
        MainWindow.sWT..(_translate("MainWindow", "My Calendar App"))
        label.sT..(_translate("MainWindow", "Events on Date"))
        groupBox.setTitle(_translate("MainWindow", "Event"))
        event_category.setItemText(0, _translate("MainWindow", "Select Category…"))
        event_category.setItemText(1, _translate("MainWindow", "New…"))
        event_category.setItemText(2, _translate("MainWindow", "Work"))
        event_category.setItemText(3, _translate("MainWindow", "Meeting"))
        event_category.setItemText(4, _translate("MainWindow", "Doctor"))
        event_category.setItemText(5, _translate("MainWindow", "Family"))
        allday_check.sT..(_translate("MainWindow", "All Day"))
        add_button.sT..(_translate("MainWindow", "Add/Update"))
        del_button.sT..(_translate("MainWindow", "Delete"))

