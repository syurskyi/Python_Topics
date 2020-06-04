# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller.ui'
#
# Created: Fri May 31 18:58:37 2013
#      by: PyQt5 UI code generator 5.0-snapshot-dd808c1bcced
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Controller o..
    ___ setupUi  Controller):
        Controller.setObjectName("Controller")
        Controller.r..(255, 111)
        gridlayout _ ?W...QGridLayout(Controller)
        gridlayout.sCM..(9, 9, 9, 9)
        gridlayout.setSpacing(6)
        gridlayout.setObjectName("gridlayout")
        label _ ?W...?L..(Controller)
        label.setAlignment(?C...__.AlignCenter)
        label.setObjectName("label")
        gridlayout.aW..(label, 1, 1, 1, 1)
        decelerate _ ?W...?PB..(Controller)
        decelerate.setObjectName("decelerate")
        gridlayout.aW..(decelerate, 2, 1, 1, 1)
        accelerate _ ?W...?PB..(Controller)
        accelerate.setObjectName("accelerate")
        gridlayout.aW..(accelerate, 0, 1, 1, 1)
        right _ ?W...?PB..(Controller)
        right.setObjectName("right")
        gridlayout.aW..(right, 1, 2, 1, 1)
        left _ ?W...?PB..(Controller)
        left.setObjectName("left")
        gridlayout.aW..(left, 1, 0, 1, 1)

        retranslateUi(Controller)
        ?C...QMetaObject.connectSlotsByName(Controller)

    ___ retranslateUi  Controller):
        _translate _ ?C... ?CA...translate
        Controller.sWT..(_translate("Controller", "Controller"))
        label.sT..(_translate("Controller", "Controller"))
        decelerate.sT..(_translate("Controller", "Decelerate"))
        accelerate.sT..(_translate("Controller", "Accelerate"))
        right.sT..(_translate("Controller", "Right"))
        left.sT..(_translate("Controller", "Left"))

