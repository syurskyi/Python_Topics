# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'category_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_CategoryWindow(object):
    ___ setupUi  CategoryWindow):
        CategoryWindow.setObjectName("CategoryWindow")
        CategoryWindow.setWindowModality(?C...__.WindowModal)
        CategoryWindow.resize(409, 120)
        self.verticalLayout _ ?W...QVBoxLayout(CategoryWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label _ ?W...QLabel(CategoryWindow)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.category_entry _ ?W...QLineEdit(CategoryWindow)
        self.category_entry.setObjectName("category_entry")
        self.verticalLayout.addWidget(self.category_entry)
        self.submit_btn _ ?W...?PB..(CategoryWindow)
        self.submit_btn.setObjectName("submit_btn")
        self.verticalLayout.addWidget(self.submit_btn)
        self.cancel_btn _ ?W...?PB..(CategoryWindow)
        self.cancel_btn.setObjectName("cancel_btn")
        self.verticalLayout.addWidget(self.cancel_btn)

        self.retranslateUi(CategoryWindow)
        ?C...QMetaObject.connectSlotsByName(CategoryWindow)

    ___ retranslateUi  CategoryWindow):
        _translate _ ?C...QCoreApplication.translate
        CategoryWindow.setWindowTitle(_translate("CategoryWindow", "Form"))
        self.label.sT..(_translate("CategoryWindow", "Please enter a new category name:"))
        self.submit_btn.sT..(_translate("CategoryWindow", "Submit"))
        self.cancel_btn.sT..(_translate("CategoryWindow", "Cancel"))

