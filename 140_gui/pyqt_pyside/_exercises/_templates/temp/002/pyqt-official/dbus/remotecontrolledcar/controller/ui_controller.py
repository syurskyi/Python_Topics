# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller.ui'
#
# Created: Fri May 31 18:58:37 2013
#      by: PyQt5 UI code generator 5.0-snapshot-dd808c1bcced
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, ?G.., ?W..

c_ Ui_Controller(object):
    ___ setupUi  Controller):
        Controller.setObjectName("Controller")
        Controller.resize(255, 111)
        self.gridlayout _ ?W...QGridLayout(Controller)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.label _ ?W...QLabel(Controller)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 1, 1, 1, 1)
        self.decelerate _ ?W...?PB..(Controller)
        self.decelerate.setObjectName("decelerate")
        self.gridlayout.addWidget(self.decelerate, 2, 1, 1, 1)
        self.accelerate _ ?W...?PB..(Controller)
        self.accelerate.setObjectName("accelerate")
        self.gridlayout.addWidget(self.accelerate, 0, 1, 1, 1)
        self.right _ ?W...?PB..(Controller)
        self.right.setObjectName("right")
        self.gridlayout.addWidget(self.right, 1, 2, 1, 1)
        self.left _ ?W...?PB..(Controller)
        self.left.setObjectName("left")
        self.gridlayout.addWidget(self.left, 1, 0, 1, 1)

        self.retranslateUi(Controller)
        QtCore.QMetaObject.connectSlotsByName(Controller)

    ___ retranslateUi  Controller):
        _translate _ QtCore.QCoreApplication.translate
        Controller.setWindowTitle(_translate("Controller", "Controller"))
        self.label.sT..(_translate("Controller", "Controller"))
        self.decelerate.sT..(_translate("Controller", "Decelerate"))
        self.accelerate.sT..(_translate("Controller", "Accelerate"))
        self.right.sT..(_translate("Controller", "Right"))
        self.left.sT..(_translate("Controller", "Left"))

