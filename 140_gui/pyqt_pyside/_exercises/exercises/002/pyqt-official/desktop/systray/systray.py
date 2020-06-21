#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
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


____ ?.?G.. ______ ?I..
____ ?.?W.. ______ (?A.., ?A.., QCheckBox, ?CB,
        ?D.., QGridLayout, ?GB.., ?HBL.., ?L.., QLineEdit,
        ?MB.., ?M.., ?PB.., SB.., ?S.., QSystemTrayIcon,
        ?TE.., ?VBL..)

______ systray_rc


c_ Window(?D..):
    ___  -
        s__(Window, self). - ()

        createIconGroupBox()
        createMessageGroupBox()

        iconLabel.sMW..(durationLabel.sH..().width())

        createActions()
        createTrayIcon()

        showMessageButton.c__.c..(sM..)
        showIconCheckBox.t__.c..(trayIcon.setVisible)
        iconComboBox.currentIndexChanged.c..(sI..)
        trayIcon.messageClicked.c..(messageClicked)
        trayIcon.activated.c..(iconActivated)

        mainLayout _ ?VBL..
        mainLayout.aW..(iconGroupBox)
        mainLayout.aW..(messageGroupBox)
        sL..(mainLayout)

        iconComboBox.sCI..(1)
        trayIcon.s..

        sWT..("Systray")
        r..(400, 300)

    ___ setVisible  visible):
        minimizeAction.sE..(visible)
        maximizeAction.sE..(no. isMaximized())
        restoreAction.sE..(isMaximized() or no. visible)
        s__(Window, self).setVisible(visible)

    ___ closeEvent  event):
        __ trayIcon.isVisible
            ?MB...i..  "Systray",
                    "The program will keep running in the system tray. To "
                    "terminate the program, choose <b>Quit</b> in the "
                    "context menu of the system tray entry.")
            hide()
            event.ignore()

    ___ sI..  index):
        icon _ iconComboBox.itemIcon(index)
        trayIcon.sI..(icon)
        sWI..(icon)

        trayIcon.sTT..(iconComboBox.iT..(index))

    ___ iconActivated  reason):
        __ reason __ (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            iconComboBox.sCI..(
                    (iconComboBox.currentIndex() + 1)
                    % iconComboBox.count())
        ____ reason __ QSystemTrayIcon.MiddleClick:
            sM..()

    ___ sM..
        icon _ QSystemTrayIcon.MessageIcon(
                typeComboBox.itemData(typeComboBox.currentIndex()))
        trayIcon.sM..(titleEdit.t__(),
                bodyEdit.toPlainText(), icon,
                durationSpinBox.v.. * 1000)

    ___ messageClicked
        ?MB...i..(N.., "Systray",
                "Sorry, I already gave what help I could.\nMaybe you should "
                "try asking a human?")

    ___ createIconGroupBox
        iconGroupBox _ ?GB..("Tray Icon")

        iconLabel _ ?L..("Icon:")

        iconComboBox _ ?CB()
        iconComboBox.aI..(?I..(':/images/bad.png'), "Bad")
        iconComboBox.aI..(?I..(':/images/heart.png'), "Heart")
        iconComboBox.aI..(?I..(':/images/trash.png'), "Trash")

        showIconCheckBox _ QCheckBox("Show icon")
        showIconCheckBox.sC__( st.

        iconLayout _ ?HBL..
        iconLayout.aW..(iconLabel)
        iconLayout.aW..(iconComboBox)
        iconLayout.addStretch()
        iconLayout.aW..(showIconCheckBox)
        iconGroupBox.sL..(iconLayout)

    ___ createMessageGroupBox
        messageGroupBox _ ?GB..("Balloon Message")

        typeLabel _ ?L..("Type:")

        typeComboBox _ ?CB()
        typeComboBox.aI..("None", QSystemTrayIcon.NoIcon)
        typeComboBox.aI..(style().standardIcon(
                ?S...SP_MessageBoxInformation), "Information",
                QSystemTrayIcon.Information)
        typeComboBox.aI..(style().standardIcon(
                ?S...SP_MessageBoxWarning), "Warning",
                QSystemTrayIcon.Warning)
        typeComboBox.aI..(style().standardIcon(
                ?S...SP_MessageBoxCritical), "Critical",
                QSystemTrayIcon.Critical)
        typeComboBox.sCI..(1)

        durationLabel _ ?L..("Duration:")

        durationSpinBox _ SB..()
        durationSpinBox.setRange(5, 60)
        durationSpinBox.setSuffix(" s")
        durationSpinBox.sV..(15)

        durationWarningLabel _ ?L..("(some systems might ignore this hint)")
        durationWarningLabel.setIndent(10)

        titleLabel _ ?L..("Title:")

        titleEdit _ QLineEdit("Cannot connect to network")

        bodyLabel _ ?L..("Body:")

        bodyEdit _ ?TE..()
        bodyEdit.sPT..("Don't believe me. Honestly, I don't have "
                "a clue.\nClick this balloon for details.")

        showMessageButton _ ?PB..("Show Message")
        showMessageButton.setDefault( st.

        messageLayout _ QGridLayout()
        messageLayout.aW..(typeLabel, 0, 0)
        messageLayout.aW..(typeComboBox, 0, 1, 1, 2)
        messageLayout.aW..(durationLabel, 1, 0)
        messageLayout.aW..(durationSpinBox, 1, 1)
        messageLayout.aW..(durationWarningLabel, 1, 2, 1, 3)
        messageLayout.aW..(titleLabel, 2, 0)
        messageLayout.aW..(titleEdit, 2, 1, 1, 4)
        messageLayout.aW..(bodyLabel, 3, 0)
        messageLayout.aW..(bodyEdit, 3, 1, 2, 4)
        messageLayout.aW..(showMessageButton, 5, 4)
        messageLayout.setColumnStretch(3, 1)
        messageLayout.setRowStretch(4, 1)
        messageGroupBox.sL..(messageLayout)

    ___ createActions
        minimizeAction _ ?A..("Mi&nimize", self, triggered_self.hide)
        maximizeAction _ ?A..("Ma&ximize", self,
                triggered_self.showMaximized)
        restoreAction _ ?A..("&Restore", self,
                triggered_self.showNormal)
        quitAction _ ?A..("&Quit", self,
                triggered_QApplication.i.. .quit)

    ___ createTrayIcon
         trayIconMenu _ ?M..
         trayIconMenu.aA..(minimizeAction)
         trayIconMenu.aA..(maximizeAction)
         trayIconMenu.aA..(restoreAction)
         trayIconMenu.aS..)
         trayIconMenu.aA..(quitAction)

         trayIcon _ QSystemTrayIcon
         trayIcon.setContextMenu(trayIconMenu)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    __ no. QSystemTrayIcon.isSystemTrayAvailable
        ?MB...c..(N.., "Systray",
                "I couldn't detect any system tray on this system.")
        ___.e..(1)

    ?A...setQuitOnLastWindowClosed F..

    window _ Window()
    window.s..
    ___.e.. ?.e..
