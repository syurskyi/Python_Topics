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


____ ?.QtGui ______ QIcon
____ ?.?W.. ______ (QAction, QApplication, QCheckBox, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QMenu, ?PB.., QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout)

______ systray_rc


class Window(QDialog):
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

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(self.iconGroupBox)
        mainLayout.addWidget(self.messageGroupBox)
        self.setLayout(mainLayout)

        self.iconComboBox.setCurrentIndex(1)
        self.trayIcon.s..

        self.setWindowTitle("Systray")
        self.resize(400, 300)

    ___ setVisible(self, visible):
        self.minimizeAction.setEnabled(visible)
        self.maximizeAction.setEnabled(not self.isMaximized())
        self.restoreAction.setEnabled(self.isMaximized() or not visible)
        super(Window, self).setVisible(visible)

    ___ closeEvent(self, event):
        if self.trayIcon.isVisible
            QMessageBox.information(self, "Systray",
                    "The program will keep running in the system tray. To "
                    "terminate the program, choose <b>Quit</b> in the "
                    "context menu of the system tray entry.")
            self.hide()
            event.ignore()

    ___ setIcon(self, index):
        icon _ self.iconComboBox.itemIcon(index)
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)

        self.trayIcon.setToolTip(self.iconComboBox.itemText(index))

    ___ iconActivated(self, reason):
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            self.iconComboBox.setCurrentIndex(
                    (self.iconComboBox.currentIndex() + 1)
                    % self.iconComboBox.count())
        elif reason == QSystemTrayIcon.MiddleClick:
            self.showMessage()

    ___ showMessage(self):
        icon _ QSystemTrayIcon.MessageIcon(
                self.typeComboBox.itemData(self.typeComboBox.currentIndex()))
        self.trayIcon.showMessage(self.titleEdit.text(),
                self.bodyEdit.toPlainText(), icon,
                self.durationSpinBox.value() * 1000)

    ___ messageClicked(self):
        QMessageBox.information(None, "Systray",
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
        iconLayout.addWidget(self.iconLabel)
        iconLayout.addWidget(self.iconComboBox)
        iconLayout.addStretch()
        iconLayout.addWidget(self.showIconCheckBox)
        self.iconGroupBox.setLayout(iconLayout)

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
        self.bodyEdit.setPlainText("Don't believe me. Honestly, I don't have "
                "a clue.\nClick this balloon for details.")

        self.showMessageButton _ ?PB..("Show Message")
        self.showMessageButton.setDefault(True)

        messageLayout _ QGridLayout()
        messageLayout.addWidget(typeLabel, 0, 0)
        messageLayout.addWidget(self.typeComboBox, 0, 1, 1, 2)
        messageLayout.addWidget(self.durationLabel, 1, 0)
        messageLayout.addWidget(self.durationSpinBox, 1, 1)
        messageLayout.addWidget(durationWarningLabel, 1, 2, 1, 3)
        messageLayout.addWidget(titleLabel, 2, 0)
        messageLayout.addWidget(self.titleEdit, 2, 1, 1, 4)
        messageLayout.addWidget(bodyLabel, 3, 0)
        messageLayout.addWidget(self.bodyEdit, 3, 1, 2, 4)
        messageLayout.addWidget(self.showMessageButton, 5, 4)
        messageLayout.setColumnStretch(3, 1)
        messageLayout.setRowStretch(4, 1)
        self.messageGroupBox.setLayout(messageLayout)

    ___ createActions(self):
        self.minimizeAction _ QAction("Mi&nimize", self, triggered_self.hide)
        self.maximizeAction _ QAction("Ma&ximize", self,
                triggered_self.showMaximized)
        self.restoreAction _ QAction("&Restore", self,
                triggered_self.showNormal)
        self.quitAction _ QAction("&Quit", self,
                triggered_QApplication.instance().quit)

    ___ createTrayIcon(self):
         self.trayIconMenu _ QMenu(self)
         self.trayIconMenu.addAction(self.minimizeAction)
         self.trayIconMenu.addAction(self.maximizeAction)
         self.trayIconMenu.addAction(self.restoreAction)
         self.trayIconMenu.addSeparator()
         self.trayIconMenu.addAction(self.quitAction)

         self.trayIcon _ QSystemTrayIcon(self)
         self.trayIcon.setContextMenu(self.trayIconMenu)


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)

    if not QSystemTrayIcon.isSystemTrayAvailable
        QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        sys.exit(1)

    QApplication.setQuitOnLastWindowClosed(False)

    window _ Window()
    window.s..
    sys.exit(app.exec_())
