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


____ ?.?G.. ______ QIcon
____ ?.?W.. ______ (?A.., ?A.., QCheckBox, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        ?MB.., QMenu, ?PB.., QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout)

______ systray_rc


c_ Window(QDialog):
    ___ __init__(self):
        super(Window, self).__init__()

        self.createIconGroupBox()
        self.createMessageGroupBox()

        self.iconLabel.setMinimumWidth(self.durationLabel.sizeHint().width())

        self.createActions()
        self.createTrayIcon()

        self.showMessageButton.c__.c..(self.showMessage)
        self.showIconCheckBox.toggled.c..(self.trayIcon.setVisible)
        self.iconComboBox.currentIndexChanged.c..(self.setIcon)
        self.trayIcon.messageClicked.c..(self.messageClicked)
        self.trayIcon.activated.c..(self.iconActivated)

        mainLayout _ ?VBL..
        mainLayout.aW..(self.iconGroupBox)
        mainLayout.aW..(self.messageGroupBox)
        self.sL..(mainLayout)

        self.iconComboBox.setCurrentIndex(1)
        self.trayIcon.s..

        self.setWindowTitle("Systray")
        self.resize(400, 300)

    ___ setVisible  visible):
        self.minimizeAction.setEnabled(visible)
        self.maximizeAction.setEnabled(no. self.isMaximized())
        self.restoreAction.setEnabled(self.isMaximized() or no. visible)
        super(Window, self).setVisible(visible)

    ___ closeEvent  event):
        __ self.trayIcon.isVisible
            ?MB...information  "Systray",
                    "The program will keep running in the system tray. To "
                    "terminate the program, choose <b>Quit</b> in the "
                    "context menu of the system tray entry.")
            self.hide()
            event.ignore()

    ___ setIcon  index):
        icon _ self.iconComboBox.itemIcon(index)
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)

        self.trayIcon.setToolTip(self.iconComboBox.itemText(index))

    ___ iconActivated  reason):
        __ reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            self.iconComboBox.setCurrentIndex(
                    (self.iconComboBox.currentIndex() + 1)
                    % self.iconComboBox.count())
        ____ reason == QSystemTrayIcon.MiddleClick:
            self.showMessage()

    ___ showMessage(self):
        icon _ QSystemTrayIcon.MessageIcon(
                self.typeComboBox.itemData(self.typeComboBox.currentIndex()))
        self.trayIcon.showMessage(self.titleEdit.t__(),
                self.bodyEdit.toPlainText(), icon,
                self.durationSpinBox.value() * 1000)

    ___ messageClicked(self):
        ?MB...information(N.., "Systray",
                "Sorry, I already gave what help I could.\nMaybe you should "
                "try asking a human?")

    ___ createIconGroupBox(self):
        self.iconGroupBox _ QGroupBox("Tray Icon")

        self.iconLabel _ QLabel("Icon:")

        self.iconComboBox _ QComboBox()
        self.iconComboBox.addItem(QIcon(':/images/bad.png'), "Bad")
        self.iconComboBox.addItem(QIcon(':/images/heart.png'), "Heart")
        self.iconComboBox.addItem(QIcon(':/images/trash.png'), "Trash")

        self.showIconCheckBox _ QCheckBox("Show icon")
        self.showIconCheckBox.setChecked(True)

        iconLayout _ QHBoxLayout()
        iconLayout.aW..(self.iconLabel)
        iconLayout.aW..(self.iconComboBox)
        iconLayout.addStretch()
        iconLayout.aW..(self.showIconCheckBox)
        self.iconGroupBox.sL..(iconLayout)

    ___ createMessageGroupBox(self):
        self.messageGroupBox _ QGroupBox("Balloon Message")

        typeLabel _ QLabel("Type:")

        self.typeComboBox _ QComboBox()
        self.typeComboBox.addItem("None", QSystemTrayIcon.NoIcon)
        self.typeComboBox.addItem(self.style().standardIcon(
                QStyle.SP_MessageBoxInformation), "Information",
                QSystemTrayIcon.Information)
        self.typeComboBox.addItem(self.style().standardIcon(
                QStyle.SP_MessageBoxWarning), "Warning",
                QSystemTrayIcon.Warning)
        self.typeComboBox.addItem(self.style().standardIcon(
                QStyle.SP_MessageBoxCritical), "Critical",
                QSystemTrayIcon.Critical)
        self.typeComboBox.setCurrentIndex(1)

        self.durationLabel _ QLabel("Duration:")

        self.durationSpinBox _ QSpinBox()
        self.durationSpinBox.setRange(5, 60)
        self.durationSpinBox.setSuffix(" s")
        self.durationSpinBox.setValue(15)

        durationWarningLabel _ QLabel("(some systems might ignore this hint)")
        durationWarningLabel.setIndent(10)

        titleLabel _ QLabel("Title:")

        self.titleEdit _ QLineEdit("Cannot connect to network")

        bodyLabel _ QLabel("Body:")

        self.bodyEdit _ QTextEdit()
        self.bodyEdit.sPT..("Don't believe me. Honestly, I don't have "
                "a clue.\nClick this balloon for details.")

        self.showMessageButton _ ?PB..("Show Message")
        self.showMessageButton.setDefault(True)

        messageLayout _ QGridLayout()
        messageLayout.aW..(typeLabel, 0, 0)
        messageLayout.aW..(self.typeComboBox, 0, 1, 1, 2)
        messageLayout.aW..(self.durationLabel, 1, 0)
        messageLayout.aW..(self.durationSpinBox, 1, 1)
        messageLayout.aW..(durationWarningLabel, 1, 2, 1, 3)
        messageLayout.aW..(titleLabel, 2, 0)
        messageLayout.aW..(self.titleEdit, 2, 1, 1, 4)
        messageLayout.aW..(bodyLabel, 3, 0)
        messageLayout.aW..(self.bodyEdit, 3, 1, 2, 4)
        messageLayout.aW..(self.showMessageButton, 5, 4)
        messageLayout.setColumnStretch(3, 1)
        messageLayout.setRowStretch(4, 1)
        self.messageGroupBox.sL..(messageLayout)

    ___ createActions(self):
        self.minimizeAction _ ?A..("Mi&nimize", self, triggered_self.hide)
        self.maximizeAction _ ?A..("Ma&ximize", self,
                triggered_self.showMaximized)
        self.restoreAction _ ?A..("&Restore", self,
                triggered_self.showNormal)
        self.quitAction _ ?A..("&Quit", self,
                triggered_QApplication.instance().quit)

    ___ createTrayIcon(self):
         self.trayIconMenu _ QMenu(self)
         self.trayIconMenu.aA..(self.minimizeAction)
         self.trayIconMenu.aA..(self.maximizeAction)
         self.trayIconMenu.aA..(self.restoreAction)
         self.trayIconMenu.addSeparator()
         self.trayIconMenu.aA..(self.quitAction)

         self.trayIcon _ QSystemTrayIcon(self)
         self.trayIcon.setContextMenu(self.trayIconMenu)


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)

    __ no. QSystemTrayIcon.isSystemTrayAvailable
        ?MB...critical(N.., "Systray",
                "I couldn't detect any system tray on this system.")
        ___.exit(1)

    ?A...setQuitOnLastWindowClosed F..

    window _ Window()
    window.s..
    ___.exit(app.exec_())
