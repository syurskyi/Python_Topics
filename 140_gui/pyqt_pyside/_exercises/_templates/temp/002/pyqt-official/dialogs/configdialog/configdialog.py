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


____ ?.?C.. ______ QDate, QSize, __
____ ?.?G.. ______ QIcon
____ ?.?W.. ______ (?A.., QCheckBox, QComboBox, QDateTimeEdit,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListView, QListWidget, QListWidgetItem, ?PB.., QSpinBox,
        QStackedWidget, QVBoxLayout, QWidget)

______ configdialog_rc


c_ ConfigurationPage(QWidget):
    ___ __init__  parent_None):
        super(ConfigurationPage, self).__init__(parent)

        configGroup _ QGroupBox("Server configuration")

        serverLabel _ QLabel("Server:")
        serverCombo _ QComboBox()
        serverCombo.addItem("Trolltech (Australia)")
        serverCombo.addItem("Trolltech (Germany)")
        serverCombo.addItem("Trolltech (Norway)")
        serverCombo.addItem("Trolltech (People's Republic of China)")
        serverCombo.addItem("Trolltech (USA)")

        serverLayout _ QHBoxLayout()
        serverLayout.aW..(serverLabel)
        serverLayout.aW..(serverCombo)

        configLayout _ ?VBL..
        configLayout.addLayout(serverLayout)
        configGroup.sL..(configLayout)

        mainLayout _ ?VBL..
        mainLayout.aW..(configGroup)
        mainLayout.addStretch(1)

        self.sL..(mainLayout)


c_ UpdatePage(QWidget):
    ___ __init__  parent_None):
        super(UpdatePage, self).__init__(parent)

        updateGroup _ QGroupBox("Package selection")
        systemCheckBox _ QCheckBox("Update system")
        appsCheckBox _ QCheckBox("Update applications")
        docsCheckBox _ QCheckBox("Update documentation")

        packageGroup _ QGroupBox("Existing packages")

        packageList _ QListWidget()
        qtItem _ QListWidgetItem(packageList)
        qtItem.sT..("Qt")
        qsaItem _ QListWidgetItem(packageList)
        qsaItem.sT..("QSA")
        teamBuilderItem _ QListWidgetItem(packageList)
        teamBuilderItem.sT..("Teambuilder")

        startUpdateButton _ ?PB..("Start update")

        updateLayout _ ?VBL..
        updateLayout.aW..(systemCheckBox)
        updateLayout.aW..(appsCheckBox)
        updateLayout.aW..(docsCheckBox)
        updateGroup.sL..(updateLayout)

        packageLayout _ ?VBL..
        packageLayout.aW..(packageList)
        packageGroup.sL..(packageLayout)

        mainLayout _ ?VBL..
        mainLayout.aW..(updateGroup)
        mainLayout.aW..(packageGroup)
        mainLayout.addSpacing(12)
        mainLayout.aW..(startUpdateButton)
        mainLayout.addStretch(1)

        self.sL..(mainLayout)


c_ QueryPage(QWidget):
    ___ __init__  parent_None):
        super(QueryPage, self).__init__(parent)

        packagesGroup _ QGroupBox("Look for packages")

        nameLabel _ QLabel("Name:")
        nameEdit _ ?LE..

        dateLabel _ QLabel("Released after:")
        dateEdit _ QDateTimeEdit(QDate.currentDate())

        releasesCheckBox _ QCheckBox("Releases")
        upgradesCheckBox _ QCheckBox("Upgrades")

        hitsSpinBox _ QSpinBox()
        hitsSpinBox.setPrefix("Return up to ")
        hitsSpinBox.setSuffix(" results")
        hitsSpinBox.setSpecialValueText("Return only the first result")
        hitsSpinBox.setMinimum(1)
        hitsSpinBox.setMaximum(100)
        hitsSpinBox.setSingleStep(10)

        startQueryButton _ ?PB..("Start query")

        packagesLayout _ QGridLayout()
        packagesLayout.aW..(nameLabel, 0, 0)
        packagesLayout.aW..(nameEdit, 0, 1)
        packagesLayout.aW..(dateLabel, 1, 0)
        packagesLayout.aW..(dateEdit, 1, 1)
        packagesLayout.aW..(releasesCheckBox, 2, 0)
        packagesLayout.aW..(upgradesCheckBox, 3, 0)
        packagesLayout.aW..(hitsSpinBox, 4, 0, 1, 2)
        packagesGroup.sL..(packagesLayout)

        mainLayout _ ?VBL..
        mainLayout.aW..(packagesGroup)
        mainLayout.addSpacing(12)
        mainLayout.aW..(startQueryButton)
        mainLayout.addStretch(1)

        self.sL..(mainLayout)


c_ ConfigDialog(QDialog):
    ___ __init__  parent_None):
        super(ConfigDialog, self).__init__(parent)

        self.contentsWidget _ QListWidget()
        self.contentsWidget.setViewMode(QListView.IconMode)
        self.contentsWidget.setIconSize(QSize(96, 84))
        self.contentsWidget.setMovement(QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setSpacing(12)

        self.pagesWidget _ QStackedWidget()
        self.pagesWidget.aW..(ConfigurationPage())
        self.pagesWidget.aW..(UpdatePage())
        self.pagesWidget.aW..(QueryPage())

        closeButton _ ?PB..("Close")

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        closeButton.c__.c..(self.close)

        horizontalLayout _ QHBoxLayout()
        horizontalLayout.aW..(self.contentsWidget)
        horizontalLayout.aW..(self.pagesWidget, 1)

        buttonsLayout _ QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.aW..(closeButton)

        mainLayout _ ?VBL..
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonsLayout)

        self.sL..(mainLayout)

        self.setWindowTitle("Config Dialog")

    ___ changePage  current, previous):
        __ no. current:
            current _ previous

        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

    ___ createIcons(self):
        configButton _ QListWidgetItem(self.contentsWidget)
        configButton.setIcon(QIcon(':/images/config.png'))
        configButton.sT..("Configuration")
        configButton.setTextAlignment(__.AlignHCenter)
        configButton.setFlags(__.ItemIsSelectable | __.ItemIsEnabled)

        updateButton _ QListWidgetItem(self.contentsWidget)
        updateButton.setIcon(QIcon(':/images/update.png'))
        updateButton.sT..("Update")
        updateButton.setTextAlignment(__.AlignHCenter)
        updateButton.setFlags(__.ItemIsSelectable | __.ItemIsEnabled)

        queryButton _ QListWidgetItem(self.contentsWidget)
        queryButton.setIcon(QIcon(':/images/query.png'))
        queryButton.sT..("Query")
        queryButton.setTextAlignment(__.AlignHCenter)
        queryButton.setFlags(__.ItemIsSelectable | __.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.c..(self.changePage)


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    dialog _ ConfigDialog()
    ___.exit(dialog.exec_())    
